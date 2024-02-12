import pandas as pd

# Load the dataset
file_path = '/data/StudentsPerformance.csv'
students_performance = pd.read_csv(file_path)

students_performance.head()

import seaborn as sns

sns.set_style("whitegrid")

# Create a figure for the histograms
plt.figure(figsize=(18, 6))

# Math Score Distribution by Gender
plt.subplot(1, 3, 1)
sns.histplot(students_performance, x="math score", hue="gender", element="step", stat="density", common_norm=False)
plt.title('Math Score Distribution by Gender')

# Reading Score Distribution by Gender
plt.subplot(1, 3, 2)
sns.histplot(students_performance, x="reading score", hue="gender", element="step", stat="density", common_norm=False)
plt.title('Reading Score Distribution by Gender')

# Writing Score Distribution by Gender
plt.subplot(1, 3, 3)
sns.histplot(students_performance, x="writing score", hue="gender", element="step", stat="density", common_norm=False)
plt.title('Writing Score Distribution by Gender')

# Display the plots
plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# Create histograms to show the distribution of scores
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

sns.histplot(students_performance['math score'], bins=20, kde=True, ax=axes[0], color='skyblue')
axes[0].set_title('Distribution of Math Scores')

sns.histplot(students_performance['reading score'], bins=20, kde=True, ax=axes[1], color='lightgreen')
axes[1].set_title('Distribution of Reading Scores')

sns.histplot(students_performance['writing score'], bins=20, kde=True, ax=axes[2], color='salmon')
axes[2].set_title('Distribution of Writing Scores')

plt.tight_layout()
plt.show()


# Box plots to compare gender performance in each subject
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

sns.boxplot(x='gender', y='math score', data=students_performance, ax=axes[0], palette="Set2")
axes[0].set_title('Math Scores by Gender')

sns.boxplot(x='gender', y='reading score', data=students_performance, ax=axes[1], palette="Set2")
axes[1].set_title('Reading Scores by Gender')

sns.boxplot(x='gender', y='writing score', data=students_performance, ax=axes[2], palette="Set2")
axes[2].set_title('Writing Scores by Gender')

plt.tight_layout()
plt.show()


# Bar charts to analyze scores by parental level of education
fig, axes = plt.subplots(3, 1, figsize=(10, 15))

# calculating mean scores
mean_scores_by_education = students_performance.groupby('parental level of education')[['math score', 'reading score', 'writing score']].mean().reset_index()

sns.barplot(x='math score', y='parental level of education', data=mean_scores_by_education, ax=axes[0], palette="coolwarm")
axes[0].set_title('Average Math Score by Parental Level of Education')

sns.barplot(x='reading score', y='parental level of education', data=mean_scores_by_education, ax=axes[1], palette="coolwarm")
axes[1].set_title('Average Reading Score by Parental Level of Education')

sns.barplot(x='writing score', y='parental level of education', data=mean_scores_by_education, ax=axes[2], palette="coolwarm")
axes[2].set_title('Average Writing Score by Parental Level of Education')

plt.tight_layout()
plt.show()


# Violin plots to visualize the distribution of scores by race/ethnicity
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

sns.violinplot(x='race/ethnicity', y='math score', data=students_performance, ax=axes[0], palette="Pastel1")
axes[0].set_title('Math Scores by Race/Ethnicity')

sns.violinplot(x='race/ethnicity', y='reading score', data=students_performance, ax=axes[1], palette="Pastel1")
axes[1].set_title('Reading Scores by Race/Ethnicity')

sns.violinplot(x='race/ethnicity', y='writing score', data=students_performance, ax=axes[2], palette="Pastel1")
axes[2].set_title('Writing Scores by Race/Ethnicity')

plt.tight_layout()
plt.show()


