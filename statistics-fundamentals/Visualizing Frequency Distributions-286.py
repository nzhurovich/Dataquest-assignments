## 2. Bar Plots ##

Exp_ordinal = wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]]
Exp_ordinal.plot.bar()
plt.show()

## 3. Horizontal Bar Plots ##

Exp_ordinal = wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]]
Exp_ordinal.plot.barh(title = 'Number of players in WNBA by level of experience')
plt.show()

## 4. Pie Charts ##

Exp_ordinal = wnba['Exp_ordinal'].value_counts().plot.pie()
plt.show()

## 5. Customizing a Pie Chart ##

import matplotlib.pyplot as plt

Exp_ordinal = wnba['Exp_ordinal'].value_counts(normalize=True).plot.pie(figsize = (6,6), autopct = "%.2f%%", title = "Percentage of players in WNBA by level of experience")
plt.ylabel('')
plt.show()

## 6. Histograms ##

wnba['PTS'].plot.hist()

## 7. The Statistics Behind Histograms ##

from numpy import arange
describe = wnba['Games Played'].describe()
wnba['Games Played'].plot.hist()
plt.show()

## 9. Binning for Histograms ##

wnba['Games Played'].plot.hist(range = (1, 32), bins = 8, title = "The distribution of players by games played")
plt.xlabel('Games played')
plt.show()

## 10. Skewed Distributions ##

wnba['AST'].plot.hist()
plt.show()
wnba['FT%'].plot.hist()
plt.show()
assists_distro = 'right skewed'
ft_percent_distro = 'left skewed'

## 11. Symmetrical Distributions ##

normal_distribution = 'Height'