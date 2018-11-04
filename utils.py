import matplotlib.pyplot as plt

def get_name_series(name, df, center=False):
    name_series = df.xs(name, level='name').groupby('year').sum()
    if center:
        max_yr = name_series['count'].idxmax()
        name_series.index -= max_yr
        
    return name_series['count']
   
def plot_name_popularity(name, df, center=False):
    name_series = get_name_series(name, df).to_frame(name)
    name_series.plot(ax=plt.gca())

def plot_top_names(year, gender, df, n=10):
    top_names =  (df.xs(year, level='year')
                    .xs(gender, level='gender')
                    .sort_values('count', ascending=False)
                    .head(n))

    top_names[::-1].plot.barh()
    plt.grid()
    ft_ax(title='Most popular names (%i, %s)' % (year, gender), left_axis=True)
    #return top_names[::-1]