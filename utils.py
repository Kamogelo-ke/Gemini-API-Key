def print_response(response):
    """Print Gemini API response neatly"""
    print("\n=== Gemini API Response ===\n")
    try:
        print(response.text)
    except Exception:
        print(str(response))
    print("\n===========================\n")
