import streamlit as st
import pandas as pd
import openpyxl
# import

st.title('Test App')
st.caption('これはテストアプリです。')
st.subheader('subheader')
st.text('テキストです。')

# #テキストボックス
# name = st.text_input('名前')
# address = st.text_input('住所')

# #ボタン
# submit_btn = st.button('送信')
# cancel_btn = st.button('キャンセル')
#
# if submit_btn:
#     st.text(f'{address}にお住いの{name}さん、ようこそ！')

# #画像
# image = Image.open('xxx.png')
# st.image(image, width=200)

# #ラジオボタン
# age = st.radio(
#     '年齢層',
#     ('子供（18歳未満）', '大人（18歳以上）')
# )

# #セレクトボックス
# center = st.selectbox(
#     'センター',
#     ('梅田', '天王寺', '三宮', '西宮', '明石', '姫路')
# )

# #複数選択
# hobby = st.multiselect(
#     '趣味',
#     ('スポーツ', '読書', '飲食', 'その他')
# )

#データの読み込み
df = pd.read_excel('./hands_data.xlsx')
staff = df['担当者']

# # カラムを追加する
# col1, col2 = st.columns(2)
#
#     with col1:
#
#     with col2:
#


#ラジオボタン
center = st.radio(
    'センター',
    ('梅田', '天王寺', '三宮', '西宮', '明石', '姫路')
)
staff = st.selectbox('職員', staff)

if center:
    df_center = df[df['担当センター']==center]
    st.write(df_center)
else:
    st.write(df)
