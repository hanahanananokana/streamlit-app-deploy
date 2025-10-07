import streamlit as st
import pandas as pd
import numpy as np

# ページの設定
st.set_page_config(
    page_title="Streamlit App Deploy",
    page_icon="🚀",
    layout="wide"
)

# メインタイトル
st.title("🚀 Streamlit App Deploy")
st.markdown("---")

# サイドバー
st.sidebar.title("メニュー")
page = st.sidebar.selectbox("ページを選択", ["ホーム", "データ分析", "チャート"])

if page == "ホーム":
    st.header("ホームページ")
    st.write("このStreamlitアプリケーションにようこそ！")
    
    # 基本的な情報表示
    st.subheader("アプリケーション情報")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("バージョン", "1.0.0")
    with col2:
        st.metric("作成日", "2025-10-07")
    with col3:
        st.metric("ステータス", "稼働中", "✅")

elif page == "データ分析":
    st.header("データ分析")
    
    # サンプルデータの生成
    if st.button("サンプルデータを生成"):
        data = pd.DataFrame({
            '日付': pd.date_range('2024-01-01', periods=100),
            '売上': np.random.randint(1000, 10000, 100),
            '訪問者数': np.random.randint(50, 500, 100)
        })
        
        st.subheader("生成されたデータ")
        st.dataframe(data)
        
        st.subheader("統計情報")
        st.write(data.describe())

elif page == "チャート":
    st.header("チャート表示")
    
    # チャートデータの生成
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    
    st.subheader("ラインチャート")
    st.line_chart(chart_data)
    
    st.subheader("エリアチャート")
    st.area_chart(chart_data)
    
    st.subheader("バーチャート")
    st.bar_chart(chart_data)

# フッター
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
