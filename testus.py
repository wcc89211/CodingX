import plotly.graph_objects as go  #import plotly套件
import pandas as pd  #import pandas套件

df = pd.read_csv('final.csv')      # final.txt 需手動轉檔 final.csv

df['text'] = df['state'] + '<br>Number of Articles：' + (df['num']).astype(str)  #存地區資料到list
limits = [(0, len(df))]  #計算地區名稱數量

fig = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    df_sub = df[lim[0]:lim[1]]
    fig.add_trace(go.Scattergeo(
        text = df_sub['text'],
        lon = df_sub['lon'],  #longtitude
        lat = df_sub['lat'],  #latitude
        marker = dict(
            size = df_sub['num'],
            color = '#d62728',  #標籤顏色
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode = 'area'
        ),
    ))

fig.update_layout(
        title_text = 'PTT(studyabroad) Popular Discussion Analysis',
        #showlegend = True,  #顯示圖例
        geo = dict(
            landcolor = 'rgb(217, 217, 217)',
        )
    )

fig.show()