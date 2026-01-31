const API_URL = "http://127.0.0.1:8000";

const ideaInput = document.getElementById("ideaInput");
const generateBtn = document.getElementById("generateBtn");
const loadingDiv = document.getElementById("loading");
const resultsSection = document.getElementById("results");
const resetBtn = document.getElementById("resetBtn");
const featuresSection = document.getElementById("featuresSection");
const tabButtons = document.querySelectorAll(".tab-btn");
const tabContents = document.querySelectorAll(".tab-content");

// Tab switching
if (tabButtons.length > 0) {
  tabButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      tabButtons.forEach(b => b.classList.remove("active"));
      tabContents.forEach(t => t.classList.add("hidden"));
      btn.classList.add("active");
      document.getElementById(btn.dataset.tab).classList.remove("hidden");
    });
  });
}

generateBtn.addEventListener("click", generateAllBranding);
resetBtn.addEventListener("click", resetForm);
ideaInput.addEventListener("keypress", (e) => {
  if (e.key === "Enter") generateAllBranding();
});

async function generateAllBranding() {
  const idea = ideaInput.value.trim();
  
  if (!idea) {
    alert("Please enter a business idea");
    return;
  }

  try {
    loadingDiv.classList.remove("hidden");
    resultsSection.classList.add("hidden");
    featuresSection.classList.add("hidden");
    generateBtn.disabled = true;

    // Generate branding
    const brandResponse = await fetch(`${API_URL}/branding/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ idea: idea }),
    });

    if (!brandResponse.ok) throw new Error(`Brand API Error: ${brandResponse.status}`);
    const brandData = await brandResponse.json();

    // Generate copy
    const copyResponse = await fetch(`${API_URL}/content/generate`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ idea: idea }),
    });

    if (!copyResponse.ok) throw new Error(`Copy API Error: ${copyResponse.status}`);
    const copyData = await copyResponse.json();

    // Generate style system
    const styleResponse = await fetch(`${API_URL}/style/generate`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ idea: idea, industry: "technology" }),
    });

    if (!styleResponse.ok) throw new Error(`Style API Error: ${styleResponse.status}`);
    const styleData = await styleResponse.json();

    // Display Brand DNA results
    document.getElementById("resultName").textContent = brandData.name;
    document.getElementById("resultSlogan").textContent = brandData.slogan;
    
    const logoImg = document.getElementById("resultLogo");
    logoImg.src = brandData.logo;
    logoImg.alt = `${brandData.name} Logo`;
    logoImg.onerror = function() {
      this.src = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300' viewBox='0 0 300 300'%3E%3Crect fill='%23ff3d81' width='300' height='300'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' font-family='Arial' font-size='40' fill='white' font-weight='bold'%3E" + brandData.name.substring(0, 2).toUpperCase() + "%3C/text%3E%3C/svg%3E";
    };
    
    document.getElementById("resultGuide").innerHTML = formatGuide(brandData.guide);

    // Display Copy Catalyst results if elements exist
    if (document.getElementById("socialPost1")) {
      document.getElementById("socialPost1").textContent = copyData.social_posts[0];
      document.getElementById("socialPost2").textContent = copyData.social_posts[1];
      document.getElementById("socialPost3").textContent = copyData.social_posts[2];
      document.getElementById("landingHeadline").textContent = copyData.landing_headline;
      document.getElementById("productDesc").textContent = copyData.product_description;
      document.getElementById("emailSubject").textContent = copyData.email_subject;
    }

    // Display Style Architect results if elements exist
    if (document.getElementById("primaryColor")) {
      document.getElementById("primaryColor").textContent = styleData.primary_color;
      document.getElementById("primaryColorBox").style.backgroundColor = styleData.primary_color;
      
      document.getElementById("secondaryColor").textContent = styleData.secondary_color;
      document.getElementById("secondaryColorBox").style.backgroundColor = styleData.secondary_color;
      
      document.getElementById("accentColor").textContent = styleData.accent_color;
      document.getElementById("accentColorBox").style.backgroundColor = styleData.accent_color;

      document.getElementById("typography").innerHTML = `
        <p><strong>Heading Font:</strong> ${styleData.typography.heading_font}</p>
        <p><strong>Body Font:</strong> ${styleData.typography.body_font}</p>
        <p><strong>Line Height:</strong> ${styleData.typography.line_height}</p>
      `;

      document.getElementById("principles").innerHTML = styleData.design_principles
        .map(p => `<li>${p}</li>`)
        .join("");
    }

    loadingDiv.classList.add("hidden");
    resultsSection.classList.remove("hidden");
    
    // Set first tab as active if tabs exist
    if (tabButtons.length > 0) {
      tabButtons[0].click();
    }

  } catch (error) {
    console.error("Error:", error);
    loadingDiv.classList.add("hidden");
    alert("Error generating brand: " + error.message);
  } finally {
    generateBtn.disabled = false;
  }
}

function resetForm() {
  ideaInput.value = "";
  resultsSection.classList.add("hidden");
  featuresSection.classList.remove("hidden");
  ideaInput.focus();
}

function formatGuide(guide) {
  // Split by numbers and periods to create a structured list
  let formatted = guide
    .split(/(\d+\.)/)
    .filter(part => part.trim())
    .join('')
    .split('\n')
    .map(line => {
      // Check for color codes (#XXXXXX format)
      const colorRegex = /#[0-9a-fA-F]{6}/g;
      const colors = line.match(colorRegex) || [];
      
      let html = line;
      
      // Replace color codes with color swatches
      colors.forEach(color => {
        const swatch = `<span class="color-swatch" style="background-color: ${color};" title="${color}"></span> <code>${color}</code>`;
        html = html.replace(color, swatch);
      });
      
      return `<p>${html}</p>`;
    })
    .join('');
  
  return formatted;
}
