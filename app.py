"""A tiny order-total calculator used only to produce genuine CI results."""
def order_total(prices):
    if any(price < 0 for price in prices):
        raise ValueError("Prices cannot be negative")
    return sum(prices)
