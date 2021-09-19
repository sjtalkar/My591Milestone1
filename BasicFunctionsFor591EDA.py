import altair as alt


def plotDistributionForColumn(df, colName):

    """
        This function plots a histogram for a column of the df  dataframe 
        At the botton of the histogram, it plots a boxplot
    """
    source = df[[colName]]

    base = alt.Chart(source, title=colName)

    B = base.mark_bar(color="green").encode(
        alt.X(f"{colName}:Q", bin=alt.Bin(maxbins=100)), y="count()",
    )

    mean_rule = alt.Chart(source).mark_rule(color="red").encode(x=f"mean({colName}):Q")

    median_rule = (
        alt.Chart(source).mark_rule(color="orange").encode(x=f"median({colName}):Q")
    )

    box_plot = base.mark_boxplot().encode(x=f"{colName}:Q",)


def plotCategoricalfeatures(df, colName):

    """
        This function plots a br graph for  a column of the df  dataframe. 
        The type of the column is categorical 
        At the botton of the histogram, it plots a boxplot
    """
    source = df[[colName]]

    base = alt.Chart(source, title=colName)

    B = base.mark_bar(color="#20b2aa").encode(alt.X(f"{colName}:N"), y="count()")

    return B

    return B + mean_rule + median_rule & box_plot


def createCorrelationScatters(df, colName, targetName):
    """
        This function created a scatter chart and a line that is a regression line between the two numerical columns passed to it
        It prints out the correlation values as well
    """

    corr = df[targetName].corr(df[colName])
    source = df

    base = alt.Chart(source)

    chart = (
        base.mark_circle()
        .encode(
            alt.X(f"{colName}:Q"), alt.Y(f"{targetName}:Q"), color=alt.value("orange")
        )
        .properties(width=300, height=150)
    )
    text = base.mark_text(align="left", baseline="top").encode(
        x=alt.value(5),  # pixels from left
        y=alt.value(5),  # pixels from top
        text=alt.value(f"corr: {corr:.3f}"),
    )

    return (
        chart
        + text
        + chart.transform_regression(colName, targetName)
        .mark_line(color="darkblue")
        .encode(color=alt.value("blue"))
    )

