import os

BASE = 'C:/Users/cbnot/Downloads/MY SITE FULL MOVE/DIGITAL MINDS SOLUTION/SITE/'

CASES = [
  {
    'slug': 'case-barcelo',
    'client': 'Barceló Hotel Group',
    'industry': 'Global Hospitality',
    'tag': '⭐ Flagship · 180 Hotels · 31 Countries',
    'url': 'barcelo.com/en-ww',
    'website': 'https://barcelo.com',
    'location': 'Global',
    'country': '🌍',
    'headline': 'How we scaled search impressions by 1,190% for one of the world\'s largest hotel groups.',
    'challenge': 'Barceló Hotel Group manages 180+ hotels across 31 countries. Their digital presence needed to match that scale — a complex website, underperforming landing pages, fragmented SEO, and an email automation system that wasn\'t converting at the rate their brand deserved.',
    'approach': 'We treated Barceló\'s digital system as one connected machine. Website flow was rebuilt around the guest journey. Landing pages were redesigned for conversion, not just aesthetics. SEO was approached at scale — technical fixes, content architecture, AEO structure for AI-driven discovery, and CRO applied to every key touchpoint in the booking funnel.',
    'img1': '../ASSETS/case-studies/Barceló Hotel/Barceló Hotel (1).jpg',
    'img2': '../ASSETS/case-studies/Barceló Hotel/Barceló Hotel (2).jpg',
    'metrics': [('+1,190%','Search Impressions'),('+800%','Landing Page Conversions'),('+400%','Qualified Leads'),('31','Countries Impacted')],
    'services': ['Website Dev','Ecommerce Dev','App Development','Landing Pages','Content & Blog','Social Media','Digital Marketing','Email Automation','Cybersecurity','AEO','SEO','CRO'],
    'quote': 'Managing a large hospitality website means every detail matters, from browsing hotels to completing a booking. The work helped improve our website flow, landing pages, content, search visibility, automation, and conversion journey.',
    'quote_author': 'Barceló Hotel Group',
    'prev': None,
    'next': ('case-mercury','Mercury Holidays'),
    'accent': '#002FA7',
    'accent_rgb': '0,47,167',
  },
  {
    'slug': 'case-mercury',
    'client': 'Mercury Holidays',
    'industry': 'Travel & Hospitality',
    'tag': '⭐ Flagship · UK-Based Travel Operator',
    'url': 'mercuryholidays.co.uk',
    'website': 'https://mercuryholidays.co.uk',
    'location': 'United Kingdom',
    'country': '🇬🇧',
    'headline': 'How we delivered +900% search impressions for a leading UK travel operator.',
    'challenge': 'Mercury Holidays had a product customers loved — but a digital journey that made it harder than it needed to be to book. Destination pages weren\'t converting. SEO wasn\'t driving the right traffic. And their email sequences were leaving qualified leads on the table.',
    'approach': 'We mapped the full customer journey from first search to booking confirmation. Destination content was restructured for intent. Landing pages rebuilt around conversion goals. SEO strategy focused on high-intent travel queries. Email automation sequences were rebuilt to nurture leads from browse to booking, and CRO applied at every drop-off point.',
    'img1': '../ASSETS/case-studies/Mercury Holidays/Mercury Holidays (1).jpg',
    'img2': '../ASSETS/case-studies/Mercury Holidays/Mercury Holidays (2).jpg',
    'metrics': [('+900%','Search Impressions'),('+450%','Landing Page Conversions'),('+300%','Qualified Leads'),('UK #1','Travel SEO Target')],
    'services': ['Website Dev','Ecommerce Dev','App Development','Landing Pages','Content & Blog','Social Media','Digital Marketing','Email Automation','Cybersecurity','AEO','SEO','CRO'],
    'quote': 'We wanted customers to move through destinations, travel options, and booking steps with less friction. The improvements to our website, content, SEO, landing pages, and automation helped create a smoother journey.',
    'quote_author': 'Mercury Holidays',
    'prev': ('case-barcelo','Barceló Hotel Group'),
    'next': ('case-kitchen-supply','Kitchen Supply Wholesale'),
    'accent': '#002FA7',
    'accent_rgb': '0,47,167',
  },
  {
    'slug': 'case-kitchen-supply',
    'client': 'Kitchen Supply Wholesale',
    'industry': 'Kitchenware & Ecommerce',
    'tag': 'Kitchenware · B2B & B2C Ecommerce',
    'url': 'kitchensupplywholesale.com',
    'website': 'https://kitchensupplywholesale.com',
    'location': 'United States',
    'country': '🇺🇸',
    'headline': 'How we grew organic traffic by 400% for a kitchenware ecommerce store.',
    'challenge': 'Kitchen Supply Wholesale had a large product catalogue but poor discoverability. Category structure was flat, content was thin, and the buying flow made it difficult for both B2B and B2C customers to find what they needed — let alone buy it.',
    'approach': 'A complete SEO and content architecture overhaul. Product categories were restructured around buyer intent. Thin pages were replaced with authoritative content. Technical SEO fixed crawlability issues. CRO work streamlined the checkout flow. The result: a store that finally worked as hard as the team running it.',
    'img1': '../ASSETS/case-studies/Kitchen Supply/Kitchen Supply (1).jpg',
    'img2': '../ASSETS/case-studies/Kitchen Supply/Kitchen Supply (2).jpg',
    'metrics': [('+400%','Search Impressions'),('+240%','Organic Clicks'),('+70%','Organic Leads'),('B2B+B2C','Dual Market')],
    'services': ['Website Dev','Content Strategy','Digital Marketing','Ecommerce Optimisation','AEO','SEO','CRO'],
    'quote': 'The biggest improvement was how much easier the store became for customers to browse. Product categories, content, search visibility, and the buying flow all felt more organized.',
    'quote_author': 'Kitchen Supply Wholesale',
    'prev': ('case-mercury','Mercury Holidays'),
    'next': ('case-defib','Defib Supplies'),
    'accent': '#E5A820',
    'accent_rgb': '229,168,32',
  },
  {
    'slug': 'case-defib',
    'client': 'Defib Supplies',
    'industry': 'AED & Medical Ecommerce',
    'tag': 'AED / Medical Ecommerce · UK',
    'url': 'defibsupplies.co.uk',
    'website': 'https://defibsupplies.co.uk',
    'location': 'United Kingdom',
    'country': '🇬🇧',
    'headline': 'How we grew search impressions by 280% for a specialist AED ecommerce brand.',
    'challenge': 'Defib Supplies sell life-saving equipment in a high-trust, high-stakes category. Customers need to find the right product fast and trust the supplier immediately. Their website wasn\'t doing either — poor structure, thin content, and weak search presence were all limiting growth.',
    'approach': 'Trust was built into every layer. Content was rewritten to educate and convert — explaining products, compliance requirements, and use cases with authority. SEO fixed structural issues that were burying product pages. Ecommerce flow was streamlined to reduce friction in a purchase decision that matters.',
    'img1': '../ASSETS/case-studies/Defib Supplies/Defib Supplies (1).jpg',
    'img2': '../ASSETS/case-studies/Defib Supplies/Defib Supplies (2).jpg',
    'metrics': [('+280%','Search Impressions'),('+59%','Organic Clicks'),('+64%','Organic Leads'),('High-Trust','Category')],
    'services': ['Website Dev','Content Writing','Ecommerce Dev','Digital Marketing'],
    'quote': 'The improvements to our website, content, ecommerce structure, and marketing helped customers find products faster and make more confident purchase decisions.',
    'quote_author': 'Defib Supplies',
    'prev': ('case-kitchen-supply','Kitchen Supply Wholesale'),
    'next': ('case-gymnastika','Gymnastika UAE'),
    'accent': '#E5A820',
    'accent_rgb': '229,168,32',
  },
  {
    'slug': 'case-gymnastika',
    'client': 'Gymnastika UAE',
    'industry': 'Youth Sports & Fitness',
    'tag': 'Youth Gymnastics · Dubai & Abu Dhabi',
    'url': 'gymnastikauae.com',
    'website': 'https://gymnastikauae.com',
    'location': 'UAE',
    'country': '🇦🇪',
    'headline': 'How we drove +330% search growth and tripled qualified leads for a UAE gymnastics academy.',
    'challenge': 'Gymnastika UAE operates across Dubai and Abu Dhabi, but their online presence wasn\'t reflecting the quality of their programme. Parents couldn\'t easily find class schedules, locations, coach profiles, or trial sign-up flows. The website was losing leads before they ever made contact.',
    'approach': 'Built the digital experience around the parent journey — not the gym\'s internal structure. Location-specific landing pages. Clear class schedule layouts. Trial booking flows with minimal friction. Email automation to follow up trial bookings and convert them to members. SEO targeting parent-intent queries in Dubai and Abu Dhabi.',
    'img1': '../ASSETS/case-studies/Gymnastika/Gymnastika (1).jpg',
    'img2': '../ASSETS/case-studies/Gymnastika/Gymnastika (2).jpg',
    'metrics': [('+330%','Search Impressions'),('+280%','Landing Conversions'),('+170%','Qualified Leads'),('2 Cities','Dubai & Abu Dhabi')],
    'services': ['Website Dev','Landing Pages','Content','Digital Marketing','Email Automation','AEO','SEO','CRO'],
    'quote': 'Parents needed a clearer way to understand our classes, locations, coaches, and trial sessions. The new website and landing page improvements made that journey much smoother.',
    'quote_author': 'Gymnastika UAE',
    'prev': ('case-defib','Defib Supplies'),
    'next': ('case-meo','My Education Online'),
    'accent': '#002FA7',
    'accent_rgb': '0,47,167',
  },
  {
    'slug': 'case-meo',
    'client': 'My Education Online (MEO)',
    'industry': 'Online Education',
    'tag': 'iGCSE & A-Level · UK Online Education',
    'url': 'myeducationonline.co.uk',
    'website': 'https://myeducationonline.co.uk',
    'location': 'United Kingdom',
    'country': '🇬🇧',
    'headline': 'How we doubled qualified leads for a UK iGCSE and A-Level online education platform.',
    'challenge': 'MEO offers a comprehensive online education platform for iGCSE and A-Level students — but was competing in a crowded UK market against larger, better-funded incumbents. Landing pages weren\'t converting. Paid ads weren\'t targeting the right intent. And manual follow-up was eating the team\'s time.',
    'approach': 'A full-funnel rebuild. Paid ads restructured around specific course queries. Landing pages rebuilt per subject with clear conversion flows. Email automation set up to handle lead nurturing end-to-end. SEO for long-tail educational queries that bigger platforms ignored. Workflow automation eliminated the manual follow-up burden entirely.',
    'img1': '../ASSETS/case-studies/MEO/MEO (1).jpg',
    'img2': '../ASSETS/case-studies/MEO/MEO (2).jpg',
    'metrics': [('+300%','Search Impressions'),('+200%','Landing Page Conversions'),('+100%','Qualified Leads'),('100%','Manual Follow-Up Automated')],
    'services': ['Website Dev','Landing Pages','Content','Digital Marketing','Paid Ads','Email Automation','Workflow Automation','Cybersecurity','AEO','SEO','CRO'],
    'quote': 'The landing pages, website content, paid ads, and automation all worked together better than before. We received stronger enquiries and spent less time managing follow-up manually.',
    'quote_author': 'My Education Online (MEO)',
    'prev': ('case-gymnastika','Gymnastika UAE'),
    'next': ('case-mymedq','MyMedQ'),
    'accent': '#002FA7',
    'accent_rgb': '0,47,167',
  },
  {
    'slug': 'case-mymedq',
    'client': 'MyMedQ',
    'industry': 'HealthTech',
    'tag': 'Patient Queue Management · HealthTech',
    'url': 'mymedq.in',
    'website': 'https://mymedq.in',
    'location': 'India',
    'country': '🇮🇳',
    'headline': 'How we translated complex HealthTech into a 350% search impression increase for MyMedQ.',
    'challenge': 'MyMedQ built a sophisticated patient queue management platform — but translating a complex B2B SaaS product into a clear, discoverable digital presence is its own challenge. Their website wasn\'t explaining the product clearly enough for decision-makers to act, and organic visibility was low.',
    'approach': 'We simplified without dumbing down. Product messaging was restructured around the outcomes it delivers — reduced wait times, better patient flow, hospital efficiency. Website design and development built clarity into every page. SEO targeted the queries healthcare administrators actually search. Digital marketing positioned MyMedQ as the obvious solution.',
    'img1': '../ASSETS/case-studies/MyMedQ/ MyMedQ (1).jpg',
    'img2': '../ASSETS/case-studies/MyMedQ/ MyMedQ (2).jpg',
    'metrics': [('+350%','Search Impressions'),('+50%','Organic Leads'),('B2B SaaS','Healthcare'),('Complex → Clear','Messaging')],
    'services': ['Website Design & Dev','App Development','Content','Digital Marketing'],
    'quote': 'Digital Minds Solution helped us turn a complex platform into a clearer digital experience. We are happy with the stronger visibility and better quality of interest we received.',
    'quote_author': 'MyMedQ',
    'prev': ('case-meo','My Education Online'),
    'next': ('case-quantum-health','Quantum Health'),
    'accent': '#002FA7',
    'accent_rgb': '0,47,167',
  },
  {
    'slug': 'case-quantum-health',
    'client': 'Quantum Health',
    'industry': 'Healthcare Navigation & Benefits',
    'tag': 'Healthcare Navigation · Employee Benefits',
    'url': 'quantum-health.com',
    'website': 'https://quantum-health.com',
    'location': 'United States',
    'country': '🇺🇸',
    'headline': 'How we increased organic leads by 44% for a US healthcare navigation company.',
    'challenge': 'Quantum Health operates in a nuanced space — healthcare navigation and employee benefits are critical services, but complex to communicate. Their website wasn\'t converting the right visitors. Content lacked the authority to build trust with HR and benefits decision-makers, and SEO wasn\'t reaching them.',
    'approach': 'Rebuilt the messaging architecture from the ground up. Content was rewritten to speak directly to HR professionals and benefits administrators. Website design and development aligned with the trust standards healthcare demands. SEO and AEO built around the specific queries decision-makers search when evaluating navigation platforms.',
    'img1': '../ASSETS/case-studies/Quantum Health/Quantum Health (1).jpg',
    'img2': '../ASSETS/case-studies/Quantum Health/Quantum Health (2).jpg',
    'metrics': [('+320%','Search Impressions'),('+46%','Organic Clicks'),('+44%','Organic Leads'),('B2B','Healthcare HR')],
    'services': ['Website Design & Dev','Content','SEO','CRO','AEO','Digital Marketing'],
    'quote': 'The work done on our website, content, SEO, and enquiry journey helped make our offer easier to understand and more direct for visitors. We saw better engagement and a more trusted digital experience.',
    'quote_author': 'Quantum Health',
    'prev': ('case-mymedq','MyMedQ'),
    'next': ('case-gravity','Gravity DXB'),
    'accent': '#E5A820',
    'accent_rgb': '229,168,32',
  },
  {
    'slug': 'case-gravity',
    'client': 'Gravity DXB',
    'industry': 'Fitness & Calisthenics',
    'tag': 'Calisthenics · HYROX · Parkour · Dubai',
    'url': 'gravitydxb.com',
    'website': 'https://gravitydxb.com',
    'location': 'Dubai, UAE',
    'country': '🇦🇪',
    'headline': "How we doubled conversions for Dubai's leading calisthenics and functional fitness gym.",
    'challenge': "Gravity DXB offers multiple disciplines — calisthenics, HYROX training, parkour — under one roof in Dubai. Their website wasn't communicating the depth of offer, trial bookings weren't converting, and their SEO wasn't reaching the high-intent fitness audience in Dubai.",
    'approach': 'Discipline-specific landing pages built around what each audience actually wants. Trial booking flows stripped of friction. Email automation to follow up enquiries and convert trials to memberships. SEO targeting functional fitness queries in Dubai. Content positioned Gravity DXB as the serious training environment it is.',
    'img1': '../ASSETS/case-studies/Gravity/Gravity (1).jpg',
    'img2': '../ASSETS/case-studies/Gravity/Gravity (2).jpg',
    'metrics': [('+230%','Search Impressions'),('+200%','Landing Conversions'),('+100%','Qualified Leads'),('Dubai','Market Leader')],
    'services': ['Website Dev','Landing Pages','Content','Digital Marketing','Email Automation','AEO','SEO','CRO'],
    'quote': 'The team improved our content, landing page flow, SEO, and trial booking journey. The result helped more visitors understand our offer and take action.',
    'quote_author': 'Gravity DXB',
    'prev': ('case-quantum-health','Quantum Health'),
    'next': ('case-santoba','Santoba Tailors'),
    'accent': '#E5A820',
    'accent_rgb': '229,168,32',
  },
  {
    'slug': 'case-santoba',
    'client': 'Santoba Tailors',
    'industry': 'Luxury Tailoring',
    'tag': 'Luxury Bespoke Tailoring · Dubai',
    'url': 'santobatailors.ae',
    'website': 'https://santobatailors.ae',
    'location': 'Dubai, UAE',
    'country': '🇦🇪',
    'headline': "How we elevated Santoba Tailors' digital presence to match their luxury craftsmanship.",
    'challenge': "Santoba Tailors create exceptional bespoke garments in Dubai — but their online presence didn't reflect the quality of their craft. A dated website, weak service pages, and poor local SEO meant clients couldn't find them, and those who did weren't converting.",
    'approach': 'Built a digital presence worthy of a luxury brand. New website designed with the visual language of high-end fashion. Service pages rebuilt to communicate quality, process, and exclusivity. Landing pages optimised for enquiry conversion. Local SEO to ensure Santoba appeared when Dubai\'s most discerning clients searched for bespoke tailoring.',
    'img1': '../ASSETS/case-studies/Santoba Tailors/Santoba Tailors (1).jpg',
    'img2': '../ASSETS/case-studies/Santoba Tailors/Santoba Tailors (2).jpg',
    'metrics': [('+350%','Search Impressions'),('+150%','Landing Conversions'),('+100%','Qualified Leads'),('Luxury','Positioning')],
    'services': ['Website Dev','Landing Pages','Content','Digital Marketing','Email Automation','AEO','SEO','CRO'],
    'quote': 'The improvements gave us a more polished online presence, clearer service pages, and a stronger enquiry path. It now feels easier for clients to understand our offer and reach out with confidence.',
    'quote_author': 'Santoba Tailors',
    'prev': ('case-gravity','Gravity DXB'),
    'next': ('case-look-family','Look Family Exteriors'),
    'accent': '#002FA7',
    'accent_rgb': '0,47,167',
  },
  {
    'slug': 'case-look-family',
    'client': 'Look Family Exteriors',
    'industry': 'Residential Roofing',
    'tag': 'Residential Roofing · Local SEO · USA',
    'url': 'lookfamilyexteriors.net',
    'website': 'https://lookfamilyexteriors.net',
    'location': 'United States',
    'country': '🇺🇸',
    'headline': 'How we grew search visibility by 280% for a residential roofing contractor.',
    'challenge': "Look Family Exteriors operate in a highly competitive local market where homeowners search, compare, and decide fast. Their service pages were generic, local SEO was weak, and the website wasn't building the trust that turns a search result into a phone call.",
    'approach': 'Local SEO built for the markets they actually serve. Service pages rewritten to speak directly to homeowners — what to expect, what it costs, what it means for their home. Technical SEO fixed the crawl issues holding rankings back. On-page optimisation across every service page. More visibility, better rankings, more enquiries.',
    'img1': '../ASSETS/case-studies/Look Family/Look Family (1).jpg',
    'img2': '../ASSETS/case-studies/Look Family/Look Family (2).jpg',
    'metrics': [('+280%','Search Impressions'),('+57%','Search Rankings'),('+20%','Organic Leads'),('Local SEO','Specialist')],
    'services': ['Local SEO','Content Strategy','On-Page SEO','Technical SEO'],
    'quote': 'Our service pages became clearer, our local SEO improved, and the website started working harder for lead generation. The increase in enquiries showed the strategy was focused on real business results.',
    'quote_author': 'Look Family Exteriors',
    'prev': ('case-santoba','Santoba Tailors'),
    'next': ('case-christopher-radko','Christopher Radko'),
    'accent': '#E5A820',
    'accent_rgb': '229,168,32',
  },
  {
    'slug': 'case-christopher-radko',
    'client': 'Christopher Radko',
    'industry': 'Luxury Ecommerce',
    'tag': 'Luxury Holiday Decor · Ecommerce · USA',
    'url': 'christopherradko.com',
    'website': 'https://christopherradko.com',
    'location': 'United States',
    'country': '🇺🇸',
    'headline': 'How we lifted conversions 22% and organic traffic 34% for an iconic luxury decor brand.',
    'challenge': "Christopher Radko is an iconic American luxury holiday decor brand with decades of history — but their ecommerce experience wasn't matching their brand prestige. Product discoverability was poor, Google Merchant Center wasn't optimised, and the website design was holding back a brand that deserved to be seen.",
    'approach': 'A website rebrand brought the digital experience in line with the luxury standard the brand represents. SEO rebuilt around product and category queries with genuine purchase intent. Google Merchant Center fully optimised — product feeds, attributes, structured data. CRO applied to the product and checkout flow to convert more of the traffic they were already getting.',
    'img1': '../ASSETS/case-studies/Christopher Radko/Christopher Radko (1).jpg',
    'img2': '../ASSETS/case-studies/Christopher Radko/Christopher Radko (2).jpg',
    'metrics': [('+57%','Search Rankings'),('+34%','Organic Traffic'),('+22%','Conversion Rate'),('Luxury','Ecommerce')],
    'services': ['Website Rebrand','SEO','Google Merchant Center Optimisation','CRO'],
    'quote': 'Our website now feels much closer to the quality of our brand. The team improved the design, product structure, SEO, and Google Merchant setup in a way that made the shopping experience cleaner.',
    'quote_author': 'Christopher Radko',
    'prev': ('case-look-family','Look Family Exteriors'),
    'next': None,
    'accent': '#002FA7',
    'accent_rgb': '0,47,167',
  },
]

TEMPLATE = '''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{client} case study — Digital Minds Solutions. {headline}">
<title>{client} Case Study — Digital Minds Solutions</title>
<link rel="icon" type="image/png" href="../ASSETS/logo/favicon.png (512x512px).png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Inter:wght@400;500&display=swap" rel="stylesheet">
<style>
:root{{--deep-space:#08101E;--klein-blue:#002FA7;--amber-gold:#E5A820;--cobalt-shade:#243B6E;--muted-blue:#B8CBE8;--muted-ink:#3A4F7A;--card-dark:#0D1826;--card-border:#1E3055;--light-bg:#F4F7FF;--light-card:#FFFFFF;--light-border:#C5D3F0;--white:#FFFFFF;--accent:{accent};--font-head:'Plus Jakarta Sans',sans-serif;--font-body:'Inter',sans-serif;--r-sm:6px;--r-md:12px;--r-lg:20px;--r-xl:32px;--container:1280px;--nav-h:72px}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth}}
body{{font-family:var(--font-body);background:var(--deep-space);color:var(--white);overflow-x:hidden;-webkit-font-smoothing:antialiased;line-height:1.7}}
a{{text-decoration:none;color:inherit}}img{{display:block;max-width:100%}}ul{{list-style:none}}button{{cursor:pointer;border:none;background:none;font:inherit}}
.container{{max-width:var(--container);margin:0 auto;padding:0 40px}}
@media(max-width:768px){{.container{{padding:0 20px}}}}
.h2{{font-family:var(--font-head);font-size:clamp(28px,3vw,48px);font-weight:800;line-height:1.12;letter-spacing:-.02em}}
.eyebrow{{display:inline-flex;align-items:center;gap:8px;font-family:var(--font-head);font-size:12px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--amber-gold);margin-bottom:20px}}
.eyebrow::before{{content:'';display:block;width:24px;height:2px;background:var(--amber-gold);border-radius:2px}}
.btn-gold{{display:inline-flex;align-items:center;gap:8px;background:var(--amber-gold);color:var(--deep-space);font-family:var(--font-head);font-size:15px;font-weight:700;padding:14px 28px;border-radius:var(--r-md);transition:transform .2s,box-shadow .2s}}
.btn-gold:hover{{transform:translateY(-2px);box-shadow:0 12px 40px rgba(229,168,32,.35)}}
.btn-ghost{{display:inline-flex;align-items:center;gap:8px;background:transparent;color:var(--white);font-family:var(--font-head);font-size:15px;font-weight:600;padding:14px 28px;border-radius:var(--r-md);border:1px solid var(--card-border);transition:border-color .2s,background .2s}}
.btn-ghost:hover{{border-color:var(--muted-blue);background:rgba(255,255,255,.04)}}
.gs{{opacity:0;transform:translateY(36px)}}
/* NAV */
#navbar{{position:fixed;top:0;left:0;right:0;height:var(--nav-h);z-index:1000;transition:background .3s,border-color .3s,backdrop-filter .3s;border-bottom:1px solid transparent}}
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
.icon-sun{{display:none}}
[data-theme="light"] .icon-moon{{display:none}}[data-theme="light"] .icon-sun{{display:block}}
.nav-hamburger{{display:none;width:38px;height:38px;border-radius:var(--r-sm);border:1px solid var(--card-border);flex-direction:column;align-items:center;justify-content:center;gap:5px}}
.nav-hamburger span{{display:block;width:18px;height:2px;background:var(--muted-blue);border-radius:2px;transition:transform .3s,opacity .3s}}
.nav-hamburger.active span:nth-child(1){{transform:translateY(7px) rotate(45deg)}}
.nav-hamburger.active span:nth-child(2){{opacity:0}}
.nav-hamburger.active span:nth-child(3){{transform:translateY(-7px) rotate(-45deg)}}
.mobile-menu{{position:fixed;inset:0;top:var(--nav-h);background:var(--deep-space);padding:40px 24px;opacity:0;visibility:hidden;transform:translateX(100%);transition:all .35s cubic-bezier(.16,1,.3,1);z-index:999;overflow-y:auto}}
.mobile-menu.open{{opacity:1;visibility:visible;transform:none}}
.mobile-menu .nav-links{{display:flex;flex-direction:column;align-items:flex-start;gap:4px;justify-content:flex-start}}
.mobile-menu .nav-links a{{font-size:22px;padding:12px 0;width:100%}}
.mobile-menu .m-ctas{{display:flex;flex-direction:column;gap:12px;margin-top:32px}}
.mobile-menu .m-ctas .btn-gold,.mobile-menu .m-ctas .btn-ghost{{justify-content:center}}
@media(max-width:900px){{.nav-links{{display:none}}.nav-hamburger{{display:flex}}.nav-inner{{padding:0 20px}}}}
/* HERO */
#cs-hero{{position:relative;min-height:80vh;display:flex;align-items:flex-end;padding-bottom:80px;padding-top:calc(var(--nav-h) + 60px);overflow:hidden}}
.cs-hero-img{{position:absolute;inset:0;z-index:0}}
.cs-hero-img img{{width:100%;height:100%;object-fit:cover;opacity:.32}}
.cs-hero-overlay{{position:absolute;inset:0;z-index:1;background:linear-gradient(135deg,rgba(8,16,30,.97) 0%,rgba(8,16,30,.72) 55%,rgba({accent_rgb},.18) 100%)}}
.cs-hero-bottom{{position:absolute;bottom:0;left:0;right:0;height:160px;background:linear-gradient(to bottom,transparent,var(--deep-space));z-index:2}}
.cs-hero-content{{position:relative;z-index:3;max-width:860px}}
.cs-breadcrumb{{display:flex;align-items:center;gap:8px;font-family:var(--font-head);font-size:13px;font-weight:600;color:var(--muted-blue);margin-bottom:24px}}
.cs-breadcrumb a{{color:var(--muted-blue);transition:color .2s}}
.cs-breadcrumb a:hover{{color:var(--white)}}
.cs-breadcrumb span{{color:var(--card-border)}}
.cs-industry{{display:inline-flex;align-items:center;gap:8px;font-family:var(--font-head);font-size:11px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--amber-gold);margin-bottom:20px;padding:6px 14px;border-radius:99px;background:rgba(229,168,32,.1);border:1px solid rgba(229,168,32,.25)}}
.cs-hero-h1{{font-family:var(--font-head);font-size:clamp(26px,3.8vw,52px);font-weight:800;line-height:1.1;letter-spacing:-.025em;color:var(--white);margin-bottom:32px}}
.cs-hero-meta{{display:flex;gap:24px;flex-wrap:wrap;align-items:center}}
.cs-meta-item{{display:flex;align-items:center;gap:8px;font-family:var(--font-head);font-size:13px;font-weight:600;color:var(--muted-blue)}}
.cs-meta-dot{{width:4px;height:4px;background:var(--amber-gold);border-radius:50%;flex-shrink:0}}
@media(max-width:768px){{#cs-hero{{min-height:unset;padding-top:calc(var(--nav-h) + 40px);padding-bottom:60px;align-items:flex-start}}.cs-hero-h1{{font-size:clamp(22px,7vw,34px)}}}}
/* METRICS */
#cs-metrics{{padding:80px 0;background:var(--card-dark);border-top:1px solid var(--card-border);border-bottom:1px solid var(--card-border)}}
.cs-metrics-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:2px;background:var(--card-border);border-radius:var(--r-xl);overflow:hidden}}
.cs-metric{{background:var(--card-dark);padding:48px 32px;text-align:center;transition:background .2s}}
.cs-metric:hover{{background:rgba(255,255,255,.02)}}
.cs-metric-val{{font-family:var(--font-head);font-size:clamp(32px,4vw,60px);font-weight:800;line-height:1;margin-bottom:10px;color:var(--amber-gold)}}
.cs-metric-lab{{font-family:var(--font-head);font-size:13px;font-weight:600;color:var(--muted-blue);letter-spacing:.06em;text-transform:uppercase;line-height:1.4}}
@media(max-width:768px){{.cs-metrics-grid{{grid-template-columns:repeat(2,1fr)}}}}
/* OVERVIEW */
#cs-overview{{padding:96px 0;background:var(--deep-space)}}
.cs-overview-grid{{display:grid;grid-template-columns:5fr 7fr;gap:80px;align-items:start}}
.cs-overview-label{{position:sticky;top:calc(var(--nav-h) + 40px)}}
.cs-section-label{{font-family:var(--font-head);font-size:12px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--amber-gold);margin-bottom:20px;display:flex;align-items:center;gap:8px}}
.cs-section-label::before{{content:'';display:block;width:24px;height:2px;background:var(--amber-gold);border-radius:2px}}
.cs-overview-label .h2{{color:var(--white);margin-bottom:20px;font-size:clamp(22px,2.2vw,34px)}}
.cs-overview-label p{{color:var(--muted-blue);font-size:15px;line-height:1.7}}
.cs-overview-content{{display:flex;flex-direction:column;gap:40px}}
.cs-block-title{{font-family:var(--font-head);font-size:16px;font-weight:800;color:var(--white);margin-bottom:12px}}
.cs-block-text{{color:var(--muted-blue);font-size:16px;line-height:1.75}}
.cs-services-chips{{display:flex;flex-wrap:wrap;gap:10px;margin-top:8px}}
.cs-service-chip{{font-family:var(--font-head);font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:6px 14px;border-radius:99px;background:rgba(0,47,167,.15);color:var(--muted-blue);border:1px solid var(--card-border);transition:color .2s,border-color .2s,background .2s}}
.cs-service-chip:hover{{color:var(--white);border-color:var(--muted-blue);background:rgba(0,47,167,.25)}}
@media(max-width:900px){{.cs-overview-grid{{grid-template-columns:1fr;gap:48px}}.cs-overview-label{{position:static}}}}
/* GALLERY */
#cs-gallery{{padding:80px 0;background:var(--card-dark);border-top:1px solid var(--card-border)}}
.cs-gallery-grid{{display:grid;grid-template-columns:1fr 1fr;gap:16px;border-radius:var(--r-xl);overflow:hidden}}
.cs-gallery-img{{aspect-ratio:16/10;overflow:hidden}}
.cs-gallery-img img{{width:100%;height:100%;object-fit:cover;transition:transform .6s ease}}
.cs-gallery-img:hover img{{transform:scale(1.04)}}
@media(max-width:640px){{.cs-gallery-grid{{grid-template-columns:1fr}}}}
/* TESTIMONIAL */
#cs-testimonial{{padding:96px 0;background:var(--deep-space);text-align:center}}
.cs-quote-wrap{{max-width:800px;margin:0 auto}}
.cs-quote-mark{{font-family:Georgia,serif;font-size:96px;line-height:.6;color:var(--amber-gold);opacity:.35;margin-bottom:16px;display:block}}
.cs-quote-text{{font-family:var(--font-head);font-size:clamp(18px,2vw,26px);font-weight:700;line-height:1.55;color:var(--white);margin-bottom:32px}}
.cs-quote-author{{font-family:var(--font-head);font-size:14px;font-weight:700;color:var(--amber-gold);letter-spacing:.1em;text-transform:uppercase}}
.cs-quote-divider{{width:64px;height:2px;background:linear-gradient(90deg,var(--klein-blue),var(--amber-gold));border-radius:2px;margin:20px auto 0}}
/* CASE NAV */
#cs-case-nav{{padding:48px 0;background:var(--card-dark);border-top:1px solid var(--card-border)}}
.cs-nav-inner{{display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap}}
.cs-nav-btn{{display:flex;align-items:center;gap:12px;font-family:var(--font-head);padding:16px 24px;border-radius:var(--r-md);border:1px solid var(--card-border);transition:border-color .2s,background .2s,transform .2s}}
.cs-nav-btn:hover{{border-color:var(--muted-blue);background:rgba(255,255,255,.04);transform:translateY(-2px)}}
.cs-nav-btn small{{display:block;font-size:11px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--muted-blue)}}
.cs-nav-btn strong{{display:block;font-size:15px;color:var(--white);margin-top:2px}}
.cs-nav-arrow{{font-size:20px;color:var(--amber-gold)}}
.cs-nav-btn--right{{text-align:right}}
.cs-nav-all{{font-family:var(--font-head);font-size:13px;font-weight:700;color:var(--muted-blue);padding:12px 20px;border-radius:var(--r-md);border:1px solid var(--card-border);transition:color .2s,border-color .2s}}
.cs-nav-all:hover{{color:var(--white);border-color:var(--muted-blue)}}
/* CTA */
#cs-cta{{padding:120px 0;background:var(--deep-space);text-align:center;position:relative;overflow:hidden}}
#cs-cta::before{{content:'';position:absolute;top:-200px;left:50%;transform:translateX(-50%);width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,rgba(0,47,167,.16) 0%,transparent 70%);pointer-events:none}}
.cs-cta-inner{{position:relative;z-index:1;max-width:620px;margin:0 auto}}
.cs-cta-inner .h2{{color:var(--white);margin-bottom:16px}}
.cs-cta-inner p{{color:var(--muted-blue);font-size:18px;margin-bottom:40px;line-height:1.65}}
.cs-cta-btns{{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}}
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
/* WHATSAPP */
.wa-float{{position:fixed;bottom:28px;right:28px;z-index:998;width:56px;height:56px;border-radius:50%;background:#25D366;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 32px rgba(37,211,102,.4);transition:transform .2s,box-shadow .2s}}
.wa-float:hover{{transform:scale(1.1)}}
.wa-float svg{{width:28px;height:28px;fill:white}}
/* COOKIE */
#cookieBanner{{position:fixed;bottom:0;left:0;right:0;z-index:1100;background:rgba(13,24,38,.97);border-top:1px solid #1E3055;backdrop-filter:blur(16px);transform:translateY(100%);transition:transform .4s cubic-bezier(.16,1,.3,1);padding:20px 0}}
#cookieBanner.visible{{transform:none}}
.cookie-inner{{max-width:1280px;margin:0 auto;padding:0 40px;display:flex;align-items:center;gap:32px;flex-wrap:wrap}}
.cookie-text{{flex:1;min-width:260px}}
.cookie-text p{{font-size:14px;color:#B8CBE8;line-height:1.6}}
.cookie-text strong{{color:#fff}}
.cookie-text a{{color:#E5A820;text-decoration:underline;text-underline-offset:3px}}
.cookie-btns{{display:flex;gap:12px;flex-shrink:0}}
.cookie-accept{{font-family:'Plus Jakarta Sans',sans-serif;font-size:14px;font-weight:700;padding:10px 22px;border-radius:10px;background:#E5A820;color:#08101E;cursor:pointer;border:none}}
.cookie-decline{{font-family:'Plus Jakarta Sans',sans-serif;font-size:14px;font-weight:600;padding:10px 22px;border-radius:10px;background:transparent;color:#B8CBE8;border:1px solid #1E3055;cursor:pointer}}
/* LIGHT */
[data-theme="light"] body{{background:var(--light-bg);color:var(--deep-space)}}
[data-theme="light"] #navbar.scrolled{{background:rgba(244,247,255,.92)}}
[data-theme="light"] .nav-links a{{color:var(--muted-ink)}}
[data-theme="light"] #cs-overview{{background:var(--light-bg)}}
[data-theme="light"] .cs-block-text{{color:var(--muted-ink)}}
[data-theme="light"] .cs-overview-label .h2{{color:var(--deep-space)}}
[data-theme="light"] #cs-cta{{background:var(--light-bg)}}
[data-theme="light"] .cs-cta-inner .h2{{color:var(--deep-space)}}
[data-theme="light"] .cs-quote-text{{color:var(--deep-space)}}
[data-theme="light"] #cs-testimonial{{background:var(--light-bg)}}
[data-theme="light"] #footer{{background:var(--white);border-color:var(--light-border)}}
[data-theme="light"] .footer-col ul a,[data-theme="light"] .footer-brand p,[data-theme="light"] .footer-bottom p,[data-theme="light"] .footer-bottom a{{color:var(--muted-ink)}}
</style>
</head>
<body>
<nav id="navbar">
  <div class="nav-inner">
    <a href="index.html" class="nav-logo"><img src="../ASSETS/logo/logo-white.svg.png" alt="Digital Minds Solutions"></a>
    <div class="nav-links">
      <a href="index.html">Home</a><a href="about.html">About</a><a href="services.html">Services</a>
      <a href="work.html" class="active">Work</a><a href="pricing.html">Pricing</a>
      <a href="insights.html">Insights</a><a href="contact.html">Contact</a>
    </div>
    <div class="nav-right">
      <button class="theme-toggle" id="themeToggle" aria-label="Toggle theme">
        <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/></svg>
        <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
      </button>
      <a href="https://cal.com/digitalminds-fx51uj" class="btn-gold" target="_blank" rel="noopener" style="padding:10px 20px;font-size:13px">Book a Call</a>
      <button class="nav-hamburger" id="navHamburger" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</nav>
<div class="mobile-menu" id="mobileMenu">
  <div class="nav-links">
    <a href="index.html">Home</a><a href="about.html">About</a><a href="services.html">Services</a>
    <a href="work.html">Work</a><a href="pricing.html">Pricing</a><a href="insights.html">Insights</a><a href="contact.html">Contact</a>
  </div>
  <div class="m-ctas">
    <a href="https://cal.com/digitalminds-fx51uj" class="btn-gold" target="_blank">Book a Free Discovery Call</a>
    <a href="https://wa.me/447426427646" class="btn-ghost" target="_blank">WhatsApp Us Directly</a>
  </div>
</div>

<section id="cs-hero">
  <div class="cs-hero-img"><img src="{img1}" alt="{client}" loading="eager"></div>
  <div class="cs-hero-overlay"></div>
  <div class="cs-hero-bottom"></div>
  <div class="cs-hero-content container">
    <div class="cs-breadcrumb gs">
      <a href="index.html">Home</a><span>/</span>
      <a href="work.html">Our Work</a><span>/</span>
      <span style="color:var(--white)">{client}</span>
    </div>
    <div class="cs-industry gs">{tag}</div>
    <h1 class="cs-hero-h1 gs">{headline}</h1>
    <div class="cs-hero-meta gs">
      <div class="cs-meta-item"><div class="cs-meta-dot"></div>{country} {location}</div>
      <div class="cs-meta-item"><div class="cs-meta-dot"></div>{industry}</div>
      <div class="cs-meta-item"><div class="cs-meta-dot"></div><a href="https://{url}" target="_blank" rel="noopener" style="color:var(--muted-blue);transition:color .2s">{url} &#8599;</a></div>
    </div>
  </div>
</section>

<section id="cs-metrics">
  <div class="container">
    <div class="cs-metrics-grid">{metrics_html}</div>
  </div>
</section>

<section id="cs-overview">
  <div class="container">
    <div class="cs-overview-grid">
      <div class="cs-overview-label">
        <div class="cs-section-label gs">Case Study</div>
        <h2 class="h2 gs">{client}</h2>
        <p class="gs">{industry} &middot; {country} {location}</p>
      </div>
      <div class="cs-overview-content">
        <div class="gs"><div class="cs-block-title">The Challenge</div><p class="cs-block-text">{challenge}</p></div>
        <div class="gs"><div class="cs-block-title">Our Approach</div><p class="cs-block-text">{approach}</p></div>
        <div class="gs"><div class="cs-block-title">Services Delivered</div><div class="cs-services-chips">{services_html}</div></div>
      </div>
    </div>
  </div>
</section>

<section id="cs-gallery">
  <div class="container">
    <div class="cs-gallery-grid">
      <div class="cs-gallery-img gs"><img src="{img1}" alt="{client} — image 1" loading="lazy"></div>
      <div class="cs-gallery-img gs"><img src="{img2}" alt="{client} — image 2" loading="lazy"></div>
    </div>
  </div>
</section>

<section id="cs-testimonial">
  <div class="container">
    <div class="cs-quote-wrap">
      <span class="cs-quote-mark gs">&ldquo;</span>
      <p class="cs-quote-text gs">{quote}</p>
      <div class="cs-quote-author gs">&mdash; {quote_author}</div>
      <div class="cs-quote-divider gs"></div>
    </div>
  </div>
</section>

<section id="cs-case-nav">
  <div class="container">
    <div class="cs-nav-inner">
      {prev_html}
      <a href="work.html" class="cs-nav-all">All Case Studies &#8599;</a>
      {next_html}
    </div>
  </div>
</section>

<section id="cs-cta">
  <div class="container">
    <div class="cs-cta-inner">
      <div class="eyebrow gs" style="justify-content:center">Your Turn</div>
      <h2 class="h2 gs">Want results like {client}?</h2>
      <p class="gs">Book a free 30-minute call. We'll show you exactly what we'd build for your business — no pitch deck, no pressure.</p>
      <div class="cs-cta-btns gs">
        <a href="https://cal.com/digitalminds-fx51uj" class="btn-gold" target="_blank" rel="noopener">Book a Free Discovery Call &rarr;</a>
        <a href="https://wa.me/447426427646" class="btn-ghost" target="_blank" rel="noopener">WhatsApp Us &rarr;</a>
      </div>
    </div>
  </div>
</section>

<footer id="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand"><img src="../ASSETS/logo/logo-white.svg.png" alt="Digital Minds Solutions"><p>Web development, AI automation, branding, marketing, and software. One team. No handoffs. Real results.</p><div style="display:flex;gap:12px;margin-top:20px"><a href="#" class="social-link">in</a><a href="#" class="social-link">ig</a><a href="https://youtu.be/96FyvCDcxRA" class="social-link" target="_blank">&#9654;</a><a href="#" class="social-link">&#120143;</a></div></div>
      <div class="footer-col"><div class="footer-col-title">Services</div><ul><li><a href="services.html">Web Development</a></li><li><a href="services.html">AI Automation</a></li><li><a href="services.html">Digital Marketing</a></li><li><a href="services.html">SEO / AEO / GEO / CRO</a></li></ul></div>
      <div class="footer-col"><div class="footer-col-title">Company</div><ul><li><a href="about.html">About Us</a></li><li><a href="work.html">Our Work</a></li><li><a href="pricing.html">Pricing</a></li><li><a href="contact.html">Contact</a></li><li><a href="privacy.html">Privacy Policy</a></li></ul></div>
      <div class="footer-col"><div class="footer-col-title">Get In Touch</div><ul><li><a href="https://cal.com/digitalminds-fx51uj" target="_blank">Book a Discovery Call</a></li><li><a href="https://wa.me/447426427646" target="_blank">WhatsApp Us</a></li><li><a href="mailto:digitalmindss01@gmail.com">digitalmindss01@gmail.com</a></li><li><a href="tel:+447426427646">+44 7426 427646</a></li></ul></div>
    </div>
    <div class="footer-bottom"><p>&copy; 2025 Digital Minds Solutions. All rights reserved.</p><p><a href="privacy.html">Privacy Policy</a> &nbsp;&middot;&nbsp; <a href="terms.html">Terms of Service</a></p></div>
  </div>
</footer>

<div id="cookieBanner" role="dialog" aria-label="Cookie consent">
  <div class="cookie-inner">
    <div class="cookie-text"><p><strong>We use cookies</strong> to improve your experience. Read our <a href="privacy.html">Privacy Policy</a>.</p></div>
    <div class="cookie-btns"><button id="cookieDecline" class="cookie-decline">Decline</button><button id="cookieAccept" class="cookie-accept">Accept All</button></div>
  </div>
</div>

<a href="https://wa.me/447426427646?text=Hi%2C%20I%27d%20like%20to%20learn%20more%20about%20Digital%20Minds%20Solutions" class="wa-float" target="_blank" rel="noopener" aria-label="WhatsApp">
  <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
</a>

<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script>
(function(){{
  'use strict';
  const root=document.documentElement,saved=localStorage.getItem('dms-theme'),preferred=window.matchMedia('(prefers-color-scheme:light)').matches?'light':'dark';
  root.setAttribute('data-theme',saved||preferred);
  document.getElementById('themeToggle').addEventListener('click',()=>{{const n=root.getAttribute('data-theme')==='dark'?'light':'dark';root.setAttribute('data-theme',n);localStorage.setItem('dms-theme',n);}});
  const nb=document.getElementById('navbar');
  window.addEventListener('scroll',()=>nb.classList.toggle('scrolled',window.scrollY>60),{{passive:true}});
  const hb=document.getElementById('navHamburger'),mm=document.getElementById('mobileMenu');
  hb.addEventListener('click',()=>{{hb.classList.toggle('active');mm.classList.toggle('open');document.body.style.overflow=mm.classList.contains('open')?'hidden':'';}});
  mm.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{{hb.classList.remove('active');mm.classList.remove('open');document.body.style.overflow=''}}));
  gsap.registerPlugin(ScrollTrigger);
  gsap.utils.toArray('#cs-hero .gs').forEach((el,i)=>gsap.fromTo(el,{{opacity:0,y:24}},{{opacity:1,y:0,duration:.75,ease:'power2.out',delay:.1+i*.13}}));
  gsap.utils.toArray('.gs:not(#cs-hero .gs)').forEach(el=>gsap.fromTo(el,{{opacity:0,y:40}},{{opacity:1,y:0,duration:.75,ease:'power2.out',scrollTrigger:{{trigger:el,start:'top 88%',toggleActions:'play none none none'}}}}));
  (function(){{var k='dms_cookie_consent',b=document.getElementById('cookieBanner');if(!b)return;if(!localStorage.getItem(k))setTimeout(()=>b.classList.add('visible'),1200);document.getElementById('cookieAccept').addEventListener('click',()=>{{localStorage.setItem(k,'accepted');b.classList.remove('visible');}});document.getElementById('cookieDecline').addEventListener('click',()=>{{localStorage.setItem(k,'declined');b.classList.remove('visible');}});}})();
  (function(C,A,L){{let p=function(a,ar){{a.q.push(ar)}};let d=C.document;C.Cal=C.Cal||function(){{let cal=C.Cal;let ar=arguments;if(!cal.loaded){{cal.ns={{}};cal.q=cal.q||[];d.head.appendChild(d.createElement('script')).src=A;cal.loaded=true}}if(ar[0]===L){{const api=function(){{p(api,arguments)}};const ns=ar[1];api.q=api.q||[];if(typeof ns==='string'){{cal.ns[ns]=cal.ns[ns]||api;p(cal.ns[ns],ar);p(cal,[L,ns,ar[2]])}}else p(cal,[L,ar[1]]);return}}p(cal,ar)}}}})(window,'https://app.cal.com/embed/embed.js','init');
  Cal('init',{{origin:'https://cal.com'}});Cal('ui',{{theme:'dark',styles:{{branding:{{brandColor:'#002FA7'}}}},hideEventTypeDetails:false,layout:'month_view'}});
  document.querySelectorAll('a[href="https://cal.com/digitalminds-fx51uj"]').forEach(el=>el.addEventListener('click',e=>{{e.preventDefault();Cal('modal',{{calLink:'digitalminds-fx51uj',config:{{layout:'month_view'}}}})}}));
}})();
</script>
</body>
</html>'''

def build(c):
    m_html = ''.join(f'\n      <div class="cs-metric gs"><div class="cs-metric-val">{v}</div><div class="cs-metric-lab">{l}</div></div>' for v,l in c['metrics'])
    s_html = ''.join(f'<span class="cs-service-chip">{s}</span>' for s in c['services'])
    prev_h = f'<a href="{c["prev"][0]}.html" class="cs-nav-btn"><span class="cs-nav-arrow">&larr;</span><span><small>Previous</small><strong>{c["prev"][1]}</strong></span></a>' if c['prev'] else '<div></div>'
    next_h = f'<a href="{c["next"][0]}.html" class="cs-nav-btn cs-nav-btn--right"><span><small>Next Case Study</small><strong>{c["next"][1]}</strong></span><span class="cs-nav-arrow">&rarr;</span></a>' if c['next'] else '<div></div>'
    return TEMPLATE.format(
        client=c['client'], industry=c['industry'], tag=c['tag'],
        url=c['url'], location=c['location'], country=c['country'],
        headline=c['headline'], challenge=c['challenge'], approach=c['approach'],
        img1=c['img1'], img2=c['img2'], quote=c['quote'], quote_author=c['quote_author'],
        accent=c['accent'], accent_rgb=c['accent_rgb'],
        metrics_html=m_html, services_html=s_html, prev_html=prev_h, next_html=next_h
    )

for c in CASES:
    path = BASE + c['slug'] + '.html'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(build(c))
    print(f'BUILT: {c["slug"]}.html')

print(f'\nDone — {len(CASES)} pages generated.')
