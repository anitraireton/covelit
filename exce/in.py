import pandas as pd

# Sample DataFrame
data = {
    'node': [1, 2, 3, 4, 5],
    'value': [10, 20, 30, 40, 50]
}
df_list = pd.DataFrame(data)

# Convert the 'node' column to a list
node_list = list(df_list['node'])

# If you want to reassign it back to the DataFrame (although this step is generally unnecessary)
df_list['node'] = node_list

# Print the list to verify
print(node_list)
