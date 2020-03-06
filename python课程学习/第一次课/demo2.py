import sys
import platform
# platform 该模块用来访问平台相关属性
# 可以产看操作系统的版本啊，类型啊，可以查看计算器网络名称，处理器信息

# sys 提供对由解释器使用或维护的某些变量、与解释器交互的函数的访问接口
# sys模块负责程序与python解释器的交互，提供了一系列的函数和变量，用于操控python运行时的环境

# 查看python版本号
print("查看python版本号:")
print(platform.python_version())
print(sys.version)
# 查看主版本号
print("查看主版本号:")
print(sys.winver)
print(sys.version_info)
# 查看Python主程序文件
print("查看Python主程序文件:")
print(sys.executable)
# 查看操作系统和计算机的相关信息
print("查看操作系统和计算机的相关信息:")
print(platform.win32_ver())
print(platform.version())
print(platform.machine())
print(platform.python_compiler())
print(platform.platform())
print(platform.architecture())
print(platform.uname())
print(platform.python_implementation())