from pathlib import Path
import base64

root = Path(__file__).parent
assets = root / "assest"
out = root / "output"
out.mkdir(parents=True, exist_ok=True)

def data_uri(path: Path) -> str:
    mime = "image/jpeg" if path.suffix.lower() in {".jpg", ".jpeg"} else "image/png"
    return (
        f"data:{mime};base64,"
        + base64.b64encode(path.read_bytes()).decode("ascii")
    )

def get_img(name):
    for ext in [".jpg", ".jpeg", ".png", ".webp"]:
        p = assets / f"{name}{ext}"
        print("Checking:", p)

        if p.exists():
            print("FOUND:", p)
            return data_uri(p)

    print("NOT FOUND:", name)
    return "https://via.placeholder.com/800x1600?text=No+Image"

imgs = {
    "home": get_img("home"),
    "home_close": get_img("home_close"),
    "wardrobe": get_img("wardrobe"),
    "generator": get_img("generator"),
    "shop": get_img("shop"),
    "profile": get_img("profile"),
    "settings": get_img("settings"),
    "login": get_img("login"),
}


html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>The Style Algorithm — Your AI Styling Universe</title>
  <meta name="description" content="A modern pastel fashion-tech website that helps users make better outfit decisions using the clothes they already own." />
  <style>
    :root {{
      --bg: #fffafb;
      --bg-soft: #fff5f8;
      --surface: rgba(255,255,255,0.74);
      --surface-strong: rgba(255,255,255,0.92);
      --text: #373245;
      --muted: #7f788e;
      --line: rgba(218, 202, 221, 0.55);
      --pink: #ffb6d9;
      --pink-strong: #ff8cc2;
      --lavender: #ddd2ff;
      --blue: #d7efff;
      --peach: #ffe4d5;
      --mint: #e6fff6;
      --shadow: 0 18px 45px rgba(207, 178, 196, 0.22);
      --shadow-soft: 0 10px 24px rgba(207, 178, 196, 0.13);
      --radius-xl: 34px;
      --radius-lg: 26px;
      --radius-md: 20px;
      --max: 1200px;
      --hero-gradient: linear-gradient(135deg, rgba(255,181,214,.9), rgba(226,210,255,.9) 56%, rgba(214,238,255,.95));
      --button-gradient: linear-gradient(90deg, #ffb3d5, #ead6ff 55%, #d6efff);
    }}

    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      margin: 0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: var(--text);
      background:
        radial-gradient(circle at top left, rgba(255, 196, 220, 0.35), transparent 28%),
        radial-gradient(circle at top right, rgba(218, 229, 255, 0.4), transparent 25%),
        linear-gradient(180deg, #fffafc, #fffdfd 35%, #fff7fb 100%);
      min-height: 100vh;
    }}

    body::before {{
      content: '';
      position: fixed;
      inset: 0;
      pointer-events: none;
      background: linear-gradient(180deg, rgba(255,255,255,0.18), rgba(255,255,255,0));
      backdrop-filter: blur(0px);
      z-index: -1;
    }}

    a {{ color: inherit; text-decoration: none; }}
    img {{ max-width: 100%; display: block; }}

    .container {{ width: min(var(--max), calc(100% - 32px)); margin: 0 auto; }}

    .site-header {{ position: sticky; top: 0; z-index: 30; padding: 18px 0; backdrop-filter: blur(18px); background: rgba(255, 250, 252, 0.72); border-bottom: 1px solid rgba(229, 218, 228, 0.55); }}
    .nav {{ display: flex; align-items: center; justify-content: space-between; gap: 18px; }}
    .brand {{ display: flex; align-items: center; gap: 12px; font-weight: 800; letter-spacing: -0.03em; }}
    .brand-badge {{ width: 46px; height: 46px; border-radius: 16px; background: var(--hero-gradient); box-shadow: var(--shadow-soft); display: grid; place-items: center; color: white; font-size: 22px; }}
    .brand small {{ display: block; color: var(--muted); font-weight: 600; letter-spacing: 0; }}
    .nav-links {{ display: flex; gap: 26px; color: var(--muted); font-weight: 600; }}
    .nav-links a:hover {{ color: var(--text); }}
    .actions {{ display: flex; gap: 12px; align-items: center; }}

    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      min-height: 52px;
      padding: 0 22px;
      border-radius: 999px;
      border: 1px solid transparent;
      font-weight: 700;
      letter-spacing: -0.02em;
      transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease, background .25s ease;
      cursor: pointer;
    }}
    .btn:hover {{ transform: translateY(-2px); }}
    .btn-primary {{ background: var(--button-gradient); color: #4f4060; box-shadow: var(--shadow); }}
    .btn-secondary {{ background: rgba(255,255,255,.76); border-color: rgba(224, 211, 223, 0.8); color: var(--text); box-shadow: var(--shadow-soft); }}

    .hero {{ padding: 42px 0 48px; }}
    .hero-grid {{ display: grid; grid-template-columns: 1.08fr .92fr; gap: 28px; align-items: center; }}
    .hero-copy {{ padding: 12px 0; }}
    .eyebrow {{ display: inline-flex; align-items: center; gap: 10px; padding: 10px 16px; border-radius: 999px; background: rgba(255,255,255,.76); border: 1px solid rgba(230, 215, 225, 0.7); box-shadow: var(--shadow-soft); color: #8f6a89; font-weight: 700; }}
    h1 {{ margin: 18px 0 16px; font-size: clamp(2.7rem, 5vw, 5.2rem); line-height: .95; letter-spacing: -0.06em; }}
    .hero-copy p {{ margin: 0 0 24px; max-width: 60ch; font-size: 1.08rem; line-height: 1.7; color: var(--muted); }}
    .hero-actions {{ display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 30px; }}
    .stats {{ display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 14px; }}
    .stat {{ background: rgba(255,255,255,.8); border: 1px solid rgba(231, 219, 228, 0.72); border-radius: 24px; padding: 18px 18px; box-shadow: var(--shadow-soft); }}
    .stat strong {{ display: block; font-size: 1.75rem; letter-spacing: -0.04em; margin-bottom: 6px; }}
    .stat span {{ color: var(--muted); font-weight: 600; font-size: .95rem; }}

    .hero-visual {{ position: relative; min-height: 720px; }}
    .blob {{ position: absolute; inset: 48px 18px 120px 54px; border-radius: 42px; background: var(--hero-gradient); filter: blur(0px); opacity: .72; }}
    .phone-stack {{ position: relative; height: 100%; }}
    .phone-card {{
      position: absolute;
      width: min(280px, 52vw);
      border-radius: 38px;
      background: rgba(255,255,255,.45);
      padding: 14px;
      box-shadow: 0 22px 55px rgba(185, 150, 182, 0.30);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(255,255,255,.55);
    }}
    .phone-card img {{ border-radius: 28px; width: 100%; height: auto; }}
    .phone-main {{ right: 10px; top: 0; z-index: 3; transform: rotate(2deg); }}
    .phone-side {{ left: 20px; top: 130px; width: min(240px, 45vw); z-index: 2; transform: rotate(-7deg); }}
    .phone-bottom {{ right: 64px; bottom: 18px; width: min(250px, 45vw); z-index: 1; transform: rotate(8deg); }}
    .floating-note {{
      position: absolute;
      left: 0;
      bottom: 120px;
      max-width: 240px;
      background: rgba(255,255,255,.88);
      border: 1px solid rgba(231, 219, 228, 0.72);
      border-radius: 26px;
      padding: 16px 16px;
      box-shadow: var(--shadow);
    }}
    .floating-note strong {{ display: block; margin-bottom: 7px; font-size: 1rem; }}
    .floating-note span {{ color: var(--muted); font-size: .94rem; line-height: 1.5; }}

    section {{ padding: 42px 0; }}
    .section-head {{ display: flex; align-items: end; justify-content: space-between; gap: 16px; margin-bottom: 22px; }}
    .section-head h2 {{ margin: 0; font-size: clamp(2rem, 3vw, 3rem); line-height: 1; letter-spacing: -0.05em; }}
    .section-head p {{ margin: 0; max-width: 560px; color: var(--muted); line-height: 1.7; }}

    .glass-panel {{ background: rgba(255,255,255,.74); border: 1px solid rgba(231, 219, 228, 0.75); box-shadow: var(--shadow-soft); backdrop-filter: blur(12px); }}

    .feature-grid {{ display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 18px; }}
    .feature-card {{ border-radius: var(--radius-xl); padding: 24px; position: relative; overflow: hidden; min-height: 320px; }}
    .feature-card::before {{ content: ''; position: absolute; inset: auto -18% -24% auto; width: 180px; height: 180px; border-radius: 50%; background: linear-gradient(135deg, rgba(255, 184, 213, 0.28), rgba(217, 233, 255, 0.34)); filter: blur(10px); }}
    .feature-icon {{ width: 54px; height: 54px; border-radius: 18px; display: grid; place-items: center; font-size: 24px; background: var(--button-gradient); box-shadow: var(--shadow-soft); }}
    .feature-card h3 {{ margin: 18px 0 10px; font-size: 1.35rem; letter-spacing: -0.03em; }}
    .feature-card p {{ margin: 0 0 16px; color: var(--muted); line-height: 1.7; }}
    .feature-list {{ margin: 0; padding: 0 0 0 18px; color: #615a72; display: grid; gap: 10px; }}

    .overview {{ display: grid; grid-template-columns: 1.02fr .98fr; gap: 22px; align-items: stretch; }}
    .overview-card {{ border-radius: 34px; padding: 24px; position: relative; overflow: hidden; }}
    .overview-card h3 {{ margin: 0 0 10px; font-size: 1.65rem; letter-spacing: -0.04em; }}
    .overview-card p {{ margin: 0; color: var(--muted); line-height: 1.7; }}
    .preview-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 22px; }}
    .preview-pane {{ border-radius: 28px; padding: 12px; background: rgba(255,255,255,.88); box-shadow: var(--shadow-soft); border: 1px solid rgba(231,219,228,.65); }}
    .preview-pane img {{
    border-radius: 22px;
    aspect-ratio: 9/19.5;
    object-fit: contain;
    width: 100%;
    background: white;
}}

    .steps {{ display: grid; grid-template-columns: repeat(4, minmax(0,1fr)); gap: 16px; }}
    .step {{ border-radius: 28px; padding: 22px; min-height: 210px; }}
    .step .num {{ width: 44px; height: 44px; border-radius: 14px; background: var(--button-gradient); display: grid; place-items: center; font-weight: 800; box-shadow: var(--shadow-soft); margin-bottom: 18px; }}
    .step h3 {{ margin: 0 0 10px; font-size: 1.15rem; }}
    .step p {{ margin: 0; color: var(--muted); line-height: 1.7; }}

    .showcase {{ display: grid; grid-template-columns: .95fr 1.05fr; gap: 22px; }}
    .showcase-copy, .showcase-panel {{ border-radius: 34px; padding: 24px; }}
    .chip-row {{ display: flex; flex-wrap: wrap; gap: 10px; margin-top: 16px; }}
    .chip {{ padding: 10px 14px; border-radius: 999px; background: rgba(255,255,255,.8); border: 1px solid rgba(229,216,227,.75); color: #7d718f; font-weight: 700; }}
    .carousel {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }}
    .carousel-card {{ border-radius: 24px; overflow: hidden; position: relative; box-shadow: var(--shadow-soft); border: 1px solid rgba(231,219,228,.65); background: white; }}
    .carousel-card img {{ width: 100%; aspect-ratio: 9/19.5; object-fit: cover; }}
    .carousel-card span {{ position: absolute; left: 12px; bottom: 12px; padding: 8px 12px; border-radius: 999px; background: rgba(255,255,255,.86); backdrop-filter: blur(8px); font-weight: 700; font-size: .88rem; }}

    .social-band {{ border-radius: 34px; padding: 28px; background: linear-gradient(135deg, rgba(255, 183, 219, 0.48), rgba(232, 219, 255, 0.55), rgba(218, 237, 255, 0.55)); border: 1px solid rgba(255,255,255,.72); box-shadow: var(--shadow); display: grid; grid-template-columns: 1fr auto; gap: 20px; align-items: center; }}
    .social-band h3 {{ margin: 0 0 10px; font-size: 1.8rem; letter-spacing: -0.04em; }}
    .social-band p {{ margin: 0; max-width: 55ch; line-height: 1.7; color: #635d73; }}

    .cta {{ padding-bottom: 70px; }}
    .cta-card {{ border-radius: 38px; padding: 34px; background: linear-gradient(135deg, rgba(255,255,255,.9), rgba(255,248,252,.92)); border: 1px solid rgba(231,219,228,.75); box-shadow: var(--shadow); display: grid; grid-template-columns: 1.05fr .95fr; gap: 22px; align-items: center; overflow: hidden; }}
    .cta-card h2 {{ margin: 0 0 14px; font-size: clamp(2rem, 4vw, 3.3rem); line-height: 1; letter-spacing: -0.05em; }}
    .cta-card p {{ margin: 0 0 20px; color: var(--muted); line-height: 1.75; }}
    .mini-gallery {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }}
    .mini-gallery .preview-pane {{ padding: 10px; }}

    footer {{ padding: 0 0 38px; color: var(--muted); }}
    .footer-row {{ display: flex; justify-content: space-between; gap: 16px; align-items: center; border-top: 1px solid rgba(230, 218, 228, 0.75); padding-top: 20px; }}

    @media (max-width: 1100px) {{
      .hero-grid, .overview, .showcase, .cta-card {{ grid-template-columns: 1fr; }}
      .feature-grid {{ grid-template-columns: repeat(2, minmax(0,1fr)); }}
      .steps {{ grid-template-columns: repeat(2, minmax(0,1fr)); }}
      .hero-visual {{ min-height: 780px; }}
      .carousel {{ grid-template-columns: repeat(2, 1fr); }}
    }}

    @media (max-width: 760px) {{
      .nav-links {{ display: none; }}
      .actions .btn-secondary {{ display: none; }}
      .hero {{ padding-top: 24px; }}
      .stats, .feature-grid, .steps, .carousel, .mini-gallery, .preview-grid {{ grid-template-columns: 1fr; }}
      .hero-visual {{ min-height: 920px; }}
      .phone-main {{ right: 0; width: min(300px, 72vw); }}
      .phone-side {{ left: 0; top: 160px; width: min(240px, 58vw); }}
      .phone-bottom {{ right: 10px; bottom: 0; width: min(250px, 58vw); }}
      .floating-note {{ left: 10px; bottom: 160px; }}
      .social-band {{ grid-template-columns: 1fr; }}
      .section-head {{ flex-direction: column; align-items: start; }}
      .footer-row {{ flex-direction: column; align-items: start; }}
      .cta-card {{ padding: 26px; }}
    }}
  </style>
</head>
<body>
  <header class="site-header">
    <div class="container nav">
      <a class="brand" href="#top">
        <span class="brand-badge">✦</span>
        <span>
          The Style Algorithm
          <small>AI Fashion • Smart Styling • Virtual Try-On</small>
        </span>
      </a>
      <nav class="nav-links">
        <a href="#features">Features</a>
        <a href="#experience">Experience</a>
        <a href="#how-it-works">How it works</a>
        <a href="#community">Community</a>
      </nav>
      <div class="actions">
        <a class="btn btn-secondary" href="#experience">See screens</a>
        <a class="btn btn-primary" href="#cta">Launch your wardrobe</a>
      </div>
    </div>
  </header>

  <main id="top">
    <section class="hero">
      <div class="container hero-grid">
        <div class="hero-copy">
          <div class="eyebrow">Pastel luxury UI · AI-powered wardrobe planning</div>
          <h1>Make better outfit decisions with the clothes you already own.</h1>
          <p>
            This polished fashion-tech website is designed to feel as soft, premium, and modern as your mobile references—while clearly selling the product value: digitize your wardrobe, generate AI looks, preview them before you wear them, and shop only when a look truly needs one missing piece.
          </p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="#cta">Get started free</a>
            <a class="btn btn-secondary" href="#features">Explore key features</a>
          </div>
          <div class="stats">
            <div class="stat"><strong>6</strong><span>core product flows highlighted</span></div>
            <div class="stat"><strong>AI</strong><span>powered outfit matching & styling logic</span></div>
            <div class="stat"><strong>Pastel</strong><span>glassmorphism-inspired premium design</span></div>
          </div>
        </div>
        <div class="hero-visual">
          <div class="blob"></div>
          <div class="phone-stack">
            <div class="phone-card phone-main"><img src="{imgs['home_close']}" alt="Home screen preview" /></div>
            <div class="phone-card phone-side"><img src="{imgs['wardrobe']}" alt="Wardrobe screen preview" /></div>
            <div class="phone-card phone-bottom"><img src="{imgs['generator']}" alt="Outfit generator preview" /></div>
            <div class="floating-note">
              <strong>Designed for real wardrobe decisions</strong>
              <span>From closet organization to styling, shopping, try-on, and social sharing—every section is framed as one elegant user journey.</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="features">
      <div class="container">
        <div class="section-head">
          <div>
            <div class="eyebrow">Core product suite</div>
            <h2>Everything users need to style smarter.</h2>
          </div>
          <p>Your requested features are translated into a premium web experience with large rounded cards, gentle gradients, light shadows, and calm editorial typography inspired by the app references.</p>
        </div>
        <div class="feature-grid">
          <article class="feature-card glass-panel">
            <div class="feature-icon">👗</div>
            <h3>Digital Wardrobe</h3>
            <p>Upload, tag, filter, and organize clothing pieces by type, season, fit, color, or mood so users can see their closet as a searchable personal archive.</p>
            <ul class="feature-list">
              <li>Closet search and category tabs</li>
              <li>Visual item grid with labels</li>
              <li>Quick add flow for new items</li>
            </ul>
          </article>
          <article class="feature-card glass-panel">
            <div class="feature-icon">✨</div>
            <h3>AI Outfit Generator</h3>
            <p>Generate combinations from wardrobe items based on occasion, weather, mood, body type, and personal preferences—without forcing users to buy more.</p>
            <ul class="feature-list">
              <li>Occasion-based filters</li>
              <li>Mood and weather controls</li>
              <li>Mix-and-match outfit suggestions</li>
            </ul>
          </article>
          <article class="feature-card glass-panel">
            <div class="feature-icon">🪞</div>
            <h3>Virtual Try-On</h3>
            <p>Help users preview outfits before getting dressed, making experimentation feel low-pressure, playful, and confidence-building.</p>
            <ul class="feature-list">
              <li>Hero recommendation cards</li>
              <li>Try-before-you-wear CTA moments</li>
              <li>Visual confidence in daily picks</li>
            </ul>
          </article>
          <article class="feature-card glass-panel">
            <div class="feature-icon">🌦️</div>
            <h3>Fashion Recommendations</h3>
            <p>Personalized suggestions combine wardrobe data, weather, occasion, and styling intent to surface the most relevant looks for each day.</p>
            <ul class="feature-list">
              <li>Daily recommendation module</li>
              <li>Weather-aware outfit logic</li>
              <li>Preference-based styling profiles</li>
            </ul>
          </article>
          <article class="feature-card glass-panel">
            <div class="feature-icon">💬</div>
            <h3>Social Features</h3>
            <p>Let users share outfits, ask friends for feedback, discuss style decisions, and build confidence through collaborative fashion conversations.</p>
            <ul class="feature-list">
              <li>Saved looks and community prompts</li>
              <li>Style chat & opinion gathering</li>
              <li>Discussion-ready outfit sharing</li>
            </ul>
          </article>
          <article class="feature-card glass-panel">
            <div class="feature-icon">🛍️</div>
            <h3>Smart Shopping</h3>
            <p>If a look is nearly complete, the system recommends only the missing pieces that match the user’s style profile and existing wardrobe palette.</p>
            <ul class="feature-list">
              <li>Match-score product cards</li>
              <li>Wardrobe-gap suggestions</li>
              <li>Low-friction “complete the look” flow</li>
            </ul>
          </article>
        </div>
      </div>
    </section>

    <section id="experience">
      <div class="container overview">
        <div class="overview-card glass-panel">
          <div class="eyebrow">Visual direction</div>
          <h3>A website system built from your app references.</h3>
          <p>The design language mirrors the screenshots: pastel pink, lavender, peach, and powder blue gradients; soft shadowed cards; rounded mobile-inspired blocks; airy whitespace; and an elegant, fashion-focused tone that feels friendly rather than overly technical.</p>
          <div class="preview-grid">
            <div class="preview-pane"><img src="{imgs['home']}" alt="Home dashboard reference" /></div>
            <div class="preview-pane"><img src="{imgs['profile']}" alt="Profile reference" /></div>
          </div>
        </div>
        <div class="overview-card glass-panel">
          <div class="eyebrow">Product framing</div>
          <h3>Professional, conversion-ready sections.</h3>
          <p>This concept positions the product as both aspirational and practical. Users immediately understand the value proposition: better outfits, less closet confusion, more confidence, and smarter shopping only when needed.</p>
          <div class="preview-grid">
            <div class="preview-pane"><img src="{imgs['shop']}" alt="Shopping reference" /></div>
            <div class="preview-pane"><img src="{imgs['settings']}" alt="Settings reference" /></div>
          </div>
        </div>
      </div>
    </section>

    <section id="how-it-works">
      <div class="container">
        <div class="section-head">
          <div>
            <div class="eyebrow">User journey</div>
            <h2>How the experience flows.</h2>
          </div>
          <p>Each step is designed to reduce decision fatigue and make wardrobe planning feel luxurious, clear, and personalized.</p>
        </div>
        <div class="steps">
          <article class="step glass-panel">
            <div class="num">1</div>
            <h3>Upload the closet</h3>
            <p>Users bring their wardrobe online with photos, categories, colors, and seasonal tags.</p>
          </article>
          <article class="step glass-panel">
            <div class="num">2</div>
            <h3>Set style preferences</h3>
            <p>Preferred silhouettes, fit, vibe, and favorite colors shape every recommendation.</p>
          </article>
          <article class="step glass-panel">
            <div class="num">3</div>
            <h3>Generate a look</h3>
            <p>AI combines owned items for brunch, office, events, weather shifts, or mood-based dressing.</p>
          </article>
          <article class="step glass-panel">
            <div class="num">4</div>
            <h3>Try on, share, refine</h3>
            <p>Users preview outfits, save favorites, ask friends, and shop only if one piece is missing.</p>
          </article>
        </div>
      </div>
    </section>

    <section>
      <div class="container showcase">
        <div class="showcase-copy glass-panel">
          <div class="eyebrow">Why this works</div>
          <h2 style="margin:14px 0 12px; font-size: clamp(2rem, 3.8vw, 3rem); line-height:1; letter-spacing:-0.05em;">A softer luxury look for a fashion-tech brand.</h2>
          <p style="margin:0; color:var(--muted); line-height:1.8;">Instead of a generic SaaS website, this direction feels editorial and emotionally resonant. Rounded forms, translucent layers, and fashion-led imagery make the experience feel premium—while still clearly explaining product mechanics.</p>
          <div class="chip-row">
            <span class="chip">Pastel gradients</span>
            <span class="chip">Glassmorphism cards</span>
            <span class="chip">Rounded mobile-inspired framing</span>
            <span class="chip">Editorial whitespace</span>
            <span class="chip">Soft luxury shadows</span>
            <span class="chip">Fashion-first storytelling</span>
          </div>
        </div>
        <div class="showcase-panel glass-panel">
          <div class="carousel">
            <div class="carousel-card"><img src="{imgs['login']}" alt="Login UI" /><span>Onboarding</span></div>
            <div class="carousel-card"><img src="{imgs['wardrobe']}" alt="Wardrobe UI" /><span>Closet</span></div>
            <div class="carousel-card"><img src="{imgs['generator']}" alt="Generator UI" /><span>AI Styling</span></div>
            <div class="carousel-card"><img src="{imgs['shop']}" alt="Shopping UI" /><span>Shopping</span></div>
          </div>
        </div>
      </div>
    </section>

    <section id="community">
      <div class="container">
        <div class="social-band">
          <div>
            <h3>Style is social—so the website should feel shareable too.</h3>
            <p>Feature community-inspired calls to action like sharing a look, getting feedback before an event, saving outfit discussions, or posting “which one should I wear?” prompts. This turns the product from a utility into a daily habit.</p>
          </div>
          <a class="btn btn-primary" href="#cta">Design my launch page</a>
        </div>
      </div>
    </section>

    <section class="cta" id="cta">
      <div class="container">
        <div class="cta-card">
          <div>
            <div class="eyebrow">Ready to build</div>
            <h2>Your fashion platform, reimagined in a premium pastel web style.</h2>
            <p>I created this as a polished, responsive website concept you can use as a foundation for your real site. It already reflects the UI mood of your references and organizes the message around your six requested features.</p>
            <div class="hero-actions" style="margin-bottom:0;">
              <a class="btn btn-primary" href="index.html">Open prototype</a>
              <a class="btn btn-secondary" href="#features">Review sections</a>
            </div>
          </div>
          <div class="mini-gallery">
            <div class="preview-pane"><img src="{imgs['profile']}" alt="Profile screen" /></div>
            <div class="preview-pane"><img src="{imgs['home_close']}" alt="Home screen detail" /></div>
            <div class="preview-pane"><img src="{imgs['settings']}" alt="Settings screen" /></div>
          </div>
        </div>
      </div>
    </section>
  </main>

  <footer>
    <div class="container footer-row">
      <div>
        <strong>ClosetMuse AI</strong><br />
        Modern wardrobe planning, AI styling, try-on, social feedback, and smart shopping.
      </div>
      <div>Designed from your provided fashion app references.</div>
    </div>
  </footer>
</body>
# write final site
</html>'''


(out / "index.html").write_text(html, encoding="utf-8")
print("Site generated successfully")