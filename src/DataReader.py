import pandas as pd
import pathlib


def write_csv(df, outputPath, separator=",", index=False,encoding="utf-8"):
    # index=False to write csv without index column which pandas added
    df.to_csv(outputPath, sep=separator, index=index, encoding=encoding)


def read_csv(file_path, separator=",", encoding="utf-8"):
    df = pd.read_csv(file_path, sep=separator, encoding=encoding)
    return df


def write_json(df, file_path):
    df.to_json(file_path)


def read_json(file_path, encoding="utf-8"):
    return pd.read_json(file_path, encoding=encoding)


def read_sas(filePath: str):
    df = pd.read_sas(filePath)
    return df


def read_file(filePath: str):
    path = pathlib.Path(filePath)
    fileExtension = path.suffix[1:]
    if fileExtension == "csv":
        df = read_csv(path)
    elif fileExtension == "sas7bdat":
        df = read_sas(filePath)
    elif fileExtension == "json":
        df = read_json(filePath)
    else:
        raise NotImplementedError("The given file format is not supported")
    return df


def main():
    root_path = "../data"
    sas_file_path = f"{root_path}/airline.sas7bdat"
    df = read_sas(sas_file_path)
    csv_file_path = f"{root_path}/airline.csv"
    json_file_path = f"{root_path}/airline.json"
    write_csv(df, csv_file_path)
    # write_json(df, json_file_path)
    df1 = read_file(sas_file_path)
    print(df1.head())
    df2 = read_file(csv_file_path)
    print( df2.head())
    df3 = read_file(json_file_path)
    print(df3.head())


if __name__ == "__main__":
    main()
