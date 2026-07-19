**The E-Commerce Cart Abandonment Funnel Diagnostic**
An enterprise-grade analytics pipeline and interactive diagnostic application designed to isolate, quantify, and programmatically model structural and behavioral revenue leakage across an e-commerce checkout architecture.

📌 Project Overview & Intent
Digital commerce architectures experience silent attrition through two core vectors: hidden edge-case software validation errors and downstream price-shocks from misaligned traffic acquisition strategies.

This project simulates an enterprise-level data workflow by:

Generating a relational database schema tracking 10,000 baseline web sessions embedded with subtle user friction points.

Building an extraction and load infrastructure to transport transactional layers directly into Google Cloud BigQuery.

Writing advanced PostgreSQL/Standard SQL queries leveraging Common Table Expressions (CTEs) and window aggregations to isolate performance drop-offs.

Deploying an interactive Streamlit production application to give corporate stakeholders a dynamic interface to evaluate operational recovery metrics in real time.

📐 Data Architecture & Schema
The underlying transactional structure mimics a production multi-stage checkout funnel tracked across three decoupled, relational tables: 
   [users]                [web_sessions]             [funnel_events]
 ──┬───────────          ──┬────────────────          ──┬─────────────────
   │ user_id   (PK) ◄──┐   │ session_id (PK) ◄──┐       │ event_id     (PK)
   │ region            └───│ user_id    (FK)    └───────│ session_id   (FK)
   │ device_type           │ traffic_source             │ step_name
   │ browser               │ campaign                   │ event_timestamp
                           │ session_start              │ revenue_impact
The 5-Stage Funnel Definition1. View Item $\rightarrow$ 2. 2. Add to Cart $\rightarrow$ 3. 3. Enter Shipping $\rightarrow$ 4. 4. Enter Payment $\rightarrow$ 5. 5. Purchase Complete🛠️ The Pipeline Workflow1. Ingestion & Synthetic Data GenerationThe synthetic engine (data_generator.py) generates 10,000 distinct session traces via NumPy and Pandas. During generation, two distinct anomaly clusters are programmatically injected into the event stream to replicate real-world tracking errors:The Technical Bug: A simulated JavaScript keyboard initialization error causes mobile Safari users operating strictly within the US-West region to drop out at an aggressive 75% rate explicitly at the Enter Shipping tier.The Marketing Friction Point: High-intent traffic driven via a targeted social acquisition campaign (Facebook-Ads / Retargeting-Promo) experiences an extreme conversion drop at the final Enter Payment gateway due to checkout price shock.
2. Google Cloud BigQuery Data EngineeringData frames are transported via the secure Cloud Client API layer into a unified BigQuery cluster. By avoiding brittle parser cell magics, the pipeline securely bypasses identifier syntax constraints on hyphenated Google Cloud project handles.

3. Advanced Diagnostic QueriesFunnel performance metrics are calculated inside a nested SQL environment. The query maps step-to-step degradation vectors alongside global absolute conversion limits, segmenting performance dimensions across devices and browser ecosystems simultaneously.📊 Analytical Findings & Business ImpactThe production database query yields the following diagnostic footprint:Dimension CategorySegment ValueS1 → S2 (Cart %)S2 → S3 (Shipping %)S3 → S4 (Payment %)Overall Conversion RateDevice TypeDesktop47.80%72.10%81.40%4.30%Device TypeMobile49.20%41.30%78.20%1.60%BrowserChrome48.10%70.40%82.00%4.40%BrowserSafari48.50%34.10%52.30%1.10%Traffic SourceFacebook-Ads88.40%71.20%9.10%0.80%[Inbound Traffic] ➔ [1. View Item] ➔ [2. Add to Cart] ➔ [3. Enter Shipping] ➔ [4. Enter Payment] ➔ [5. Purchase Complete]
                                            │                      │
                                            ▼                      ▼
                             [Tech Edge-Case: Mobile Safari] [Marketing Anomaly: Ad-Shock]
                             (75% Drop Anomaly Isolated)      (90.9% Attrition at Payment)
🛑 Critical Analytical InsightsThe Mobile Safari Failure: While core browser variants execute a smooth $\sim 70\%$ conversion step from Cart to Shipping, the Safari application layer drops drastically to $34.1\%$. This confirms the presence of a technical rendering block on iOS engines.The Paid Traffic Shock: The Facebook Retargeting cohort shows exceptional product engagement ($88.4\%$ Add-to-Cart velocity), but collapses to a final $9.1\%$ progression rate at payment initialization. This points to a severe mismatch between ad-spend promo copy and hidden fulfillment charges applied at checkout.

📈 Financial Opportunity ModelingThe integrated Python calculation framework isolates localized transaction values to compute the operational revenue opportunity of rolling out engineering fixes.$$\text{Financial Opportunity} = (\text{Lost Users} \times \text{Target Recovery Rate}) \times \text{Average Order Value (AOV)}$$Average Order Value (AOV): $84.72Identified Leaked Volume (US-West Safari Cluster): 684 SessionsTarget Recovery Capture Rate: 25%Immediate Annualized Revenue Upside: +$14,487.12

🚀 Execution & Deployment StrategyTo run this pipeline environment locally:
1. Initialize RequirementsEnsure your Python local virtual container is running with the specified configuration manifests:Bashpip install -r requirements.txt
2. Process Extraction & Direct Stream UploadsUpdate your Google Cloud project identities inside the operational notebook layer and execute the secure storage run:Pythonfrom google.cloud import bigquery
client = bigquery.Client(project="your-gcp-project-id")
3. Launch Local User Dashboard UISpin up the local microservices container engine to view the application layer interface locally at localhost:8501:Bashstreamlit run app.py
👔 Strategic Executive RecommendationsDeploy Frontend Engineering Hotfix on iOS Form Layouts: Frontend UI/UX developers must optimize viewports within the shipping form fields. The data confirms a layout sizing or script error on iOS Safari clients that blocks text element focus.Implement Price Transparency Models within Ad Funnels: The growth marketing division should adjust advertising copy templates for the Retargeting-Promo campaign cluster. Displaying local sales taxes and shipping minimums early in the journey will eliminate late-stage checkout price shock and stabilize top-of-funnel conversion value.

🔗 Live Interactive LinkExplore the functional logic and toggle dynamic optimization scenarios on the live dashboard: 
https://ecommerce-funnel-diagnostic.streamlit.app/
