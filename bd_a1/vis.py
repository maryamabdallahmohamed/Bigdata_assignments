import dpre
import matplotlib.pyplot as plt
import seaborn as sns

corr_with_sleep_disorder = dpre.clean_df.corr()['Sleep Disorder'].sort_values(ascending=False)
sns.heatmap(corr_with_sleep_disorder.to_frame(), annot=True, cmap='coolwarm', vmin=-1, vmax=1, cbar_kws={'label': 'Correlation'})
plt.title('Correlation with Sleep Disorder')
plt.savefig('vis.png', dpi=300, bbox_inches='tight')