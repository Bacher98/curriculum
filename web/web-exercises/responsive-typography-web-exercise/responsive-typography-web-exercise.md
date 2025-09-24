---
author: Stefan-Stojanovic
type: normal
category: coding
webSetupCode:
  startingHtml: |
    <div class="your-code">
      <h1>Responsive Typography</h1>
      <p>This paragraph text should adjust nicely for different screen sizes.</p>
    </div>
  startingCss: |
    /* 
    Task:
    1. Set a base font size for the page.
    2. Use relative units (em, rem) for the paragraph.
    3. Add a media query to make the heading smaller on narrow screens.
    4. Keep the text readable and balanced.
    */

    body {
      font-family: Arial, sans-serif;
    }

    /* Write your CSS below */
  startingJs: |
    // No JavaScript needed
---

# Responsive Typography

---

## Content

In this exercise, you will:
- Learn how to scale text across devices.
- Use **relative units** for font sizes.
- Apply **media queries** to adjust typography on small screens.

📱 **Note:** On mobile, `:hover` doesn’t trigger.  
Use `:focus` or `:active` instead to test your button effect.

If you’re unsure how, check the hints[1].

---

## Footnotes

[1: Hints]

- Base font size:  

```css
body {
  font-size: 16px;
}
```

- Use rem units for scaling:
```css
p {
  font-size: 1rem; /* 16px */
}
```

- Responsive heading with media query:

```css
h1 {
  font-size: 2.5rem;
}

@media (max-width: 600px) {
  h1 {
    font-size: 1.8rem;
  }
}
```