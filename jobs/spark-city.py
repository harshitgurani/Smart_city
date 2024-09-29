from pyspark import SparkSession

def main():
    spark = SparkSession.builder.appName("SmartCityStreaming")

if __name__ == "__main__":
    main()


