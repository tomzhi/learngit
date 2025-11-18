#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
质数判断程序
功能：判断用户输入的正整数是否为质数，如果不是，则显示所有因数
"""

import math


def is_prime(n):
    """
    判断一个数是否为质数

    参数:
        n: 待判断的正整数

    返回:
        True: 是质数
        False: 不是质数
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # 只需检查到 sqrt(n)
    sqrt_n = int(math.sqrt(n))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False

    return True


def get_all_factors(n):
    """
    获取一个数的所有因数（约数）

    参数:
        n: 待分解的正整数

    返回:
        排序后的因数列表
    """
    factors = []
    sqrt_n = int(math.sqrt(n))

    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:  # 避免重复添加（如当n为完全平方数时）
                factors.append(n // i)

    return sorted(factors)


def main():
    """
    主程序
    """
    # Python 3 理论上支持任意大的整数，但考虑算法效率，设定实际限制
    MAX_VALUE = 10 ** 15  # 1,000,000,000,000,000

    print("=" * 50)
    print("质数判断程序")
    print("=" * 50)
    print(f"说明：本程序支持判断 1 到 {MAX_VALUE:,} 之间的正整数")
    print(f"Python 3 不存在整数溢出问题，但超大数字判断可能耗时较长")
    print("=" * 50)
    print()

    while True:
        try:
            # 获取用户输入
            user_input = input("请输入一个正整数（输入 'q' 退出）：").strip()

            # 检查是否退出
            if user_input.lower() == 'q':
                print("感谢使用，再见！")
                break

            # 转换为整数
            number = int(user_input)

            # 验证输入范围
            if number < 1:
                print("错误：请输入大于0的正整数！\n")
                continue

            if number > MAX_VALUE:
                print(f"警告：输入值超过推荐范围 {MAX_VALUE:,}，计算可能耗时较长")
                confirm = input("是否继续？(y/n): ").strip().lower()
                if confirm != 'y':
                    print("已取消\n")
                    continue

            # 判断是否为质数
            print(f"\n正在判断 {number:,} ...\n")

            if is_prime(number):
                print("YES，这是个质数")
            else:
                print("NO，这不是质数")
                print("该数的所有因数为：")
                factors = get_all_factors(number)

                # 格式化输出因数
                print(", ".join(map(str, factors)))

            print("\n" + "-" * 50 + "\n")

        except ValueError:
            print("错误：请输入有效的整数！\n")
        except KeyboardInterrupt:
            print("\n\n程序被用户中断，再见！")
            break
        except Exception as e:
            print(f"发生错误：{e}\n")


if __name__ == "__main__":
    main()
