# 🛒 The E-Commerce Cart Abandonment Funnel Diagnostic

An enterprise-grade, data analytics portfolio project designed to identify technical and psychological drop-off points in a multi-stage digital checkout funnel. This project demonstrates end-to-end data pipeline capabilities: from synthetic data generation and cloud database querying (SQL) to interactive metric visualization.

🔗 **Live Interactive Dashboard:**# 🛒 The E-Commerce Cart Abandonment Funnel Diagnostic

An enterprise-grade, data analytics portfolio project designed to identify technical and psychological drop-off points in a multi-stage digital checkout funnel. This project demonstrates end-to-end data pipeline capabilities: from synthetic data generation and cloud database querying (SQL) to interactive metric visualization.

🔗 **Live Interactive Dashboard:** # 🛒 The E-Commerce Cart Abandonment Funnel Diagnostic

An enterprise-grade, data analytics portfolio project designed to identify technical and psychological drop-off points in a multi-stage digital checkout funnel. This project demonstrates end-to-end data pipeline capabilities: from synthetic data generation and cloud database querying (SQL) to interactive metric visualization.

🔗 **Live Interactive Dashboard:** https://ecommerce-funnel-diagnostic.streamlit.app/

---

## 📊 Project Overview & Financial Impact
Digital checkout systems lose massive revenue daily due to hidden device bugs and marketing mismatches. This diagnostic framework builds a relational database tracking 10,000 user web sessions to isolate funnel friction nodes. 

### Key Discoveries:
1. **The Technical Anomaly:** A massive **75% user drop-off pattern at the "Enter Shipping" stage** specifically affecting **Mobile Safari users in the US-West region** (simulating a complex frontend JavaScript keyboard rendering bug).
2. **The Marketing Anomaly:** Paid traffic from a specific Facebook **Retargeting Campaign** displayed incredibly high "Add to Cart" intent, but suffered an abysmal conversion rate at the final **Payment Stage** (simulating user price shock from hidden costs).

**Financial Recovery Potential:** By patching the Mobile Safari technical bug and recovering just **25% of those lost users**, the business stands to recover an estimated **$14,500+ in lost gross revenue** based on the dataset's baseline Average Order Value (AOV).

---

## 🛠️ Data Architecture & Tech Stack
* **Python (Pandas & NumPy):** Used to programmatically synthesize 10,000 messy transactional user records and seed hidden behavioral bugs.
* **Google Cloud BigQuery (SQL):** Used to execute production-grade Advanced CTEs and window functions to compute step-by-step conversion rates across dimensions.
* **Streamlit Community Cloud:** Used to build and host the public-facing executive dashboard displaying interactive recovery models.

### Relational Database Schema

---

## 📊 Project Overview & Financial Impact
Digital checkout systems lose massive revenue daily due to hidden device bugs and marketing mismatches. This diagnostic framework builds a relational database tracking 10,000 user web sessions to isolate funnel friction nodes. 

### Key Discoveries:
1. **The Technical Anomaly:** A massive **75% user drop-off pattern at the "Enter Shipping" stage** specifically affecting **Mobile Safari users in the US-West region** (simulating a complex frontend JavaScript keyboard rendering bug).
2. **The Marketing Anomaly:** Paid traffic from a specific Facebook **Retargeting Campaign** displayed incredibly high "Add to Cart" intent, but suffered an abysmal conversion rate at the final **Payment Stage** (simulating user price shock from hidden costs).

**Financial Recovery Potential:** By patching the Mobile Safari technical bug and recovering just **25% of those lost users**, the business stands to recover an estimated **$14,500+ in lost gross revenue** based on the dataset's baseline Average Order Value (AOV).

---

## 🛠️ Data Architecture & Tech Stack
* **Python (Pandas & NumPy):** Used to programmatically synthesize 10,000 messy transactional user records and seed hidden behavioral bugs.
* **Google Cloud BigQuery (SQL):** Used to execute production-grade Advanced CTEs and window functions to compute step-by-step conversion rates across dimensions.
* **Streamlit Community Cloud:** Used to build and host the public-facing executive dashboard displaying interactive recovery models.

### Relational Database Schema

---

## 📊 Project Overview & Financial Impact
Digital checkout systems lose massive revenue daily due to hidden device bugs and marketing mismatches. This diagnostic framework builds a relational database tracking 10,000 user web sessions to isolate funnel friction nodes. 

### Key Discoveries:
1. **The Technical Anomaly:** A massive **75% user drop-off pattern at the "Enter Shipping" stage** specifically affecting **Mobile Safari users in the US-West region** (simulating a complex frontend JavaScript keyboard rendering bug).
2. **The Marketing Anomaly:** Paid traffic from a specific Facebook **Retargeting Campaign** displayed incredibly high "Add to Cart" intent, but suffered an abysmal conversion rate at the final **Payment Stage** (simulating user price shock from hidden costs).

**Financial Recovery Potential:** By patching the Mobile Safari technical bug and recovering just **25% of those lost users**, the business stands to recover an estimated **$14,500+ in lost gross revenue** based on the dataset's baseline Average Order Value (AOV).

---

## 🛠️ Data Architecture & Tech Stack
* **Python (Pandas & NumPy):** Used to programmatically synthesize 10,000 messy transactional user records and seed hidden behavioral bugs.
* **Google Cloud BigQuery (SQL):** Used to execute production-grade Advanced CTEs and window functions to compute step-by-step conversion rates across dimensions.

[users] ➔ user_id (PK), region, device_type, browser
[web_sessions] ➔ session_id (PK), user_id (FK), traffic_source, campaign, session_start
[funnel_events] ➔ event_id (PK), session_id (FK), step_name, event_timestamp, revenue_impact

---

## 🚀 Step-by-Step Methodology

### 1. Data Ingestion & Seeding
The data pipeline starts by structuring raw session layers. User device signatures are mapped alongside multi-stage checkout events. The five standard checkout steps tracked include:
`1. View Item` ➔ `2. Add to Cart` ➔ `3. Enter Shipping` ➔ `4. Enter Payment` ➔ `5. Purchase Complete`

### 2. Behavioral Segmentation
Advanced SQL queries segment user performance side-by-side across Devices, Browsers, and Marketing Campaigns. This isolates normal funnel degradation from sudden systemic drop-offs.

### 3. Financial Opportunity Modeling
The data framework programmatically separates traffic volumes by cohort to map exact financial leakage. This creates a clear roadmap for engineers and marketers to prioritize tasks based on dollar value.

---

## 💡 Executive Action Items

* **Fix the US-West Mobile Safari Form Bug:** Engineering teams must urgently audit viewport resizing scripts inside the shipping address form layout. The 75% drop-off pattern confirms that iOS devices are failing to complete inputs when the mobile keyboard initializes.
* **Optimize Retargeting Ad Cost Transparency:** The marketing team should modify Facebook Retargeting ad copies to explicitly state shipping thresholds or clear baseline fees upfront. This bridges the expectation gap and eliminates the price shock dropping users at the payment gateway.

---

## 📂 Repository Structure
* `app.py`: The core Streamlit application script containing code for visualizations and interactive slider calculations.
* `funnel_master_data.csv`: The processed master transactional data file generated for analysis.
* `requirements.txt`: The system dependencies required to deploy the public cloud container.
* **Streamlit Community Cloud:** Used to build and host the public-facing executive dashboard displaying interactive recovery models.

### Relational Database Schema
