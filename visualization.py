import streamlit as st
import pandas as pd
import base64
from data_process import process_data
import plotly.graph_objects as go

def display_options(data):
    data = process_data(data)
    pd.set_option('display.max_colwidth', None)

    st.sidebar.markdown('<p class="font">Ransomware Data Database</p>', unsafe_allow_html=True)
    st.sidebar.subheader("About the App")
    st.sidebar.text("""
        Exploration of the Ransomware Attacks by Group, per Target and Date 
    """)

    st.sidebar.subheader('Statistics')
    if st.sidebar.checkbox('Full Data Set', key='full_data_set'):
        st.subheader('Data Starting with Most Recent Attacks')
        st.write(data.iloc[:, :3]) 

    if st.sidebar.checkbox('Show attacks over time', help='Toggle to view the number of attacks over time'):
        st.subheader('Attacks Over Time')

        all_groups = data['Group'].unique().tolist()
        selected_groups = st.multiselect('Select Groups', all_groups, default=[])
        filtered_data = data[data['Group'].isin(selected_groups)]

        if not selected_groups:
            st.write("Select at least one group to display the graph")
        else:
            # Ensure 'Date' column is in datetime format
            filtered_data['Date'] = pd.to_datetime(filtered_data['Date'])

            # Set 'Date' as index and resample the data monthly
            filtered_data = filtered_data.set_index('Date').groupby('Group').resample('M').size().reset_index(name='Number of Attacks')
            filtered_data['Date'] = filtered_data['Date'].dt.strftime('%b %Y')

            # Initialize an empty figure
            fig = go.Figure()

            # Loop over the groups to add a line for each group
            for group in selected_groups:
                group_data = filtered_data[filtered_data['Group'] == group]
                fig.add_trace(go.Scatter(
                    x=group_data['Date'], 
                    y=group_data['Number of Attacks'], 
                    mode='lines+markers+text', 
                    name=group, 
                    text=group_data['Number of Attacks'], 
                    textposition='top center',
                    line=dict(color='#f8931d'),  # set the color of the line
                    marker=dict(
                        symbol='star',
                        color='black',  # set the color of the marker
                        size=10  # adjust the size of the marker
                    )

                ))
            
            fig.update_layout(
                title='Attacks Over Time by Group',
                title_x=0.5, 
                xaxis_title='Date', 
                yaxis_title='Number of Attacks',
                hovermode='x unified',
                plot_bgcolor='#f8fafc',
                paper_bgcolor='#f8fafc',
                font=dict(color='#222222')
            )

            # Display the figure
            st.plotly_chart(fig, use_container_width=True)
            if st.checkbox('Show description for "Attacks Over Time"'):
                st.markdown("""
                    The chart above depicts the number of ransomware attacks over time for the selected groups. 
                    The x-axis represents time (in months and years), while the y-axis represents the count of attacks. Each line corresponds to a different group.
                    The markers show the number of attacks for each month. The plot allows us to analyze the frequency and trend of attacks over time for each group.
                """)

    if st.sidebar.checkbox('Show repeated targets by group and date'):
        st.subheader('Repeated Targets by Group and Date')
        group_target_dates = data.groupby(['Group', 'Title'])['Date'].apply(list).reset_index(name='Dates')
        group_target_dates = group_target_dates[group_target_dates['Dates'].str.len() > 1]
        st.write(group_target_dates)
        groups = group_target_dates['Group'].unique().tolist()
        selected_group = st.selectbox('Select a Group', groups)
        targets = group_target_dates[group_target_dates['Group'] == selected_group]['Title'].unique().tolist()
        selected_target = st.multiselect('Select a Target', targets)  # Using multiselect for targets
        selected_data = group_target_dates[(group_target_dates['Group'] == selected_group) &
                                            (group_target_dates['Title'].isin(selected_target))]

        if not selected_target:
            st.write("Select at least one target to display the graph")
        else:
            # Ensure 'Date' column is in datetime format
            selected_data['Dates'] = selected_data['Dates'].apply(lambda x: pd.to_datetime(x))
            
            # Initialize an empty figure
            fig = go.Figure()
            for target in selected_target:
                target_data = selected_data[selected_data['Title'] == target]
                for date in target_data['Dates'].values[0]:
                    fig.add_trace(go.Scatter(
                        x=group_data['Date'], 
                        y=group_data['Number of Attacks'], 
                        mode='lines+markers+text', 
                        name=group, 
                        text=group_data['Number of Attacks'], 
                        textposition='top center',
                        line=dict(color='#f8931d'),  # set the color of the line
                        marker=dict(
                            symbol='star',
                            color='black',  # set the color of the marker
                            size=10  # adjust the size of the marker
                        )
                    ))

            # Update layout
            fig.update_layout(
                title=f"{selected_group} attacking selected targets",
                title_x=0.5,
                xaxis_title='Date',
                hovermode='x unified',
                plot_bgcolor='#f8fafc',
                paper_bgcolor='#f8fafc',
                font=dict(color='#222222')
            )

            # Display the figure
            st.plotly_chart(fig, use_container_width=True)
            if st.checkbox('Show description for "Repeated Targets by Group and Date"'):
                st.markdown("""
                    This scatter plot represents the repeated attacks on selected targets by the selected group. 
                    Each marker on the plot represents an attack. The x-axis represents time (dates of attacks) and the y-axis represents the targets. 
                    This visualization helps us understand which targets are repeatedly attacked by a particular group.
                """)



    if st.sidebar.checkbox('Download CSV file'):
        csv = data.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        linko= f'<a href="data:file/csv;base64,{b64}" download="myfilename.csv">Download CSV File</a>'
        st.markdown(linko, unsafe_allow_html=True)