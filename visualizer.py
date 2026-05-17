import matplotlib.pyplot as plt
import seaborn as sns

def plot_bar(df, x_col, y_col):
    fig, ax = plt.subplots(figsize=(9,4))
    sns.barplot(data=df, x=x_col, y=y_col, ax=ax, palette="Blues_d")
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
    fig, ax = plt.subplots(figsize=(4,3))

    df.groupby(col).sum(numeric_only=True).iloc[:, 0].plot.pie(
        autopct="%1.1f%%",ax=ax,colors=sns.color_palette("Blues"),
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
    ax.scatter(df[x_col], df[y_col], color='steelblue', s=100)
    ax.set_title(f"{x_col} vs {y_col}")
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    return fig

def plot_histogram(df, col):

    fig, ax = plt.subplots(figsize=(7,4))

    ax.hist(
        df[col],
        bins=8,
        color="#cfe8f3",
        edgecolor="#1f77b4",
        linewidth=1
    )

    ax.set_title(
        f"{col} Distribution",
        fontsize=16,
        fontweight='bold',
        pad=15
    )

    ax.set_xlabel(col, fontsize=12)
    ax.set_ylabel("Number of Students", fontsize=12)

   

    ax.set_axisbelow(True)

    fig.tight_layout()

    return fig