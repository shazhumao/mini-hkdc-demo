# 🪙 Circle Demo Stablecoin (MiniHKDC)

This is a demo project built for Hong Kong–based stablecoin experimentation. It includes a minimal ERC20 contract, backend APIs for minting and querying balances, and a frontend wallet interface.

---

## 📦 Project Structure
```
circle_demo_stablecoin/
├── contracts/
│   └── MiniUSDC.sol            # ERC20 contract (MiniHKDC)
├── deploy/
│   └── deploy.py               # Python deploy script
├── backend/
│   └── main.py                 # FastAPI API for balance & mint
├── front/
│   └── index.html              # Wallet + mint + transfer UI
├── .env                        # Contract, RPC, Wallet config
└── requirements.txt            # Python deps
```

---

## 🚀 How to Run the Project

### 1. Install dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Compile and Deploy MiniUSDC
```bash
python deploy/deploy.py
```
This will output a contract address. Paste it into `.env` and `front/index.html`.

### 3. Start Backend
```bash
uvicorn backend.main:app --reload
```
Backend will be available at `http://localhost:8000`

### 4. Open Frontend
Open `front/index.html` directly in browser. Use MetaMask + Sepolia.

---

## ⚙️ .env Format
```env
PRIVATE_KEY=your_private_key
RPC_URL=https://sepolia.infura.io/v3/...
CHAIN_ID=11155111
CONTRACT_ADDRESS=0x...
```

---

## 🧪 Features
- 🧾 ERC20 contract (`MiniUSDC`) with `mint()` and `transfer()`
- 🔐 Admin-controlled minting (via backend)
- 🌐 MetaMask-connected frontend
- ⚖️ Real-time balance check

---

## 🧱 Tech Stack
- Solidity (ERC20 + Ownable)
- Python (FastAPI, Web3.py)
- HTML + JS (Ethers.js)

---

## 📌 Notes
- Use Sepolia faucet to get ETH: https://sepoliafaucet.com
- Token may appear as `<0.0001` in MetaMask—set correct `decimals()` in contract.
- You can add token manually via MetaMask > Add Token > Paste contract address.

---

## 🛠 Next Steps
- [ ] Add burn functionality
- [ ] Add reserve backing + proof
- [ ] Add KYC gating
- [ ] Audit gas + security

---

Created with ❤️ for Hong Kong digital asset innovation.

---

MIT License
