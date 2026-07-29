import streamlit as st
import pandas as pd
import plotly.express as px # dynamic visualization library
from streamlit_option_menu import option_menu
st.cache_data.clear()
st.set_page_config(layout="wide")
st.title("Cric Info Application")

df=pd.read_csv("new_data.csv")

# st.dataframe(df)

select = option_menu(
    menu_title=None,
    options=["Home","Player Analysis","country insights","Comparison","Data Explorer","About"],
    icons=["house","person","globe","bar-chart","table","info-circle"],
    orientation="horizontal"
)



##-------Home-----
if select=="Home":
    st.title("Cricket Analysis Dashboard")


    col1,col2,col3,col4 = st.columns(4)


    
    col1.metric("Total Players", df["player"].nunique())
    
    col2.metric("Total Runs",df['Runs'].sum())

    col3.metric("Countries",df["country"].nunique())

    col4.metric("Total Matches",df["matches"].sum())

    st.dataframe(df.head(10))



elif select=="Player Analysis":
    st.title("Player Analysis Stats")

    player = st.selectbox("select player",df["player"].unique())
    pdata = df[df["player"]==player]        

    df2=pdata[["matches","Inns","high_score","avg","100","50","4s","6s"]]
    df3=df2.T.reset_index()
    st.dataframe(df3)

    fig=px.bar(df3,x="index",y=df3.columns[1],color="index")

    df_pie=pdata[["100","50","6s","4s"]]
    pie1=df_pie.T.reset_index()
    fig_pie=px.pie(pie1,names="index",values=pie1.columns[1])

    col1,col2 = st.columns(2)

    with col1:
        st.plotly_chart(fig,use_container_width=True)
    with col2:
        st.plotly_chart(fig_pie,use_container_width=True)


#======= Country insights===========


elif select=="country insights":
    st.title("country wise cricket analysis")

    scountry=st.selectbox("select country", df['country'].unique())

    col1, col2, col3, col4 = st.columns(4)

    cdata=df[df["country"]==scountry]

    players=cdata["player"].nunique()
    total_runs=cdata["Runs"].sum()
    total_matches=cdata["matches"].sum()
    total_innings=cdata["Inns"].sum()

    col1.metric("Total Players",players)
    col2.metric("Total runs",total_runs)
    col3.metric("Total Matches",total_matches)
    col4.metric("Total innings",total_innings)

    df2 = cdata[["player","Runs"]]

    df3=cdata[["player","Runs","matches","100","6s"]]

    df4= ["Runs","matches","100","6s"]

    fig=px.pie(df2,names="player")

    selectc=st.selectbox("select choice",df4)

    fig2=px.bar(df3,x="player",y=selectc,color="player")

    st.plotly_chart(fig2,use_container_width=True)

#====Player comparison=======

elif select=="Comparison":
    st.title("Player comparison")

    players = st.multiselect("Compare Players" , df["player"],default=df["player"].head(3))

    compare=df[df["player"].isin(players)]

    fig=px.scatter(compare,x="strike_rate",y="avg", size="Runs",color="country",hover_name="player")
    st.plotly_chart(fig,use_container_width=True)





elif select=="Data Explorer":
    st.title("Data Exploration")
    st.dataframe(df)

elif select=="About":
    st.info("About this project")
    st.text("Project by: Muhammmad Irfan Khan")
    st.success("End to End Streamlit Data Analysis Dashboard using Python For Cricket Analysis")

    url1= "https://www.linkedin.com/in/irfankhaninsights/"

    url2= "https://github.com/irfankhaninsights"
        
    col1,col2,col3,col4 = st.columns(4)
        
    with col1:
        st.link_button("linkedin",url1)
    with col2:
        st.link_button("github",url2)

