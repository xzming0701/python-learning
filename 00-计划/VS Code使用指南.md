# VS Code 使用指南（学习期主力编辑器）

> 背景：PyCharm 专业版试用到期，学生授权还在审批（1–2 周）。审批下来前用 VS Code。
> 实际上 VS Code 是**长期更值得熟练的**工具 —— 后面做数据分析跑 Jupyter、连远程 GPU 服务器都用它。

---

## 一、第一步：把仓库作为「文件夹」打开

**关键：一定要「打开文件夹」，不要「打开文件」。**

之前你在 PyCharm 里打开的是单个 `.py` 文件，结果文件被复制到了 `AppData\Local\Temp\` 临时目录 —— 这是个经典陷阱，代码会莫名其妙"找不到"。

### 操作

1. 打开 VS Code
2. 菜单 **文件 → 打开文件夹**（或按 `Ctrl+K` 然后 `Ctrl+O`）
3. 选择 **`D:\code\python-learning`**
4. 如果弹出「是否信任此文件夹中的作者」→ 选 **是，我信任**

左侧应该出现完整的仓库结构：`00-计划`、`01-Python基础`、`notes`、`参考` 等。

> 命令行等价操作：在 VS Code 里按 `` Ctrl+` `` 打开终端，然后
> ```bash
> code D:\code\python-learning
> ```

---

## 二、第二步：装 Python 扩展（只做一次）

左侧点击**方块图标**（扩展），搜索并安装这三个：

| 扩展 | 作者 | 作用 |
|---|---|---|
| **Python** | Microsoft | 运行、调试、语法高亮 |
| **Pylance** | Microsoft | 智能提示、类型检查 |
| **Jupyter** | Microsoft | 跑 `.ipynb` 笔记（D031 之后要用） |

装完 **重启 VS Code**。

---

## 三、第三步：选择 Python 解释器（最容易卡住的一步）

VS Code 不知道用哪个 Python，**不选的话运行会失败**。

### 操作

1. 按 **`Ctrl+Shift+P`** 打开命令面板
2. 输入 `Python: Select Interpreter`，回车
3. 选这个：

```
Python 3.10.11  C:\Users\lenovo\AppData\Local\Programs\Python\Python310\python.exe
```

> 以后你建了 conda 的 `rl` 环境，这里会多出一个 `Python 3.10.11 ('rl')`，
> **那时候改选带 `('rl')` 的那个**。

**怎么确认选对了**：VS Code 右下角状态栏会显示 `Python 3.10.11`。

---

## 四、第四步：运行代码

打开 `01-Python基础\week1\D001_hello.py`，三种运行方式：

| 方式 | 操作 | 说明 |
|---|---|---|
| **最快** | 右上角 **▶ 三角按钮** | 直接运行当前文件 |
| 快捷键 | `Ctrl+F5` | 不调试直接运行 |
| 终端 | `` Ctrl+` `` 开终端，敲 `python "01-Python基础/week1/D001_hello.py"` | 最接近真实环境 |

输出会出现在下方的「终端」面板。

---

## 五、⚠️ 中文乱码问题（已修好，但你必须重启）

**好消息**：我已经帮你设好了永久环境变量：

```
PYTHONUTF8 = 1
```

**但环境变量只对"新开的进程"生效。** 所以：

| 必须做 | 原因 |
|---|---|
| ✅ **完全关闭 VS Code，重新打开** | VS Code 的集成终端要重启才会继承新变量 |
| ✅ **关掉所有旧的 PowerShell / CMD 窗口** | 旧窗口里变量还是空的 |
| ⚠️ 不用重启电脑 | 但重启了也不会有坏处 |

**验证方法**：新开终端，敲这行 ——

```bash
echo $env:PYTHONUTF8
```

输出 `1` 就对了（输出空白说明终端还是旧的，关掉重开）。

**效果对比**（我实测过）：

```
设置前： ���Ǵ󹤵ģ�104 �����Ҫ��д PPO     ← 乱码
设置后： 我是大工的，104 天后我要手写 PPO    ← 正常
```

> 为什么会乱码：Windows 中文系统的默认编码是 GBK，而 Python 默认按 UTF-8 输出中文，两边对不上。
> `PYTHONUTF8=1` 让 Python 的输出编码跟随系统终端，问题消失。

---

## 六、每天的工作流（VS Code 版）

```bash
# 1. 打开 VS Code，确认右下角显示 Python 3.10.11（或 rl 环境）

# 2. 打开终端（Ctrl+`），提交前先看看改了什么
git status

# 3. 写今天的代码
#    文件放对应文件夹，名字带 Day 编号，例：01-Python基础/week1/D002_变量.py

# 4. 运行验证（▶ 按钮 或 Ctrl+F5）

# 5. 记笔记：打开 notes/learning-log.ipynb（D031 之前可以先跳过）

# 6. 提交
git add .
git commit -m "D001: 环境搭建 + 第一行 Python 代码"
```

---

## 七、常用快捷键（收藏这一段）

| 快捷键 | 作用 |
|---|---|
| `Ctrl+Shift+P` | 命令面板（万能入口，忘了什么都按它） |
| `` Ctrl+` `` | 打开/关闭终端 |
| `Ctrl+F5` | 运行当前 Python 文件 |
| `Ctrl+S` | 保存（**改完必须保存才会执行新代码**） |
| `Ctrl+/` | 注释/取消注释当前行 |
| `Alt+↑ / Alt+↓` | 上下移动当前行 |
| `Shift+Alt+↓` | 向下复制当前行 |
| `Ctrl+F` | 文件内搜索 |
| `Ctrl+Shift+F` | 全仓库搜索（找"我什么时候学过这个"特别好用） |

> ⚠️ 最常见的低级错误：**改完代码没保存就运行**，然后纳闷"怎么没生效"。养成 `Ctrl+S` 的肌肉记忆。

---

## 八、出问题了查这里

| 症状 | 原因 | 解决 |
|---|---|---|
| 运行按钮点了没反应 / 报 `python: command not found` | 没选解释器 | `Ctrl+Shift+P` → `Python: Select Interpreter` |
| 中文乱码 | 终端是旧的 | **完全关闭 VS Code 重开** |
| `ModuleNotFoundError: No module named 'xxx'` | 包装在了另一个 Python 里 | 先 `conda activate rl`，再看右下角解释器是不是 `('rl')` |
| 改完代码没生效 | 没保存 | `Ctrl+S` |
| 文件明明存在却报找不到 | 你打开的是单个文件，不是文件夹 | 文件 → 打开文件夹 → `D:\code\python-learning` |
| 终端里 `git` 不认中文文件名 | 已帮你设过 `core.quotepath=false` | 如果还乱，敲 `git config --global core.quotepath false` |

---

## 九、学生授权批下来之后（1–2 周）

1. 去 https://www.jetbrains.com/zh-cn/pycharm/download/ 下载最新版 PyCharm
2. 安装后用**你的 JetBrains 账号**（申请时注册的那个）登录
3. 授权会自动生效，Pro 功能全部解锁

**但你不一定需要换回去。** VS Code 在这几件事上比 PyCharm 更顺：

- 写 Jupyter 笔记（D031 开始天天用）
- 连远程服务器跑训练（后面租云 GPU 时）
- 轻量、启动快、插件生态大

**建议**：两个都装着，**主线用 VS Code**，等尚硅谷课程讲到需要 PyCharm 特有功能时再开它对照。

---

**现在做三件事**：
1. **完全关闭 VS Code**（不是最小化，是退出）
2. 重新打开，**打开文件夹** `D:\code\python-learning`
3. 装 Python 扩展 → 选解释器 → 运行 `D001_hello.py`，看到中文正常就成功
