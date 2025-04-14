import altair as alt
import pandas as pd

# Read the dataset
data = pd.read_csv("ObesityDataSet_raw_and_data_sinthetic.csv")

# Create an Altair box plot for age distribution by obesity level
chart = alt.Chart(data).mark_boxplot(size=40).encode(
    # X-axis: Obesity level as a nominal variable with a rotated axis label for better readability
    x=alt.X("NObeyesdad:N", title="Obesity Level", axis=alt.Axis(labelAngle=45)),
    # Y-axis: Age as a quantitative variable
    y=alt.Y("Age:Q", title="Age"),
    # Color encoding using obesity level
    color=alt.Color("NObeyesdad:N", legend=None)
).properties(
    title="Relationship Between Age and Obesity Level",  # Chart title
    width=600,
    height=400
)

# Save the chart as an HTML file so it can be viewed in a web browser
chart.save("box_plot_altair.html")
print("The box plot has been saved as 'box_plot_altair.html'")
