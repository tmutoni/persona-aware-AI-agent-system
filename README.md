# Persona‑Aware AI Agent System — DiCorner Demo


# Persona-Aware AI Agent System

**Owner:** Product Manager (DiCorner)
**Stakeholders:** E-commerce Brand Team, Design, Engineering, Data Science

## 1. Vision & Objectives

**Vision:** Enable an autonomous, persona-aware AI agent embedded in the brand’s e-commerce site to classify each visitor’s micro-persona in real time and serve the next best action—product recommendation, tutorial, or A/B tested creative—in a seamless checkout experience.

**Objectives:**

* Leverage GenAI-driven personalization to increase add-to-cart conversion by 15% for hobbyist segments.
* Use context-aware, persona-tailored recommendations to reduce time-to-first-purchase by 20% for power users.
* Employ an adaptive GenAI experimentation engine to double testing velocity and optimize CTAs for each micro‑segment in real time.

## 2. Key Features

1. **Persona Classifier Agent**

   * Input: clickstream, referral source, browsing patterns
   * Output: persona tag (e.g., `photo_first`, `vector_first`, `shopper_pro`)
   * SLA: classification <150ms
2. **Product Advisor Agent**

   * Input: persona tag, session context, product catalog
   * Output: next best product carousel or tutorial link
3. **Experimentation Bandit Agent**

   * Input: real-time performance signals (clicks, adds, purchases)
   * Output: dynamic assignment of hero images and CTAs by micro-segment

## 3. User Stories & Flows

### 3.1 Visitor Journey (Hobbyist)

1. Land on homepage via social ad (UTM parameters tracked)
2. PersonaClassifier tags as `novice_shopper`
3. ProductAdvisor displays beginner bundle carousel
4. Visitor clicks "Try Bundle"
5. Checkout flow pre-populates recommended add-ons
6. BanditAgent dynamically swaps hero messaging mid-session based on click-through

### 3.2 Visitor Journey (Pro)

1. Clicks "Explore Collections" from email link
2. PersonaClassifier tags as `shopper_pro`
3. ProductAdvisor surfaces high-end product grid
4. BanditAgent selects creative variant emphasizing urgency ("Limited stock")
5. Visitor adds to cart and checks out

## 4. UI/UX Requirements

* **Creative Concierge Modal**

  * Trigger on entry or after 3 pages
  * Three-option card layout: primary recommendation, alternative, "Learn more"
  * Progressive disclosure: show advanced features only after second interaction
* **Recommendation Carousel**

  * Swipeable on mobile, scrollable on desktop
  * Each card: product image, persona-specific callout, one-click action
* **Checkout Assistant**

  * Sidebar chat widget: "Need help?" recommending upsells

## 5. Data & Analytics

* **Inputs:**

  * First-party profile (logged in), anonymous session ID, clickstream events
  * Real-time metrics: pageViews/sec, click-through rates, add-to-cart events
* **Outputs:**

  * Persona labels per session, recommendation impressions, conversion lift
* **Storage:** AEP-like event stream (Kafka), feature store (Redis), experiment logs (Postgres)

## 6. Architecture Overview

```
[Browser] ↔ [Front-End] ↔ [Concierge Agent (Streamlit/React)]
                              ↑
                         gRPC Mesh
                              ↓
      [PersonaClassifier]  [ProductAdvisor]  [ExperimentationBandit]
                             ↕
                      [Feature Store (Redis)]
```

* Microservices in containers, orchestrated via Kubernetes or Docker Compose.

## 7. Metrics & KPIs

* **Conversion lift:** baseline vs. personalized recommendations
* **Experiment velocity:** tests per week
* **Engagement:** session duration, recommendation clicks
* **System latency:** agent response times

## 8. Roadmap & Milestones

* **week 0** stub services + Streamlit demo + Loom walkthrough
* **Week 1:** integrate real product API and A/B engine
* **Week 2:** user testing & UX refinements, dashboard for analytics

## 9. Open Questions

* What personas map best to our catalog? (define taxonomy)
* What pricing tiers should default options anchor on?
* How to securely surface first-party profile in UI?



## Current status

| Service | Tech | State |
|---------|------|-------|
| PersonaClassifier | FastAPI | **✅ stub running** |
| ProductAdvisor | — | ⬜ planned |
| ExperimentationBandit | — | ⬜ planned |

Run locally:

```bash
docker compose up --build
# or
python agent_core/server.py   # dev mode
