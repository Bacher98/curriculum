---
author: Stefan-Stojanovic
type: normal
category: coding
webSetupCode:
  startingHtml: |
    <div class="your-code">
      <h1 class="title">Hello World</h1>
      <button class="btn">Click Me</button>
    </div>
  startingCss: |
    /* 
    Task:
    1. Define a CSS variable for the main color.
    2. Apply it to the title and button background.
    3. Add a second variable for text color.
    4. Use the variables in your styles.
    */

    :root {
      /* Define your variables here */
    }

    .title {
      /* Use var(--main-color) for color */
    }

    .btn {
      padding: 10px 20px;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      /* Use var(--main-color) and var(--text-color) */
    }
  startingJs: |
    // No JavaScript needed
---

# CSS Variables (Custom Properties)

---

## Content

In this exercise, you will:
- Learn how to use **CSS variables** (`--variable-name`).
- Apply variables to style text and buttons.
- Prepare for themes and easy color switching.

📱 **Note:** On mobile, `:hover` doesn’t trigger.  
Use `:focus` or `:active` instead to test your button effect.

If you’re unsure how, check the hints[1].

---

## Footnotes

[1: Hints]

- Define variables at the `:root` level:  

```css
:root {
  --main-color: #3498db;
  --text-color: #ffffff;
}
```

- Use them with var():
```css
.title {
  color: var(--main-color);
}

.btn {
  background: var(--main-color);
  color: var(--text-color);
}
```
