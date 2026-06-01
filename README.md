```markdown
# Security Log Hashing on Ethereum

A lightweight system that hashes local system logs via SHA-256 and stores them on a local Ethereum blockchain to prevent tampering.

---

## Technical Stack
* **Smart Contract:** Solidity `^0.8.0`
* **Backend:** Python 3 (`web3.py`, `hashlib`)
* **Local Network:** Ganache CLI (Port `7545`)
* **IDE:** Remix Online Compiler

---

## Quick Start

### 1. Run the Local Blockchain
```bash
ganache --port 7545



 Deploy the Contract

1. Open [remix.ethereum.org](https://www.google.com/search?q=https://remix.ethereum.org).
2. Create `LogRegistry.sol`, paste the Solidity code, and press **Ctrl + S**.
3. In the **Deploy & Run Transactions** tab, set **ENVIRONMENT** to **Dev - Ganache Provider**.
4. Enter http://loopbackIP and click **Deploy**.

 Run the Backend

1. Copy the deployed contract address from the bottom of the Remix sidebar.
2. Paste the address into the `contract_address` variable inside `script.py`.
3. Execute the script 

```

```

```
