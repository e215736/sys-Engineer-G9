import streamlit as st
from survey_pages import show_survey_page, show_results_page

def initialize_session_state():
    """セッション状態を初期化"""
    if 'page' not in st.session_state:
        st.session_state.page = 'survey'
    if 'answers' not in st.session_state:
        st.session_state.answers = {}

def configure_page():
    """ページ設定"""
    st.set_page_config(
        page_title="気象予測アンケート調査", 
        layout="wide",
        initial_sidebar_state="collapsed"
    )

def main():
    """メイン処理"""
    # ページ設定
    configure_page()
    
    # セッション状態の初期化
    initialize_session_state()
    
    # ページルーティング
    if st.session_state.page == 'survey':
        show_survey_page()
    elif st.session_state.page == 'results':
        show_results_page()
    else:
        # 未知のページの場合はアンケートページにリダイレクト
        st.session_state.page = 'survey'
        st.rerun()

if __name__ == "__main__":
    main()