import sqlite3
import os

# Défaut 1 : secret exposé en dur (à détecter par Gitleaks)
API_KEY = "sk-test-51H8x9K2mP4qR7vN3wZ8yT6bL0cF5dA2e"

def get_user(user_id):
    """Défaut 2 : injection SQL (à détecter par Semgrep)"""
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    return cursor.fetchone()

def process_order(order, user, discount, stock, is_vip, region, payment_method, has_coupon):
    """Défaut 3 : complexité cyclomatique excessive (à détecter par SonarCloud)"""
    if order:
        if user:
            if discount > 0:
                if is_vip:
                    if region == "EU":
                        if payment_method == "card":
                            if has_coupon:
                                if stock > 0:
                                    return "processed_vip_eu_card_coupon"
                                else:
                                    return "out_of_stock"
                            else:
                                return "processed_vip_eu_card"
                        else:
                            return "processed_vip_eu_other"
                    else:
                        return "processed_vip_other_region"
                else:
                    return "processed_regular"
            else:
                return "no_discount"
        else:
            return "no_user"
    else:
        return "no_order"

def run_command(user_input):
    """Défaut 4 bonus : eval() dangereux (autre chose pour Semgrep)"""
    return eval(user_input)
