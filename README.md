# Coffee Online Store (متجر القهوة)

A full-stack e-commerce web application for a specialty coffee shop with integrated Google Analytics 4 (GA4) user behavior tracking.

---

## Overview
A web development and data analytics project built using **Python (Flask)** and **SQLite**. The application delivers a full e-commerce ordering workflow—including user registration, product browsing across specialty coffee origins, dynamic cart calculations, and checkout confirmation—complemented by end-to-end user engagement tracking via Google Analytics 4.

## Problem Statement
Small specialty coffee roasters need an intuitive, fast platform for customers to explore curated coffee origins and place online orders. This project addresses both sides of the e-commerce lifecycle: building an accessible ordering flow and analyzing real user interaction data to derive conversion insights.

## Features & Implementation

1. **User Registration & Session Management:** Collects user details (Name & Email) to instantiate a `User` record and maintain session state.
2. **Specialty Product Catalog:** Features 3 distinct coffee origins with detailed tasting notes, pricing, and visual assets:
   * **Ethiopian Yirgacheffe**
   * **Colombian Huila**
   * **Yemeni Harazi**
3. **Database-Backed Cart System:** Utilizes per-user product counters stored directly in SQLite for lightweight, real-time item tracking.
4. **Dynamic Cart & Checkout:** Calculates line-item totals, sub-totals, and order confirmations dynamically.
5. **RTL Arabic Interface:** Styled with a clean, fully responsive Right-to-Left layout for native Arabic user experience.
6. **GA4 Analytics Tracking:** Instrumented with Google Analytics 4 to monitor pageviews, custom events (Add-to-Cart), user engagement, and conversion drop-offs.

## Tech Stack
* **Backend:** Python 3.x, Flask, Flask-SQLAlchemy
* **Database:** SQLite
* **Frontend:** HTML5, CSS3 (RTL/Arabic Layout), Vanilla JavaScript (Form Validation)
* **Analytics:** Google Analytics 4 (GA4)

## Analytics & Conversion Metrics
User behavior was tracked over a **13-day evaluation window (May 28 – June 9, 2026)** using GA4. Key performance indicators recorded:

| Metric | Measured Value |
|---|---|
| **Total Page Views** | 114 |
| **Total Captured Events** | 386 |
| **Add-to-Cart Events** | 42 (36.8% rate) |
| **Key Conversions (Checkout)** | 36 (**31.6% conversion rate**) |
| **Scroll Engagement** | 102 events (89.5% scroll rate) |
| **Unique Visitors** | 7 (100% new visitors) |
| **Traffic Acquisition** | 100% Direct |

### Key Findings
* **Conversion Rate:** Achieved a **31.6% conversion rate**, significantly higher than standard e-commerce benchmarks (~1–3%), reflecting smooth UX across a focused user sample.
* **Engagement:** High scroll rate (89.5%) indicates high content readability and clear product presentation.
* **Acquisition Limitation:** All recorded sessions originated from direct links, highlighting the opportunity for future organic and social channel expansion.

## Installation & Setup

### Prerequisites
* Python 3.8+ installed on your machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/26-3-26/coffee-online-website.git](https://github.com/26-3-26/coffee-online-website.git)
cd coffee-online-website

