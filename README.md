# Bittensor Demo 项目

## 项目概述

这是一个基于 Bittensor 网络的演示项目，用于连接和查询 Bittensor 子网信息。项目使用 Python 3.12+ 开发，通过 Bittensor SDK 连接到主网（Finney 网络）并查询 Subnet 55 的神经元信息。

## 项目结构

```
Bittensor_demo/
├── main.py           # 主程序文件
├── pyproject.toml    # 项目配置和依赖管理
├── uv.lock          # 依赖锁定文件
├── logs.log         # 日志文件（当前为空）
└── README.md        # 项目说明文档
```

## 功能特性

- **网络连接**: 连接到 Bittensor 主网（Finney 网络）
- **子网查询**: 查询指定子网（Subnet 55）的神经元信息
- **神经元统计**: 显示子网中神经元的总数量

## 技术栈

- **Python**: 3.12+
- **Bittensor**: >=9.12.1 (核心 SDK)
- **python-socks**: >=2.7.2 (网络代理支持)
- **包管理**: uv (现代 Python 包管理工具)

## 安装和运行

### 前置要求

- Python 3.12 或更高版本
- uv 包管理器

### 安装依赖

```bash
# 使用 uv 安装依赖
uv sync
```

### 运行程序

```bash
# 直接运行
python main.py

# 或使用 uv 运行
uv run main.py
```

## 代码说明

### main.py

主程序文件包含以下功能：

```python
import bittensor as bt

# 创建子网连接
subtensor = bt.subtensor(network='finney')  # 主网

# 查询 Subnet 55 信息
metagraph = subtensor.metagraph(netuid=55)

print(f"Subnet 55 有 {len(metagraph.neurons)} 个神经元")
```

**功能说明**:
1. 导入 Bittensor SDK
2. 创建连接到 Finney 主网的 subtensor 实例
3. 获取 Subnet 55 的元图（metagraph）
4. 统计并显示该子网中的神经元数量

## 配置说明

### pyproject.toml

项目配置文件定义了：

- **项目名称**: bittensor-demo
- **版本**: 0.1.0
- **Python 要求**: >=3.12
- **核心依赖**:
  - `bittensor>=9.12.1`: Bittensor 网络 SDK
  - `python-socks>=2.7.2`: SOCKS 代理支持

## 网络信息

- **目标网络**: Finney (Bittensor 主网)
- **目标子网**: Subnet 55
- **查询内容**: 神经元数量和基本信息

## 使用场景

这个演示项目适用于：

1. **学习 Bittensor**: 了解如何连接到 Bittensor 网络
2. **子网探索**: 查询特定子网的神经元信息
3. **网络监控**: 监控子网的健康状态和神经元数量
4. **开发基础**: 作为更复杂 Bittensor 应用的起点

## 扩展建议

可以考虑添加以下功能：

1. **多子网查询**: 支持查询多个子网
2. **详细信息**: 显示神经元的详细属性（如 stake、rank 等）
3. **实时监控**: 定期查询并记录子网状态变化
4. **数据可视化**: 将查询结果以图表形式展示
5. **错误处理**: 添加网络连接和查询的异常处理

## 注意事项

- 确保网络连接正常，能够访问 Bittensor 主网
- 首次运行可能需要一些时间来同步网络数据
- 查询结果可能会因为网络状态而有所变化

## 许可证

请根据项目需要添加适当的许可证信息。

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目。