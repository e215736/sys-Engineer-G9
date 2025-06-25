import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# matplotlib日本語フォント設定
plt.rcParams['font.family'] = 'DejaVu Sans'
sns.set_style("whitegrid")

def create_pie_chart(data, title="円グラフ"):
    """円グラフを作成
    
    Args:
        data: pandas Series形式のデータ
        title: グラフのタイトル
    
    Returns:
        matplotlib figure object
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    colors = ['#ff6b6b', '#4ecdc4']
    wedges, texts, autotexts = ax.pie(data.values, labels=data.index, 
                                    autopct='%1.1f%%', colors=colors, startangle=90)
    ax.set_title(title, fontsize=14, fontweight='bold')
    plt.tight_layout()
    return fig

def create_bar_chart(data, title="棒グラフ", xlabel="回答", ylabel="回答数"):
    """棒グラフを作成
    
    Args:
        data: pandas Series形式のデータ
        title: グラフのタイトル
        xlabel: x軸のラベル
        ylabel: y軸のラベル
    
    Returns:
        matplotlib figure object
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(data.index, data.values, 
                  color=plt.cm.viridis(np.linspace(0, 1, len(data))))
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    return fig

def create_horizontal_bar_chart(data, title="横棒グラフ", xlabel="回答数", ylabel="シチュエーション"):
    """横棒グラフを作成
    
    Args:
        data: pandas Series形式のデータ
        title: グラフのタイトル
        xlabel: x軸のラベル
        ylabel: y軸のラベル
    
    Returns:
        matplotlib figure object
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # 水平バーチャートを作成
    y_pos = np.arange(len(data))
    colors = plt.cm.plasma(np.linspace(0, 1, len(data)))
    bars = ax.barh(y_pos, data.values, color=colors)
    
    # ラベルと設定
    ax.set_yticks(y_pos)
    ax.set_yticklabels(data.index)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title, fontsize=14, fontweight='bold')
    
    # y軸を反転させて上位から表示
    ax.invert_yaxis()
    
    plt.tight_layout()
    return fig

def create_q1_chart(q1_counts):
    """質問1用の円グラフを作成"""
    return create_pie_chart(q1_counts, "回答分布")

def create_q2_chart(q2_counts):
    """質問2用の棒グラフを作成"""
    return create_bar_chart(q2_counts, "回答分布", "回答", "回答数")

def create_q3_chart(q3_counts):
    """質問3用の横棒グラフを作成"""
    return create_horizontal_bar_chart(q3_counts, "よくある回答 TOP10", "回答数", "シチュエーション")