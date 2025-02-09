import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('atlas_all_appointments.csv')

# Create a DataFrame that counts affiliations by status
affiliation_status_counts = df.groupby([' Affiliation', ' Status']).size().unstack(fill_value=0)

# 1. Select the top 10 most frequent affiliations
top_affiliations = affiliation_status_counts.sum(axis=1).nlargest(30).index
top_affiliation_counts = affiliation_status_counts.loc[top_affiliations]
# Reverse the order of the rows so that the most frequent is on top
top_affiliation_counts = top_affiliation_counts[::-1]
# 1. Stacked area plot of Affiliation according to Status values for top 10
top_affiliation_counts.plot(kind='barh', stacked=True, figsize=(10, 6))
# Add a vertical dashed line at x-axis = 10
plt.axvline(x=50, color='red', linestyle='--')
plt.title('Top Affiliations for Appointments')
plt.xlabel('Count')
plt.ylabel('Affiliation')
plt.legend(title='Status', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('results/Top-Affiliations-stacked.png')
plt.show()
plt.close()


# 2. Create a horizontal bar plot of Affiliation according to active Status values
# Select only the counts for the "active" status
top_active_affiliations_counts = affiliation_status_counts['active'].nlargest(30)  # Get top 10 active affiliations
top_active_affiliations_counts = top_active_affiliations_counts[::-1]
top_active_affiliations_counts.plot(kind='barh', figsize=(8, 6))  # Regular horizontal bar plot
# Add a vertical dashed line at x-axis = 10
plt.axvline(x=10, color='red', linestyle='--')
plt.title('Top Affiliations for Active Appointments')
plt.xlabel('Count')
plt.ylabel('Affiliation')
plt.tight_layout()
plt.savefig('results/Top-Affiliations-active.png')
plt.show()
plt.close()


# 3. Histograms of Affiliation if Appointment contains "CP group"
cp_group_df = df[df[' Appointment'].str.contains("CP group", na=False)]
cp_affiliation_counts = cp_group_df[' Affiliation'].value_counts().nlargest(30)
cp_affiliation_counts = cp_affiliation_counts[::-1]
cp_affiliation_counts.plot(kind='barh', figsize=(8, 6))
# Add a vertical dashed line at x-axis = 5
plt.axvline(x=5, color='red', linestyle='--')
plt.title('Top Affiliations for CP group Appointments')
plt.xlabel('Count')
plt.ylabel('Affiliation')
plt.tight_layout()
plt.savefig('results/Top-Affiliations-CP-groups.png')
plt.show()
plt.close()


# 4. Histograms of Affiliation if Appointment contains "physics group"
ph_group_df = df[df[' Appointment'].str.contains("physics group", na=False)]
ph_affiliation_counts = ph_group_df[' Affiliation'].value_counts().nlargest(30)
ph_affiliation_counts = ph_affiliation_counts[::-1]
ph_affiliation_counts.plot(kind='barh', figsize=(8, 6))
# Add a vertical dashed line at x-axis = 5
plt.axvline(x=5, color='red', linestyle='--')
plt.title('Top Affiliations for physics group Appointments')
plt.xlabel('Count')
plt.ylabel('Affiliation')
plt.tight_layout()
plt.savefig('results/Top-Affiliations-ph-groups.png')
plt.show()
plt.close()


# 5. Histograms of Affiliation if Appointment contains "CP group"
cp_group_df = df[df[' Appointment'].str.contains("CP group", na=False)]
active_cp_group_df = cp_group_df[cp_group_df[' Status'] == 'active']
cp_affiliation_counts = active_cp_group_df[' Affiliation'].value_counts().nlargest(30)
cp_affiliation_counts = cp_affiliation_counts[::-1]
cp_affiliation_counts.plot(kind='barh', figsize=(8, 6))
plt.title('Top Affiliations for active CP group Appointments')
plt.xlabel('Count')
plt.ylabel('Affiliation')
plt.tight_layout()
plt.savefig('results/Top-Affiliations-CP-groups-active.png')
plt.show()
plt.close()


# 6. Histograms of Affiliation if Appointment contains "physics group"
ph_group_df = df[df[' Appointment'].str.contains("physics group", na=False)]
active_ph_group_df = ph_group_df[ph_group_df[' Status'] == 'active']
ph_affiliation_counts = active_ph_group_df[' Affiliation'].value_counts().nlargest(30)
ph_affiliation_counts = ph_affiliation_counts[::-1]
ph_affiliation_counts.plot(kind='barh', figsize=(10, 6))
plt.title('Top Affiliations for active physics group Appointments')
plt.xlabel('Count')
plt.ylabel('Affiliation')
plt.tight_layout()
plt.savefig('results/Top-Affiliations-ph-groups-active.png')
plt.show()
plt.close()