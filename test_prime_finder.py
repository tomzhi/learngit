#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
质数查找器测试程序
用小范围测试程序的正确性
"""

from prime_range_finder import find_primes_in_range
import os


def test_small_range():
    """
    使用小范围测试程序
    """
    print("=" * 70)
    print("测试程序 - 小范围质数查找")
    print("=" * 70)

    # 测试范围：1000 到 1100
    test_file = "test_primes.csv"

    print("\n测试1: 查找 1000-1100 之间的质数")
    print("-" * 70)
    find_primes_in_range(1000, 1100, test_file, batch_size=10, progress_interval=50)

    # 验证结果
    print("\n验证结果：")
    known_primes = [1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061,
                    1063, 1069, 1087, 1091, 1093, 1097]

    with open(test_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()[1:]  # 跳过标题行
        found_primes = [int(line.strip().split(',')[1]) for line in lines]

    print(f"已知该范围内的质数: {known_primes}")
    print(f"程序找到的质数: {found_primes}")

    if found_primes == known_primes:
        print("\n[OK] 测试通过！程序运行正常")
    else:
        print("\n[FAIL] 测试失败！结果不匹配")
        print(f"缺失的质数: {set(known_primes) - set(found_primes)}")
        print(f"多余的质数: {set(found_primes) - set(known_primes)}")

    # 清理测试文件
    if os.path.exists(test_file):
        os.remove(test_file)
        print(f"\n已清理测试文件: {test_file}")


def test_trillion_range_sample():
    """
    测试万亿级别的一个小样本
    """
    print("\n\n" + "=" * 70)
    print("测试2: 万亿级别样本测试")
    print("=" * 70)

    # 测试 1×10^12 附近的100个数字
    start = 1 * 10**12
    test_file = "test_trillion_sample.csv"

    print(f"\n测试范围: {start:,} 到 {start + 100:,}")
    print("-" * 70)
    find_primes_in_range(start, start + 100, test_file, batch_size=10, progress_interval=50)

    # 显示结果
    with open(test_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print(f"\n找到的质数:")
        for line in lines:
            print(line.strip())

    # 清理测试文件
    if os.path.exists(test_file):
        os.remove(test_file)
        print(f"\n已清理测试文件: {test_file}")


if __name__ == "__main__":
    test_small_range()
    test_trillion_range_sample()

    print("\n" + "=" * 70)
    print("所有测试完成！")
    print("=" * 70)
