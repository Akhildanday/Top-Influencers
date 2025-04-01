# 📊 Top Influencers - Engagement Rate Predictor  

This project predicts the **Instagram Engagement Rate** of influencers using Machine Learning and a **Streamlit Web App**.  
It is based on a dataset of **top Instagram influencers** with features like **followers, likes, posts, and influence score**.

---

## 🚀 **Live Demo**
🔗 **Try the App**: [Streamlit Live App](https://akhildanday-top-influencers-app-6gbyt9.streamlit.app/)  

---

## 📂 **Project Structure**
```
Top-Influencers/
│-- engagement_model.pkl   # Trained Machine Learning model  
│-- app.py                 # Streamlit web app for predictions  
│-- requirements.txt        # List of dependencies  
│-- README.md               # Project documentation  
│-- dataset/                # (If dataset is included)
```

---

## ⚙️ **Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Akhildanday/Top-Influencers.git
cd Top-Influencers
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Streamlit App**
```bash
streamlit run app.py
```
This will launch the web app in your browser. 🚀  

---

## 📀 **Dataset Description**
The dataset consists of **200 Instagram influencers** with the following key features:
- **Followers**: Total number of followers.
- **Avg Likes**: Average likes per post.
- **New Post Avg Likes**: Average likes on recent posts.
- **Total Likes**: Cumulative likes on all posts.
- **Posts**: Total number of posts.
- **Influence Score**: A score from 0 to 100 indicating influence power.
- **Country**: Encoded categorical feature representing the influencer's country.

---

## 💪 **How to Use the Web App**
1. **Enter influencer details** (followers, likes, posts, etc.).  
2. **Select country** from the dropdown.  
3. **Click "Predict Engagement Rate"** to get results.  

---

## 🔬 **Machine Learning Model**
- **Model Used:** `RandomForestRegressor`  
- **Accuracy (R² Score):** `~75.5%`  
- **Features Used:** `Followers, Likes, Total Likes, Posts, Influence Score, Country`  
- **Target Variable:** `Engagement Rate`  

---

## 📃 **Deployment on Streamlit Cloud**
This app is deployed on **Streamlit Cloud**. To deploy your own version:

1. Push your project to GitHub.
2. Go to **[Streamlit Cloud](https://share.streamlit.io/)**.
3. Click **"New App"**.
4. Select your repository and enter `app.py` as the file name.
5. Click **Deploy** 🚀.

---

## 📜 **License**
This project is open-source under the **MIT License**.

---

## ✨ **Contributing**
- Feel free to **fork the repository** and submit pull requests!  
- If you find any **bugs or have feature requests**, create an **issue**.

---

## 📩 **Contact**
🔗 **GitHub**: [Akhildanday](https://github.com/Akhildanday)  

