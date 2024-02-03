import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# 페이지 1의 내용
def upgrading_level_by_target_done():
    df = pd.DataFrame([['Venus','목표WC 달성 ~6회',0.1,1,2445,92],
              ['Venus','목표WC 달성 7회~',0.7,32,23672,368],
              ['Earth','목표WC 달성 ~6회',0.1,9,2053,-59],
              ['Earth','목표WC 달성 7회~',1.0,13,35533,890]],
               columns = ['행정','구분','AR','BC','W권','WC/권'])
    df.columns = [x.strip() for x in df.columns]
    df['AR'] = df['AR'].apply(lambda x : round(x,1))
    df['BC'] = df['BC'].apply(lambda x : round(x))
    df['WC'] = df['WC'].apply(lambda x : round(x))
    df['WC/권'] = df['WC/권'].apply(lambda x : round(x))
    df.rename(columns = {'WC/권':'WC/BC'}, inplace = True)

    st.subheader('목표WC 달성에 따른 성장치 분석')
    st.write("학습 데이터 : 17기 (2023년 1월 ~ 2023년 12월")
    
    # Streamlit select box for grade selection
    selected_grade = st.selectbox('Select a Grade', df['행성'].unique())

    # Filter the DataFrame based on the selected grades
    filtered_df = df[df['행성'] == selected_grade].reset_index(drop = True)

    # Create a figure with subplots
    fig, axs = plt.subplots(1, 4, figsize=(20, 5))

    # Adjust the space between plots
    plt.subplots_adjust(wspace=0.5)

    # 폰트 패밀리 설정
    plt.rcParams['font.family'] = 'NanumBarunGothic'

    for i in range(len(filtered_df.columns)-2):
        # Positions of the bars on the x-axis
        for j in range(len(filtered_df)):
            # Plotting each subplot
            bars = axs[i].bar(0.3*j, filtered_df.loc[j,filtered_df.columns[i+2]], width=0.3, label=filtered_df.loc[j,'구분'])
            for bar in bars:
                axs[i].text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height()}',ha='center', va='bottom')
        
        axs[i].set_title(filtered_df.columns[i+2])
        
        # Adding legend to each subplot
        axs[i].legend(loc='upper left')

    # Display the plots in Streamlit
    st.pyplot(fig)

    df_table = filtered_df.copy()
    df_table['AR'] = df_table['AR'].apply(lambda x : str(x))
    df_table['BC'] = df_table['BC'].apply(lambda x : str(x)+'권')
    df_table['WC'] = df_table['WC'].apply(lambda x : str(x)+'words')
    df_table['WC/BC'] = df_table['WC/BC'].apply(lambda x : str(x)+'words')
    st.dataframe(df_table,width = 2000)



# 페이지 2의 내용
def page_2_content(seven_days_ago_str_title, current_date_str_title):
    pass

def page_3_content(seven_days_ago_str_title, current_date_str_title):
    pass




with st.sidebar:
    menu_list = ["목표WC 달성 여부에 따른 성장치 분석"]
    page = st.sidebar.radio("Menu", menu_list, index=0)

# 선택된 페이지에 따라 해당하는 함수 호출
if page == menu_list[0]:
    upgrading_level_by_target_done()











































# st.set_page_config(layout="wide")
# # Sidebar에 페이지 선택 메뉴 추가
# with st.sidebar:
#     choice = st.selectbox("Menu", ["표", "그래프"], index=0)

# # 페이지 1의 내용
# if choice == "표":
#     purple_img = Image.open('C:/Users/전략사업부/Desktop/Wep_page/logo_purple.png')
#     st.image(purple_img)

#     st.subheader('르네상스 Top 10 도서 목록🌸')
#     st.write("집계 기간: {} ~ {}".format(seven_days_ago_str_title, current_date_str_title))
#     st.dataframe(top_10_book, width=30000, height=400)

#     st.subheader('릿프로 Top 10 도서 목록🌸')
#     st.write("집계 기간: {} ~ {}".format(seven_days_ago_str_title, current_date_str_title))
#     st.dataframe(top_10_book_LIT, width=30000, height=400)

#     st.subheader('르네상스 Top 10 다독왕 학생 목록🌸')
#     st.write("집계 기간: {} ~ {}".format(seven_days_ago_str_title, current_date_str_title))
#     st.dataframe(top_10_student_merge, width=30000, height=400)

#     st.subheader('릿프로 Top 10 다독왕 학생 목록🌸')
#     st.write("집계 기간: {} ~ {}".format(seven_days_ago_str_title, current_date_str_title))
#     st.dataframe(top_10_student_merge_lit, width=30000, height=400)



# # 페이지 2의 내용
# elif choice == "그래프":
#     # 홈페이지 관련 코드
#     purple_img = Image.open('C:/Users/전략사업부/Desktop/Wep_page/logo_purple.png')
#     st.image(purple_img, use_column_width=True)

#     # 첫 번째 그래프 (Top 10 도서)
#     st.subheader('AR Top 10 도서🌸')
#     st.write("집계 기간: {} ~ {}".format(seven_days_ago_str_title, current_date_str_title))
#     fig1 = px.bar(top_10_book, x='Title', y='count', color='count')
#     fig1.update_layout(xaxis_title='도서 이름', yaxis_title='도서 수', title='Top 10 도서')
#     fig1.update_layout(hovermode='x')
#     st.plotly_chart(fig1)
    
#     # 첫 번째 그래프 (Top 10 도서)
#     st.subheader('LITPRO Top 10 도서🌸')
#     st.write("집계 기간: {} ~ {}".format(seven_days_ago_str_title, current_date_str_title))
#     fig2 = px.bar(top_10_book_LIT, x='Title', y='count', color='count')
#     fig2.update_layout(xaxis_title='도서 이름', yaxis_title='도서 수', title='Top 10 도서')
#     fig2.update_layout(hovermode='x')
#     st.plotly_chart(fig2)


#     # 3번째 그래프 (Top 10 다독왕 학생)
#     st.subheader('르네상스 Top 10 다독왕 학생 목록🌸')
#     st.write("집계 기간: {} ~ {}".format(seven_days_ago_str_title, current_date_str_title))
#     fig3 = px.bar(top_10_student_merge, x='학생명', y='독서량', color='독서량')
#     fig3.update_layout(xaxis_title='학생명', yaxis_title='읽은 횟수', title='Top 10 다독왕 학생')
#     fig3.update_layout(hovermode='x')
#     st.plotly_chart(fig3)

#     st.subheader('릿프로 Top 10 다독왕 학생 목록🌸')
#     st.write("집계 기간: {} ~ {}".format(seven_days_ago_str_title, current_date_str_title))
#     fig4 = px.bar(top_10_student_merge_lit, x='학생명', y='독서량', color='독서량')
#     fig4.update_layout(xaxis_title='학생명', yaxis_title='읽은 횟수', title='Top 10 다독왕 학생')
#     fig4.update_layout(hovermode='x')
#     st.plotly_chart(fig4)











# purple_img = Image.open('C:/Users/전략사업부/Desktop/Wep_page/logo_purple.png')
# st.image(purple_img)

# st.subheader('르네상스 Top 10 도서 목록🌸')
# st.write("집계 기간: {} ~ {}".format(seven_days_ago_str_title, current_date_str_title))
# st.dataframe(top_10_book, width=30000, height=400)

# st.subheader('릿프로 Top 10 도서 목록🌸')
# st.write("집계 기간: {} ~ {}".format(seven_days_ago_str_title, current_date_str_title))
# st.dataframe(top_10_book_LIT, width=30000, height=400)

# st.subheader('르네상스 Top 10 다독왕 학생 목록🌸')
# st.write("집계 기간: {} ~ {}".format(seven_days_ago_str_title, current_date_str_title))
# st.dataframe(top_10_student_merge,width=30000, height=400)

# st.subheader('릿프로 Top 10 다독왕 학생 목록🌸')
# st.write("집계 기간: {} ~ {}".format(seven_days_ago_str_title, current_date_str_title))
# st.dataframe(top_10_student_merge_lit,width=30000, height=400)






#     # 탭 생성
# tab1, tab2 = st.tabs(["tab1", "tab2"])
#     # 텝 A 내용 (여기에는 예시로 텍스트만 넣었습니다)
# with tab1:
#     purple_img = Image.open('C:/Users/전략사업부/Desktop/Wep_page/logo_purple.png')
#     st.image(purple_img, use_column_width=True)
#     st.subheader('Top 10 도서 목록🌸')
#     st.write("집계 기간: {} ~ {}".format(seven_days_ago_str_title, current_date_str_title))
#     st.dataframe(top_10_book, width=30000, height=400)
#     # st.table(top_10_book)
#     st.subheader('Top 10 다독왕 학생 목록🌸')
#     st.write("집계 기간: {} ~ {}".format(seven_days_ago_str_title, current_date_str_title))
#     st.table(top_10_student_merge)


#     # 텝 B 내용
# with tab2:
#     # 홈페이지 관련 코드
#     purple_img = Image.open('C:/Users/전략사업부/Desktop/Wep_page/logo_purple.png')
#     st.image(purple_img, use_column_width=True)

#     # 첫 번째 그래프 (Top 10 도서)
#     st.subheader('Top 10 도서🌸')
#     st.write("집계 기간: {} ~ {}".format(seven_days_ago_str_title, current_date_str_title))
#     fig1 = px.bar(top_10_book, x='Title', y='count', color='count')
#     fig1.update_layout(xaxis_title='도서 이름', yaxis_title='도서 수', title='Top 10 도서')
#     fig1.update_layout(hovermode='x')
#     st.plotly_chart(fig1)

#     # 두 번째 그래프 (Top 10 다독왕 학생)
#     st.subheader('Top 10 다독왕 학생🌸')
#     st.write("집계 기간: {} ~ {}".format(seven_days_ago_str_title, current_date_str_title))
#     fig2 = px.bar(top_10_student_merge, x='학생명', y='독서량', color='독서량')
#     fig2.update_layout(xaxis_title='학생명', yaxis_title='읽은 횟수', title='Top 10 다독왕 학생')
#     fig2.update_layout(hovermode='x')
#     st.plotly_chart(fig2)






































# # 로그인 폼 생성
# st.title("로그인")

# # 사용자 이름과 비밀번호 입력 필드 추가
# username = st.text_input("사용자 이름")
# password = st.text_input("비밀번호", type="password")
# logged_in = False

# # 로그인 버튼을 클릭하면 실행되는 코드
# if st.button("로그인"):
#     # 간단한 예시: 사용자 이름이 "admin"이고 비밀번호가 "password"인 경우에만 로그인 성공
#     if username == "admin" and password == "password":
#         st.success("로그인 성공!")
#         logged_in = True
#         # 여기에 로그인 후 작업을 추가할 수 있습니다.
#     else:
#         st.error("로그인 실패. 사용자 이름 또는 비밀번호를 확인하세요.")
#         logged_in = False

# if logged_in:
#     # 탭 생성
#     tab1, tab2 = st.tabs(["tab1", "tab2"])
#     # 텝 A 내용 (여기에는 예시로 텍스트만 넣었습니다)
#     with tab1:
#         purple_img = Image.open('C:/Users/전략사업부/Desktop/Wep_page/logo_purple.png')
#         st.image(purple_img, use_column_width=True)
#         st.subheader('Top 10 도서 목록🌸')
#         # 스크롤 가능한 표 생성
#         table_html = top_10_book.to_html(escape=False)
#         st.write(table_html, unsafe_allow_html=True)
#         # st.table(top_10_book)
#         st.subheader('Top 10 다독왕 학생 목록🌸')
#         st.table(top_10_student_merge)


#     # 텝 B 내용
#     with tab2:
#         # 홈페이지 관련 코드
#         purple_img = Image.open('C:/Users/전략사업부/Desktop/Wep_page/logo_purple.png')
#         st.image(purple_img, use_column_width=True)

#         # 첫 번째 그래프 (Top 10 도서)
#         st.subheader('Top 10 도서🌸')
#         fig1 = px.bar(top_10_book, x='Title', y='count', color='count')
#         fig1.update_layout(xaxis_title='도서 이름', yaxis_title='도서 수', title='Top 10 도서')
#         fig1.update_layout(hovermode='x')
#         st.plotly_chart(fig1)

#         # 두 번째 그래프 (Top 10 다독왕 학생)
#         st.subheader('Top 10 다독왕 학생🌸')
#         fig2 = px.bar(top_10_student_merge, x='학생명', y='독서량', color='독서량')
#         fig2.update_layout(xaxis_title='학생명', yaxis_title='읽은 횟수', title='Top 10 다독왕 학생')
#         fig2.update_layout(hovermode='x')
#         st.plotly_chart(fig2)


























