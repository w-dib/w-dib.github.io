---
title: Godot Collision Layer Confusion
description: "My personal experience grappling with Godot 4.4.dev7's collision layers and masks"
date: 2025-01-01T12:57:14.547Z
preview: ""
tags: []
categories: [godot engine]
---

> This post is based on my experience as an amateur Godot developer using **Godot 4.4.dev7**. I'm basically giving a blow-by-blow account of how I discovered the difference between simple collision layers in the Inspector versus the hex/binary/decimal madness in the code editor. 
{: .prompt-tip }

### Solitaire, collision layers, and raycasts

Having recently played [Balatro](https://www.playbalatro.com/), I wanted to learn how 2D card game mechanics work in Godot, so I challenged myself to learn how to code Solitaire 🃏. My main focus was to learn two things:

- What's the best way to "click" a card, and signal its information to other parts of the game.
- How to store and manage the game's card states in arrays.

The second bullet point is irrelevant to this blog post, because I spent days diving deep into **why** collision shapes register layers differently in the code editor and inspector.

Let's take a step back: understanding collision layers and collision masks is, like, [Godot 101](https://docs.godotengine.org/en/stable/tutorials/physics/physics_introduction.html#collision-layers-and-masks). Assigning a node its layers is straight forward through the inspector, and allows nodes to identify when other bodies or areas collide with them. Layers define which "group(s)" your node belongs to, and Masks define which "group(s)" your node can interact with. In the inspector, doing this is as easy as a simply clicking which layers and masks you want your node to belong to. 

![](/public/assets/lib/Godot%20collisions.png)
_The inspector shows you up to 32 layers and masks you can allow your node to belong to._

I see little checkboxes labeled "Layer 1," "Layer 2," "Layer 3," etc. Great, so if I want to enable layers 1, 2, and 3, I just click those three checkboxes and call it a day. Armed with the above basic knowledge, I wanted to see if I can trigger the `input_event` signal of a card (an `Area2D` in this case) by clicking on it. It worked in its most basic sense: clicking on a single card triggered the `input_event` signa. Unfortunately, this approach proved janky the moment there were two cards overlapping, no matter how small the overlap was, which completely defeated the purpose. Why? Because the entire idea of Solitaire is about stacking cards on top of eachother. The below image explains the issue:

![](/public/assets/lib/card_overlap.png)
_Clicking on the dangerzone activates both cards_

If I click on a stack of cards (`Area2D`s), it would trigger the `input_event` of all the cards in the stack, because the `input_event` triggers if the mouse clicks _anywhere_ on the `Area2D`. I needed a new approach, which was to dynamically identify a node's collision layer on the exact pixel the mouse clicked at.

To do this, I had to [raycast](https://docs.godotengine.org/en/stable/tutorials/physics/ray-casting.html) exactly where the mouse was clicking, as shown below:

```gdscript

func _raycast_at_card() -> Card:
	var space_state := get_world_2d().direct_space_state
	var parameters := PhysicsPointQueryParameters2D.new()
	parameters.position = get_global_mouse_position()
	parameters.collide_with_areas = true
	parameters.collision_mask = CARD_COLLISION
	var result := space_state.intersect_point(parameters)
	if result.size() > 0:
		return result[0].collider
	return null
```

This function is basically my quick way to “raycast” at whatever card my mouse is hovering over. First, I grab the 2D world’s `direct_space_state` (which is Godot’s way of letting me query objects in the physics space). Then I create a `PhysicsPointQueryParameters2D` object, set its position to my current mouse location, allow it to collide with areas (`collide_with_areas = true`), and define which layer I want to detect (`collision_mask = CARD_COLLISION`).

After that, I do `intersect_point(parameters)`, which shoots out a check at that point in space to see what’s there. If the results array has any items (`result.size() > 0`), I return the first collider I find (which should be a `Card` node). If nothing’s there, I just return `null`. It’s basically me saying, “Hey, Godot, which card am I on right now?” and it promptly points me to the right card—if there is one. 

### Which finally brings us to the purpose of this blog post.

Where `CARD_COLLISION` in `parameters.collision_mask = CARD_COLLISION` from the above code block is a `const` valued at `1`. 

This makes sense, right? Well it does, so long as your `collision_mask` is `1` in both the inspector and the code editor. `2` works as well. But layer 3 from the inspector? That’s actually `4` in code `(2^(3-1) = 4)`.

_Wait, what?_

Why does `3` in the inspector = `4` in the code when it comes to layers? I immediately forget about the Solitaire project at hand and spend the next few hours figuring this out. To calm myself down, I started digging into the Godot Docs, and found this enlightening snippet:

> “In function calls, layers are specified as a bitmask. Where a function enables all layers by default, the layer mask will be given as `0xffffffff`. Your code can use binary, hexadecimal, or decimal notation for layer masks, depending on your preference.”

```gdscript 
# Example: Setting mask value for enabling layers 1, 3 and 4

# Binary - set the bit corresponding to the layers you want to enable (1, 3, and 4) to 1, set all other bits to 0.
# Note: Layer 32 is the first bit, layer 1 is the last. The mask for layers 4,3 and 1 is therefore
0b00000000_00000000_00000000_00001101
# (This can be shortened to 0b1101)

# Hexadecimal equivalent (1101 binary converted to hexadecimal)
0x000d
# (This value can be shortened to 0xd)

# Decimal - Add the results of 2 to the power of (layer to be enabled - 1).
# (2^(1-1)) + (2^(3-1)) + (2^(4-1)) = 1 + 4 + 8 = 13
pow(2, 1-1) + pow(2, 3-1) + pow(2, 4-1)
```

What they mean is, behind the scenes, Godot doesn’t just store a normal integer for each collision layer. It stores a **bitmask**—a fancy term for a sequence of bits (zeroes and ones) that represent which layers are enabled or not. 

So if you enable Layers 1, 3, and 4 in the Inspector, you’re essentially flipping bits 1, 3, and 4 to be “1,” while leaving everything else at “0.” But in code, you’re not forced to use “layers = 1,3,4.” Instead, you specify the bits in different numeric formats: **binary**, **hexadecimal**, or **decimal**.

### Wait---Binary, Hex, Decimal?

Yes. **Binary** just means a value like `0b1101` (which is 1's and 0's). **Hexadecimal** is something like `0x000d`. **Decimal** is what we use every day, e.g. `13`.

If this is new to you, here's a quick breakdown:

1.  **Binary (0b...)**

    -   Each digit can only be `0` or `1`.
    -   For example, `0b1101` means:
        -   1 × 2^3 + 1 × 2^2 + 0 × 2^1 + 1 × 2^0 = 8 + 4 + 0 + 1 = 13
2.  **Hexadecimal (0x...)**

    -   Each digit can be `0-9` or `A-F`.
    -   `0x000d` is basically the same as 13 in decimal.
        -   Each hex digit represents four bits, so `0xD` = `1101` in binary, which again is 13 in decimal.
3.  **Decimal**

    -   Plain old everyday numbers, e.g. `13`.

> "The code equivalent of the above example where layers 1, 3, and 4 were enabled would be `0b00000000_00000000_00000000_00001101`, or `0x000d`, or `13`."
{: .prompt-tip }

## Why is Layer 1 in Code = 2^(1-1) = 1, but Layer 3 = 2^(3-1) = 4?

Each checkbox in the Inspector corresponds to a **power of two** in code. If you want to enable "Layer 3," you're actually enabling the bit that stands for 2^(3-1) = 4. Meanwhile, "Layer 1" is 2^(1-1) = 1, "Layer 2" is 2^(2-1) = 2, etc.

In decimal terms:

```gdscript
var layer1 = 1     # 2^(1-1) = 1
var layer2 = 2     # 2^(2-1) = 2
var layer3 = 4     # 2^(3-1) = 4
var layer4 = 8     # 2^(4-1) = 8
```

So enabling layers 1, 3, and 4 in code is:

```gdscript
var layers_enabled = layer1 + layer3 + layer4  # 1 + 4 + 8 = 13
print(layers_enabled)  # prints 13
```

That same `13` can also be expressed in binary as `0b1101`, or in hexadecimal as `0xd`. This is why the Godot Docs say you can specify the collision layer in any of those formats---it all compiles down to the same bitmask.

## Real Example: Debugging My Collision

Let's say I tried the following line in code and wondered why it turned on layers 1, 3, and 4:

```gdscript
collision_layer = 13
print(collision_layer)  # 13
```

Now, if I manually convert 13 to binary, I get:

```gdscript
# 13 decimal is 8 + 4 + 1 = 1101 in binary
print(0b1101)  # also 13
```

And that means bits for layers 4, 3, and 1 are set.

Or I can do:

```gdscript
print(0x000d)   # 13 in hex
print(0xd)      # shorter hex, also 13
```

So if you ever wonder: *"Why is the code using 13 to turn on layers 1, 3, and 4?"*---well, it's because 13 is the sum of 1 (2^0) + 4 (2^2) + 8 (2^3). Mind-boggling at first, but it clicks once you see it in action.

##Export Annotations in GDScript

The [docs](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_exports.html) also mention a neat trick:

```gdscript
@export_flags_2d_physics var layers_2d_physics
```

This basically allows you to edit a bitmask directly in the Godot Inspector with a friendly GUI. When you check/uncheck boxes in that field, you're effectively flipping those bits in code.

> "Export annotations can be used to export bitmasks in the editor with a user-friendly GUI."
{: .prompt-tip }

**In short**, if you're confused why Layer 3 in the Inspector doesn't line up with "3" in your code, it's because the Inspector just labels them as 1, 2, 3... in a user-friendly way, but under the hood, **each "layer number" is a different bit** in a binary integer.

The next time you're banging your head on the keyboard wondering why your collisions aren't working:

1.  **Check your Inspector** to see which layers or masks you've actually enabled.
2.  **Check your code** to make sure your `collision_layer` or `collision_mask` are set using the correct bitmask.
3.  Convert decimal/binary/hex as needed:
    -   Decimal = *sum of powers of two*
    -   Binary = *0b...*
    -   Hexadecimal = *0x...*
