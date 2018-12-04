import pandas as pd 

def create_features(df, bin_edges, feature_name):
	bin_series = pd.cut(df[feature_name], bins=bin_edges)

	for index, edge in enumerate(bin_edges):
		name = feature_name + '_' + str(edge) + '_to_' + str(bin_edges[index + 1])
		df[name] = bin_series.apply(lambda i: 1 if i.left == edge else 0)

	return df