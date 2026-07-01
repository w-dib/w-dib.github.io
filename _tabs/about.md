---
# the default layout is 'page'
icon: fas fa-info-circle
order: 4
title: Hey 👋
---

I'm Walid Dib — an entrepreneur and operator focused on building products from zero to revenue, with an emphasis on speed, leverage, and clear thinking.

Here's what I've worked on over the years.

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
