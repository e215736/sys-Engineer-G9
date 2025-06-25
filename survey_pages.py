import streamlit as st
import pandas as pd
from graph_utils import create_q1_chart, create_q2_chart, create_q3_chart

def show_survey_page():
    """アンケートフォームページ"""
    st.title("🌧️ 気象予測に関するアンケート調査")
    
    st.markdown("""
    ### 研究テーマ
    研究の社会的価値は、**既存の設備を活用し局地的な気象予測を低コストで行うことができ、フレキシブルな防災が可能になる**と考えています。
    
    この社会的価値が適切か否かを客観的に把握するために、以下のアンケートにご協力ください。
    """)
    
    st.divider()
    
    # 質問1
    st.subheader("質問1")
    st.markdown("**急に雨に降られて困ったことはありますか？**")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("はい", key="q1_yes", use_container_width=True):
            st.session_state.answers['q1'] = "はい"
    with col2:
        if st.button("いいえ", key="q1_no", use_container_width=True):
            st.session_state.answers['q1'] = "いいえ"
    
    if 'q1' in st.session_state.answers:
        st.success(f"回答済み: {st.session_state.answers['q1']}")
    
    st.divider()
    
    # 質問2
    st.subheader("質問2")
    st.markdown("**空の写真を撮ると雨が降るか判別するアプリがあれば活用したいですか？**")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("ぜひ使いたい", key="q2_definitely", use_container_width=True):
            st.session_state.answers['q2'] = "ぜひ使いたい"
    with col2:
        if st.button("使ってみたい", key="q2_try", use_container_width=True):
            st.session_state.answers['q2'] = "使ってみたい"
    with col3:
        if st.button("ものによる", key="q2_depends", use_container_width=True):
            st.session_state.answers['q2'] = "ものによる"
    with col4:
        if st.button("使わない", key="q2_no", use_container_width=True):
            st.session_state.answers['q2'] = "使わない"
    
    if 'q2' in st.session_state.answers:
        st.success(f"回答済み: {st.session_state.answers['q2']}")
    
    st.divider()
    
    # 質問3
    st.subheader("質問3")
    st.markdown("**急に雨に降られると困るのはいつどんな時ですか？**")
    st.markdown("*（20文字程度でお答えください）*")
    
    q3_answer = st.text_input("", key="q3_input", max_chars=30, placeholder="例：外出時、平日の朝、洗濯物を干している時など")
    
    if q3_answer:
        st.session_state.answers['q3'] = q3_answer
        st.success(f"回答済み: {q3_answer}")
    
    st.divider()
    
    # 回答完了チェック
    if len(st.session_state.answers) == 3:
        st.success("全ての質問に回答いただきありがとうございます！")
        if st.button("📊 結果を見る", use_container_width=True, type="primary"):
            st.session_state.page = 'results'
            st.rerun()
    else:
        remaining = 3 - len(st.session_state.answers)
        st.info(f"残り {remaining} 問の回答をお願いします。")

def show_results_page():
    """アンケート結果表示ページ"""
    st.title("📊 アンケート結果")
    
    # 戻るボタン
    if st.button("← アンケートに戻る"):
        st.session_state.page = 'survey'
        st.rerun()
    
    st.divider()
    
    # 仮データの作成
    fake_data = get_fake_data()
    
    # 回答者数表示
    st.metric("総回答者数", "100名（仮データ）")
    
    # 質問1の結果
    display_q1_results(fake_data)
    
    st.divider()
    
    # 質問2の結果
    display_q2_results(fake_data)
    
    st.divider()
    
    # 質問3の結果
    display_q3_results(fake_data)
    
    st.divider()
    
    # 分析結果
    display_analysis_results()

def get_fake_data():
    """仮データを生成"""
    return {
        'q1': ['はい'] * 75 + ['いいえ'] * 25,
        'q2': ['ぜひ使いたい'] * 30 + ['使ってみたい'] * 40 + ['ものによる'] * 25 + ['使わない'] * 5,
        'q3': [
            '外出時', '平日の朝', '洗濯物を干している時', '通勤時', '散歩中',
            '買い物中', '子供の送迎時', '運動中', 'デート中', '旅行中',
            '仕事中', '屋外イベント時', 'バーベキュー時', '釣り中', 'ゴルフ中'
        ] * 7 + ['その他'] * 5
    }

def display_q1_results(fake_data):
    """質問1の結果を表示"""
    st.subheader("質問1: 急に雨に降られて困ったことはありますか？")
    q1_df = pd.DataFrame({'回答': fake_data['q1']})
    q1_counts = q1_df['回答'].value_counts()
    
    col1, col2 = st.columns(2)
    with col1:
        fig1 = create_q1_chart(q1_counts)
        st.pyplot(fig1, use_container_width=True)
    
    with col2:
        st.write("**回答数**")
        for answer, count in q1_counts.items():
            percentage = (count / len(fake_data['q1'])) * 100
            st.write(f"- {answer}: {count}名 ({percentage:.1f}%)")

def display_q2_results(fake_data):
    """質問2の結果を表示"""
    st.subheader("質問2: 空の写真を撮ると雨が降るか判別するアプリがあれば活用したいですか？")
    q2_df = pd.DataFrame({'回答': fake_data['q2']})
    q2_counts = q2_df['回答'].value_counts()
    
    col1, col2 = st.columns(2)
    with col1:
        fig2 = create_q2_chart(q2_counts)
        st.pyplot(fig2, use_container_width=True)
    
    with col2:
        st.write("**回答数**")
        for answer, count in q2_counts.items():
            percentage = (count / len(fake_data['q2'])) * 100
            st.write(f"- {answer}: {count}名 ({percentage:.1f}%)")

def display_q3_results(fake_data):
    """質問3の結果を表示"""
    st.subheader("質問3: 急に雨に降られると困るのはいつどんな時ですか？")
    q3_df = pd.DataFrame({'回答': fake_data['q3']})
    q3_counts = q3_df['回答'].value_counts().head(10)  # 上位10位まで表示
    
    col1, col2 = st.columns(2)
    with col1:
        fig3 = create_q3_chart(q3_counts)
        st.pyplot(fig3, use_container_width=True)
    
    with col2:
        st.write("**主な回答**")
        for i, (answer, count) in enumerate(q3_counts.items(), 1):
            percentage = (count / len(fake_data['q3'])) * 100
            st.write(f"{i}. {answer}: {count}名 ({percentage:.1f}%)")

def display_analysis_results():
    """分析結果を表示"""
    st.subheader("📈 分析結果")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("雨で困った経験がある人", "75%", "高い関心度")
    with col2:
        st.metric("アプリを使いたい人", "70%", "前向きな反応")
    with col3:
        st.metric("最も多い困るシーン", "外出時", "7名が回答")
    
    st.markdown("""
    ### 📝 考察
    - **75%** の人が急に雨に降られて困った経験があり、ニーズの高さが確認できました
    - **70%** の人がアプリの活用に前向きで、社会的価値への関心が高いことが分かります
    - 困るシーンとして「外出時」「平日の朝」「洗濯物を干している時」が上位にあり、日常生活での実用性が期待されています
    
    **結論**: 研究の社会的価値は適切であり、多くの人にとって有用なソリューションになる可能性が高いと考えられます。
    """)