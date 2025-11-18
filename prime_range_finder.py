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
import argparse
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


def find_primes_in_range(start, end, output_file, max_primes=None, batch_size=10000, progress_interval=10000000):
    """
    在指定范围内查找所有质数并写入CSV文件

    参数:
        start: 起始值（包含）
        end: 结束值（包含）
        output_file: 输出CSV文件路径
        max_primes: 最大质数数量限制（None表示无限制）
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
    if max_primes:
        print(f"质数数量限制: {max_primes} 个")
    else:
        print(f"质数数量限制: 无限制（完整遍历）")
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

                # 检查是否达到质数数量限制
                if max_primes and prime_count >= max_primes:
                    print(f"\n已找到 {max_primes} 个质数，达到限制，停止遍历")
                    break

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


def estimate_time_and_space(mode, start, end):
    """
    估算运行时间和磁盘空间

    参数:
        mode: 运行模式 (mini/pro/full)
        start: 起始值
        end: 结束值

    返回:
        (预计时间秒数, 预计磁盘空间MB, 预计质数数量)
    """
    # 基于测试的速度：万亿级别约900个/秒
    CHECK_SPEED = 900  # 每秒检查的数字数量

    # 每个CSV行约占用字节数（序号+逗号+质数+换行，约30字节）
    BYTES_PER_PRIME = 30

    if mode == 'mini':
        target_primes = 10
        # 根据质数定理，1e12附近质数密度约为 1/ln(n) ≈ 1/27.6
        # 平均每28个数有1个质数，所以找10个质数约需检查280个数
        estimated_checks = target_primes * 28
        estimated_time = estimated_checks / CHECK_SPEED
        estimated_space = target_primes * BYTES_PER_PRIME / (1024 * 1024)  # MB
        return estimated_time, estimated_space, target_primes

    elif mode == 'pro':
        target_primes = 100
        estimated_checks = target_primes * 28
        estimated_time = estimated_checks / CHECK_SPEED
        estimated_space = target_primes * BYTES_PER_PRIME / (1024 * 1024)  # MB
        return estimated_time, estimated_space, target_primes

    else:  # full
        # 完整范围：需要检查的奇数数量
        total_checks = (end - start) // 2
        # 根据质数定理估算质数数量
        # π(x) ≈ x / ln(x)
        primes_at_start = start / math.log(start)
        primes_at_end = end / math.log(end)
        estimated_primes = int(primes_at_end - primes_at_start)

        estimated_time = total_checks / CHECK_SPEED
        estimated_space = estimated_primes * BYTES_PER_PRIME / (1024 * 1024)  # MB
        return estimated_time, estimated_space, estimated_primes


def main():
    """
    主程序
    """
    # 解析命令行参数
    parser = argparse.ArgumentParser(
        description='大范围质数遍历程序 - 查找 1×10^12 到 2×10^12-1 范围内的质数',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
运行模式说明：
  mini  - 找到前10个质数后停止（快速测试）
  pro   - 找到前100个质数后停止（中等测试）
  full  - 完整遍历整个范围（需要数天甚至数月）

使用示例：
  python prime_range_finder.py --mode mini
  python prime_range_finder.py --mode pro
  python prime_range_finder.py --mode full
        """
    )

    parser.add_argument(
        '--mode',
        type=str,
        choices=['mini', 'pro', 'full'],
        default='mini',
        help='运行模式：mini(10个质数) / pro(100个质数) / full(完整遍历)'
    )

    args = parser.parse_args()
    mode = args.mode

    # 定义范围
    START = 1 * 10**12  # 1,000,000,000,000
    END = 2 * 10**12 - 1  # 1,999,999,999,999
    OUTPUT_FILE = "prime_13bits.csv"

    # 根据模式设置质数数量限制
    MODE_CONFIG = {
        'mini': {'max_primes': 10, 'description': '快速模式（前10个质数）'},
        'pro': {'max_primes': 100, 'description': '专业模式（前100个质数）'},
        'full': {'max_primes': None, 'description': '完整模式（全部遍历）'}
    }

    max_primes = MODE_CONFIG[mode]['max_primes']
    mode_description = MODE_CONFIG[mode]['description']

    # 估算时间和磁盘空间
    estimated_time, estimated_space, estimated_primes = estimate_time_and_space(mode, START, END)

    # 显示模式信息
    print("\n" + "=" * 70)
    print("大范围质数查找器")
    print("=" * 70)
    print(f"运行模式: {mode.upper()} - {mode_description}")
    print(f"查找范围: {START:,} 到 {END:,}")
    print(f"范围大小: {END - START + 1:,} 个数字")
    print("=" * 70)

    # 显示预估信息
    print("\n【预估信息】")
    print(f"预计找到质数: {estimated_primes:,} 个")

    if estimated_time < 1:
        print(f"预计运行时间: {estimated_time:.2f} 秒")
    elif estimated_time < 60:
        print(f"预计运行时间: {estimated_time:.1f} 秒")
    elif estimated_time < 3600:
        print(f"预计运行时间: {estimated_time/60:.1f} 分钟")
    elif estimated_time < 86400:
        print(f"预计运行时间: {estimated_time/3600:.1f} 小时")
    else:
        days = estimated_time / 86400
        print(f"预计运行时间: {days:.1f} 天 ({days/30:.1f} 月)")

    if estimated_space < 1:
        print(f"预计磁盘空间: {estimated_space*1024:.2f} KB")
    elif estimated_space < 1024:
        print(f"预计磁盘空间: {estimated_space:.2f} MB")
    else:
        print(f"预计磁盘空间: {estimated_space/1024:.2f} GB")

    print(f"输出文件: {OUTPUT_FILE}")

    # 根据模式显示不同的警告
    if mode == 'full':
        print("\n" + "!" * 70)
        print("【重要警告】")
        print("!" * 70)
        print("完整模式将遍历整个范围，这需要极长的时间和大量磁盘空间！")
        print(f"- 预计需要检查约 {(END - START)//2:,} 个奇数")
        print(f"- 可能需要 {estimated_time/86400:.0f} 天甚至更长时间")
        print(f"- 磁盘空间需求约 {estimated_space/1024:.1f} GB")
        print("\n建议：")
        print("1. 确保有足够的磁盘空间")
        print("2. 建议在高性能服务器上运行")
        print("3. 考虑使用 mini 或 pro 模式进行测试")
        print("4. 可以按 Ctrl+C 随时中断程序")
        print("!" * 70)
    else:
        print("\n提示：")
        print("- 程序会在找到指定数量的质数后自动停止")
        print("- 可以按 Ctrl+C 随时中断程序")
        print("- 已找到的质数会自动保存到文件")

    # 二次确认
    print("\n" + "=" * 70)
    try:
        response = input(f"确认以 {mode.upper()} 模式运行？(yes/no): ").strip().lower()
        if response not in ['yes', 'y']:
            print("程序已取消")
            return
    except KeyboardInterrupt:
        print("\n程序已取消")
        return

    print()

    # 开始查找质数
    try:
        find_primes_in_range(START, END, OUTPUT_FILE, max_primes=max_primes)
    except KeyboardInterrupt:
        print("\n\n程序被用户中断！")
        print(f"已找到的质数已保存到 {OUTPUT_FILE}")
    except Exception as e:
        print(f"\n发生错误：{e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
