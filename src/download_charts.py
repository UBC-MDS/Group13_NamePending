import altair as alt
from preprocess import split_test_data

data, _ = split_test_data("../data/raw/winequality/winequality-white.csv")

alt.renderers.enable('mimetype')

chart1 = alt.Chart(data, title="Distribution of white wine quality").mark_bar().encode(
    x=alt.X("quality", bin=alt.Bin(maxbins=12), title="Wine quality (/10)"),
    y="count()"
)

chart1.save('../results/Distribution_of_white_wine_quality.png')


chart2 = alt.Chart(data).mark_boxplot(opacity=1, size=10).encode(
    y=alt.Y(alt.repeat(), type="quantitative", scale=alt.Scale(zero=False)),
    x=alt.X("quality", scale=alt.Scale(zero=False)),
    color=alt.Color("quality", legend=None)
).properties(
    width=200,
    height=400
).repeat(
    ["fixed acidity", "volatile acidity", "citric acid", "residual sugar"]
)

chart2.save('../results/relationship_between_individual_features_and_the_quality_1.png')

chart3 = alt.Chart(data).mark_boxplot(opacity=1, size=10).encode(
    y=alt.Y(alt.repeat(), type="quantitative", scale=alt.Scale(zero=False)),
    x=alt.X("quality", scale=alt.Scale(zero=False)),
    color=alt.Color("quality", legend=None)
).properties(
    width=200,
    height=400
).repeat(
    ["chlorides", "free sulfur dioxide", "total sulfur dioxide", "density"]
)

chart3.save('../results/relationship_between_individual_features_and_the_quality_2.png')

chart4 = alt.Chart(data).mark_boxplot(opacity=1, size=10).encode(
    y=alt.Y(alt.repeat(), type="quantitative", scale=alt.Scale(zero=False)),
    x=alt.X("quality", scale=alt.Scale(zero=False)),
    color=alt.Color("quality", legend=None)
).properties(
    width=200,
    height=400
).repeat(
    ["pH", "sulphates", "alcohol"]
)

chart4.save('../results/relationship_between_individual_features_and_the_quality_3.png')
