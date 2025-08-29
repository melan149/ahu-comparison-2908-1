import streamlit as st
if impeller_size_col or impeller_efficiency_col:
st.subheader("Fan Section Data")
if impeller_size_col:
row_cols = st.columns([2] + [3]*n_units)
row_cols[0].markdown("**Impeller size (available optins)**")
for i, fu in enumerate(filtered_units):
val = fu[impeller_size_col].iloc[0] if impeller_size_col in fu.columns and not fu.empty else "-"
row_cols[i+1].write(val)
if impeller_efficiency_col:
row_cols = st.columns([2] + [3]*n_units)
row_cols[0].markdown("**Impeller efficiency at optimal airflow [%]**")
for i, fu in enumerate(filtered_units):
val = fu[impeller_efficiency_col].iloc[0] if impeller_efficiency_col in fu.columns and not fu.empty else "-"
row_cols[i+1].write(val)


# Construction Details
if base_frame_height_col or cabling_col:
st.subheader("Construction Details")
if base_frame_height_col:
row_cols = st.columns([2] + [3]*n_units)
row_cols[0].markdown("**Base frame/Feets height [mm]**")
for i, fu in enumerate(filtered_units):
val = fu[base_frame_height_col].iloc[0] if base_frame_height_col in fu.columns and not fu.empty else "-"
row_cols[i+1].write(val)
if cabling_col:
row_cols = st.columns([2] + [3]*n_units)
row_cols[0].markdown("**Cabling**")
for i, fu in enumerate(filtered_units):
val = fu[cabling_col].iloc[0] if cabling_col in fu.columns and not fu.empty else "-"
row_cols[i+1].write(val)


# --- Example Chart (Unit size vs Region) ---
if size_col and region_col:
st.subheader("Example Chart: Unit size by Region")
chart_data = []
for i, fu in enumerate(filtered_units):
if not fu.empty:
chart_data.append({
"Unit": f"Unit {i+1} - {fu[brand_col].iloc[0]}",
"Size": fu[size_col].iloc[0],
"Region": fu[region_col].iloc[0]
})
if chart_data:
chart_df = pd.DataFrame(chart_data)
fig = px.bar(chart_df, x="Unit", y="Size", color="Region", barmode="group")
st.plotly_chart(fig, use_container_width=True)


# --- CSV Export ---
csv_data = []
header_row = ["Parameter"] + [f"Unit {i+1}" for i in range(n_units)]
csv_data.append(header_row)


for col in df.columns:
row = [col]
for fu in filtered_units:
row.append(fu[col].iloc[0] if col in fu.columns and not fu.empty else "-")
csv_data.append(row)


csv_df = pd.DataFrame(csv_data)
csv_string = csv_df.to_csv(index=False, header=False)
st.download_button("Download Comparison CSV", csv_string, file_name="comparison.csv", mime="text/csv")


else:
st.warning("At least one selected unit has no data. Please adjust selections.")