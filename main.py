import csv
import sys

def parse_input_structure(input_file) :
	table_columns = []
	with open(input_file) as csv_file :
		for row in csv.reader(csv_file, delimiter=',') :
			for col in row :
				table_columns.append(col)
			return input_file.split('.csv')[0], table_columns

def create_table(table_name, column_names) :
	query_start = "CREATE TABLE " + table_name + " ("
	query_end = ");\n"
	column_names_formated = []
	# Add default columns
	column_names_formated.append("id SERIAL UNIQUE")
	column_names_formated.append(" created_at timestamp default current_timestamp")
	# Loop over column names
	for column in column_names :
		column_names_formated.append(" " + column + " TEXT")
	return query_start + ','.join(column_names_formated) + query_end

def insert_statements(input_file, table_name, column_names) :
	query_start = "INSERT INTO " + table_name + "(" + ', '.join(column_names) + ") VALUES "
	row_counter = 0
	row_buffer = []
	with open(input_file) as csv_file :
			for row in csv.reader(csv_file, delimiter=',') :
				# The first row is the column names which we have already parsed
				if row_counter > 0 :
					row_buffer.append("('" + "', '".join(row) + "')")
				row_counter =+ 1
	return query_start + ', '.join(row_buffer[:-1]) + ', ' + ''.join(row_buffer[len(row_buffer) - 1]) + ";"

def write_output_query(output_dir, table_name, create_table_query, insert_query) :
	with open(output_dir + table_name + '.sql', 'w') as output_file :
		output_file.write(create_table_query + insert_query)

if __name__ == '__main__' :
	input_file = sys.argv[1]
	output_dir = sys.argv[2]

	table_name, column_names = parse_input_structure(input_file)
	create_table_query = create_table(table_name, column_names)
	insert_query = insert_statements(input_file, table_name, column_names)
	write_output_query(output_dir, table_name, create_table_query, insert_query)
	print "Script finished!"
	print "You can now find your finished SQL file and write it to your database."
