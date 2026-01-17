import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib

# Load preprocessed dataset
df = pd.read_csv("train_preprocessed.csv")

X = df["user_message"]
y = df["bot_response"]

# Train-test split (same logic as before)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# TF-IDF (v3 – SAME PARAMETERS)
tfidf = TfidfVectorizer(
    max_features=8000,
    ngram_range=(1, 3),
    min_df=2,
    stop_words=None
)

X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

print("✔ Improved TF-IDF trained locally")

# (Optional) Evaluate Top-K again (for confirmation)
def chatbot_top_k(user_input, k=3):
    user_vector = tfidf.transform([user_input])
    similarities = cosine_similarity(user_vector, X_train_tfidf)[0]
    top_k_indices = similarities.argsort()[-k:][::-1]
    return y_train.iloc[top_k_indices].tolist()

# Save FINAL v3 model (LOCAL, COMPATIBLE)
joblib.dump(tfidf, "tfidf_vectorizer_v3.pkl")
joblib.dump(X_train_tfidf, "train_vectors_v3.pkl")
joblib.dump(y_train.tolist(), "train_responses_v3.pkl")

print("✅ v3 model retrained & saved locally (Python 3.13 compatible)")
