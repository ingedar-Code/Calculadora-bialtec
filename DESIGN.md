---
name: Bialtec Precision Nutrition
colors:
  surface: '#f7f9ff'
  surface-dim: '#d7dae0'
  surface-bright: '#f7f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f4fa'
  surface-container: '#ebeef4'
  surface-container-high: '#e5e8ef'
  surface-container-highest: '#e0e2e9'
  on-surface: '#181c21'
  on-surface-variant: '#444652'
  inverse-surface: '#2d3136'
  inverse-on-surface: '#eef1f7'
  outline: '#747683'
  outline-variant: '#c4c6d4'
  surface-tint: '#3759b3'
  primary: '#00205f'
  on-primary: '#ffffff'
  primary-container: '#00338d'
  on-primary-container: '#81a1ff'
  inverse-primary: '#b4c5ff'
  secondary: '#376b00'
  on-secondary: '#ffffff'
  secondary-container: '#92f92f'
  on-secondary-container: '#3a6f00'
  tertiary: '#232526'
  on-tertiary: '#ffffff'
  tertiary-container: '#383b3c'
  on-tertiary-container: '#a3a5a6'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b4c5ff'
  on-primary-fixed: '#00174b'
  on-primary-fixed-variant: '#19409a'
  secondary-fixed: '#94fc32'
  secondary-fixed-dim: '#7adf00'
  on-secondary-fixed: '#0d2000'
  on-secondary-fixed-variant: '#285000'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#f7f9ff'
  on-background: '#181c21'
  surface-variant: '#e0e2e9'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  h2:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  h3:
    fontFamily: Manrope
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  data-mono:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '500'
    lineHeight: 24px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 24px
  container-max: 1200px
---

## Brand & Style

The design system is engineered for veterinary nutritionists who require precision, reliability, and scientific rigor. The brand personality is authoritative yet modern, bridging the gap between clinical biotechnology and digital efficiency. 

The aesthetic follows a **Minimalist Corporate** approach. It prioritizes clarity and high-density information architecture without visual clutter. The UI avoids all decorative elements, focusing on mathematical accuracy and professional utility. By utilizing heavy white space and a disciplined color application, the interface conveys a sense of sterility and pharmaceutical-grade quality that aligns with Bialtec's biological and technological expertise.

## Colors

The palette is derived directly from the Bialtec corporate identity. 
- **Primary:** The deep blue (#00338D) serves as the anchor for headers, primary actions, and brand identification, evoking trust and scientific depth.
- **Secondary:** The vibrant lime (#7ADF00) is used sparingly as a functional accent for "success" states, calculation results, or critical data points that require immediate visual attention.
- **Background & Neutrals:** The UI utilizes a layered light approach. The base is pure white (#FFFFFF), with the light gray (#F7F8F9) used for grouping input sections and secondary containers to maintain a clean, organized layout.
- **Typography:** A dark charcoal is used for body text to ensure high legibility against white backgrounds, avoiding the harshness of pure black.

## Typography

To integrate with Bialtec's Aller/Oxygen stack while ensuring modern UI performance, this design system utilizes **Manrope** for headlines and **Inter** for all functional and body text.

- **Manrope** provides a geometric, professional structure for titles and section headers, mirroring the modern industrial feel of the brand.
- **Inter** is selected for its exceptional legibility in data-heavy environments. 
- **Numerical Data:** For the calculator's numeric inputs and outputs, Inter's tabular figures (`tnum`) must be enabled to ensure columns of numbers align perfectly for easy comparison.

## Layout & Spacing

The layout employs a **Fixed Grid** system centered on a 12-column structure for desktop and a single column for mobile. 

- **Structure:** Content is housed in a maximum 1200px container to prevent eye strain during data entry.
- **Rhythm:** A 4px baseline grid ensures vertical rhythm. Sections are separated by large margins (40px-64px) to emphasize the minimalist, uncrowded feel.
- **Data Density:** While the overall layout is spacious, input groups use tight spacing (8px-16px) to maintain the relationship between labels and their respective fields.

## Elevation & Depth

This design system uses a **Low-Contrast Outline** and **Tonal Layering** approach rather than traditional shadows. This reinforces the "clean and serious" directive.

- **Planes:** The primary surface is White (#FFFFFF). Secondary grouping containers use the Light Gray (#F7F8F9) with a 1px border in a slightly darker neutral shade.
- **Hierarchy:** High-priority calculation results are highlighted with a subtle 2px left-border accent using the Primary Blue, rather than being lifted with a shadow.
- **Interactions:** Subtle background color shifts (e.g., from #FFFFFF to #F7F8F9) indicate hover states on interactive rows or list items.

## Shapes

The shape language is **Soft (0.25rem)**. This slight rounding takes the edge off the clinical nature of the tool without becoming informal or "bubbly."

- **Input Fields & Buttons:** Use a 4px corner radius to maintain a precise, engineering-focused appearance.
- **Cards/Sections:** Use a 8px corner radius (`rounded-lg`) for larger containers to provide a gentle structural definition against the page background.
- **Status Indicators:** Small, circular dots are used for status, but all functional containers remain rectangular with minimal rounding.

## Components

- **Input Fields:** Minimalist design with a 1px border. Labels are positioned above the field in `label-caps`. Focus states use a 2px Primary Blue border.
- **Buttons:** Primary buttons are solid Primary Blue with white text. Secondary buttons use a Primary Blue outline with no fill. No gradients or shadows are permitted.
- **Data Cards:** Simple containers with #F7F8F9 backgrounds. Used to group related nutritional parameters (e.g., Proteins, Minerals, Vitamins).
- **Result Panels:** High-impact areas for calculation totals. Use a light version of the Secondary Lime as a background with dark text to signify a completed calculation or "positive" nutritional balance.
- **Unit Toggles:** Small, segmented controls to switch between metric and imperial units, using a subtle gray fill for the inactive state and Primary Blue for the active state.
- **Data Tables:** Borderless rows with thin horizontal dividers. Header rows use the Primary Blue as text color to define the start of the data set.