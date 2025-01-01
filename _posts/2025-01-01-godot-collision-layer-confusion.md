---
title: Godot Collision Layer Confusion
description: "My personal experience grappling with Godot 4's collision layers and masks"
date: 2025-01-01T12:57:14.547Z
preview: ""
tags: []
categories: [godot engine]
math: true
---

> This post is based on my experience as an amateur Godot developer using **Godot 4**. I'm basically giving a blow-by-blow account of how I discovered the difference between simple collision layers in the Inspector versus the hex/binary/decimal madness in the code editor. 
{: .prompt-tip }

### Solitaire, collision layers, and raycasts

After playing [Balatro](https://www.playbalatro.com/), I wanted to code a Solitaire clone in Godot to learn about card-click signals and data arrays—but I ended up spending days untangling why collision shapes register layers differently in the code editor and inspector.

Let's take a step back: understanding collision layers and collision masks is, like, [Godot 101](https://docs.godotengine.org/en/stable/tutorials/physics/physics_introduction.html#collision-layers-and-masks). Assigning a node its layers is straight forward through the inspector, and allows nodes to identify when other bodies or areas collide with them. Layers define which "group(s)" your node belongs to, and Masks define which "group(s)" your node can interact with. In the inspector, doing this is as easy as simply clicking which layers and masks you want your node to belong to. 

![](/public/assets/lib/Godot%20collisions.png)
_The inspector shows you up to 32 layers and masks you can allow your node to belong to._

By default, you might be tempted to rely on the `input_event` signal from each card (an `Area2D`), but if multiple cards overlap, the signal can trigger for *every* overlapping card at once. That defeats the goal of selecting a *single* card at a time. Hence, I needed a more precise way to detect exactly which card I'm clicking—which led me to [raycasting](https://docs.godotengine.org/en/stable/tutorials/physics/ray-casting.html). The code snippet I used is shown below:

```gdscript

func _raycast_at_card() -> Card:
	var space_state := get_world_2d().direct_space_state
	var parameters := PhysicsPointQueryParameters2D.new()
	parameters.position = get_global_mouse_position()
	parameters.collide_with_areas = true
	parameters.collision_mask = CARD_COLLISION # a constant of type int I set earlier to be layer 1.
	var result := space_state.intersect_point(parameters)
	if result.size() > 0:
		return result[0].collider
	return null
```

This function is basically my quick way to “raycast” at whatever card my mouse is clicking. First, I grab the 2D world’s `direct_space_state` (which is Godot’s way of letting me query objects in the physics space). Then I create a `PhysicsPointQueryParameters2D` object, set its position to my current mouse location, allow it to collide with areas (`collide_with_areas = true`), and define which layer I want to detect (`collision_mask = CARD_COLLISION`).

After that, I do `intersect_point(parameters)`, which shoots out a check at that point in space to see what’s there. If the results array has any items (`result.size() > 0`), I return the first collider I find (which should be a `Card` node). If nothing’s there, I just return `null`. It’s basically me saying, “Hey, Godot, which card am I on right now?” and it promptly points me to the right card—if there is one. 

### Which finally brings us to the purpose of this blog post

`CARD_COLLISION` in `parameters.collision_mask = CARD_COLLISION` is simply a constant set to `1`. That’s fine if your collision mask is also `1` in both the Inspector and code. Using `2` works for layer 2 as well. But layer 3 in the Inspector is actually `4` in code. You can test it yourself, if you set a `$Node` collision mask to `3` in the inspector, and then print it, you'll get

```gdscript
print($Node.collision_mask)

# OUTPUT: 4
```

_Wait, what?_

Why does `3` in the inspector = `4` in the code when it comes to layers? I immediately forget about the Solitaire project at hand and spend the next few hours figuring this out. To calm myself down, I started digging into the Godot Docs, and found [this](https://docs.godotengine.org/en/3.4/tutorials/physics/physics_introduction.html#code-example) enlightening snippet:

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

In code, you don't just write “layers = 1, 3, 4.” Instead, you specify them as a **bitmask**, which is basically a sequence of bits (zeros and ones) that represent on/off states. For instance, if you enable Layers `1`, `3`, and `4` in the Inspector, you’re actually flipping bits `1`, `3`, and `4` to “1,” while all other bits remain “0.”  

Because Godot can have up to 32 collision layers, using a single integer bitmask is an efficient way to track those multiple on/off states, and performing bitwise checks is extremely fast internally. That’s why the docs show examples like `0b00000000_00000000_00000000_00001101` (binary), `0x000d` (hex), or `13` (decimal). All three just mean, “Layers 1, 3, and 4 are active.” in different numeric representations.

### How Binary, Hex, and Decimal Represent the Same Value

1. **Binary (`0b...`)**  
   - Each digit is either 0 or 1, representing **powers of 2** from right to left.  
   - For instance, `0b1101` means:  
      $$(1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0) = 8 + 4 + 0 + 1 = 13$$
   - So, `0b1101` is just another way of writing 13.

1. **Hexadecimal (`0x...`)**  
   - Each digit is 0–9 or A–F (where A=10, B=11, C=12, **D=13**, E=14, and F=15). 
   - Each hex digit corresponds to **4 bits** (since each bit can be 0 or 1, and 2^4 = 16 possible values).  
   - We know that **D=13**, therefore `0xD` is `13` in decimal, which is `1101` in binary (8 + 4 + 0 + 1 = 13). Hence, `0x000d` is just another way of writing `13` in hexadecimal. 
   - The prefix `0x` indicates that the number is in base 16.

2. **Decimal (plain numbers)**  
   - The everyday integers we use, e.g. `13`, `42`, `2025`.  
   - Under the hood, this decimal is still the same bitmask. It’s just a different notation.

Each checkbox in the Inspector corresponds to a **power of two** in code[^footnote]. If you want to enable "Layer 3," you're actually enabling the bit that stands for 2^(3-1) = 4. Meanwhile, "Layer 1" is 2^(1-1) = 1, "Layer 2" is 2^(2-1) = 2, etc.

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

### Real Example: Debugging My Collision

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

So if you ever wonder: *"Why is the code using 13 to turn on layers 1, 3, and 4?"*---well, it’s because 13 is the sum of $1 (2^0)$ + $4 (2^2)$ + $8 (2^3)$. Mind-boggling at first, but it clicks once you see it in action.

### Export Annotations in GDScript

The [docs](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_exports.html) also mention a neat trick:

```gdscript
@export_flags_2d_physics var layers_2d_physics
```

This basically allows you to edit a bitmask directly in the Godot Inspector with a friendly GUI. When you check/uncheck boxes in that field, you're effectively flipping those bits in code.

---

The next time you're banging your head on the keyboard wondering why your collisions aren't working:

1.  **Check your Inspector** to see which layers or masks you've actually enabled.
2.  **Check your code** to make sure your `collision_layer` or `collision_mask` are set using the correct bitmask.
3.  Convert decimal/binary/hex as needed:
    -   Decimal = *sum of powers of two*
    -   Binary = *0b...*
    -   Hexadecimal = *0x...*

[^footnote]: Each checkbox in the Inspector represents one **bit** in a binary number. That bit’s position corresponds to a power of two. For example, if you check “Layer 3,” under the hood you’re flipping the bit for $2^{3-1} = 4$. Checking “Layer 1” flips $2^{1-1} = 1$, and so forth. This is how Godot tracks multiple layers in a single integer—each layer is just one more bit in the binary representation.


