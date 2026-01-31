def generate_logo(prompt: str) -> str:
    """Mock SDXL logo generator"""
    # Use a reliable placeholder service that generates unique images
    import hashlib
    hash_val = hashlib.md5(prompt.encode()).hexdigest()
    return f"https://ui-avatars.com/api/?name={prompt.replace(' ', '+')}&background=random&size=300&bold=true"