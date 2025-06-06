import streamlit as st
import google.generativeai as genai

# Streamlitの秘密管理機能からAPIキーを読み込む
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
    st.error("APIキーが設定されていません。アプリの管理者に連絡してください。")
    # st.error(e) # デバッグ用にエラーメッセージを表示したい場合
    st.stop() # APIキーがない場合はここで処理を停止

st.title("AI献立提案アプリ 🍳")

# ユーザーが食材を入力するテキストボックス
ingredients = st.text_area("冷蔵庫にある食材をカンマ区切りで入力してください (例: 豚肉, 玉ねぎ, 卵)")

# 提案ボタン
if st.button("献立を提案してもらう"):
    if ingredients:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"冷蔵庫にある食材：{ingredients}。これらの食材を使って作れる料理のレシピを3つ、以下の形式で提案してください。\n\n**【料理名】**\n- 材料リスト\n- 簡単な作り方"
        
        with st.spinner("AIが考えています..."):
            response = model.generate_content(prompt)
            st.write(response.text)
    else:
        st.warning("食材を入力してください。")