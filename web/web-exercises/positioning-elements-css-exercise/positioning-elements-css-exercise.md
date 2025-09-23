---
author: Stefan-Stojanovic
type: normal
category: coding
webSetupCode:
  startingHtml: |
    <div class="your-code">
      <div class="box parent">
        Parent
        <div class="box child">Child</div>
      </div>
    </div>
  startingCss: |
    /* 
    Task:
    1. Give the parent a border and some padding.
    2. Position the child box absolutely inside the parent.
    3. Try placing the child in the bottom-right corner.
    4. Experiment with relative vs absolute positioning.
    */

    .box {
      padding: 20px;
      border: 2px solid black;
      margin: 20px;
    }

    .child {
      background: lightblue;
      padding: 10px;
    }

    /* Write your CSS below */
  startingJs: |
    // No JavaScript needed
---

# Positioning Elements with CSS

---

## Content

In this exercise, you will:
- Learn how **relative** and **absolute** positioning interact.
- Place elements inside containers at specific positions.
- Practice controlling layout beyond flexbox/grid.

📱 **Note:** On mobile, `:hover` doesn’t trigger.  
Use `:focus` or `:active` instead to test your button effect.

If you’re unsure how, check the hints[1].

---

## Footnotes

[1: Hints]

- Set the parent to relative so the child is positioned inside:  

```css
.parent {
  position: relative;
  height: 200px;
}
```

- Absolutely position the child:

```css
.child {
  position: absolute;
  bottom: 10px;
  right: 10px;
}
```
