# utils.py
def print_response(response):
    """Print Gemini response safely"""
    print("=== Gemini API Response ===")
    # response.text may be model-dependent; adjust if structure differs
    try:
        print(response.text)
    except Exception:
        print(str(response))
