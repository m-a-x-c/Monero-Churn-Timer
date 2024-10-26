# Monero Churn Timer

Welcome to **Monero Churn Timer** — a utility designed to generate randomized wait times for Monero (XMR) transactions, helping you schedule transaction "churns" for enhanced privacy.

## 📌 Overview

The Monero Churn Timer leverages data collected from a random sample of **100,000 Monero transactions** (between blocks 2.75 million and 3.25 million) to determine the **age distribution of decoys**. Using this sample, a **lognormal distribution** was fitted to simulate realistic wait times for future churns. While the generated distribution isn’t an exact match, it closely approximates real-world decoy usage patterns.

**Live Demo:** [Monero Churn Timer](https://m-a-x-c.github.io/Monero-Churn-Timer/churn.html)

## 🚀 How It Works

1. **Receive Monero:** After receiving a Monero transaction, open the **Monero Churn Timer**.
2. **Generate Random Wait Time:** The timer provides a random wait time in **days and blocks**.
3. **Set a Reminder:** Use the generated wait time to schedule a "churn" — **re-send the Monero to yourself at a new address**.
4. **Repeat (Optional):** If needed, repeat the process with another random wait time for further obfuscation.

## 📝 Disclaimer

While churning may increase privacy by making it harder to trace transactions, **misusing churns can also have the opposite effect**, making your transactions more identifiable. It is crucial to be aware of several **factors** that may affect the effectiveness of churning:

- **Number of inputs/outputs** used in the transaction  
- **Time of day** and patterns in transaction behavior  
- **Remote nodes** vs. local wallets (network settings)  

Carefully managing these elements is key to avoiding unintended transaction fingerprinting. **Churning isn’t a one-size-fits-all solution**—it requires caution to ensure privacy isn’t inadvertently compromised.

## 🔧 Technical Details

The **Monero Churn Timer** uses a **lognormal distribution** with shape and scale parameters derived from the sampled transaction data. Here's the core logic:

```javascript
function logNormRnd(shape, scale) {
  const normalValue = randomNormal(0, shape); // Mean = 0, StdDev = shape (sigma)
  return Math.exp(normalValue) * scale;
}

const days = logNormRnd(2.135, 1.77).toFixed(3);
const blocks = Math.floor(days * 720);
```

The **Box-Muller Transform** generates normally distributed random values, which are then converted into lognormal values for realistic churn intervals. Each time the page is refreshed, **a new wait time is displayed**.

## 📂 Project Structure

- **`churn.html`** – Core page for generating and displaying the random churn interval.
- **JavaScript Logic** – Responsible for calculating wait times in days and converting them into blocks (Monero has ~720 blocks per day).
- **Styling** – Custom CSS for a simple and intuitive user interface.

## 🛠 Usage Instructions

1. **Access the Churn Timer:** Visit [churn.html](https://m-a-x-c.github.io/Monero-Churn-Timer/churn.html).
2. **Get Random Wait Time:** Wait time is displayed as **days** and **blocks**.
3. **Refresh for New Wait Time:** Simply **refresh the page** to generate a new random time.

## ⚠️ Important Note

This tool is intended to help users explore the concept of **churning** within the Monero network. **Use with caution** and ensure you understand the privacy risks involved. The timer only provides a simulation and should not be considered foolproof.

---

Feel free to contribute to the project or report issues!
