import requests

# define a function to get the exchange rate
def get_exchange_rate(base_currency: str, target_currency: str):
    """
    Fetches the current exchange rate between two currencies

    Args:
        base_currency (str): The base currency (eg. "CAD")
        target_currency (str): The target currency (eg. "USD")

    Returns:
        The exchange rate information as a json response, or None
        if the rate could not be fetched.
    """

    base_url = "https://hexarate.paikama.co/api/rates/latest"
    api_url = f"{base_url}/{base_currency}?target={target_currency}"

    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None