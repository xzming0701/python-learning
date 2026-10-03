# 02 - NumPy / pandas / Matplotlib（D030–D043）

**主课**：[Numpy+Pandas+Matplotlib 教程](https://www.bilibili.com/video/BV12Hac6fETB)
**时间分配**：NumPy 60% ｜ Matplotlib 25% ｜ pandas 15%

**为什么不能跳**：强化学习的代码 90% 是「矩阵运算 + 随机采样 + 画曲线」。跳过这 14 天，第四阶段必然卡死。

## D030 先装依赖

```bash
conda activate rl
pip install jupyter numpy pandas matplotlib
jupyter notebook        # 或者直接在 VS Code 里新建 .ipynb
```

笔记写在 `../notes/learning-log.ipynb`，这个文件夹放独立脚本。

## 必须吃透的 4 个概念

| 概念 | 为什么重要 | 自检 |
|---|---|---|
| **广播 broadcasting** | 写错 shape 是 RL 代码最常见 bug | 能说出广播的 3 条规则 |
| **axis 参数** | `sum(axis=0)` 和 `axis=1` 分不清就废了 | 对 3×4 矩阵能手算两种结果 |
| **布尔索引** | `a[a > 0]` 比循环快 100 倍 | 能从随机数组筛出 >0.5 的元素 |
| **np.random** | RL 全是随机采样；seed 保证实验可复现 | 每次跑实验先 `np.random.seed(42)` |

## 🔴 阶段验收（D043）

**A. 纯 NumPy 实现线性回归的批量梯度下降**（不许用任何 for 循环、不许用 sklearn）

```python
# 要求：
# 1. 自己造数据 y = 3x + 2 + 噪声
# 2. 手写 MSE loss 和梯度公式
# 3. 纯矩阵运算更新 w 和 b
# 4. 画出 loss 下降曲线（要清晰到能放进笔记）
# 5. 最终学到 w≈3, b≈2
```

> 这一题是**第三阶段手写反向传播的预演**。当时觉得难没关系，D062 会再来一次。

**B. 随机游走模拟**：10000 个粒子各走 1000 步，画最终位置直方图，观察接近什么分布

**C. 数据可视化小项目**：自己造「某班 50 人 5 门课成绩」数据 → pandas 分析 → Matplotlib 画 2×2 汇总图（分布 / 相关性 / 排名 / 箱线图）
