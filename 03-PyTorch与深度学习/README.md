# 03 - PyTorch 与深度学习（D044–D064）

**主课**：[刘二大人《PyTorch 深度学习实践》](https://www.bilibili.com/video/BV1Y7411d7Ys)（第一遍，快）
**辅课**：[李沐《动手学深度学习》](https://courses.d2l.ai/zh-v2/)（第二遍，深。B 站搜「跟李沐学AI」）
**辅课重点**：线性神经网络 → 多层感知机 → 深度学习计算 → 卷积神经网络（前 6 章）

**硬件**：RTX 4070 Laptop (8GB) —— 训练 MNIST / CIFAR-10 绰绰有余，注意笔记本散热。

## D044 先装 PyTorch

```bash
conda activate rl
# 去 https://pytorch.org/get-started/locally/ 选 Windows + Conda + CUDA 12.x，复制它给的命令

# 装完立刻验证（这一步不能省）
python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
# 必须输出 True！输出 False 说明装成了 CPU 版，卸载重装
```

> ⚠️ 别直接用 `pip install torch`，容易装成 CPU 版或者从国外源慢到超时。

## 训练五步循环（背下来，RL 阶段天天用）

```python
for epoch in range(n_epochs):
    y_pred = model(x)              # 1 前向传播
    loss = criterion(y_pred, y)    # 2 计算损失
    optimizer.zero_grad()          # 3 梯度清零  ← 忘了这步必错
    loss.backward()                # 4 反向传播
    optimizer.step()               # 5 更新参数
```

## 🔴 阶段验收（D064）

**A. 不用 autograd，纯 NumPy 手写两层 MLP 的反向传播** ★ 全计划最硬的骨头

```python
# 要求（不许用 torch.autograd）：
# 1. 网络：输入 784 → 隐藏 128 (ReLU) → 输出 10 (Softmax)
# 2. 手推并手写 dW2, db2, dW1, db1 的梯度公式
# 3. 在 MNIST 上训练到 >90%
# 4. 写笔记：把链式法则的推导过程完整写下来
```

> 做完这一题，你就真的懂神经网络了。做过的人不到学过深度学习的人的 20%。

**B. CIFAR-10 训练脚本**：用 `argparse` 传参（lr / batch_size / epochs），画 loss + accuracy 曲线，保存最佳权重（准确率 >70%）

**C. 能回答这 5 个问题**（写进笔记）

1. `optimizer.zero_grad()` 不写会怎样？
2. `model.eval()` 和 `torch.no_grad()` 分别解决什么问题？
3. 为什么需要激活函数？不加会退化成什么？
4. `BCELoss` 和 `CrossEntropyLoss` 对输入的要求有什么区别？
5. 过拟合的三个典型信号是什么？

## 第一批项目文件命名建议

```
D044_cuda_check.py           D050_训练五步循环.py
D054_mnist_mlp.py            D057_cifar10_cnn.py
D062_手写反向传播/
    ├── mlp_numpy.py         ← 纯 numpy 版本
    ├── mlp_torch.py         ← 对照的 torch 版本
    └── 推导笔记.md
```
