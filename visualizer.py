import matplotlib.pyplot as plt
import seaborn as sns

def plot_bar(df, x_col, y_col):
    fig, ax = plt.subplots()

    sns.barplot(
        data=df,
        x=x_col,
        y=y_col,
        ax=ax,
        palette="pastel"
    )

    ax.set_title(f"{y_col} by {x_col}")
    plt.xticks(rotation=45)

    return fig

def plot_line(df, x_col, y_col):
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(df[x_col], df[y_col], marker='o', color='steelblue')
    ax.set_title(f"{y_col} trend over {x_col}")
    plt.xticks(rotation=45)
    return fig

def plot_pie(df, col):
    fig, ax = plt.subplots(figsize=(5,5))

    df.groupby(col).sum(numeric_only=True).iloc[:, 0].plot.pie(
        autopct="%1.1f%%",ax=ax,colors=sns.color_palette("Set2"),
        radius=0.65,
        textprops={'fontsize': 10}
    )

    ax.set_title(
        f"{col} Distribution",
        fontsize=8
    )

    ax.set_ylabel("")

    fig.tight_layout(pad=0)
    return fig
def plot_scatter(df, x_col, y_col):
    fig, ax = plt.subplots(figsize=(8,4))
    colors=sns.color_palette("Set2",len(df))
    ax.scatter(df[x_col], df[y_col], c=colors, s=100)
    ax.set_title(f"{x_col} vs {y_col}")
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    return fig

def plot_histogram(df, col):

    fig, ax = plt.subplots(figsize=(7,4))

    n, bins, patches = ax.hist(
        df[col],
        bins=8,
        edgecolor="white",
        linewidth=0
    )

    colors = sns.color_palette("pastel", len(patches))

    for patch, color in zip(patches, colors):
        patch.set_facecolor(color)

    ax.set_title(f"{col} Distribution")

    return fig