import os, logging, argparse
from toolkit import *
from utils import load_csv

if __name__=='__main__':
    os.makedirs("Logs", exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename='logs/app.log',
        filemode='a'
    )
    
    parser = argparse.ArgumentParser(
        description="Dataset Toolkit CLI"
    )
    
    parser.add_argument("--file", required=True)
    parser.add_argument("--rows", action="store_true")
    parser.add_argument("--column", action="store_true")
    parser.add_argument("--head", type=int)
    parser.add_argument("--unique", type=str)
    parser.add_argument("--filter", type=str)
    parser.add_argument("--sort-by", type=str)
    parser.add_argument("--desc", action="store_true")
    parser.add_argument("--top", type=int)
    parser.add_argument("--summary", action="store_true")
    
    logging.info("Program has started.")
    
    args = parser.parse_args()
    file_path = 'sample_data/'+args.file
    data = load_csv(file_path)
    datatoolkit = DatasetToolkit(data)
    
    
    if args.rows:
        print(datatoolkit.row_count())
    if args.column:
        print(datatoolkit.columns())
    if args.head:
        print(datatoolkit.head(args.head))
    if args.unique:
        print(datatoolkit.unique_values(args.unique))
    if args.filter:
        if "=" not in args.filter:
            print("Error: --filter must be in column=value format")
        else:
            column, value = args.filter.split("=", 1)
            results = datatoolkit.filter_rows(column, value)

            if not results:
                print(f"No rows found for {column}={value}")
            else:
                print(f"Rows where {column}={value}:")
                for row in results:
                    print(row)
    if args.sort_by:
        print(datatoolkit.sort_rows(args.sort_by, args.desc))
    if args.top:
        if not args.sort_by:
            print("Error: --top requires --sort-by <column>")
        else:
            print(datatoolkit.top_n(args.sort_by, args.top))
    if args.summary:
        print(datatoolkit.summary())
    
    logging.info("Program has ended.")