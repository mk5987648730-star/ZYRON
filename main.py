from flask import Flask, jsonify, request

app = Flask(__name__)

search_counter = 0

DEMO_DATABASE = {
    "9999999999": {
        "demo_id": "ZYR-XYZ-001",
        "name": "XYZ Alpha Tester",
        "city": "XYZ Metro City (Demo)",
        "status": "ACTIVE - TEST MODE",
        "note": "Fictional XYZ Testing Data"
    },
    "8888888888": {
        "demo_id": "ZYR-XYZ-002",
        "name": "XYZ Cyber Node",
        "city": "Neo Sector 07 (Demo)",
        "status": "VERIFIED - TEST MODE",
        "note": "Fictional XYZ Testing Data"
    },
    "7777777777": {
        "demo_id": "ZYR-XYZ-003",
        "name": "XYZ Phantom Demo",
        "city": "Virtual Hub 09 (Demo)",
        "status": "SANDBOX - TEST MODE",
        "note": "Fictional XYZ Testing Data"
    }
}

DEMO_CITIES = [
    "XYZ Metro City (Demo)",
    "Cyber Sector 04 (Demo)",
    "Tech Valley XYZ (Demo)",
    "Neo Grid City (Demo)",
    "Sandbox Zone 01 (Demo)"
]

HTML_PAGE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>ZYRON API // Demo Terminal</title>
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      background-color: #050814;
      background-image:
        radial-gradient(circle at top right, rgba(0, 240, 255, 0.12), transparent 45%),
        radial-gradient(circle at bottom left, rgba(37, 99, 235, 0.14), transparent 45%);
      color: #e2e8f0;
      font-family: -apple-system, BlinkMacSystemFont, "SF Mono", "Segoe UI", Roboto, monospace;
      min-height: 100vh;
      padding: 20px 14px 40px;
      display: flex;
      justify-content: center;
      align-items: flex-start;
    }
    .container {
      width: 100%;
      max-width: 520px;
    }
    .header {
      text-align: center;
      margin-bottom: 20px;
      padding: 18px 14px;
      background: rgba(10, 16, 34, 0.85);
      border: 1px solid rgba(0, 240, 255, 0.28);
      border-radius: 16px;
      box-shadow: 0 0 24px rgba(0, 240, 255, 0.08);
    }
    .badge {
      display: inline-block;
      font-size: 11px;
      letter-spacing: 1.5px;
      color: #00f0ff;
      background: rgba(0, 240, 255, 0.1);
      border: 1px solid rgba(0, 240, 255, 0.35);
      padding: 4px 10px;
      border-radius: 999px;
      margin-bottom: 10px;
    }
    .logo {
      font-size: 30px;
      font-weight: 800;
      letter-spacing: 4px;
      color: #ffffff;
      text-shadow: 0 0 14px rgba(0, 240, 255, 0.65);
    }
    .subtitle {
      font-size: 12px;
      color: #94a3b8;
      margin-top: 6px;
      letter-spacing: 0.8px;
    }
    .stats-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      margin-bottom: 16px;
    }
    .stat-box {
      flex: 1;
      background: rgba(10, 16, 34, 0.9);
      border: 1px solid rgba(56, 189, 248, 0.22);
      border-radius: 12px;
      padding: 12px;
      text-align: center;
    }
    .stat-label {
      font-size: 10px;
      color: #94a3b8;
      letter-spacing: 1px;
      text-transform: uppercase;
    }
    .stat-value {
      font-size: 18px;
      font-weight: 700;
      color: #00f0ff;
      margin-top: 4px;
    }
    .card {
      background: rgba(10, 16, 34, 0.92);
      border: 1px solid rgba(0, 240, 255, 0.25);
      border-radius: 16px;
      padding: 18px;
      margin-bottom: 16px;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.45);
    }
    .label {
      display: block;
      font-size: 12px;
      color: #38bdf8;
      letter-spacing: 1px;
      margin-bottom: 8px;
      text-transform: uppercase;
    }
    .input-group {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    input[type="tel"] {
      width: 100%;
      padding: 14px 16px;
      font-size: 16px;
      font-family: inherit;
      color: #f8fafc;
      background: #040711;
      border: 1px solid rgba(0, 240, 255, 0.35);
      border-radius: 12px;
      outline: none;
      letter-spacing: 2px;
    }
    input[type="tel"]:focus {
      border-color: #00f0ff;
      box-shadow: 0 0 12px rgba(0, 240, 255, 0.25);
    }
    .btn-primary {
      width: 100%;
      padding: 14px;
      font-size: 15px;
      font-weight: 700;
      letter-spacing: 1.5px;
      color: #020617;
      background: linear-gradient(90deg, #00f0ff, #3b82f6);
      border: none;
      border-radius: 12px;
      cursor: pointer;
      text-transform: uppercase;
    }
    .btn-primary:active {
      transform: scale(0.98);
    }
    .quick-row {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 12px;
      align-items: center;
    }
    .quick-label {
      font-size: 11px;
      color: #94a3b8;
    }
    .chip {
      font-size: 12px;
      color: #00f0ff;
      background: rgba(0, 240, 255, 0.08);
      border: 1px solid rgba(0, 240, 255, 0.3);
      padding: 5px 10px;
      border-radius: 8px;
      cursor: pointer;
      font-family: inherit;
    }
    .error-msg {
      margin-top: 12px;
      padding: 10px 12px;
      border-radius: 10px;
      background: rgba(239, 68, 68, 0.14);
      border: 1px solid rgba(239, 68, 68, 0.45);
      color: #fca5a5;
      font-size: 13px;
      display: none;
    }
    .result-section {
      display: none;
    }
    .section-title {
      font-size: 12px;
      color: #00f0ff;
      letter-spacing: 1.2px;
      text-transform: uppercase;
      margin-bottom: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .data-grid {
      display: grid;
      gap: 10px;
    }
    .data-item {
      background: #040711;
      border: 1px solid rgba(148, 163, 184, 0.18);
      border-radius: 10px;
      padding: 10px 12px;
    }
    .data-key {
      font-size: 10px;
      color: #64748b;
      text-transform: uppercase;
      letter-spacing: 1px;
    }
    .data-val {
      font-size: 15px;
      color: #f1f5f9;
      font-weight: 600;
      margin-top: 3px;
      word-break: break-word;
    }
    .json-box {
      background: #02040a;
      border: 1px solid rgba(0, 240, 255, 0.25);
      border-radius: 12px;
      padding: 12px;
      color: #38bdf8;
      font-size: 12px;
      line-height: 1.5;
      overflow-x: auto;
      white-space: pre-wrap;
      word-break: break-word;
    }
    .copy-btn {
      font-size: 11px;
      color: #e2e8f0;
      background: rgba(59, 130, 246, 0.2);
      border: 1px solid rgba(59, 130, 246, 0.45);
      padding: 4px 10px;
      border-radius: 6px;
      cursor: pointer;
      font-family: inherit;
    }
    .footer {
      text-align: center;
      font-size: 11px;
      color: #64748b;
      margin-top: 10px;
      line-height: 1.6;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="badge">● SYSTEM ONLINE // V1.0</div>
      <div class="logo">ZYRON API</div>
      <div class="subtitle">DARK CYBER DEMO TERMINAL • @zyrondev</div>
    </div>

    <div class="stats-bar">
      <div class="stat-box">
        <div class="stat-label">Search Counter</div>
        <div class="stat-value" id="searchCount">0</div>
      </div>
      <div class="stat-box">
        <div class="stat-label">Mode</div>
        <div class="stat-value" style="font-size: 14px;">XYZ DEMO</div>
      </div>
    </div>

    <div class="card">
      <label class="label" for="mobileInput">Target Demo Number (10 Digits)</label>
      <div class="input-group">
        <input
          type="tel"
          id="mobileInput"
          maxlength="10"
          inputmode="numeric"
          placeholder="9999999999"
        />
        <button class="btn-primary" id="searchBtn" onclick="runSearch()">
          Execute Search
        </button>
      </div>

      <div class="quick-row">
        <span class="quick-label">Quick Test:</span>
        <button class="chip" onclick="fillDemo('9999999999')">9999999999</button>
        <button class="chip" onclick="fillDemo('8888888888')">8888888888</button>
        <button class="chip" onclick="fillDemo('7777777777')">7777777777</button>
      </div>

      <div class="error-msg" id="errorBox"></div>
    </div>

    <div class="result-section" id="resultSection">
      <div class="card">
        <div class="section-title">
          <span>// Demo Record Output</span>
          <span style="color:#22c55e;">200 OK</span>
        </div>
        <div class="data-grid">
          <div class="data-item">
            <div class="data-key">Demo ID</div>
            <div class="data-val" id="resId">-</div>
          </div>
          <div class="data-item">
            <div class="data-key">Demo Name</div>
            <div class="data-val" id="resName">-</div>
          </div>
          <div class="data-item">
            <div class="data-key">City</div>
            <div class="data-val" id="resCity">-</div>
          </div>
          <div class="data-item">
            <div class="data-key">Status</div>
            <div class="data-val" id="resStatus">-</div>
          </div>
        </div>
      </div>

      <div class="card">
        <div class="section-title">
          <span>// Raw JSON API Response</span>
          <button class="copy-btn" onclick="copyJson()">Copy JSON</button>
        </div>
        <pre class="json-box" id="jsonOutput">{}</pre>
      </div>
    </div>

    <div class="footer">
      ZYRON DEMO INTERFACE • FICTIONAL XYZ TESTING DATA ONLY<br />
      No real personal data is stored or accessed.
    </div>
  </div>

  <script>
    let localSearches = Number(localStorage.getItem("zyron_searches") || "0");
    document.getElementById("searchCount").textContent = localSearches;

    function fillDemo(num) {
      document.getElementById("mobileInput").value = num;
      runSearch();
    }

    async function runSearch() {
      const input = document.getElementById("mobileInput").value.trim();
      const errorBox = document.getElementById("errorBox");
      const resultSection = document.getElementById("resultSection");
      const btn = document.getElementById("searchBtn");

      errorBox.style.display = "none";

      if (!/^\d{10}$/.test(input)) {
        errorBox.textContent = "Error: कृपया 10 अंकों का सही Demo Mobile Number दर्ज करें।";
        errorBox.style.display = "block";
        resultSection.style.display = "none";
        return;
      }

      btn.textContent = "SCANNING...";
      btn.disabled = true;

      try {
        const res = await fetch("/api/search?number=" + encodeURIComponent(input));
        const data = await res.json();

        if (!res.ok || data.status !== "success") {
          errorBox.textContent = data.message || "Search failed.";
          errorBox.style.display = "block";
          resultSection.style.display = "none";
        } else {
          localSearches += 1;
          localStorage.setItem("zyron_searches", String(localSearches));
          document.getElementById("searchCount").textContent = Math.max(localSearches, data.search_count || 0);

          document.getElementById("resId").textContent = data.result.demo_id;
          document.getElementById("resName").textContent = data.result.name;
          document.getElementById("resCity").textContent = data.result.city;
          document.getElementById("resStatus").textContent = data.result.status;
          document.getElementById("jsonOutput").textContent = JSON.stringify(data, null, 2);

          resultSection.style.display = "block";
        }
      } catch (err) {
        errorBox.textContent = "Network Error: API से कनेक्ट नहीं हो सका।";
        errorBox.style.display = "block";
      } finally {
        btn.textContent = "Execute Search";
        btn.disabled = false;
      }
    }

    function copyJson() {
      const text = document.getElementById("jsonOutput").textContent;
      navigator.clipboard.writeText(text).then(() => {
        const btn = document.querySelector(".copy-btn");
        btn.textContent = "Copied!";
        setTimeout(() => { btn.textContent = "Copy JSON"; }, 1500);
      });
    }

    document.getElementById("mobileInput").addEventListener("keypress", function (e) {
      if (e.key === "Enter") {
        runSearch();
      }
    });
  </script>
</body>
</html>
"""


@app.route("/")
def home():
    return HTML_PAGE


@app.route("/api")
def api_welcome():
    return jsonify({
        "status": "online",
        "project": "ZYRON API",
        "developer": "@zyrondev",
        "message": "Welcome to ZYRON",
        "mode": "Fictional XYZ Testing Data",
        "endpoints": {
            "frontend": "/",
            "search": "/api/search?number=9999999999"
        }
    })


@app.route("/api/search")
def api_search():
    global search_counter
    number = request.args.get("number", "").strip()

    if not number.isdigit() or len(number) != 10:
        return jsonify({
            "status": "error",
            "developer": "@zyrondev",
            "message": "Invalid number. Please enter a 10-digit demo number."
        }), 400

    search_counter += 1

    if number in DEMO_DATABASE:
        record = DEMO_DATABASE[number].copy()
    else:
        city_index = int(number[-1]) % len(DEMO_CITIES)
        record = {
            "demo_id": f"ZYR-XYZ-{number[-3:]}",
            "name": f"XYZ Demo User {number[-2:]}",
            "city": DEMO_CITIES[city_index],
            "status": "GENERATED - TEST MODE",
            "note": "Fictional XYZ Testing Data"
        }

    record["mobile"] = number

    return jsonify({
        "status": "success",
        "project": "ZYRON API",
        "developer": "@zyrondev",
        "search_count": search_counter,
        "result": record
    })


if __name__ == "__main__":
    app.run(debug=True)
