---
# the default layout is 'page'
icon: fas fa-info-circle
order: 4
title: Hey 👋
---

I'm Walid Dib — an entrepreneur and operator focused on building products from zero to revenue, with an emphasis on speed, leverage, and clear thinking.

I'm currently building [**10Demo**](https://10demo.com), an AI SDR that puts product demos on autopilot. Below is the rest of what I've worked on.

<h2 class="cv-heading">Companies</h2>
<div class="cv-list">
{% for item in site.data.projects.companies %}
  <div class="cv-item">
    <div class="cv-item-head">
      <a class="cv-name" href="{{ item.url }}" target="_blank" rel="noopener noreferrer">{{ item.name }}</a>
      <span class="cv-pill cv-pill--{{ item.status }}">{{ item.label }}</span>
    </div>
    <p class="cv-blurb">{{ item.blurb }}</p>
  </div>
{% endfor %}
</div>

<h2 class="cv-heading">Side projects</h2>
<div class="cv-list">
{% for item in site.data.projects.side_projects %}
  <div class="cv-item">
    <div class="cv-item-head">
      <a class="cv-name" href="{{ item.url }}" target="_blank" rel="noopener noreferrer">{{ item.name }}</a>
      <span class="cv-pill cv-pill--{{ item.status }}">{{ item.label }}</span>
    </div>
    <p class="cv-blurb">{{ item.blurb }}</p>
  </div>
{% endfor %}
</div>
