#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
大范围质数遍历程序
功能：遍历 1×10^12 到 2×10^12-1 范围内的所有质数，输出到CSV文件
作者：质数查找器
日期：2025-11-18
"""

import csv
import math
import time
from datetime import datetime


def is_prime(n):
    """
    高效的质数判断算法（Miller-Rabin素性测试的简化版本）

    参数:
        n: 待判断的正整数

    返回:
        True: 是质数
        False: 不是质数
    """
    # 处理小于2的情况
    if n < 2:
        return False

    # 处理2和3
    if n == 2 or n == 3:
        return True

    # 排除偶数
    if n % 2 == 0:
        return False

    # 排除3的倍数
    if n % 3 == 0:
        return False

    # 6k±1优化：所有质数都可以表示为6k±1的形式（除了2和3）
    # 只需检查到sqrt(n)
    sqrt_n = int(math.sqrt(n))

    # 从5开始，按6k±1的形式检查
    i = 5
    while i <= sqrt_n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def find_primes_in_range(start, end, output_file, batch_size=10000, progress_interval=10000000):
    """
    在指定范围内查找所有质数并写入CSV文件

    参数:
        start: 起始值（包含）
        end: 结束值（包含）
        output_file: 输出CSV文件路径
        batch_size: 批量写入的大小（减少I/O操作）
        progress_interval: 进度报告间隔
    """
    print("=" * 70)
    print("大范围质数遍历程序")
    print("=" * 70)
    print(f"起始值: {start:,}")
    print(f"结束值: {end:,}")
    print(f"范围大小: {end - start + 1:,} 个数字")
    print(f"输出文件: {output_file}")
    print("=" * 70)
    print()

    # 确保起始值是奇数（偶数除了2都不是质数）
    if start % 2 == 0:
        start += 1

    prime_count = 0
    checked_count = 0
    batch = []

    start_time = time.time()
    last_progress_time = start_time

    # 打开CSV文件准备写入
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)

        # 写入标题行
        csv_writer.writerow(['序号', '质数'])

        print(f"开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"正在遍历质数...\n")

        # 遍历范围内的所有奇数
        for num in range(start, end + 1, 2):
            checked_count += 1

            # 检查是否为质数
            if is_prime(num):
                prime_count += 1
                batch.append([prime_count, num])

                # 批量写入，减少I/O操作
                if len(batch) >= batch_size:
                    csv_writer.writerows(batch)
                    batch.clear()

            # 定期显示进度
            if checked_count % progress_interval == 0:
                elapsed_time = time.time() - start_time
                current_time = time.time()
                interval_time = current_time - last_progress_time
                last_progress_time = current_time

                progress = (num - start) / (end - start) * 100
                speed = progress_interval / interval_time if interval_time > 0 else 0

                print(f"进度: {progress:.2f}% | "
                      f"当前数字: {num:,} | "
                      f"已找到质数: {prime_count:,} | "
                      f"速度: {speed:,.0f} 个/秒 | "
                      f"耗时: {elapsed_time:.1f}秒")

        # 写入剩余的质数
        if batch:
            csv_writer.writerows(batch)

    # 计算总耗时
    total_time = time.time() - start_time

    print("\n" + "=" * 70)
    print("遍历完成！")
    print("=" * 70)
    print(f"结束时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"总耗时: {total_time:.2f} 秒 ({total_time/3600:.2f} 小时)")
    print(f"检查数字总数: {checked_count:,}")
    print(f"找到质数总数: {prime_count:,}")
    print(f"平均速度: {checked_count/total_time:,.0f} 个/秒")
    print(f"质数密度: {prime_count/checked_count*100:.4f}%")
    print(f"结果已保存到: {output_file}")
    print("=" * 70)


def main():
    """
    主程序
    """
    # 定义范围
    START = 1 * 10**12  # 1,000,000,000,000
    END = 2 * 10**12 - 1  # 1,999,999,999,999
    OUTPUT_FILE = "prime_13bits.csv"

    print("\n警告：此程序将遍历 1 万亿个数字，可能需要数小时甚至数天！")
    print(f"预计需要检查约 {(END - START)//2:,} 个奇数")
    print("\n提示：")
    print("1. 建议在性能较好的计算机上运行")
    print("2. 可以按 Ctrl+C 随时中断程序")
    print("3. 程序会定期显示进度和预计剩余时间")
    print("4. 结果会批量写入文件，避免数据丢失\n")

    # 确认是否继续
    try:
        response = input("是否继续运行？(yes/no): ").strip().lower()
        if response not in ['yes', 'y']:
            print("程序已取消")
            return
    except KeyboardInterrupt:
        print("\n程序已取消")
        return

    print()

    # 开始查找质数
    try:
        find_primes_in_range(START, END, OUTPUT_FILE)
    except KeyboardInterrupt:
        print("\n\n程序被用户中断！")
        print(f"已找到的质数已保存到 {OUTPUT_FILE}")
    except Exception as e:
        print(f"\n发生错误：{e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
