# CapitalPulse

A 股行业板块、个股资金流向看板。项目采集行业板块及个股资金流数据，实时展示主力、超大单、大单、中单和小单的资金流向。

## 界面预览

![CapitalPulse 功能界面总览](frontend/overview.png)

## 功能特性

- 行业板块实时主力资金流监控
- 行业及个股细分资金流向监控
- 实时与历史数据可视化
- SQLite 本地数据持久化

## 项目结构

```text
CapitalPulse/
├── backend/
│   ├── routers/                    # REST API 路由
│   ├── services/                   # 行情采集、历史回填与持久化
│   ├── tests/                      # 后端单元测试
│   ├── utils/                      # 行业筛选等工具
│   ├── .env.example                # 后端环境变量模板
│   ├── config.py                   # 环境变量与上游接口配置
│   ├── main.py                     # FastAPI 入口
│   └── requirements.txt            # Python 依赖
├── frontend/
│   ├── public/                     # 静态资源
│   ├── src/app/                    # Next.js 页面与样式
│   └── .env.example                # 前端环境变量模板
├── bun.lock                        # Bun 依赖锁定文件
├── LICENSE
└── package.json                    # 项目命令与前端工作区配置
```

运行时数据库默认保存在 `backend/data/sector_flow_realtime.sqlite3`，部署时请注意持久化和备份。

## 环境要求

| 软件 | 要求 | 说明 |
| --- | --- | --- |
| Anaconda 或 Miniconda | 较新的稳定版本 | 推荐体积更小的 Miniconda |
| Python | 3.11 | 通过独立 Conda 环境安装 |
| Node.js | 24 LTS 推荐，最低 20.9 | Next.js 16 最低要求 20.9；不要新装已结束支持的 Node.js 20 |
| Bun | 1.2 或更高版本 | 安装前端依赖和执行项目命令 |

目前项目仅在 Windows 上完成实际测试，已安装的软件可以跳过，但请先执行版本检查。

## Windows 部署

以下命令使用 PowerShell。安装 Conda 后，也可以在 Anaconda Prompt 中执行项目命令。

### 1. 安装 Miniconda 或 Anaconda

1. 打开 [Anaconda 下载页面](https://www.anaconda.com/download)。
2. 下载 Windows x86-64 的 Miniconda 安装程序；需要 Navigator 图形界面时可改装完整 Anaconda Distribution。
3. 运行安装程序，选择 `Just Me`，其他选项保持默认。
4. 安装完成后打开 Anaconda Prompt。

验证 Conda：

```powershell
conda --version
```

### 2. 安装 Node.js

1. 打开 [Node.js 下载页面](https://nodejs.org/en/download)。
2. 选择最新的 **LTS** 版本，下载 Windows Installer（`.msi`）。
3. 使用默认选项完成安装，然后重新打开终端。

验证 Node.js：

```powershell
node --version
npm --version
```

### 3. 安装 Bun

在 PowerShell 中执行 Bun 官方安装命令：

```powershell
powershell -c "irm bun.sh/install.ps1 | iex"
```

关闭并重新打开 PowerShell，然后验证：

```powershell
bun --version
```

### 4. 创建 Python 环境

```powershell
conda create -n capitalpulse python=3.11 -y
conda activate capitalpulse
python -m pip install --upgrade pip
python -m pip install -r backend\requirements.txt
```

### 5. 配置环境变量并安装前端依赖

```powershell
Copy-Item backend\.env.example backend\.env
Copy-Item frontend\.env.example frontend\.env.local
bun install --frozen-lockfile
```

按需编辑 `backend\.env` 和 `frontend\.env.local`。后端会自动读取 `backend\.env`

#### 后端：`backend/.env`

```dotenv
HOST=0.0.0.0
PORT=8100

SECTOR_FLOW_ENABLED=true
SECTOR_FLOW_POLL_SECONDS=3
STOCK_FLOW_POLL_SECONDS=3
SECTOR_FLOW_DB_PATH=data/sector_flow_realtime.sqlite3
SECTOR_FLOW_RETENTION_DAYS=30
```

#### 前端：`frontend/.env.local`

```dotenv
VANE_API_URL=http://localhost:8100
# NEXT_PUBLIC_SECTOR_FLOW_WS_URL=ws://localhost:8100/ws/sector-flow
```

### 6. 启动开发环境

打开两个 PowerShell 或 Anaconda Prompt 窗口，两个窗口都进入项目根目录。

终端一启动后端：

```powershell
conda activate capitalpulse
bun run dev:api
```

终端二启动前端：

```powershell
conda activate capitalpulse
bun run dev:web
```

## 风险提示

本项目仅用于技术研究和数据展示，不保证数据的准确性、完整性与实时性，不构成任何投资建议。因使用本项目产生的交易、投资或其他损失，由使用者自行承担。

## License

本项目采用 [MIT License](LICENSE) 开源。

## 作者

- 小红书：[阿溪研究点啥](https://www.xiaohongshu.com/user/profile/62af3f61000000001902be20)

分享财经信息、实用工具和AI前沿，欢迎交流~
