import pandas as pd
import streamlit as st
import numpy as np
import io


tab1, tab2=st.tabs([ "Historical Data","Nothing to add"])
with tab1:
    data=st.file_uploader("upload your excel file", key='read1')
    if data!=None:
        data=pd.read_excel(data, engine='openpyxl')
    st.dataframe(data)











        
    #     def newcal01(df):
    #       limit=pd.Series(df.Time.unique())
    #       result=pd.DataFrame()
    #       a=0
    #       while a < len(limit):
    #         mark=df[df['Time']==limit[a]]
    #         mark['call_max']=mark['CALL_OI'].max()
    #         mark['put_max']=mark['PUT_OI'].max()
    #         mark['CALL_OI_Per']=(mark['CALL_OI']/mark['call_max'])*100
    #         mark['PUT_OI_Per']=(mark['PUT_OI']/mark['put_max'])*100
    #         mark['CE_Vol_max']=mark['CALL_VOLUME'].max()
    #         mark['PE_Vol_max']=mark['PUT_VOLUME'].max()
    #         mark['CALL_VOL_Per']=(mark['CALL_VOLUME']/mark['CE_Vol_max'])*100
    #         mark['PUT_VOL_Per']=(mark['PUT_VOLUME']/mark['PE_Vol_max'])*100
    #         mark['Sum_CE']=mark['CALL_OI'].sum()
    #         mark['Sum_PE']=mark['PUT_OI'].sum()
    #         mark['Overall_PCR']=mark['Sum_PE']/mark['Sum_CE']
    #         mark['CE_Price']=mark['CALL_VOLUME']/mark['CE_Vol_max']*50 + mark['STRIKE']
    #         mark['PE_Price']= mark['STRIKE'] - mark['PUT_VOLUME']/mark['PE_Vol_max']*50 
    #         mark['PCR']=mark['PUT_OI']/mark['CALL_OI']
    #         mark['PCR_Val']=(mark['PCR'])*50
    #         result=pd.concat([result,mark], axis=0, join='outer', ignore_index=True)
    #         a+=1
    #         return result
            
    # def highlight_second_highest(s):
    #     max_val = s.max()
    #     second_highest = s.nlargest(2).iloc[-1]  # get second largest value
    #     threshold = 0.75 * max_val
    #     def color_val(val):
    #         if val > threshold and val == second_highest:
    #             return 'background-color: yellow'
    #         elif val == max_val:
    #             return 'background-color: green; color:black'
    #         else:
    #             return 'background-color:#f7f4d6; color:black'
    #         return s.apply(color_val)
    
    # def highlight_negative(val):
    #     color = 'red' if val < 0 else 'green' 
    #     return f'color: {color}'

    # def color_two(val, props='background-color:orange; color:black'):
    #     return props if val >0 else ''

    # def color_all(val, props='background-color:#f7f4d6; color:black'):
    #     return props if val >0 else props
######################### background change ####################
   
# col1, col2, col3, col4, col5, col6, col7, col8= st.columns(8)
# with col1:
#     expiry01=st.selectbox("please select expiry date", options=datafile.Expiry.unique(), key='expiry_01')
#     date01=st.selectbox("please select date", options=datafile.Date.unique(), key='date_01')
#     time_01 = st.selectbox("please select time", options=datafile.Time.sort_values(ascending=False).unique(), key='time_01')
#     stockexpiry=datafile[datafile['Expiry']==expiry01]
#     stockdate=datafile[datafile['Expiry']==date01]
#     stocktime = datafile [datafile ['Time']==time_01] 
#     strike_option = list(stocktime.STRIKE.unique())  
#     spot_price = stocktime.Spot_Price.iloc[0].round(-2)
#     ind0 = strike_option.index(spot_price)
#     ind1 = ind0-6
#     ind2 = ind0+6
# with col2:
#     con_strike1=st.selectbox("Select first strike", options=strike_option, index=ind1, key='first1')
# with col3:
#     con_strike2=st.selectbox("Select first strike", options=strike_option,index=ind2, key='first2')
#     refined = stocktime[stocktime.STRIKE.between(con_strike1, con_strike2)]                          
# with col4:
#     sleeptime =st.selectbox("Sleep Time", options=[3,6,9,12,15], index=0)
# with col5:
#     sub_table1=st.button("Filter Data", key='fil1', type='primary', use_container_width=True)
        
# love01 = refined.style.apply(highlight_second_highest, subset =['CALL_CHNG','CALL_OI','CALL_VOLUME','PUT_VOLUME','PUT_OI','PUT_CHNG'])\
#          .format(precision=0).format(precision=2, subset=['Time', 'CHNG','CHNG.1','CALL_LTP', 'PCR','PUT_LTP']).format(precision=0, subset=['CALL_CHNG','CALL_OI','CALL_VOLUME','PUT_VOLUME','PUT_OI','PUT_CHNG','STRIKE'])\
#          .map(color_two, subset=['STRIKE']) .map(color_all, subset=['IV','IV.1', 'BID QTY', 'BID',  'BID.1', 'BID QTY.1', 'ASK.1','ASK QTY.1', 'Spot_Price','ASK QTY', 'ASK', 'PUT_LTP', 'CALL_LTP', 'CE_Price','PE_Price', 'CALL_OI_Per', 'PUT_OI_Per', 'CALL_VOL_Per', 'PUT_VOL_Per','PCR', 'PCR_Val'])\
    
# if sub_table1==True:
#     st.dataframe(love01, height=500, hide_index=True, column_order=['Time','CALL_OI_Per','CALL_CHNG','CALL_OI','CALL_VOLUME','CALL_VOL_Per','CALL_LTP','CE_Price','STRIKE','PE_Price','PUT_LTP','PUT_VOL_Per','PUT_VOLUME','PUT_OI','PUT_CHNG','PUT_OI_Per','Spot_Price', 'PCR', 'PCR_Val'], use_container_width=True)
#     col1, col2, col3=st.columns(3)
#     with col1:
#         st.bar_chart(refined, x='STRIKE', y=['CALL_VOLUME', 'PUT_VOLUME'], stack=False, color= ["#F20712", "#19543F"])
#     with col2:
#         OI_chart=st.bar_chart(refined, x='STRIKE', y=['CALL_OI', 'PUT_OI'],  stack=False, color= ["#F20712", "#19543F"])
#     with col3:
#         OI_chart=st.bar_chart(refined, x='STRIKE', y=['CALL_CHNG', 'PUT_CHNG'], stack=False, color= ["#F20712", "#19543F"])
                  
# col1, col2, col3=st.columns(3)
# with col1:
#     OI_chart=st.bar_chart(refined, x='STRIKE', y=['CALL_VOLUME', 'PUT_VOLUME'], stack=False, color= ["#F20712", "#19543F"],horizontal=True, height=300, width=300)
#     PCR= datafile[datafile['STRIKE']== round (datafile.Spot_Price.iloc[0], -2)] [['Time','Sum_CE', 'Sum_PE', 'Overall_PCR']].sort_values(by='Time', ascending=False).style.background_gradient(cmap='Oranges').format(precision=2, subset=['Time', 'Overall_PCR'])        
#     st.dataframe(PCR, hide_index=True, height=300)
# with col2:
#     OI_chart=st.bar_chart(refined, x='STRIKE', y=['CALL_OI', 'PUT_OI'],  stack=False, color= ["#F20712", "#19543F"],horizontal=True, height=300,width=300)
#     st.line_chart(PCR, x='Time', y='Overall_PCR', color= ["#DE1BD1"],height=300, width=100)
#     #   PCR coding ends here
# with col3:
#     OI_chart=st.bar_chart(refined, x='STRIKE', y=['CALL_CHNG', 'PUT_CHNG'], stack=False, color= ["#F20712", "#19543F"],horizontal=True, height=300, width=300)
#     sumpe=datafile[datafile['STRIKE']== spot_price]
#     st.line_chart(sumpe, x='Time', y=['Sum_CE', 'Sum_PE'], color=['#B62626', '#26B669'], height=300)
                
# #   play button
# time_option1=datafile.Time.unique()
# playdata=datafile[datafile['STRIKE'].between(con_strike1, con_strike2)]
# ############################### play button colde
# if 'page' not in st.session_state:
#     st.session_state.page = 0 

# # function for button of next and previous
# def previous():
#     if st.session_state.page >0:
#         st.session_state.page -=1
                
# def next():
#     if (st.session_state.page +1) < len(time_option1):
#         st.session_state.page +=1
    
# def play():
#     val =0
#     placeholder = st.empty() 
#     while val < len (time_option1):
#         frame = playdata[playdata['Time']== time_option1[val]]
#         nextplay = frame.style.apply(highlight_second_highest, subset=['CALL_OI', 'PUT_OI','CALL_VOLUME','PUT_VOLUME','CALL_CHNG','PUT_CHNG',])\
#             .format(precision=1).map(color_two, subset=['STRIKE']).format(precision=2, subset=['Time'])\
#             .map(color_all, subset=['CALL_OI_Per', 'CALL_LTP','PUT_LTP','PUT_OI_Per','Spot_Price','CALL_VOL_Per','PUT_VOL_Per','CE_Price','PE_Price'])\
#             .format(precision=0, subset =['PE_Price','CE_Price']).set_sticky(axis=1)#.apply(highlight_row, axis=1, subset=['STRIKE','CALL_LTP','PUT_LTP','PUT_VOL_Per','CHNG', 'CHNG.1','CALL_VOL_Per', 'CE_Price', 'PE_Price'])
#         placeholder = st.dataframe(nextplay,hide_index=True, column_order=['Time','CALL_OI_Per','CALL_CHNG','CALL_OI','CALL_VOLUME','CALL_VOL_Per','CALL_LTP','CE_Price','STRIKE','PE_Price','PUT_LTP','PUT_VOL_Per','PUT_VOLUME','PUT_OI','PUT_CHNG','PUT_OI_Per','Spot_Price'], use_container_width=True, height=800)
#         val+=1
#         time.sleep(sleeptime)
#         placeholder.empty()

# ##### play buttons
# with col6:
#     st.button("play", on_click=play, use_container_width=True, type='primary')
# with col7:
#     previous01 = st.button("previous", on_click=previous, use_container_width=True, type='primary')
# with col8:
#     next01= st.button("next", on_click=next, use_container_width=True, type='primary')

# ################ button logic
# if previous01 == True:
#     frame = playdata[playdata['Time']== time_option1[st.session_state.page]]
#     nextplay = frame.style.apply(highlight_second_highest, subset=['CALL_OI', 'PUT_OI','CALL_VOLUME','PUT_VOLUME','CALL_CHNG','PUT_CHNG',])\
#         .format(precision=1).map(color_two, subset=['STRIKE']).format(precision=2, subset=['Time'])\
#         .map(color_all, subset=['CALL_OI_Per', 'CALL_LTP','PUT_LTP','PUT_OI_Per','Spot_Price','CALL_VOL_Per','PUT_VOL_Per','CE_Price','PE_Price'])\
#         .format(precision=0, subset =['PE_Price','CE_Price']).set_sticky(axis=1)
        
#     st.dataframe(nextplay,hide_index=True, column_order=['Time','CALL_OI_Per','CALL_CHNG','CALL_OI','CALL_VOLUME','CALL_VOL_Per','CALL_LTP','CE_Price','STRIKE','PE_Price','PUT_LTP','PUT_VOL_Per','PUT_VOLUME','PUT_OI','PUT_CHNG','PUT_OI_Per','Spot_Price'], use_container_width=True, height=800)
       
# if next01 == True:
#     frame = playdata[playdata['Time']== time_option1[st.session_state.page]]
#     nextplay =frame.style.apply(highlight_second_highest, subset=['CALL_OI', 'PUT_OI','CALL_VOLUME','PUT_VOLUME','CALL_CHNG','PUT_CHNG',])\
#         .format(precision=1).map(color_two, subset=['STRIKE']).format(precision=2, subset=['Time'])\
#         .applymap(color_all, subset=['CALL_OI_Per', 'CALL_LTP','PUT_LTP','PUT_OI_Per','Spot_Price','CALL_VOL_Per','PUT_VOL_Per','CE_Price','PE_Price'])\
#         .format(precision=0, subset =['PE_Price','CE_Price']).set_sticky(axis=1)
    
#     st.dataframe(nextplay,hide_index=True, column_order=['Time','CALL_OI_Per','CALL_CHNG','CALL_OI','CALL_VOLUME','CALL_VOL_Per','CALL_LTP','CE_Price','STRIKE','PE_Price','PUT_LTP','PUT_VOL_Per','PUT_VOLUME','PUT_OI','PUT_CHNG','PUT_OI_Per','Spot_Price'], use_container_width=True, height=800)
# # end of play button
