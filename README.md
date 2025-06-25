# 必要なライブラリをインストール
pip install streamlit pandas matplotlib seaborn numpy

# アプリを実行
streamlit run main_app.py


📂 プロジェクト構成  
project/  
├── main.py              # メインアプリ（エントリーポイント）  
├── graph_utils.py       # グラフ描画機能  
└── survey_pages.py      # アンケートページ機能  

🔧 各ファイルの役割
1. main.py

アプリのエントリーポイント
ページ設定とセッション状態の初期化
ページルーティング（survey ↔ results）

2. graph_utils.py

matplotlib/seabornを使ったグラフ描画機能
円グラフ、棒グラフ、横棒グラフの作成関数
各質問専用のグラフ作成関数

3. survey_pages.py

アンケートフォームページ（質問1-3）
結果表示ページ（グラフ＋分析）
仮データ生成機能
