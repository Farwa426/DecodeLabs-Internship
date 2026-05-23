#!/usr/bin/env python3
"""
Enterprise Random Password Generator
Project 3 - DecodeLabs Internship

This tool generates cryptographically secure passwords using the secrets module
and follows NIST SP 800-63-4 guidelines for password security.
Implements Input-Process-Output architecture with rigorous input validation.
"""

import string
import secrets
import math
import sys


def get_password_length() -> int:
    """
    Phase 1: Input validation.
    Prompts the user for a password length and validates the input.
    
    Returns:
        int: Validated password length (positive integer)
    """
    while True:
        try:
            user_input = input("Enter desired password length (positive integer): ").strip()
            if not user_input:
                print("Error: No input provided. Please enter a number.")
                continue
            
            length = int(user_input)
            
            if length <= 0:
                print("Error: Password length must be a positive integer (greater than 0).")
                continue
            
            # Security advisory based on NIST guidelines
            if length < 12:
                print("Warning: NIST recommends at least 12 characters for moderate security,"
                      " and 15+ for high-security contexts.")
            elif length > 128:
                print("Note: Extremely long passwords may cause usability issues.")
                
            return length
        
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer.")


def calculate_entropy(pool_size: int, length: int) -> float:
    """
    Calculate the information entropy of a password in bits.
    Entropy = length * log2(pool_size)
    
    Args:
        pool_size (int): Number of possible characters in the pool
        length (int): Password length
    
    Returns:
        float: Entropy in bits
    """
    return length * math.log2(pool_size)


def estimate_crack_time(entropy_bits: float, guesses_per_second: float = 1e9) -> str:
    """
    Estimate the time required to brute-force a password.
    Uses a conservative estimate of 1 billion guesses per second.
    
    Args:
        entropy_bits (float): Password entropy in bits
        guesses_per_second (float): Number of guesses per second
    
    Returns:
        str: Human-readable crack time estimate
    """
    total_combinations = 2 ** entropy_bits
    seconds = total_combinations / guesses_per_second
    
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds / 60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds / 3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds / 86400:.2f} days"
    elif seconds < 31536000 * 100:
        return f"{seconds / 31536000:.2f} years"
    else:
        return f"{seconds / 31536000:.2e} years"


def generate_password(length: int) -> str:
    """
    Phase 2: Backend transformation engine.
    Generates a cryptographically secure password using the secrets module.
    
    Character pool: ASCII letters (uppercase + lowercase) and digits.
    Uses join() for O(n) time complexity and minimal memory overhead.
    
    Args:
        length (int): Desired password length
    
    Returns:
        str: Generated password
    """
    # Professional character pool using string module (avoids manual typing)
    character_pool = string.ascii_letters + string.digits
    
    # Generate password using list comprehension for efficiency
    # secrets.choice provides cryptographically secure randomness
    password_chars = [secrets.choice(character_pool) for _ in range(length)]
    
    # join() performs memory allocation exactly once (linear time complexity)
    password = ''.join(password_chars)
    
    return password, character_pool


def main() -> None:
    """
    Main orchestrator following Input-Process-Output (IPO) architectural scaffold.
    """
    print("=" * 60)
    print("Enterprise Random Password Generator")
    print("DecodeLabs Internship Project 3")
    print("=" * 60)
    print("Generates cryptographically secure passwords using secrets module.\n")
    
    while True:
        # Phase 1: Input
        length = get_password_length()
        
        # Phase 2: Process (Backend transformation)
        password, pool = generate_password(length)
        pool_size = len(pool)
        
        # Phase 3: Output & Security Mathematics
        entropy = calculate_entropy(pool_size, length)
        crack_estimate = estimate_crack_time(entropy)
        
        print("\n" + "-" * 40)
        print("GENERATED PASSWORD:")
        print(f"{password}")
        print("-" * 40)
        print(f"Password Length: {length} characters")
        print(f"Character Pool Size: {pool_size}")
        print(f"Total Possibilities: {pool_size ** length:,}")
        print(f"Information Entropy: {entropy:.2f} bits")
        print(f"Estimated Crack Time (1B guesses/sec): {crack_estimate}")
        print("-" * 40)
        
        # Optional: Regeneration loop
        while True:
            choice = input("\nGenerate another password? (y/n): ").strip().lower()
            if choice in ('y', 'yes'):
                print("\n" + "=" * 60)
                break
            elif choice in ('n', 'no'):
                print("\nExiting. Secure your credentials responsibly.")
                sys.exit(0)
            else:
                print("Invalid input. Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()