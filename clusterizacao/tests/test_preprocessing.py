from services.pre_processing_knn import PreProcessing


input_file = "alunos_categoricos.csv"
output_file = "alunos_transformados.csv"

headers, datas = PreProcessing.load_csv(input_file)
categorical_columns = PreProcessing.search_categorical_columns(datas, headers)
new_headers = PreProcessing.generate_new_headers(headers, categorical_columns, datas)
transformed_data = PreProcessing.apply_one_hot_encoding(datas, categorical_columns)
PreProcessing.save_csv(new_headers, transformed_data, "alunos transformados.csv")