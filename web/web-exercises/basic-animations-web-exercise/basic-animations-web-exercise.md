---
author: Stefan-Stojanovic
type: normal
category: coding
webSetupCode:
  startingHtml: |
    <div class="your-code">
      <h1 class="title">Welcome!</h1>
      <button class="pulse-btn">Click Me</button>
    </div>
  startingCss: |
    /* 
    Task:
    1. Create a simple animation using @keyframes.
    2. Make the button gently "pulse" when hovered.
    3. Animate the title to fade in when the page loads.
    */

    /* Write your CSS below */
  startingJs: |
    // No JavaScript needed
---

# Basic Animations with CSS

---

## Content

In this exercise, you will:
- Use `@keyframes` to create a simple animation.
- Apply an interaction-based pulsing effect to the button  
- Animate the title to fade in when the page loads.

📱 **Note:** On mobile, `:hover` doesn’t trigger.  
Use `:focus` or `:active` instead to test your button effect.

If you’re unsure how, check the hints[1].
---

## Footnotes

[1: Hints]

- Define keyframes like this:  

```css
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
```

- Apply the animation to the title:

```css
.title {
  animation: fadeIn 1s ease-in-out;
}
```

- For the button pulse (works on both desktop + mobile):

```css
.pulse-btn:hover,
.pulse-btn:focus,
.pulse-btn:active {
  animation: pulse 0.6s infinite alternate;
}

@keyframes pulse {
  from { transform: scale(1); }
  to { transform: scale(1.1); }
}
```