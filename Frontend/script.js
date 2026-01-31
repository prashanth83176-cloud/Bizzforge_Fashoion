const API_URL = "https://bizzforge-fashoion.onrender.com";

const ideaInput = document.getElementById("ideaInput");
const generateBtn = document.getElementById("generateBtn");
const loadingDiv = document.getElementById("loading");
const resultsSection = document.getElementById("results");
const resetBtn = document.getElementById("resetBtn");
const featuresSection = document.getElementById("featuresSection");
const tabButtons = document.querySelectorAll(".tab-btn");
const tabContents = document.querySelectorAll(".tab-content");

// Add this at the top to switch between tabs
tabButtons.forEach(button => {
  button.addEventListener("click", () => {
    const target = button.dataset.tab;

    // Update active button
    tabButtons.forEach(btn => btn.classList.remove("active"));
    button.classList.add("active");

    // Update active content
    tabContents.forEach(content => content.classList.remove("active"));
    document.getElementById(target).classList.add("active");
  });
});

generateBtn.addEventListener("click", generateAllBranding);
resetBtn.addEventListener("click", resetForm);

ideaInput.addEventListener("keypress", (e) => {
  if (e.key === "Enter") {
    generateAllBranding();
  }
});

async function generateAllBranding() {
  const idea = ideaInput.value.trim();

  if (!idea) {
    alert("Please enter a business idea");
    return;
  }

  loadingDiv.classList.remove("hidden");
  resultsSection.classList.add("hidden");
  featuresSection.classList.add("hidden");

  try {
    // Call Brand DNA API
    const brandResponse = await fetch(`${API_URL}/branding/brand-dna`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ idea })
    });

    if (!brandResponse.ok) {
      throw new Error("Failed to generate brand DNA");
    }

    const brandData = await brandResponse.json();

    // Display Brand DNA results
    document.getElementById("resultName").textContent = brandData.name;
    document.getElementById("resultSlogan").textContent = brandData.slogan;

    const logoImg = document.getElementById("resultLogo");
    logoImg.src = brandData.logo;
    logoImg.alt = `${brandData.name} Logo`;
    logoImg.onerror = function () {
      this.src = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Crect fill='%23667eea' width='200' height='200'/%3E%3Ctext x='50%25' y='50%25' font-size='24' fill='white' text-anchor='middle' dy='.3em'%3ELogo%3C/text%3E%3C/svg%3E";
    };

    document.getElementById("resultGuide").innerHTML = formatGuide(brandData.guide);

    // Call Marketing Copy API
    const copyResponse = await fetch(`${API_URL}/content/copy-catalyst`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ idea })
    });

    if (copyResponse.ok) {
      const copyData = await copyResponse.json();
      document.getElementById("copyResult").innerHTML = `
        <h4>Social Media Post</h4>
        <p>${copyData.social_post}</p>
        <h4>Product Description</h4>
        <p>${copyData.product_description}</p>
        <h4>Email Campaign</h4>
        <p>${copyData.email_campaign}</p>
      `;
    }

    // Call Style API
    const styleResponse = await fetch(`${API_URL}/style/style-architect`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ idea })
    });

    if (styleResponse.ok) {
      const styleData = await styleResponse.json();
      document.getElementById("styleResult").innerHTML = `
        <h4>Color Palette</h4>
        <div style="display:flex;gap:10px;margin:10px 0;">
          ${styleData.colors.map(c => `<div style="background:${c};width:50px;height:50px;border-radius:8px;" title="${c}"></div>`).join('')}
        </div>
        <h4>Typography</h4>
        <p><strong>Heading:</strong> ${styleData.typography.heading}</p>
        <p><strong>Body:</strong> ${styleData.typography.body}</p>
      `;
    }

    // Call Sentiment API
    const sentimentResponse = await fetch(`${API_URL}/content/sentiment-analysis`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: brandData.slogan })
    });

    if (sentimentResponse.ok) {
      const sentimentData = await sentimentResponse.json();
      document.getElementById("sentimentResult").innerHTML = `
        <p><strong>Sentiment:</strong> ${sentimentData.sentiment}</p>
        <p><strong>Score:</strong> ${sentimentData.score.toFixed(2)}</p>
        <p><strong>Rationale:</strong> ${sentimentData.rationale}</p>
      `;
    }

    loadingDiv.classList.add("hidden");
    resultsSection.classList.remove("hidden");

  } catch (error) {
    console.error("Error:", error);
    alert("Failed to generate branding. Please try again.");
    loadingDiv.classList.add("hidden");
    featuresSection.classList.remove("hidden");
  }
}

function resetForm() {
  ideaInput.value = "";
  resultsSection.classList.add("hidden");
  featuresSection.classList.remove("hidden");
  ideaInput.focus();
}

function formatGuide(guide) {
  // Convert guide text to nice HTML with proper formatting
  return guide
    .split('\n')
    .map(line => {
      if (line.startsWith('**') && line.endsWith('**')) {
        return `<h4>${line.replace(/\*\*/g, '')}</h4>`;
      } else if (line.trim() === '') {
        return '<br>';
      } else if (line.startsWith('- ')) {
        return `<li>${line.substring(2)}</li>`;
      } else {
        return `<p>${line}</p>`;
      }
    })
    .join('');
}
