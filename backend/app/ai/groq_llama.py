def llama_generate(prompt: str) -> str:
    """Mock Groq LLaMA text generation"""
    import hashlib
    
    prompt_lower = prompt.lower()
    hash_digest = hashlib.md5(prompt.encode()).hexdigest()
    hash_int = int(hash_digest[:8], 16)
    
    # Brand name generation
    if "name" in prompt_lower and "brand" in prompt_lower:
        name_prefixes = ["Cloud", "Vital", "Quantum", "Nexus", "Zenith", "Apex", "Pinnacle", "Nova", "Flux", "Prism"]
        name_suffixes = ["Mind", "Edge", "Flow", "Sync", "Pulse", "Wave", "Core", "Hub", "Link", "Sphere"]
        
        prefix_idx = hash_int % len(name_prefixes)
        suffix_idx = (hash_int // len(name_prefixes)) % len(name_suffixes)
        
        return f"{name_prefixes[prefix_idx]}{name_suffixes[suffix_idx]}"
    
    # Slogan generation
    elif "slogan" in prompt_lower:
        slogans = [
            "Transforming Tomorrow, Today",
            "Intelligence Reimagined",
            "Your Success, Our Mission",
            "Innovation Unlocked",
            "The Future is Now",
            "Empowering Excellence",
            "Simplifying Complexity",
            "Where Vision Meets Reality",
            "Elevate Your Potential",
            "Building Better Futures"
        ]
        return slogans[hash_int % len(slogans)]
    
    # Social media posts
    elif "social" in prompt_lower and "post" in prompt_lower:
        posts = [
            "🚀 Just launched something extraordinary. Here's what makes it different... [link]",
            "Behind every great brand is a story. Here's ours 👇 [link]",
            "3 reasons why this changes everything. Swipe for #1 →",
            "We just solved a problem nobody knew they had. Here's how... [link]",
            "The future of [industry] starts here. Welcome. 🎉 [link]",
            "What if everything you knew about [industry] was about to change?",
            "We didn't just build a product. We built a movement. [link]",
            "Tired of the same old? We built something different 🔥 [link]"
        ]
        return posts[hash_int % len(posts)]
    
    # Landing page headlines
    elif "headline" in prompt_lower or "landing page" in prompt_lower:
        headlines = [
            "Unlock the Future of Your Business",
            "The [Industry] Solution You've Been Waiting For",
            "Stop Struggling. Start Winning.",
            "Enter the Next Era of [Industry]",
            "Your Competitive Advantage Starts Here",
            "Transform Your [Industry] in Minutes, Not Months",
            "The Last [Industry] Tool You'll Ever Need",
            "Join Thousands Who've Already Made the Switch"
        ]
        return headlines[hash_int % len(headlines)]
    
    # Product descriptions
    elif "product description" in prompt_lower or "professional" in prompt_lower:
        descriptions = [
            "Engineered for performance. Designed for simplicity. Built for scale. Our solution combines cutting-edge technology with user-centric design to deliver unparalleled value.",
            "Experience the perfect balance of power and elegance. We've reimagined what's possible in the [industry] space, delivering results that exceed expectations.",
            "More than just a tool. A transformation. Unlock new possibilities and watch your productivity soar with our next-generation platform.",
            "Purpose-built for professionals who refuse to settle. We deliver the precision, reliability, and innovation your business demands."
        ]
        return descriptions[hash_int % len(descriptions)]
    
    # Email subjects
    elif "email subject" in prompt_lower:
        subjects = [
            "You're invited to experience something different",
            "The [industry] breakthrough you can't ignore",
            "Ready to transform your business?",
            "See what everyone's talking about (2-min read)",
            "Your [industry] game is about to change",
            "Exclusive access: The future is here",
            "Stop wasting time. Start winning.",
            "This changes everything about how you [action]"
        ]
        return subjects[hash_int % len(subjects)]
    
    return f"Generated content for: {prompt}"
    