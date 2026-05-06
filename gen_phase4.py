#!/usr/bin/env python3
"""Phase 4: Inject JSON-LD schema + Open Graph + Twitter Card meta into all 28 pages."""

import json, re, os

BASE = "https://digitalmindssolutions.com"
OG_DEFAULT = f"{BASE}/assets/og/og-default.jpg"
TWITTER = "@DigitalMindsSol"

ORG = {
    "@type": "Organization",
    "@id": f"{BASE}/#organization",
    "name": "Digital Minds Solutions",
    "url": BASE,
    "logo": {"@type": "ImageObject", "url": f"{BASE}/assets/logo/logo-white.svg.png"},
    "description": "Web development, AI automation, branding, digital marketing, and software. One team. No outsourcing. Real results.",
    "address": {"@type": "PostalAddress", "addressLocality": "Houston", "addressRegion": "TX", "addressCountry": "US"},
    "contactPoint": [
        {"@type": "ContactPoint", "telephone": "+44-7426-427646", "contactType": "customer service", "availableLanguage": "English"},
        {"@type": "ContactPoint", "email": "digitalmindss01@gmail.com", "contactType": "sales"}
    ],
    "sameAs": ["https://www.linkedin.com/company/digital-minds-solutions", "https://www.instagram.com/digitalminds_solution"]
}

# ── Page definitions ──────────────────────────────────────────────────────────
PAGES = [
    {
        "file": "index.html",
        "url": f"{BASE}/",
        "og_type": "website",
        "title": "Digital Minds Solutions — Web, AI & Marketing Agency | Houston, TX",
        "desc": "One team. No outsourcing. Web development, AI automation, branding, and marketing that generates real revenue. 12 named clients. Real results.",
        "og_img": OG_DEFAULT,
        "schema": [
            {"@context": "https://schema.org", "@graph": [
                ORG,
                {"@type": "WebSite", "@id": f"{BASE}/#website", "url": BASE, "name": "Digital Minds Solutions",
                 "potentialAction": {"@type": "SearchAction", "target": {"@type": "EntryPoint", "urlTemplate": f"{BASE}/work?q={{search_term_string}}"}, "query-input": "required name=search_term_string"}},
                {"@type": "LocalBusiness", "@id": f"{BASE}/#localbusiness", "name": "Digital Minds Solutions",
                 "url": BASE, "telephone": "+44-7426-427646", "email": "digitalmindss01@gmail.com",
                 "address": {"@type": "PostalAddress", "addressLocality": "Houston", "addressRegion": "TX", "addressCountry": "US"},
                 "priceRange": "$$$", "openingHours": "Mo-Fr 09:00-18:00",
                 "servesCuisine": None,
                 "aggregateRating": {"@type": "AggregateRating", "ratingValue": "5", "reviewCount": "12"}}
            ]}
        ]
    },
    {
        "file": "about.html",
        "url": f"{BASE}/about",
        "og_type": "website",
        "title": "About Digital Minds Solutions — Houston Digital Agency",
        "desc": "15+ years experience. Two founders. One team. No outsourcing. Web, AI, design, marketing, and software built by the same people every time.",
        "og_img": OG_DEFAULT,
        "schema": [{"@context": "https://schema.org", "@graph": [
            ORG,
            {"@type": "AboutPage", "@id": f"{BASE}/about#webpage", "url": f"{BASE}/about",
             "name": "About Digital Minds Solutions", "isPartOf": {"@id": f"{BASE}/#website"},
             "description": "15+ years experience. Two founders. One team. No outsourcing."}
        ]}]
    },
    {
        "file": "services.html",
        "url": f"{BASE}/services",
        "og_type": "website",
        "title": "Services — Web, AI, Design, Marketing & Software | Digital Minds Solutions",
        "desc": "6 service pillars. One team. Web development, AI automation, graphic design, digital marketing, software development, SEO/AEO/GEO/CRO. No outsourcing.",
        "og_img": OG_DEFAULT,
        "schema": [{"@context": "https://schema.org", "@graph": [
            ORG,
            {"@type": "WebPage", "@id": f"{BASE}/services#webpage", "url": f"{BASE}/services",
             "name": "Services — Digital Minds Solutions", "isPartOf": {"@id": f"{BASE}/#website"}},
            {"@type": "ItemList", "name": "Digital Minds Solutions Services", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Web Development & App Solutions", "url": f"{BASE}/service-web"},
                {"@type": "ListItem", "position": 2, "name": "AI Automation & Business Systems", "url": f"{BASE}/service-ai"},
                {"@type": "ListItem", "position": 3, "name": "Graphic Design & Brand Identity", "url": f"{BASE}/service-design"},
                {"@type": "ListItem", "position": 4, "name": "Digital Marketing & Growth", "url": f"{BASE}/service-marketing"},
                {"@type": "ListItem", "position": 5, "name": "Software & Product Development", "url": f"{BASE}/service-software"},
                {"@type": "ListItem", "position": 6, "name": "SEO, AEO, GEO & CRO", "url": f"{BASE}/service-seo"},
            ]}
        ]}]
    },
    {
        "file": "work.html",
        "url": f"{BASE}/work",
        "og_type": "website",
        "title": "Our Work — 12 Real Clients, Real Results | Digital Minds Solutions",
        "desc": "12 named case studies. +1,190% search impressions (Barceló). +800% landing page conversions. +400% qualified leads. No vanity metrics.",
        "og_img": OG_DEFAULT,
        "schema": [{"@context": "https://schema.org", "@graph": [
            ORG,
            {"@type": "CollectionPage", "@id": f"{BASE}/work#webpage", "url": f"{BASE}/work",
             "name": "Case Studies — Digital Minds Solutions", "isPartOf": {"@id": f"{BASE}/#website"}},
            {"@type": "ItemList", "name": "Digital Minds Solutions Case Studies", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Barceló Hotel Group", "url": f"{BASE}/case-barcelo"},
                {"@type": "ListItem", "position": 2, "name": "Mercury Holidays", "url": f"{BASE}/case-mercury"},
                {"@type": "ListItem", "position": 3, "name": "Kitchen Supply Wholesale", "url": f"{BASE}/case-kitchen-supply"},
                {"@type": "ListItem", "position": 4, "name": "Defib Supplies", "url": f"{BASE}/case-defib"},
                {"@type": "ListItem", "position": 5, "name": "Gymnastika UAE", "url": f"{BASE}/case-gymnastika"},
                {"@type": "ListItem", "position": 6, "name": "My Education Online", "url": f"{BASE}/case-meo"},
                {"@type": "ListItem", "position": 7, "name": "MyMedQ", "url": f"{BASE}/case-mymedq"},
                {"@type": "ListItem", "position": 8, "name": "Quantum Health", "url": f"{BASE}/case-quantum-health"},
                {"@type": "ListItem", "position": 9, "name": "Gravity DXB", "url": f"{BASE}/case-gravity"},
                {"@type": "ListItem", "position": 10, "name": "Santoba Tailors", "url": f"{BASE}/case-santoba"},
                {"@type": "ListItem", "position": 11, "name": "Look Family Exteriors", "url": f"{BASE}/case-look-family"},
                {"@type": "ListItem", "position": 12, "name": "Christopher Radko", "url": f"{BASE}/case-christopher-radko"},
            ]}
        ]}]
    },
    {
        "file": "pricing.html",
        "url": f"{BASE}/pricing",
        "og_type": "website",
        "title": "Pricing — Transparent Agency Pricing | Digital Minds Solutions",
        "desc": "No hidden fees. No hourly billing surprises. Fixed-scope pricing for web development, AI automation, marketing, and full-service digital retainers.",
        "og_img": OG_DEFAULT,
        "schema": [{"@context": "https://schema.org", "@graph": [
            ORG,
            {"@type": "WebPage", "@id": f"{BASE}/pricing#webpage", "url": f"{BASE}/pricing",
             "name": "Pricing — Digital Minds Solutions", "isPartOf": {"@id": f"{BASE}/#website"}}
        ]}]
    },
    {
        "file": "insights.html",
        "url": f"{BASE}/insights",
        "og_type": "website",
        "title": "Insights — Digital Marketing & Web Dev Blog | Digital Minds Solutions",
        "desc": "Actionable articles on SEO, AEO, AI automation, web development, and conversion rate optimisation from the Digital Minds Solutions team.",
        "og_img": OG_DEFAULT,
        "schema": [{"@context": "https://schema.org", "@graph": [
            ORG,
            {"@type": "Blog", "@id": f"{BASE}/insights#webpage", "url": f"{BASE}/insights",
             "name": "Insights — Digital Minds Solutions", "isPartOf": {"@id": f"{BASE}/#website"}}
        ]}]
    },
    {
        "file": "contact.html",
        "url": f"{BASE}/contact",
        "og_type": "website",
        "title": "Contact Digital Minds Solutions — Book a Free Discovery Call",
        "desc": "Book a free 30-minute discovery call. WhatsApp us directly. Response within 24 hours. Houston, Texas USA. No commitment required.",
        "og_img": OG_DEFAULT,
        "schema": [{"@context": "https://schema.org", "@graph": [
            ORG,
            {"@type": "ContactPage", "@id": f"{BASE}/contact#webpage", "url": f"{BASE}/contact",
             "name": "Contact — Digital Minds Solutions", "isPartOf": {"@id": f"{BASE}/#website"}}
        ]}]
    },
    {
        "file": "privacy.html",
        "url": f"{BASE}/privacy",
        "og_type": "website",
        "title": "Privacy Policy — Digital Minds Solutions",
        "desc": "Privacy Policy for Digital Minds Solutions. GDPR and CCPA compliant. How we collect, use, and protect your data.",
        "og_img": OG_DEFAULT,
        "schema": [{"@context": "https://schema.org", "url": f"{BASE}/privacy", "@type": "WebPage", "name": "Privacy Policy — Digital Minds Solutions", "isPartOf": {"@id": f"{BASE}/#website"}}]
    },
    {
        "file": "terms.html",
        "url": f"{BASE}/terms",
        "og_type": "website",
        "title": "Terms of Service — Digital Minds Solutions",
        "desc": "Terms of Service for Digital Minds Solutions. Governing law, service terms, and client obligations.",
        "og_img": OG_DEFAULT,
        "schema": [{"@context": "https://schema.org", "url": f"{BASE}/terms", "@type": "WebPage", "name": "Terms of Service — Digital Minds Solutions", "isPartOf": {"@id": f"{BASE}/#website"}}]
    },
]

# ── Service landing pages ─────────────────────────────────────────────────────
SERVICES_META = [
    ("service-web", "Web Development & App Solutions", "Lead-focused websites, mobile apps, landing pages, and ecommerce built to convert from launch day. React, Next.js, WordPress, Shopify. No outsourcing.", "Web Development", "WebDevelopment"),
    ("service-ai", "AI Automation & Business Systems", "AI chatbots live in 5 days. Full CRM automation in 3 weeks. Lead follow-up, WhatsApp flows, and workflow automation built in-house.", "AI Automation", "SoftwareApplication"),
    ("service-design", "Graphic Design & Brand Identity", "Full brand identity systems, UI/UX, packaging, social media, email, and pitch decks. Design that makes premium brands look premium.", "Graphic Design", "DesignService"),
    ("service-marketing", "Digital Marketing & Growth", "Google Ads, Meta Ads, LinkedIn, email marketing, and social media management. Marketing tied to revenue, not impressions.", "Digital Marketing", "MarketingService"),
    ("service-software", "Software & Product Development", "SaaS platforms, APIs, internal tools, and enterprise systems. From MVP to production. One team. No outsourcing.", "Software Development", "SoftwareApplication"),
    ("service-seo", "SEO, AEO, GEO & CRO", "Rank on Google. Appear in ChatGPT and Perplexity answers. Convert every visit. Technical SEO, AEO, GEO, and conversion rate optimisation.", "SEO & AEO", "ProfessionalService"),
]

for slug, title, desc, short, stype in SERVICES_META:
    PAGES.append({
        "file": f"{slug}.html",
        "url": f"{BASE}/{slug}",
        "og_type": "website",
        "title": f"{title} — Digital Minds Solutions",
        "desc": desc,
        "og_img": OG_DEFAULT,
        "schema": [{"@context": "https://schema.org", "@graph": [
            ORG,
            {"@type": "WebPage", "@id": f"{BASE}/{slug}#webpage", "url": f"{BASE}/{slug}",
             "name": f"{title} — Digital Minds Solutions", "isPartOf": {"@id": f"{BASE}/#website"},
             "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
                 {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
                 {"@type": "ListItem", "position": 2, "name": "Services", "item": f"{BASE}/services"},
                 {"@type": "ListItem", "position": 3, "name": title, "item": f"{BASE}/{slug}"},
             ]}},
            {"@type": stype, "name": title, "provider": {"@id": f"{BASE}/#organization"},
             "url": f"{BASE}/{slug}", "description": desc}
        ]}]
    })

# ── Case study pages ──────────────────────────────────────────────────────────
CASES_META = [
    ("case-barcelo",          "Barceló Hotel Group",       "Global Hospitality · 180 Hotels · 31 Countries",    "+1,190% search impressions, +800% landing page conversions, +400% qualified leads for Barceló Hotel Group.",    "../ASSETS/case-studies/Barceló Hotel/Barceló Hotel (1).jpg"),
    ("case-mercury",          "Mercury Holidays",           "Travel & Hospitality",                              "+900% search impressions, +450% landing conversions, +300% qualified leads for Mercury Holidays.",            "../ASSETS/case-studies/Mercury Holidays/Mercury Holidays (1).jpg"),
    ("case-kitchen-supply",   "Kitchen Supply Wholesale",   "Kitchenware Ecommerce",                             "+400% search impressions, +240% organic clicks, +70% organic leads for Kitchen Supply Wholesale.",            "../ASSETS/case-studies/Kitchen Supply/Kitchen Supply (1).jpg"),
    ("case-defib",            "Defib Supplies",             "AED Medical Ecommerce",                             "+280% search impressions, +59% organic clicks, +64% organic leads for Defib Supplies.",                      "../ASSETS/case-studies/Defib Supplies/Defib Supplies (1).jpg"),
    ("case-gymnastika",       "Gymnastika UAE",             "Youth Sports · Dubai & Abu Dhabi",                  "+330% search impressions, +280% landing conversions, +170% qualified leads for Gymnastika UAE.",              "../ASSETS/case-studies/Gymnastika/Gymnastika (1).jpg"),
    ("case-meo",              "My Education Online",        "Online Education · iGCSE & A-Level",                "+300% search impressions, +200% landing conversions, +100% qualified leads for My Education Online.",          "../ASSETS/case-studies/MEO/MEO (1).jpg"),
    ("case-mymedq",           "MyMedQ",                     "HealthTech · Patient Queue Management",             "+350% search impressions, +50% organic leads for MyMedQ patient queue management platform.",                  "../ASSETS/case-studies/MyMedQ/ MyMedQ (1).jpg"),
    ("case-quantum-health",   "Quantum Health",             "Healthcare Navigation & Benefits",                  "+320% search impressions, +46% organic clicks, +44% organic leads for Quantum Health.",                      "../ASSETS/case-studies/Quantum Health/Quantum Health (1).jpg"),
    ("case-gravity",          "Gravity DXB",                "Calisthenics · HYROX · Parkour · Dubai",            "+230% search impressions, +200% landing conversions, +100% qualified leads for Gravity DXB.",                 "../ASSETS/case-studies/Gravity/Gravity (1).jpg"),
    ("case-santoba",          "Santoba Tailors",            "Luxury Tailoring · Dubai",                          "+350% search impressions, +150% landing conversions, +100% qualified leads for Santoba Tailors.",             "../ASSETS/case-studies/Santoba Tailors/Santoba Tailors (1).jpg"),
    ("case-look-family",      "Look Family Exteriors",      "Residential Roofing · Local SEO",                   "+280% search impressions, +57% search rankings, +20% organic leads for Look Family Exteriors.",              "../ASSETS/case-studies/Look Family/Look Family (1).jpg"),
    ("case-christopher-radko","Christopher Radko",          "Luxury Holiday Decor · Ecommerce",                  "+57% search rankings, +34% organic traffic, +22% conversion rate for Christopher Radko.",                    "../ASSETS/case-studies/Christopher Radko/Christopher Radko (1).jpg"),
]

for slug, client, industry, desc, img in CASES_META:
    PAGES.append({
        "file": f"{slug}.html",
        "url": f"{BASE}/{slug}",
        "og_type": "article",
        "title": f"{client} Case Study — Digital Minds Solutions",
        "desc": desc,
        "og_img": OG_DEFAULT,
        "schema": [{"@context": "https://schema.org", "@graph": [
            ORG,
            {"@type": "Article", "@id": f"{BASE}/{slug}#article",
             "headline": f"{client} — Digital Minds Solutions Case Study",
             "description": desc,
             "publisher": {"@id": f"{BASE}/#organization"},
             "url": f"{BASE}/{slug}",
             "datePublished": "2026-05-03",
             "dateModified": "2026-05-03",
             "author": {"@id": f"{BASE}/#organization"}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
                {"@type": "ListItem", "position": 2, "name": "Our Work", "item": f"{BASE}/work"},
                {"@type": "ListItem", "position": 3, "name": client, "item": f"{BASE}/{slug}"},
            ]}
        ]}]
    })

# ── Inject helpers ────────────────────────────────────────────────────────────

def og_block(p):
    lines = [
    f'<meta property="og:type" content="{p["og_type"]}">',
    f'<meta property="og:url" content="{p["url"]}">',
    f'<meta property="og:title" content="{p["title"]}">',
    f'<meta property="og:description" content="{p["desc"]}">',
    f'<meta property="og:image" content="{p["og_img"]}">',
    f'<meta property="og:image:width" content="1200">',
    f'<meta property="og:image:height" content="630">',
    f'<meta property="og:site_name" content="Digital Minds Solutions">',
    f'<meta property="og:locale" content="en_US">',
    f'<meta name="twitter:card" content="summary_large_image">',
    f'<meta name="twitter:site" content="{TWITTER}">',
    f'<meta name="twitter:title" content="{p["title"]}">',
    f'<meta name="twitter:description" content="{p["desc"]}">',
    f'<meta name="twitter:image" content="{p["og_img"]}">',
    f'<link rel="canonical" href="{p["url"]}">',
    ]
    return '\n'.join(lines)

def ld_block(schemas):
    parts = []
    for s in schemas:
        parts.append(f'<script type="application/ld+json">\n{json.dumps(s, indent=2)}\n</script>')
    return '\n'.join(parts)

MARKER_OG  = '<!-- DMS:OG -->'
MARKER_LD  = '<!-- DMS:LD -->'

def inject(p):
    path = p["file"]
    if not os.path.exists(path):
        print(f"SKIP (not found): {path}")
        return

    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove previous injections if re-running
    html = re.sub(r'<!-- DMS:OG -->.*?<!-- /DMS:OG -->', '', html, flags=re.DOTALL)
    html = re.sub(r'<!-- DMS:LD -->.*?<!-- /DMS:LD -->', '', html, flags=re.DOTALL)

    og = f'{MARKER_OG}\n{og_block(p)}\n<!-- /DMS:OG -->'
    ld = f'{MARKER_LD}\n{ld_block(p["schema"])}\n<!-- /DMS:LD -->'

    # Insert OG block before </head>
    if '</head>' in html:
        html = html.replace('</head>', og + '\n</head>', 1)
    else:
        print(f"WARN: no </head> in {path}")

    # Insert LD block before </body>
    if '</body>' in html:
        html = html.replace('</body>', ld + '\n</body>', 1)
    else:
        print(f"WARN: no </body> in {path}")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'DONE: {path}')

if __name__ == '__main__':
    for p in PAGES:
        inject(p)
    print(f'\nPhase 4 complete — {len(PAGES)} pages patched.')
