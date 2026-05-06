#!/usr/bin/env python3
"""Generate 6 individual service landing pages for Digital Minds Solutions."""

SERVICES = [
    {
        "slug": "service-web",
        "num": "01",
        "anchor": "web",
        "title": "Web Development & App Solutions",
        "eyebrow": "Pillar One · Web Development",
        "meta_desc": "Digital Minds Solutions web development services — responsive websites, mobile apps, landing pages, and ecommerce built to convert. Lead-focused builds from day one.",
        "page_title": "Web Development & App Solutions — Digital Minds Solutions",
        "headline": "Websites &amp; apps that<br>generate leads from<br><span>launch day.</span>",
        "sub": "Lead-focused digital properties built to convert visitors, not just look good. Full-stack development. Mobile-first. Performance scores above 90. No outsourcing.",
        "accent": "#002FA7",
        "accent_rgb": "0,47,167",
        "hero_img": "../ASSETS/case-studies/Barceló Hotel/Barceló Hotel (1).jpg",
        "deliverables": [
            ("🖥️", "Responsive Website Design & Development", "Pixel-precise UI, mobile-first layouts, WCAG 2.2 AA accessibility, and performance scores above 90 on every device. Built to rank and convert from day one."),
            ("📱", "Mobile App Development — iOS & Android", "Native and cross-platform mobile apps built for real users. We design the UX, build the backend, and deliver app-store-ready products on schedule."),
            ("🎯", "High-Converting Landing Pages", "Single-purpose pages tied to specific offers, funnels, and paid campaigns. A/B testing frameworks and heat-map-ready structure from the start."),
            ("🛒", "Ecommerce Development & Optimisation", "Shopify, WooCommerce, and custom ecommerce builds optimised for conversion rate. Product page architecture, checkout flow, and Merchant Center integration."),
            ("⚡", "Core Web Vitals & Speed Optimisation", "LCP/CLS/FID fixes, image compression, code splitting, and CDN configuration. Every technical factor that affects how Google ranks and how users experience your site."),
            ("🔬", "Lead-Focused UI with Behaviour Analytics", "Designs built using heatmaps, session recordings, and AI-generated user intent data. Every button placement, headline, and CTA tested against real conversion data."),
            ("🔒", "Cybersecurity & Hosting Architecture", "SSL, WAF, regular vulnerability scanning, and secure hosting setup. We protect the digital property we build so it stays online and trusted."),
            ("📊", "CMS Integration & Content Management", "WordPress, Webflow, and headless CMS implementations. Your team can update content without touching code. We train you on launch day."),
        ],
        "process": [
            ("Week 1–2", "Discovery & Architecture", "Stakeholder interviews, competitor analysis, sitemap design, wireframes, and tech stack selection. You approve before we build."),
            ("Week 2–5", "Design & Development", "High-fidelity UI design in Figma, then full front-end and back-end development. Daily check-ins and staging environment from week 2."),
            ("Week 5–6", "QA, Speed & SEO", "Cross-browser testing, Lighthouse audits above 90, structured data markup, sitemap submission, and Google Search Console setup."),
            ("Week 6+", "Launch & Optimise", "Go-live with monitoring. We track Core Web Vitals, conversion events, and bounce rates. First optimisation sprint at 30 days post-launch."),
        ],
        "results": [
            ("+1,190%", "Search Impressions", "Barceló Hotel Group", "case-barcelo.html"),
            ("+400%", "Search Impressions", "Kitchen Supply Wholesale", "case-kitchen-supply.html"),
            ("+800%", "Landing Page Conversions", "Barceló Hotel Group", "case-barcelo.html"),
        ],
        "for_who": [
            ("🏢", "Established businesses", "Your current site is dated, slow, or not generating enquiries. You need a rebuild that looks premium and actually produces leads."),
            ("🚀", "Growth-stage companies", "You have traction but your digital presence doesn't match your product quality. You need a site that converts at the same rate your sales team does."),
            ("🌐", "International brands", "You need multilingual sites, multiple domains, or a content architecture that scales across markets without breaking."),
        ],
        "faqs": [
            ("How long does a website build take?", "A standard marketing website takes 4–6 weeks. A full ecommerce store or web app takes 8–14 weeks. We don't cut corners to hit artificial deadlines."),
            ("Do you build on WordPress or custom?", "Both. We recommend the right tool for your business — WordPress for content-heavy sites, custom builds for complex functionality, Webflow for marketing teams who need design control."),
            ("Will my site rank on Google?", "Every site we build includes on-page SEO, structured data, sitemap submission, and Core Web Vitals optimisation. It's not an add-on — it's the foundation."),
            ("Do you redesign existing sites?", "Yes. We audit your current site, identify what's working and what's not, then rebuild with your audience and conversion goals as the brief — not just aesthetics."),
            ("What happens after launch?", "We monitor for 30 days post-launch and run an optimisation sprint based on real user behaviour data. Ongoing retainers are available for continuous improvement."),
        ],
        "tools": ["React / Next.js", "HTML5 / CSS3", "Webflow", "WordPress", "Shopify", "iOS & Android", "Figma", "Core Web Vitals"],
        "prev_slug": None,
        "prev_title": None,
        "next_slug": "service-ai.html",
        "next_title": "AI Automation",
    },
    {
        "slug": "service-ai",
        "num": "02",
        "anchor": "ai",
        "title": "AI Automation & Business Systems",
        "eyebrow": "Pillar Two · AI Automation",
        "meta_desc": "AI chatbots, CRM automation, lead follow-up systems, and workflow automation built by Digital Minds Solutions. Your business runs while you sleep.",
        "page_title": "AI Automation & Business Systems — Digital Minds Solutions",
        "headline": "Your business runs<br>while you sleep.<br><span>AI makes it real.</span>",
        "sub": "Lead follow-up automated. Repetitive tasks eliminated. AI chatbot live in 5 days. Full CRM automation in 3 weeks. One team builds and manages the whole system.",
        "accent": "#002FA7",
        "accent_rgb": "0,47,167",
        "hero_img": "../ASSETS/case-studies/MyMedQ/ MyMedQ (1).jpg",
        "deliverables": [
            ("🤖", "AI Chatbots & Conversational Agents", "Custom-built AI assistants trained on your business knowledge. Qualify leads, answer FAQs, and book appointments 24/7 — without a human in the loop."),
            ("📩", "Lead Capture & Follow-Up Automation", "Every lead gets contacted within minutes, not hours. Automated email and WhatsApp sequences nurture prospects from first touch to booked call."),
            ("🔄", "CRM Integration & Workflow Automation", "HubSpot, GoHighLevel, Salesforce, and custom CRM builds. Your pipeline updates automatically. Your team focuses on selling, not admin."),
            ("📊", "Data Pipelines & Reporting Dashboards", "Automated data collection, cleaning, and visualisation. Real-time dashboards that show revenue, leads, and campaign performance in one place."),
            ("📧", "Email Marketing Automation", "Behavioural trigger sequences, list segmentation, A/B tested subject lines, and automated re-engagement flows. Average open rates above 28%."),
            ("🔗", "App & API Integration", "Zapier, Make, and custom webhook builds connecting your tools — CRM, calendar, payment gateway, analytics, and support desk — into one seamless system."),
            ("🧠", "Custom AI Model Training", "Fine-tuned language models trained on your products, policies, and tone. AI that sounds like your brand and knows your business inside out."),
            ("📱", "WhatsApp & SMS Automation", "Automated WhatsApp Business flows for lead qualification, appointment reminders, and post-purchase sequences. Response rates 4× higher than email."),
        ],
        "process": [
            ("Day 1–3", "Audit & Map", "We map your current lead flow, identify every manual touchpoint, and design the automation architecture. You see exactly what we're building before we build it."),
            ("Day 3–5", "Build & Test", "AI chatbot built, trained on your content, and tested with real conversations. Integration with your existing calendar, CRM, and communication tools."),
            ("Week 2–3", "Full CRM & Sequences", "Email sequences, WhatsApp flows, and pipeline automation deployed. Every trigger tested against real lead behaviour before going live."),
            ("Week 4+", "Monitor & Optimise", "We track open rates, reply rates, booking rates, and pipeline velocity. Weekly reports. Monthly optimisation sprints to improve every metric."),
        ],
        "results": [
            ("+300%", "Qualified Leads", "My Education Online", "case-meo.html"),
            ("+50%", "Organic Leads", "MyMedQ", "case-mymedq.html"),
            ("5 days", "Chatbot Live", "Typical AI Automation Delivery", "service-ai.html"),
        ],
        "for_who": [
            ("📞", "High-volume lead businesses", "You're getting leads but your team can't follow up fast enough. Automation means every lead gets a response in under 5 minutes, always."),
            ("🏥", "Service businesses", "Healthcare, education, fitness, legal, real estate — any service business where booking, qualification, and follow-up eat your team's time."),
            ("📈", "Scaling companies", "You're growing fast and your manual processes are breaking. AI systems that scale with you — without hiring three more people to run them."),
        ],
        "faqs": [
            ("Do I need to know how AI works?", "No. We build, train, and manage everything. You tell us how your business works — we build the system that automates it."),
            ("How quickly can an AI chatbot go live?", "A trained AI chatbot integrated with your website and WhatsApp Business can be live in 5 business days. Full CRM automation takes 3 weeks."),
            ("Will it sound like a robot?", "No. We train every chatbot on your brand voice, product knowledge, and real customer conversations. It handles routine queries and escalates complex ones to your team."),
            ("What CRM platforms do you work with?", "HubSpot, GoHighLevel, Salesforce, Pipedrive, and custom builds. We can also integrate with any tool that has an API or Zapier support."),
            ("What if a lead needs a human?", "Every automation has a defined escalation path. When a conversation reaches a point that requires a human, your team is notified instantly with full context."),
        ],
        "tools": ["OpenAI / Claude", "GoHighLevel", "HubSpot", "Zapier / Make", "WhatsApp Business API", "Twilio", "n8n", "Custom APIs"],
        "prev_slug": "service-web.html",
        "prev_title": "Web Development",
        "next_slug": "service-design.html",
        "next_title": "Design & Branding",
    },
    {
        "slug": "service-design",
        "num": "03",
        "anchor": "design",
        "title": "Graphic Design & Brand Identity",
        "eyebrow": "Pillar Three · Design & Branding",
        "meta_desc": "Brand identity, logo design, UI/UX, print, and visual content by Digital Minds Solutions. Design that makes premium brands look premium.",
        "page_title": "Graphic Design & Brand Identity — Digital Minds Solutions",
        "headline": "Design that makes<br>premium brands<br><span>look premium.</span>",
        "sub": "Brand identity systems that command trust. UI/UX that guides visitors to convert. Print, packaging, and social assets that look $50,000 quality — because they are.",
        "accent": "#E5A820",
        "accent_rgb": "229,168,32",
        "hero_img": "../ASSETS/case-studies/Santoba Tailors/Santoba Tailors (1).jpg",
        "deliverables": [
            ("🎨", "Brand Identity & Logo Design", "Full brand identity systems — logo suite, colour palette, typography, iconography, and brand guidelines. Every asset vector-ready and print/digital-ready on delivery."),
            ("📐", "UI/UX Design & Prototyping", "High-fidelity Figma prototypes tested with real users before a single line of code is written. Interaction design that guides visitors toward conversion."),
            ("📦", "Packaging & Print Design", "Product packaging, brochures, business cards, signage, and event materials. Print-ready files delivered in every format your printer requires."),
            ("📱", "Social Media Visual Design", "Branded templates for Instagram, LinkedIn, Facebook, and TikTok. Consistent visual identity across every channel your audience uses."),
            ("✉️", "Email Design & Template Systems", "HTML email templates designed for deliverability and conversion. Dark-mode compatible. Tested across Gmail, Outlook, and Apple Mail."),
            ("🎬", "Pitch Decks & Presentation Design", "Investor decks, sales presentations, and proposal designs that make complex ideas clear and compelling. Slide-by-slide storytelling that wins rooms."),
            ("🖼️", "Ad Creative & Campaign Visuals", "Performance-focused creative for Google, Meta, LinkedIn, and YouTube ads. Static, animated, and video ad formats built for the platform they run on."),
            ("🏷️", "Brand Refresh & Rebrand", "Strategic brand refresh for established businesses that have outgrown their current identity. We preserve brand equity while elevating perception."),
        ],
        "process": [
            ("Week 1", "Brand Discovery", "Brand audit, competitor landscape review, audience profiling, and positioning workshop. We define what your brand should say before we decide how it looks."),
            ("Week 1–2", "Concept Development", "3 distinct visual directions presented. Each with logo, colour palette, typography, and one real-world mockup. You choose and we develop."),
            ("Week 2–3", "Full System Build", "Complete brand identity system built — all logo variations, brand guidelines document, and application across your primary touchpoints."),
            ("Week 3–4", "Delivery & Handoff", "All files delivered in AI, EPS, SVG, PDF, PNG, and WEBP formats. Full brand guidelines PDF. Training session on brand application."),
        ],
        "results": [
            ("+22%", "Conversion Rate", "Christopher Radko", "case-christopher-radko.html"),
            ("+150%", "Landing Conversions", "Santoba Tailors", "case-santoba.html"),
            ("+34%", "Organic Traffic", "Christopher Radko", "case-christopher-radko.html"),
        ],
        "for_who": [
            ("👔", "Premium & luxury brands", "You're selling a high-ticket product or service. Your brand needs to communicate value before a prospect reads a single word of copy."),
            ("🚀", "Startups raising investment", "Your deck, your brand, and your digital presence are your first impression with investors. We make sure it's the right one."),
            ("🔄", "Established brands rebranding", "Your business has grown and your brand hasn't kept up. We refresh the identity without losing the recognition you've already built."),
        ],
        "faqs": [
            ("How many logo concepts do we get?", "We present 3 distinct directions in the first round. One is selected and refined through 2 rounds of revisions. The final system includes all variations you need."),
            ("Do you provide brand guidelines?", "Yes. Every brand identity project includes a comprehensive brand guidelines document — logo usage, colour values, typography rules, and do/don't examples."),
            ("What file formats do we receive?", "AI, EPS, SVG, PDF, PNG, and WEBP. Print-ready and screen-ready versions of every asset. You own everything outright on final payment."),
            ("Can you redesign our existing logo?", "Yes. We audit what's working about your current identity, identify what's holding it back, and evolve the design rather than replacing it wholesale — unless a full rebuild is clearly needed."),
            ("Do you design websites too?", "Yes — design and development are the same team here. No handoff between a design agency and a dev agency. We design and build in the same project."),
        ],
        "tools": ["Figma", "Adobe Illustrator", "Adobe Photoshop", "Adobe InDesign", "After Effects", "Canva Pro", "Principle", "Lottie"],
        "prev_slug": "service-ai.html",
        "prev_title": "AI Automation",
        "next_slug": "service-marketing.html",
        "next_title": "Digital Marketing",
    },
    {
        "slug": "service-marketing",
        "num": "04",
        "anchor": "marketing",
        "title": "Digital Marketing & Growth",
        "eyebrow": "Pillar Four · Digital Marketing",
        "meta_desc": "Paid ads, social media, email marketing, and full-funnel growth strategy by Digital Minds Solutions. Marketing that generates revenue, not just impressions.",
        "page_title": "Digital Marketing & Growth — Digital Minds Solutions",
        "headline": "Marketing that generates<br>revenue, not just<br><span>impressions.</span>",
        "sub": "Full-funnel paid and organic marketing across Google, Meta, LinkedIn, and email. Every campaign tied to real business outcomes — not vanity metrics.",
        "accent": "#002FA7",
        "accent_rgb": "0,47,167",
        "hero_img": "../ASSETS/case-studies/Gymnastika/Gymnastika (1).jpg",
        "deliverables": [
            ("🎯", "Google Ads — Search, Display & Shopping", "Keyword strategy, ad copy, bidding optimisation, and conversion tracking. Every pound and dollar spent tracked to pipeline, not clicks."),
            ("📘", "Meta Ads — Facebook & Instagram", "Audience segmentation, creative testing, retargeting sequences, and funnel-stage targeting. Average ROAS tracked weekly and optimised monthly."),
            ("💼", "LinkedIn Ads & B2B Lead Generation", "LinkedIn Lead Gen Forms, sponsored content, and account-based targeting for B2B businesses where decision-makers are on the platform."),
            ("📱", "Social Media Management & Content", "Monthly content calendars, copywriting, design, scheduling, and community management across the platforms your audience actually uses."),
            ("📧", "Email Marketing & Lifecycle Campaigns", "Segmented lists, behavioural triggers, A/B tested campaigns, and monthly reporting. Not newsletters — revenue-generating email systems."),
            ("🎬", "Video Marketing & YouTube Ads", "Video ad production, YouTube campaign management, and in-stream ad targeting. Video content that builds brand and drives measurable response."),
            ("📊", "Marketing Analytics & Attribution", "Google Analytics 4, Google Tag Manager, and custom attribution models. You know which channel drives revenue — not just which drives traffic."),
            ("🔁", "Retargeting & Funnel Re-Engagement", "Custom audiences from site visitors, email lists, and video viewers. Multi-touch retargeting sequences that bring warm prospects back to convert."),
        ],
        "process": [
            ("Week 1", "Audit & Strategy", "Full audit of your current marketing — ads, analytics, email, and organic. We identify what's wasting budget and where the real growth opportunity is."),
            ("Week 1–2", "Setup & Architecture", "Campaign architecture, tracking installation, audience building, and creative production. Everything configured before a single pound is spent."),
            ("Week 2–4", "Launch & Calibrate", "Campaigns live with controlled budget. We test audiences, creatives, and bidding strategies in parallel. First optimisation report at day 14."),
            ("Month 2+", "Scale & Compound", "Budget scaled to top-performing audiences and creatives. Monthly strategy sessions, quarterly audits, and continuous creative refresh."),
        ],
        "results": [
            ("+280%", "Landing Page Conversions", "Gymnastika UAE", "case-gymnastika.html"),
            ("+200%", "Landing Page Conversions", "My Education Online", "case-meo.html"),
            ("+200%", "Landing Page Conversions", "Gravity DXB", "case-gravity.html"),
        ],
        "for_who": [
            ("📈", "Businesses with a proven offer", "You know your product works. You need more people to see it and buy it. Paid marketing at scale is the fastest path."),
            ("🏋️", "Fitness, education & local services", "High-competition verticals where visibility is everything. We've generated leads for gyms, tutoring centres, and service businesses across UAE, UK, and USA."),
            ("🛒", "Ecommerce brands", "Google Shopping, Meta DPA, and email automation for product-led businesses. Every channel configured to maximise ROAS, not just traffic."),
        ],
        "faqs": [
            ("What's the minimum ad budget you work with?", "We work with monthly ad budgets from $1,500. Below that, there isn't enough data to optimise properly. Our management fee is separate from your ad spend."),
            ("How long before I see results?", "Paid ads typically show meaningful data within 2–4 weeks. SEO takes 3–6 months. We tell you the honest timeline upfront — not what you want to hear."),
            ("Do you handle creative production?", "Yes. Ad creative (static, video, and animated) is included in our full-service retainers. We produce, test, and replace creative based on performance data."),
            ("Which platforms do you manage?", "Google (Search, Display, Shopping, YouTube), Meta (Facebook & Instagram), LinkedIn, and TikTok. We recommend the right mix based on your audience, not our preferences."),
            ("Can you take over existing campaigns?", "Yes. We audit your current account, identify wasted spend and missed opportunities, then restructure before scaling. Most inherited accounts improve ROAS within 30 days."),
        ],
        "tools": ["Google Ads", "Meta Ads Manager", "LinkedIn Campaign Manager", "Google Analytics 4", "Google Tag Manager", "Klaviyo", "Mailchimp", "TikTok Ads"],
        "prev_slug": "service-design.html",
        "prev_title": "Design & Branding",
        "next_slug": "service-software.html",
        "next_title": "Software Development",
    },
    {
        "slug": "service-software",
        "num": "05",
        "anchor": "software",
        "title": "Software & Product Development",
        "eyebrow": "Pillar Five · Software Development",
        "meta_desc": "Custom software, SaaS products, APIs, and internal tools built by Digital Minds Solutions. From MVP to enterprise-scale systems — one team, no outsourcing.",
        "page_title": "Software & Product Development — Digital Minds Solutions",
        "headline": "Custom software built<br>for real business<br><span>problems.</span>",
        "sub": "SaaS platforms, internal tools, APIs, and enterprise systems. From MVP to production-scale. No outsourcing. One team. Every technical decision made with your business outcome as the brief.",
        "accent": "#002FA7",
        "accent_rgb": "0,47,167",
        "hero_img": "../ASSETS/case-studies/MyMedQ/ MyMedQ (1).jpg",
        "deliverables": [
            ("💻", "SaaS Product Development", "Full-stack SaaS platform development — subscription billing, user auth, multi-tenancy, and admin dashboards. From architecture to production deployment."),
            ("⚙️", "API Design & Backend Development", "RESTful and GraphQL APIs built for reliability and scale. Database architecture, caching, queuing, and documentation included on every project."),
            ("🏢", "Internal Tools & Business Systems", "Custom CRM, inventory management, reporting dashboards, and operational tools that replace expensive off-the-shelf software with exactly what your business needs."),
            ("🔗", "Third-Party Integrations", "Payment gateways, shipping APIs, ERP systems, CRM platforms, and any third-party service your business depends on — integrated and tested."),
            ("📱", "Progressive Web Apps (PWA)", "Mobile-app-quality experiences in the browser. Offline capability, push notifications, and install-to-homescreen — without the app store submission process."),
            ("🔒", "Security Architecture & Compliance", "GDPR, HIPAA, and SOC 2-aware development practices. Penetration testing, vulnerability scanning, and security audit reports included on enterprise projects."),
            ("☁️", "Cloud Infrastructure & DevOps", "AWS, GCP, and Azure deployment. CI/CD pipelines, containerisation with Docker, Kubernetes orchestration, and 99.9% uptime SLA configuration."),
            ("📊", "Analytics & Instrumentation", "Event tracking, funnel analysis, and product analytics integrated from day one. You know how users behave in your product before you scale."),
        ],
        "process": [
            ("Week 1–2", "Discovery & Architecture", "Requirements gathering, user story mapping, data model design, and technology selection. Detailed technical specification signed off before development begins."),
            ("Week 2–8", "MVP Development", "Iterative sprints with weekly demos on staging. You see working software from week 2 — not a Gantt chart and a promise."),
            ("Week 8–10", "QA & Security", "Automated test suite, manual QA, security audit, load testing, and performance profiling. Nothing ships that we wouldn't use ourselves."),
            ("Week 10+", "Launch & Scale", "Production deployment with monitoring, alerting, and on-call support. We stay on retainer for the first 60 days post-launch as standard."),
        ],
        "results": [
            ("+350%", "Search Impressions", "MyMedQ HealthTech Platform", "case-mymedq.html"),
            ("+900%", "Search Impressions", "Mercury Holidays App", "case-mercury.html"),
            ("14 wks", "Avg MVP Delivery", "Enterprise-grade SaaS", "service-software.html"),
        ],
        "for_who": [
            ("🏗️", "Founders building a product", "You have an idea, a brief, or a half-built product that needs a technical team to take it to market. We've been that team for healthtech, edtech, and travel platforms."),
            ("🏢", "Enterprises with legacy systems", "Your internal tools are breaking under growth. We build modern replacements that integrate with existing systems and eliminate the bottlenecks."),
            ("💡", "Non-technical business owners", "You know what your software needs to do — you just need a team that can translate that into a working product without requiring you to become a developer."),
        ],
        "faqs": [
            ("Do you build MVPs?", "Yes. We scope, design, and build MVPs in 8–14 weeks depending on complexity. Enough to validate with real users — not so much that you've spent 12 months building the wrong thing."),
            ("What stack do you build on?", "React / Next.js frontend, Node.js / Python backend, PostgreSQL / MongoDB databases, and AWS or GCP for hosting. We choose the right tools for each project — not the same tools for every project."),
            ("Who owns the code?", "You do, completely. On final payment, you receive full source code access, repository ownership, and all credentials. No lock-in, ever."),
            ("Do you take on ongoing maintenance?", "Yes. We offer monthly engineering retainers for updates, new features, performance monitoring, and security patches. Most clients stay with us post-launch."),
            ("Can you take over an existing codebase?", "Yes. We audit the codebase, document what exists, identify technical debt, and create a remediation plan before touching anything. We don't rewrite without evidence."),
        ],
        "tools": ["React / Next.js", "Node.js / Python", "PostgreSQL / MongoDB", "AWS / GCP", "Docker / Kubernetes", "GitHub Actions", "Stripe API", "Twilio"],
        "prev_slug": "service-marketing.html",
        "prev_title": "Digital Marketing",
        "next_slug": "service-seo.html",
        "next_title": "SEO / AEO / GEO / CRO",
    },
    {
        "slug": "service-seo",
        "num": "06",
        "anchor": "seo",
        "title": "SEO, AEO, GEO & CRO",
        "eyebrow": "Pillar Six · SEO / AEO / GEO / CRO",
        "meta_desc": "Search engine optimisation, AI answer engine optimisation, GEO, and conversion rate optimisation by Digital Minds Solutions. Rank now. Convert always.",
        "page_title": "SEO, AEO, GEO & CRO — Digital Minds Solutions",
        "headline": "Rank on Google.<br>Appear in AI answers.<br><span>Convert every visit.</span>",
        "sub": "Traditional SEO is table stakes. We optimise for Google, ChatGPT, Perplexity, and every AI answer engine that's replacing the search bar. Then we convert the traffic we send you.",
        "accent": "#E5A820",
        "accent_rgb": "229,168,32",
        "hero_img": "../ASSETS/case-studies/Look Family/Look Family (1).jpg",
        "deliverables": [
            ("🔍", "Technical SEO Audit & Remediation", "Full crawl analysis, Core Web Vitals fixes, sitemap architecture, robots.txt, canonical tags, hreflang, and structured data markup. The foundation everything else depends on."),
            ("✍️", "Content Strategy & SEO Copywriting", "Keyword research, search intent mapping, content briefs, and long-form SEO content written to rank and convert — not just fill a content calendar."),
            ("🤖", "AEO — AI Answer Engine Optimisation", "Optimise your content to appear in ChatGPT, Perplexity, Claude, and Google SGE answers. The next frontier of organic visibility, and most of your competitors haven't started."),
            ("🌍", "GEO — Generative Engine Optimisation", "Structured data, entity optimisation, and knowledge graph strategies that make your brand the trusted source AI systems cite when answering questions in your industry."),
            ("📍", "Local SEO & Google Business Profile", "Google Business Profile optimisation, local citation building, review strategy, and local pack ranking. For businesses where physical location matters."),
            ("📈", "CRO — Conversion Rate Optimisation", "Heatmaps, session recordings, A/B tests, and funnel analysis to find where visitors drop off — and fix it. Every percentage point of CRO improvement compounds forever."),
            ("🔗", "Link Building & Digital PR", "Editorial link acquisition through content marketing, digital PR, and strategic outreach. Domain authority built on quality, not quantity."),
            ("📊", "Monthly Reporting & Search Analytics", "Google Search Console, GA4, and custom dashboards. You know which keywords drive pipeline, not just which keywords you rank for."),
        ],
        "process": [
            ("Week 1–2", "Full Audit", "Technical crawl, keyword landscape analysis, competitor backlink audit, Core Web Vitals assessment, and content gap analysis. You get a prioritised action list."),
            ("Week 2–4", "Technical Fixes & Foundation", "All critical technical issues resolved. Sitemap, robots.txt, structured data, and canonical architecture corrected. Foundation set for everything that follows."),
            ("Month 2–3", "Content & Authority", "SEO content calendar launched, on-page optimisations deployed, and link building outreach begun. AEO and GEO optimisations applied to existing high-value pages."),
            ("Month 4+", "Compound Growth", "Rankings compound as authority builds. Monthly content, ongoing link acquisition, and CRO testing layers on top of a strengthening foundation."),
        ],
        "results": [
            ("+1,190%", "Search Impressions", "Barceló Hotel Group", "case-barcelo.html"),
            ("+280%", "Search Impressions", "Look Family Exteriors", "case-look-family.html"),
            ("+57%", "Search Rankings", "Christopher Radko", "case-christopher-radko.html"),
        ],
        "for_who": [
            ("🏗️", "Businesses with no organic presence", "You're paying for every lead through ads. SEO gives you a compounding asset — traffic that grows every month without a corresponding ad spend increase."),
            ("📉", "Sites hit by Google algorithm updates", "Your traffic dropped and you don't know why. We audit, diagnose, and recover — then protect you against the next update."),
            ("🌐", "Brands entering AI-first search", "You understand that ChatGPT, Perplexity, and Google AI Overviews are changing how customers find information. You want to be the brand they reference."),
        ],
        "faqs": [
            ("How long does SEO take to show results?", "Technical fixes show impact in 4–8 weeks. Content and authority building compounds over 3–6 months. Anyone promising top rankings in 30 days is selling something else."),
            ("What is AEO and why does it matter?", "AI Answer Engine Optimisation is the process of making your content appear in AI-generated answers from ChatGPT, Perplexity, Claude, and Google SGE. As more search happens through AI interfaces, AEO becomes as important as traditional SEO."),
            ("Do you guarantee rankings?", "No ethical agency does. We guarantee the work — comprehensive technical fixes, quality content, and sustainable link building. Rankings follow the work."),
            ("Can you do SEO without us changing the website?", "We can do a lot with on-page content changes and structured data additions. But the biggest gains usually require technical changes to the site. We flag this clearly in the audit."),
            ("How do you report on progress?", "Monthly reports covering keyword rankings, search impressions, organic clicks, and conversion attribution. Quarterly strategy sessions to review direction and adjust priorities."),
        ],
        "tools": ["Google Search Console", "Ahrefs", "Semrush", "Screaming Frog", "Google Analytics 4", "Google Tag Manager", "Schema.org", "Clearscope"],
        "prev_slug": "service-software.html",
        "prev_title": "Software Development",
        "next_slug": None,
        "next_title": None,
    },
]

# ─── TEMPLATE ────────────────────────────────────────────────────────────────

TEMPLATE = """\
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{meta_desc}">
<title>{page_title}</title>
<link rel="icon" type="image/png" href="../ASSETS/logo/favicon.png (512x512px).png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Inter:wght@400;500&family=Fira+Code:wght@400&display=swap" rel="stylesheet">
<style>
:root{{--deep-space:#08101E;--klein-blue:#002FA7;--amber-gold:#E5A820;--cobalt-shade:#243B6E;--muted-blue:#B8CBE8;--muted-ink:#3A4F7A;--card-dark:#0D1826;--card-border:#1E3055;--light-bg:#F4F7FF;--light-card:#FFFFFF;--light-border:#C5D3F0;--white:#FFFFFF;--accent:{accent};--font-head:'Plus Jakarta Sans',sans-serif;--font-body:'Inter',sans-serif;--r-sm:6px;--r-md:12px;--r-lg:20px;--r-xl:32px;--container:1280px;--nav-h:72px}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth}}
body{{font-family:var(--font-body);background:var(--deep-space);color:var(--white);overflow-x:hidden;-webkit-font-smoothing:antialiased;line-height:1.7}}
a{{text-decoration:none;color:inherit}}img{{display:block;max-width:100%}}ul{{list-style:none}}button{{cursor:pointer;border:none;background:none;font:inherit}}
.container{{max-width:var(--container);margin:0 auto;padding:0 40px}}
@media(max-width:768px){{.container{{padding:0 20px}}}}
.eyebrow{{display:inline-flex;align-items:center;gap:8px;font-family:var(--font-head);font-size:12px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--amber-gold);margin-bottom:20px}}
.eyebrow::before{{content:'';display:block;width:24px;height:2px;background:var(--amber-gold);border-radius:2px}}
.h2{{font-family:var(--font-head);font-size:clamp(28px,3.5vw,52px);font-weight:800;line-height:1.1;letter-spacing:-.025em}}
.h3{{font-family:var(--font-head);font-size:clamp(18px,1.8vw,24px);font-weight:700;line-height:1.25}}
.h4{{font-family:var(--font-head);font-size:16px;font-weight:700;line-height:1.3}}
.btn-gold{{display:inline-flex;align-items:center;gap:8px;background:var(--amber-gold);color:var(--deep-space);font-family:var(--font-head);font-size:15px;font-weight:700;padding:14px 28px;border-radius:var(--r-md);transition:transform .2s,box-shadow .2s}}
.btn-gold:hover{{transform:translateY(-2px);box-shadow:0 12px 40px rgba(229,168,32,.35)}}
.btn-ghost{{display:inline-flex;align-items:center;gap:8px;background:transparent;color:var(--white);font-family:var(--font-head);font-size:15px;font-weight:600;padding:14px 28px;border-radius:var(--r-md);border:1px solid var(--card-border);transition:border-color .2s,background .2s}}
.btn-ghost:hover{{border-color:var(--muted-blue);background:rgba(255,255,255,.04)}}
.gs{{opacity:0;transform:translateY(36px)}}
/* NAV */
#navbar{{position:fixed;top:0;left:0;right:0;height:var(--nav-h);z-index:1000;transition:background .3s,border-color .3s;border-bottom:1px solid transparent}}
#navbar.scrolled{{background:rgba(8,16,30,.88);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-color:var(--card-border)}}
.nav-inner{{max-width:var(--container);margin:0 auto;height:100%;display:flex;align-items:center;justify-content:space-between;gap:32px;padding:0 40px}}
.nav-logo img{{height:36px;width:auto}}
.nav-links{{display:flex;align-items:center;gap:4px;flex:1;justify-content:center}}
.nav-links a{{font-family:var(--font-head);font-size:14px;font-weight:600;color:var(--muted-blue);padding:8px 14px;border-radius:var(--r-sm);transition:color .2s,background .2s}}
.nav-links a:hover,.nav-links a.active{{color:var(--white);background:rgba(255,255,255,.06)}}
.nav-right{{display:flex;align-items:center;gap:12px}}
.theme-toggle{{width:38px;height:38px;border-radius:var(--r-sm);border:1px solid var(--card-border);display:flex;align-items:center;justify-content:center;color:var(--muted-blue);transition:color .2s,border-color .2s,background .2s}}
.theme-toggle:hover{{color:var(--white);border-color:var(--muted-blue);background:rgba(255,255,255,.06)}}
.theme-toggle svg{{width:18px;height:18px}}
.icon-sun{{display:none}}[data-theme="light"] .icon-moon{{display:none}}[data-theme="light"] .icon-sun{{display:block}}
.nav-hamburger{{display:none;width:38px;height:38px;border-radius:var(--r-sm);border:1px solid var(--card-border);flex-direction:column;align-items:center;justify-content:center;gap:5px}}
.nav-hamburger span{{display:block;width:18px;height:2px;background:var(--muted-blue);border-radius:2px;transition:transform .3s,opacity .3s}}
.nav-hamburger.active span:nth-child(1){{transform:translateY(7px) rotate(45deg)}}
.nav-hamburger.active span:nth-child(2){{opacity:0}}
.nav-hamburger.active span:nth-child(3){{transform:translateY(-7px) rotate(-45deg)}}
.mobile-menu{{position:fixed;inset:0;top:var(--nav-h);background:var(--deep-space);padding:40px 24px;opacity:0;visibility:hidden;transform:translateX(100%);transition:all .35s cubic-bezier(.16,1,.3,1);z-index:999;overflow-y:auto}}
.mobile-menu.open{{opacity:1;visibility:visible;transform:none}}
.mobile-menu .nav-links{{display:flex;flex-direction:column;align-items:flex-start;gap:4px}}
.mobile-menu .nav-links a{{font-size:22px;padding:12px 0;width:100%}}
.mobile-menu .m-ctas{{display:flex;flex-direction:column;gap:12px;margin-top:32px}}
@media(max-width:900px){{.nav-links{{display:none}}.nav-hamburger{{display:flex}}.nav-inner{{padding:0 20px}}}}
/* HERO */
#sv-hero{{position:relative;min-height:80vh;display:flex;align-items:flex-end;padding-bottom:80px;padding-top:calc(var(--nav-h) + 60px);overflow:hidden}}
.sv-hero-img{{position:absolute;inset:0;z-index:0}}
.sv-hero-img img{{width:100%;height:100%;object-fit:cover;opacity:.22}}
.sv-hero-overlay{{position:absolute;inset:0;z-index:1;background:linear-gradient(135deg,rgba(8,16,30,.98) 0%,rgba(8,16,30,.75) 55%,rgba({accent_rgb},.15) 100%)}}
.sv-hero-bottom{{position:absolute;bottom:0;left:0;right:0;height:180px;background:linear-gradient(to bottom,transparent,var(--deep-space));z-index:2}}
.sv-hero-content{{position:relative;z-index:3;max-width:900px}}
.sv-breadcrumb{{display:flex;align-items:center;gap:8px;font-family:var(--font-head);font-size:13px;font-weight:600;color:var(--muted-blue);margin-bottom:24px}}
.sv-breadcrumb a{{color:var(--muted-blue);transition:color .2s}}
.sv-breadcrumb a:hover{{color:var(--white)}}
.sv-breadcrumb span{{color:var(--card-border)}}
.sv-num{{font-family:var(--font-head);font-size:11px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--amber-gold);margin-bottom:12px;opacity:.7}}
.sv-hero-h1{{font-family:var(--font-head);font-size:clamp(34px,5vw,72px);font-weight:800;line-height:1.06;letter-spacing:-.03em;color:var(--white);margin-bottom:28px}}
.sv-hero-h1 span{{color:var(--amber-gold)}}
.sv-hero-sub{{font-size:clamp(16px,1.4vw,20px);color:var(--muted-blue);max-width:640px;margin-bottom:36px;line-height:1.7}}
.sv-hero-ctas{{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:48px}}
.sv-tools{{display:flex;gap:8px;flex-wrap:wrap}}
.sv-tool-chip{{font-family:var(--font-head);font-size:12px;font-weight:600;padding:6px 14px;border-radius:99px;background:rgba(255,255,255,.05);border:1px solid var(--card-border);color:var(--muted-blue)}}
@media(max-width:768px){{#sv-hero{{min-height:unset;padding-top:calc(var(--nav-h) + 32px);padding-bottom:48px;align-items:flex-start}}.sv-hero-h1{{font-size:clamp(28px,8vw,42px)}}.sv-hero-ctas{{flex-direction:column;gap:10px}}}}
/* DELIVERABLES */
#sv-deliverables{{padding:96px 0;background:var(--card-dark);border-top:1px solid var(--card-border)}}
.sv-del-header{{text-align:center;max-width:640px;margin:0 auto 64px}}
.sv-del-header .h2{{color:var(--white);margin-bottom:16px}}
.sv-del-header p{{color:var(--muted-blue);font-size:17px}}
.sv-del-grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:2px;background:var(--card-border);border-radius:var(--r-xl);overflow:hidden}}
.sv-del-item{{background:var(--card-dark);padding:40px 36px;transition:background .2s}}
.sv-del-item:hover{{background:rgba(255,255,255,.02)}}
.sv-del-icon{{font-size:28px;margin-bottom:16px}}
.sv-del-title{{font-family:var(--font-head);font-size:17px;font-weight:700;color:var(--white);margin-bottom:10px}}
.sv-del-desc{{font-size:15px;color:var(--muted-blue);line-height:1.65}}
@media(max-width:700px){{.sv-del-grid{{grid-template-columns:1fr}}.sv-del-item{{padding:28px 24px}}}}
/* PROCESS */
#sv-process{{padding:96px 0;background:var(--deep-space)}}
.sv-process-header{{max-width:540px;margin-bottom:64px}}
.sv-process-header .h2{{color:var(--white);margin-bottom:16px}}
.sv-process-header p{{color:var(--muted-blue);font-size:17px}}
.sv-process-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:0;position:relative}}
.sv-process-grid::before{{content:'';position:absolute;top:32px;left:calc(12.5%);right:calc(12.5%);height:1px;background:linear-gradient(to right,transparent,var(--card-border) 15%,var(--card-border) 85%,transparent);z-index:0}}
.sv-step{{position:relative;z-index:1;padding:0 24px;text-align:center}}
.sv-step-dot{{width:64px;height:64px;border-radius:50%;background:var(--card-dark);border:2px solid var(--accent);display:flex;align-items:center;justify-content:center;margin:0 auto 20px;font-family:var(--font-head);font-size:13px;font-weight:700;color:var(--amber-gold)}}
.sv-step-phase{{font-family:var(--font-head);font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--amber-gold);margin-bottom:8px}}
.sv-step-title{{font-family:var(--font-head);font-size:16px;font-weight:700;color:var(--white);margin-bottom:10px}}
.sv-step-desc{{font-size:14px;color:var(--muted-blue);line-height:1.6}}
@media(max-width:768px){{.sv-process-grid{{grid-template-columns:1fr;gap:32px}}.sv-process-grid::before{{display:none}}.sv-step{{padding:0;text-align:left;display:grid;grid-template-columns:64px 1fr;gap:0 24px;align-items:start}}.sv-step-dot{{margin:0}}.sv-step-phase,.sv-step-title,.sv-step-desc{{grid-column:2}}}}
/* RESULTS */
#sv-results{{padding:80px 0;background:var(--card-dark);border-top:1px solid var(--card-border);border-bottom:1px solid var(--card-border)}}
.sv-results-header{{text-align:center;max-width:540px;margin:0 auto 48px}}
.sv-results-header .h2{{color:var(--white);margin-bottom:12px}}
.sv-results-header p{{color:var(--muted-blue)}}
.sv-results-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}}
.sv-result-card{{background:var(--deep-space);border:1px solid var(--card-border);border-radius:var(--r-xl);padding:40px 32px;text-align:center;position:relative;overflow:hidden;transition:border-color .2s,transform .2s}}
.sv-result-card:hover{{border-color:rgba(229,168,32,.4);transform:translateY(-4px)}}
.sv-result-card::before{{content:'';position:absolute;top:-40px;left:50%;transform:translateX(-50%);width:200px;height:200px;border-radius:50%;background:radial-gradient(circle,rgba({accent_rgb},.08) 0%,transparent 70%);pointer-events:none}}
.sv-result-val{{font-family:var(--font-head);font-size:clamp(36px,4vw,56px);font-weight:800;color:var(--amber-gold);line-height:1;margin-bottom:10px}}
.sv-result-label{{font-family:var(--font-head);font-size:13px;font-weight:600;color:var(--white);margin-bottom:6px}}
.sv-result-client{{font-size:12px;color:var(--muted-blue)}}
.sv-result-link{{display:inline-flex;align-items:center;gap:4px;font-family:var(--font-head);font-size:12px;font-weight:700;color:var(--amber-gold);margin-top:12px;transition:opacity .2s}}
.sv-result-link:hover{{opacity:.7}}
@media(max-width:768px){{.sv-results-grid{{grid-template-columns:1fr}}}}
/* FOR WHO */
#sv-forwho{{padding:96px 0;background:var(--deep-space)}}
.sv-forwho-header{{max-width:540px;margin:0 auto 56px;text-align:center}}
.sv-forwho-header .h2{{color:var(--white);margin-bottom:16px}}
.sv-forwho-header p{{color:var(--muted-blue)}}
.sv-forwho-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}}
.sv-who-card{{background:var(--card-dark);border:1px solid var(--card-border);border-radius:var(--r-xl);padding:40px 32px}}
.sv-who-icon{{font-size:32px;margin-bottom:20px}}
.sv-who-title{{font-family:var(--font-head);font-size:17px;font-weight:700;color:var(--white);margin-bottom:12px}}
.sv-who-desc{{font-size:15px;color:var(--muted-blue);line-height:1.65}}
@media(max-width:768px){{.sv-forwho-grid{{grid-template-columns:1fr}}}}
/* FAQ */
#sv-faq{{padding:96px 0;background:var(--card-dark);border-top:1px solid var(--card-border)}}
.sv-faq-header{{max-width:540px;margin:0 auto 56px;text-align:center}}
.sv-faq-header .h2{{color:var(--white);margin-bottom:12px}}
.sv-faq-header p{{color:var(--muted-blue)}}
.sv-faq-list{{max-width:800px;margin:0 auto;display:flex;flex-direction:column;gap:0}}
.sv-faq-item{{border-bottom:1px solid var(--card-border)}}
.sv-faq-q{{font-family:var(--font-head);font-size:17px;font-weight:700;color:var(--white);padding:28px 0;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:16px;transition:color .2s}}
.sv-faq-q:hover{{color:var(--amber-gold)}}
.sv-faq-icon{{width:28px;height:28px;border-radius:50%;border:1px solid var(--card-border);display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:16px;transition:transform .3s,background .2s,border-color .2s;color:var(--muted-blue)}}
.sv-faq-item.open .sv-faq-icon{{transform:rotate(45deg);background:var(--amber-gold);border-color:var(--amber-gold);color:var(--deep-space)}}
.sv-faq-a{{font-size:16px;color:var(--muted-blue);line-height:1.75;max-height:0;overflow:hidden;transition:max-height .35s cubic-bezier(.16,1,.3,1),padding .35s}}
.sv-faq-item.open .sv-faq-a{{max-height:400px;padding-bottom:28px}}
/* CTA */
#sv-cta{{padding:120px 0;background:var(--deep-space);text-align:center;position:relative;overflow:hidden}}
#sv-cta::before{{content:'';position:absolute;top:-120px;left:50%;transform:translateX(-50%);width:800px;height:800px;border-radius:50%;background:radial-gradient(circle,rgba({accent_rgb},.14) 0%,transparent 70%);pointer-events:none}}
.sv-cta-inner{{position:relative;z-index:1;max-width:640px;margin:0 auto}}
.sv-cta-inner .h2{{color:var(--white);margin-bottom:20px}}
.sv-cta-inner p{{color:var(--muted-blue);font-size:18px;margin-bottom:40px;line-height:1.7}}
.sv-cta-btns{{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}}
/* SERVICE NAV */
#sv-nav{{padding:48px 0;background:var(--card-dark);border-top:1px solid var(--card-border)}}
.sv-nav-inner{{display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap}}
.sv-nav-link{{display:flex;flex-direction:column;gap:4px;max-width:260px}}
.sv-nav-link span{{font-family:var(--font-head);font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--muted-blue)}}
.sv-nav-link strong{{font-family:var(--font-head);font-size:16px;font-weight:700;color:var(--white);transition:color .2s}}
.sv-nav-link:hover strong{{color:var(--amber-gold)}}
.sv-nav-all{{font-family:var(--font-head);font-size:14px;font-weight:700;color:var(--amber-gold);border:1px solid rgba(229,168,32,.35);padding:10px 20px;border-radius:var(--r-md);transition:background .2s}}
.sv-nav-all:hover{{background:rgba(229,168,32,.08)}}
/* FOOTER */
#footer{{background:var(--card-dark);border-top:1px solid var(--card-border);padding:64px 0 32px}}
.footer-grid{{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:48px;margin-bottom:48px}}
.footer-brand img{{height:32px;margin-bottom:16px}}
.footer-brand p{{font-size:14px;color:var(--muted-blue);line-height:1.65;max-width:280px}}
.footer-col-title{{font-family:var(--font-head);font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--white);margin-bottom:20px}}
.footer-col ul{{display:flex;flex-direction:column;gap:10px}}
.footer-col ul a{{font-size:14px;color:var(--muted-blue);transition:color .2s}}
.footer-col ul a:hover{{color:var(--white)}}
.footer-bottom{{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px;padding-top:32px;border-top:1px solid var(--card-border)}}
.footer-bottom p,.footer-bottom a{{font-size:13px;color:var(--muted-blue)}}
.footer-bottom a:hover{{color:var(--white)}}
.social-link{{width:36px;height:36px;border-radius:var(--r-sm);border:1px solid var(--card-border);display:flex;align-items:center;justify-content:center;color:var(--muted-blue);font-size:14px;transition:color .2s,border-color .2s,background .2s}}
.social-link:hover{{color:var(--white);border-color:var(--muted-blue);background:rgba(255,255,255,.06)}}
@media(max-width:900px){{.footer-grid{{grid-template-columns:1fr 1fr}}}}
@media(max-width:600px){{.footer-grid{{grid-template-columns:1fr}}}}
/* WhatsApp */
.wa-float{{position:fixed;bottom:28px;right:28px;z-index:998;width:56px;height:56px;border-radius:50%;background:#25D366;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 32px rgba(37,211,102,.4);transition:transform .2s}}
.wa-float:hover{{transform:scale(1.1)}}
.wa-float svg{{width:28px;height:28px;fill:white}}
.wa-tooltip{{position:absolute;right:68px;top:50%;transform:translateY(-50%) translateX(8px);background:var(--card-dark);border:1px solid var(--card-border);color:var(--white);border-radius:var(--r-md);padding:8px 14px;font-family:var(--font-head);font-size:13px;font-weight:600;white-space:nowrap;pointer-events:none;opacity:0;transition:all .2s}}
.wa-float:hover .wa-tooltip{{opacity:1;transform:translateY(-50%) translateX(0)}}
/* COOKIE */
#cookieBanner{{position:fixed;bottom:0;left:0;right:0;z-index:1100;background:rgba(13,24,38,.97);border-top:1px solid #1E3055;backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);transform:translateY(100%);transition:transform .4s cubic-bezier(.16,1,.3,1);padding:20px 0}}
#cookieBanner.visible{{transform:none}}
.cookie-inner{{max-width:1280px;margin:0 auto;padding:0 40px;display:flex;align-items:center;gap:32px;flex-wrap:wrap}}
.cookie-text{{flex:1;min-width:260px}}
.cookie-text p{{font-size:14px;color:#B8CBE8;line-height:1.6}}
.cookie-text strong{{color:#fff}}
.cookie-text a{{color:#E5A820;text-decoration:underline;text-underline-offset:3px}}
.cookie-btns{{display:flex;gap:12px;flex-shrink:0}}
.cookie-accept{{font-family:'Plus Jakarta Sans',sans-serif;font-size:14px;font-weight:700;padding:10px 22px;border-radius:10px;background:#E5A820;color:#08101E;cursor:pointer;border:none;transition:background .2s}}
.cookie-accept:hover{{background:#f0b820}}
.cookie-decline{{font-family:'Plus Jakarta Sans',sans-serif;font-size:14px;font-weight:600;padding:10px 22px;border-radius:10px;background:transparent;color:#B8CBE8;border:1px solid #1E3055;cursor:pointer;transition:border-color .2s,color .2s}}
.cookie-decline:hover{{border-color:#B8CBE8;color:#fff}}
@media(max-width:600px){{.cookie-inner{{padding:0 20px;gap:16px}}.cookie-btns{{width:100%}}.cookie-accept,.cookie-decline{{flex:1;text-align:center}}}}
</style>
</head>
<body>

<!-- NAV -->
<nav id="navbar">
  <div class="nav-inner">
    <a href="index.html" class="nav-logo"><img src="../ASSETS/logo/logo-main.svg.png" alt="Digital Minds Solutions"></a>
    <ul class="nav-links">
      <li><a href="index.html">Home</a></li>
      <li><a href="about.html">About</a></li>
      <li><a href="work.html">Work</a></li>
      <li><a href="services.html" class="active">Services</a></li>
      <li><a href="pricing.html">Pricing</a></li>
      <li><a href="insights.html">Insights</a></li>
    </ul>
    <div class="nav-right">
      <button class="theme-toggle" id="themeToggle"><svg class="icon-moon" viewBox="0 0 24 24" fill="none"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg><svg class="icon-sun" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="5" stroke="currentColor" stroke-width="1.8"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></button>
      <a href="https://cal.com/digitalminds-fx51uj" class="btn-gold">Book a Free Call</a>
      <button class="nav-hamburger" id="navHamburger"><span></span><span></span><span></span></button>
    </div>
  </div>
</nav>
<div class="mobile-menu" id="mobileMenu">
  <ul class="nav-links"><li><a href="index.html">Home</a></li><li><a href="about.html">About</a></li><li><a href="work.html">Work</a></li><li><a href="services.html">Services</a></li><li><a href="pricing.html">Pricing</a></li><li><a href="insights.html">Insights</a></li></ul>
  <div class="m-ctas"><a href="https://cal.com/digitalminds-fx51uj" class="btn-gold">Book a Free Discovery Call</a><a href="https://wa.me/447426427646" class="btn-ghost" target="_blank">WhatsApp Us</a></div>
</div>

<!-- HERO -->
<section id="sv-hero">
  <div class="sv-hero-img"><img src="{hero_img}" alt="{title}" loading="eager"></div>
  <div class="sv-hero-overlay"></div>
  <div class="sv-hero-bottom"></div>
  <div class="container">
    <div class="sv-hero-content">
      <div class="sv-breadcrumb">
        <a href="index.html">Home</a>
        <span>/</span>
        <a href="services.html">Services</a>
        <span>/</span>
        <span style="color:var(--white)">{title}</span>
      </div>
      <div class="sv-num gs">{eyebrow}</div>
      <h1 class="sv-hero-h1 gs">{headline}</h1>
      <p class="sv-hero-sub gs">{sub}</p>
      <div class="sv-hero-ctas gs">
        <a href="https://cal.com/digitalminds-fx51uj" class="btn-gold">Get a Free Proposal →</a>
        <a href="services.html" class="btn-ghost">All Services →</a>
      </div>
      <div class="sv-tools gs">{tool_chips}</div>
    </div>
  </div>
</section>

<!-- DELIVERABLES -->
<section id="sv-deliverables">
  <div class="container">
    <div class="sv-del-header">
      <div class="eyebrow gs">What's Included</div>
      <h2 class="h2 gs">Everything your business needs.<br>Nothing it doesn't.</h2>
      <p class="gs">Every deliverable below is built in-house by the same team. No outsourcing. No handoffs. No surprises.</p>
    </div>
    <div class="sv-del-grid gs">
{deliverable_items}
    </div>
  </div>
</section>

<!-- PROCESS -->
<section id="sv-process">
  <div class="container">
    <div class="sv-process-header">
      <div class="eyebrow gs">How It Works</div>
      <h2 class="h2 gs">From brief to<br>measurable results.</h2>
      <p class="gs">A clear process, honest timelines, and no surprises. You know what's happening at every step.</p>
    </div>
    <div class="sv-process-grid">
{process_steps}
    </div>
  </div>
</section>

<!-- RESULTS -->
<section id="sv-results">
  <div class="container">
    <div class="sv-results-header">
      <div class="eyebrow gs">Proven Results</div>
      <h2 class="h2 gs">Real clients.<br>Real numbers.</h2>
      <p class="gs">Not estimates. Not case-study cherry-picks. These are actual outcomes from named businesses in this service category.</p>
    </div>
    <div class="sv-results-grid gs">
{result_cards}
    </div>
  </div>
</section>

<!-- FOR WHO -->
<section id="sv-forwho">
  <div class="container">
    <div class="sv-forwho-header">
      <div class="eyebrow gs">Who It's For</div>
      <h2 class="h2 gs">Right for your business?</h2>
      <p class="gs">We work with businesses at specific stages. Here's who gets the most from this service.</p>
    </div>
    <div class="sv-forwho-grid gs">
{who_cards}
    </div>
  </div>
</section>

<!-- FAQ -->
<section id="sv-faq">
  <div class="container">
    <div class="sv-faq-header">
      <div class="eyebrow gs">FAQ</div>
      <h2 class="h2 gs">Questions we always<br>get asked.</h2>
      <p class="gs">Honest answers. No marketing fluff.</p>
    </div>
    <div class="sv-faq-list">
{faq_items}
    </div>
  </div>
</section>

<!-- CTA -->
<section id="sv-cta">
  <div class="container">
    <div class="sv-cta-inner">
      <div class="eyebrow gs" style="justify-content:center">Start Here</div>
      <h2 class="h2 gs">Ready to get<br>started?</h2>
      <p class="gs">Book a free 30-minute call. No pitch deck. No commitment. Just a clear conversation about your situation and what we'd do about it.</p>
      <div class="sv-cta-btns gs">
        <a href="https://cal.com/digitalminds-fx51uj" class="btn-gold">Book a Free Discovery Call →</a>
        <a href="https://wa.me/447426427646?text=Hi%2C%20I%27d%20like%20to%20discuss%20your%20services" class="btn-ghost" target="_blank">WhatsApp Us →</a>
      </div>
      <p style="margin-top:20px;font-size:13px;color:var(--muted-blue);font-family:var(--font-head);font-weight:600">Response within 24hrs · No commitment · Free 30-min discovery call</p>
    </div>
  </div>
</section>

<!-- SERVICE NAV -->
<section id="sv-nav">
  <div class="container">
    <div class="sv-nav-inner">
      {prev_nav}
      <a href="services.html" class="sv-nav-all">All Services ↗</a>
      {next_nav}
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer id="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand"><img src="../ASSETS/logo/logo-white.svg.png" alt="Digital Minds Solutions"><p>Web development, AI automation, branding, marketing, and software. One team. No handoffs. Real results.</p><div style="display:flex;gap:12px;margin-top:20px"><a href="#" class="social-link">in</a><a href="#" class="social-link">ig</a><a href="https://youtu.be/96FyvCDcxRA" class="social-link" target="_blank">▶</a><a href="#" class="social-link">𝕏</a></div></div>
      <div class="footer-col"><div class="footer-col-title">Services</div><ul><li><a href="service-web.html">Web Development</a></li><li><a href="service-ai.html">AI Automation</a></li><li><a href="service-design.html">Design & Branding</a></li><li><a href="service-marketing.html">Digital Marketing</a></li><li><a href="service-software.html">Software Dev</a></li><li><a href="service-seo.html">SEO / AEO / GEO / CRO</a></li></ul></div>
      <div class="footer-col"><div class="footer-col-title">Company</div><ul><li><a href="about.html">About Us</a></li><li><a href="work.html">Our Work</a></li><li><a href="pricing.html">Pricing</a></li><li><a href="insights.html">Insights</a></li><li><a href="contact.html">Contact</a></li><li><a href="privacy.html">Privacy Policy</a></li></ul></div>
      <div class="footer-col"><div class="footer-col-title">Get In Touch</div><ul><li><a href="https://cal.com/digitalminds-fx51uj" target="_blank">Book a Discovery Call</a></li><li><a href="https://wa.me/447426427646" target="_blank">WhatsApp Us</a></li><li><a href="mailto:digitalmindss01@gmail.com">digitalmindss01@gmail.com</a></li><li><a href="tel:+447426427646">+44 7426 427646</a></li></ul></div>
    </div>
    <div class="footer-bottom"><p>© 2025 Digital Minds Solutions. All rights reserved. US-registered company.</p><p><a href="privacy.html">Privacy Policy</a> &nbsp;·&nbsp; <a href="terms.html">Terms of Service</a></p></div>
  </div>
</footer>

<a href="https://wa.me/447426427646?text=Hi%2C%20I%27d%20like%20to%20learn%20more%20about%20Digital%20Minds%20Solutions" class="wa-float" target="_blank" rel="noopener">
  <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
  <div class="wa-tooltip">WhatsApp us directly</div>
</a>

<!-- COOKIE CONSENT -->
<div id="cookieBanner" role="dialog" aria-label="Cookie consent" aria-live="polite">
  <div class="cookie-inner">
    <div class="cookie-text"><p><strong>We use cookies</strong> to improve your experience, analyse traffic, and personalise content. By clicking "Accept", you consent to our use of cookies. Read our <a href="privacy.html">Privacy Policy</a>.</p></div>
    <div class="cookie-btns">
      <button id="cookieDecline" class="cookie-decline">Decline</button>
      <button id="cookieAccept" class="cookie-accept">Accept All</button>
    </div>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script>
(function(){{
  'use strict';
  const root=document.documentElement,saved=localStorage.getItem('dms-theme'),preferred=window.matchMedia('(prefers-color-scheme: light)').matches?'light':'dark';
  root.setAttribute('data-theme',saved||preferred);
  document.getElementById('themeToggle').addEventListener('click',()=>{{const next=root.getAttribute('data-theme')==='dark'?'light':'dark';root.setAttribute('data-theme',next);localStorage.setItem('dms-theme',next);}});
  const navbar=document.getElementById('navbar');
  window.addEventListener('scroll',()=>navbar.classList.toggle('scrolled',window.scrollY>60),{{passive:true}});
  const hb=document.getElementById('navHamburger'),mm=document.getElementById('mobileMenu');
  hb.addEventListener('click',()=>{{hb.classList.toggle('active');mm.classList.toggle('open');document.body.style.overflow=mm.classList.contains('open')?'hidden':'';}});
  mm.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{{hb.classList.remove('active');mm.classList.remove('open');document.body.style.overflow=''}}));
  /* FAQ accordion */
  document.querySelectorAll('.sv-faq-q').forEach(q=>{{
    q.addEventListener('click',()=>{{
      const item=q.closest('.sv-faq-item');
      const wasOpen=item.classList.contains('open');
      document.querySelectorAll('.sv-faq-item').forEach(i=>i.classList.remove('open'));
      if(!wasOpen) item.classList.add('open');
    }});
  }});
  /* GSAP */
  gsap.registerPlugin(ScrollTrigger);
  gsap.utils.toArray('#sv-hero .gs').forEach((el,i)=>{{gsap.fromTo(el,{{opacity:0,y:30}},{{opacity:1,y:0,duration:.8,ease:'power2.out',delay:.1+i*.15}});}});
  gsap.utils.toArray('.gs:not(#sv-hero .gs)').forEach(el=>{{
    gsap.fromTo(el,{{opacity:0,y:40}},{{opacity:1,y:0,duration:.75,ease:'power2.out',scrollTrigger:{{trigger:el,start:'top 88%',toggleActions:'play none none none'}}}});
  }});
  /* COOKIE */
  (function(){{
    var COOKIE_KEY='dms_cookie_consent';
    var banner=document.getElementById('cookieBanner');
    if(!banner)return;
    if(!localStorage.getItem(COOKIE_KEY)){{setTimeout(function(){{banner.classList.add('visible')}},1400);}}
    document.getElementById('cookieAccept').addEventListener('click',function(){{localStorage.setItem(COOKIE_KEY,'accepted');banner.classList.remove('visible');}});
    document.getElementById('cookieDecline').addEventListener('click',function(){{localStorage.setItem(COOKIE_KEY,'declined');banner.classList.remove('visible');}});
  }})();
}})();
</script>
<!-- CAL.COM POPUP EMBED -->
<script type="text/javascript">
(function(C,A,L){{
  let p=function(a,ar){{a.q.push(ar)}};let d=C.document;
  C.Cal=C.Cal||function(){{let cal=C.Cal;let ar=arguments;if(!cal.loaded){{cal.ns={{}};cal.q=cal.q||[];d.head.appendChild(d.createElement("script")).src=A;cal.loaded=true}}if(ar[0]===L){{const api=function(){{p(api,arguments)}};const namespace=ar[1];api.q=api.q||[];if(typeof namespace==="string"){{cal.ns[namespace]=cal.ns[namespace]||api;p(cal.ns[namespace],ar);p(cal,[L,namespace,ar[2]])}}else p(cal,[L,ar[1]]);return}}p(cal,ar)}};
}})(window,"https://app.cal.com/embed/embed.js","init");
Cal("init",{{origin:"https://cal.com"}});
Cal("ui",{{theme:"dark",styles:{{branding:{{brandColor:"#002FA7"}}}},hideEventTypeDetails:false,layout:"month_view"}});
document.querySelectorAll('a[href="https://cal.com/digitalminds-fx51uj"]').forEach(function(el){{
  if(!el.closest('footer')){{el.addEventListener('click',function(e){{e.preventDefault();Cal('modal',{{calLink:'digitalminds-fx51uj',config:{{layout:'month_view'}}}});}});}}}});
<\/script>
</body>
</html>
"""

def build_tool_chips(tools):
    return ''.join(f'<span class="sv-tool-chip">{t}</span>' for t in tools)

def build_deliverables(items):
    html = ""
    for icon, title, desc in items:
        html += f"""      <div class="sv-del-item">
        <div class="sv-del-icon">{icon}</div>
        <div class="sv-del-title">{title}</div>
        <div class="sv-del-desc">{desc}</div>
      </div>\n"""
    return html

def build_process(steps):
    html = ""
    for i, (phase, title, desc) in enumerate(steps, 1):
        html += f"""      <div class="sv-step gs">
        <div class="sv-step-dot">0{i}</div>
        <div class="sv-step-phase">{phase}</div>
        <div class="sv-step-title">{title}</div>
        <div class="sv-step-desc">{desc}</div>
      </div>\n"""
    return html

def build_results(items):
    html = ""
    for val, label, client, link in items:
        html += f"""      <div class="sv-result-card">
        <div class="sv-result-val">{val}</div>
        <div class="sv-result-label">{label}</div>
        <div class="sv-result-client">{client}</div>
        <a href="{link}" class="sv-result-link">View Case Study →</a>
      </div>\n"""
    return html

def build_who(items):
    html = ""
    for icon, title, desc in items:
        html += f"""      <div class="sv-who-card gs">
        <div class="sv-who-icon">{icon}</div>
        <div class="sv-who-title">{title}</div>
        <div class="sv-who-desc">{desc}</div>
      </div>\n"""
    return html

def build_faqs(items):
    html = ""
    for i, (q, a) in enumerate(items):
        html += f"""      <div class="sv-faq-item">
        <div class="sv-faq-q">{q}<span class="sv-faq-icon">+</span></div>
        <div class="sv-faq-a">{a}</div>
      </div>\n"""
    return html

def build_nav(c):
    if c["prev_slug"]:
        prev = f'<a href="{c["prev_slug"]}" class="sv-nav-link"><span>← Previous Service</span><strong>{c["prev_title"]}</strong></a>'
    else:
        prev = '<div></div>'
    if c["next_slug"]:
        nxt = f'<a href="{c["next_slug"]}" class="sv-nav-link" style="text-align:right"><span>Next Service →</span><strong>{c["next_title"]}</strong></a>'
    else:
        nxt = '<div></div>'
    return prev, nxt

def build(c):
    prev_nav, next_nav = build_nav(c)
    html = TEMPLATE.format(
        slug=c["slug"],
        title=c["title"],
        eyebrow=c["eyebrow"],
        meta_desc=c["meta_desc"],
        page_title=c["page_title"],
        headline=c["headline"],
        sub=c["sub"],
        accent=c["accent"],
        accent_rgb=c["accent_rgb"],
        hero_img=c["hero_img"],
        num=c["num"],
        tool_chips=build_tool_chips(c["tools"]),
        deliverable_items=build_deliverables(c["deliverables"]),
        process_steps=build_process(c["process"]),
        result_cards=build_results(c["results"]),
        who_cards=build_who(c["for_who"]),
        faq_items=build_faqs(c["faqs"]),
        prev_nav=prev_nav,
        next_nav=next_nav,
    )
    fname = f'{c["slug"]}.html'
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'BUILT: {fname}')

if __name__ == '__main__':
    for s in SERVICES:
        build(s)
    print(f'\nDone — {len(SERVICES)} service pages generated.')
