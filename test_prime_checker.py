#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试质数判断程序的核心功能
"""

from prime_checker import is_prime, get_all_factors


def test_is_prime():
    """测试质数判断功能"""
    print("测试质数判断功能:")
    print("-" * 40)

    test_cases = [
        (1, False, "1不是质数"),
        (2, True, "2是最小的质数"),
        (3, True, "3是质数"),
        (4, False, "4不是质数（2的倍数）"),
        (17, True, "17是质数"),
        (100, False, "100不是质数"),
        (97, True, "97是质数"),
        (1000000007, True, "1000000007是大质数"),
    ]

    for num, expected, description in test_cases:
        result = is_prime(num)
        status = "✓" if result == expected else "✗"
        print(f"{status} {num}: {result} - {description}")

    print()


def test_get_all_factors():
    """测试因数获取功能"""
    print("测试因数获取功能:")
    print("-" * 40)

    test_cases = [
        (12, [1, 2, 3, 4, 6, 12]),
        (20, [1, 2, 4, 5, 10, 20]),
        (36, [1, 2, 3, 4, 6, 9, 12, 18, 36]),
        (100, [1, 2, 4, 5, 10, 20, 25, 50, 100]),
    ]

    for num, expected in test_cases:
        result = get_all_factors(num)
        status = "✓" if result == expected else "✗"
        print(f"{status} {num}的因数: {result}")

    print()


def demo_output():
    """演示程序输出"""
    print("演示程序输出:")
    print("=" * 50)

    # 测试质数
    print("测试案例1: 输入 17（质数）")
    if is_prime(17):
        print("YES，这是个质数")
    print()

    # 测试合数
    print("测试案例2: 输入 12（合数）")
    if not is_prime(12):
        print("NO，这不是质数")
        print("该数的所有因数为：")
        factors = get_all_factors(12)
        print(", ".join(map(str, factors)))
    print()

    # 测试较大的合数
    print("测试案例3: 输入 100（合数）")
    if not is_prime(100):
        print("NO，这不是质数")
        print("该数的所有因数为：")
        factors = get_all_factors(100)
        print(", ".join(map(str, factors)))
    print()


if __name__ == "__main__":
    test_is_prime()
    test_get_all_factors()
    demo_output()
    print("=" * 50)
    print("所有测试完成！")
