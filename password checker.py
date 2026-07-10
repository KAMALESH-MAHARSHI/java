import re
import math

COMMON_PASSWORDS = {
    'password', '123456', '123456789', 'qwerty', 'admin', 'letmein',
    'welcome', 'iloveyou', 'monkey', 'dragon', 'abc123', 'password1'
}

SYMBOLS = set('!@#$%^&*()-_=+[]{}|;:\'",.<>/?`~\\')


def analyze_password(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in SYMBOLS for c in password)

    score = 0
    score += min(length * 4, 40)
    score += 10 if has_upper else 0
    score += 10 if has_lower else 0
    score += 10 if has_digit else 0
    score += 15 if has_symbol else 0
    score += 5 if length >= 12 else 0
    score += 5 if password.lower() not in COMMON_PASSWORDS else -20

    score = max(0, min(100, score))

    if score >= 80:
        strength = 'STRONG 🟢'
    elif score >= 60:
        strength = 'MODERATE 🟡'
    elif score >= 40:
        strength = 'WEAK 🟠'
    else:
        strength = 'VERY WEAK 🔴'

    charset = 0
    if has_lower:
        charset += 26
    if has_upper:
        charset += 26
    if has_digit:
        charset += 10
    if has_symbol:
        charset += 32
    charset = max(charset, 10)

    guesses = charset ** max(length, 1)
    guesses_per_sec = 1e9
    seconds = guesses / guesses_per_sec
    years = seconds / (60 * 60 * 24 * 365)

    if years < 1:
        crack_time = f'≈ {int(seconds // 60)} minutes'
    elif years < 1000:
        crack_time = f'≈ {int(years)} years'
    else:
        crack_time = '≈ very long time'

    suggestions = []
    if length < 12:
        suggestions.append('Use at least 12 characters')
    if not has_upper:
        suggestions.append('Add uppercase letters')
    if not has_lower:
        suggestions.append('Add lowercase letters')
    if not has_digit:
        suggestions.append('Add numbers')
    if not has_symbol:
        suggestions.append('Add symbols')
    if password.lower() in COMMON_PASSWORDS:
        suggestions.append('Avoid common passwords')
    if not suggestions:
        suggestions.append('Excellent Password')

    return {
        'password': password,
        'strength': strength,
        'score': score,
        'has_upper': has_upper,
        'has_lower': has_lower,
        'has_digit': has_digit,
        'has_symbol': has_symbol,
        'crack_time': crack_time,
        'suggestions': suggestions,
    }


def print_report(result):
    print('====================================')
    print('PASSWORD SECURITY ANALYZER')
    print('====================================\n')
    print('Enter Password:')
    print(result['password'])
    print(f"\nPassword Strength : {result['strength']}")
    print(f"Security Score    : {result['score']}/100\n")
    print('Contains')
    print('✔ Uppercase' if result['has_upper'] else '✘ Uppercase')
    print('✔ Lowercase' if result['has_lower'] else '✘ Lowercase')
    print('✔ Numbers' if result['has_digit'] else '✘ Numbers')
    print('✔ Symbols' if result['has_symbol'] else '✘ Symbols')
    print('\nEstimated Crack Time')
    print(result['crack_time'])
    print('\nSuggestions')
    for s in result['suggestions']:
        print(f'✓ {s}')


if __name__ == '__main__':
    password = input('Enter Password: ')
    result = analyze_password(password)
    print_report(result)