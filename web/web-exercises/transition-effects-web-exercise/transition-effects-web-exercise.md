---
author: Stefan-Stojanovic
type: normal
category: coding
webSetupCode:
  startingHtml: |
    <div class="your-code">
      <button class="transition-btn">Hover Me</button>
      <div class="card">
        <h3>Card Title</h3>
        <p>This is some content inside the card.</p>
      </div>
    </div>
  startingCss: |
    /* 
    Task:
    1. Add a smooth interaction transition to the button 
       (change background & scale on hover/active/focus).
    2. Add an interaction effect to the card 
       (shadow + slight movement).
    3. Keep the design clean and mobile-friendly.
    */

    .transition-btn {
      padding: 12px 24px;
      font-size: 16px;
      background: #3498db;
      color: white;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      transition: background 0.3s ease, transform 0.3s ease;
    }

    .transition-btn:hover,
    .transition-btn:focus,
    .transition-btn:active {
      background: #1d6fa5;
      transform: scale(1.05);
    }

    .card {
      margin-top: 20px;
      padding: 16px;
      background: white;
      border-radius: 8px;
      box-shadow: 0 0 6px rgba(0,0,0,0.1);
      transition: box-shadow 0.3s ease, transform 0.3s ease;
    }

    .card:hover,
    .card:focus,
    .card:active {
      box-shadow: 0 4px 12px rgba(0,0,0,0.2);
      transform: translateY(-4px);
    }
  startingJs: |
    // No JavaScript needed
---

# Smooth Transitions in CSS

---

## Content

In this exercise, you will:
- Learn how to create smooth interaction effects using `transition`.
- Apply scaling and background-color changes on a button.
- Enhance cards with shadows and movement.

📱 **Note:** On mobile, `:hover` doesn’t trigger.  
Use `:focus` or `:active` instead to test your button effect.

If you’re unsure how, check the hints[1].

---

## Footnotes

[1: Hints]

- Add transition to multiple properties:  

```css
transition: background 0.3s ease, transform 0.3s ease;
```

- Use `transform` to slightly enlarge elements on hover:

```css
transform: scale(1.05)
```

- Use `box-shadow` to make hover effects more interactive:

```css
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
```

- Combine transitions with interaction states:

```css
.element:hover,
.element:focus,
.element:active {
  transform: scale(1.05);
  box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}
```