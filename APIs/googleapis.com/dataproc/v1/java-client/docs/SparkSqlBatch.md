

# SparkSqlBatch

A configuration for running Apache Spark SQL (https://spark.apache.org/sql/) queries as a batch workload.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jarFileUris** | **List&lt;String&gt;** | Optional. HCFS URIs of jar files to be added to the Spark CLASSPATH. |  [optional] |
|**queryFileUri** | **String** | Required. The HCFS URI of the script that contains Spark SQL queries to execute. |  [optional] |
|**queryVariables** | **Map&lt;String, String&gt;** | Optional. Mapping of query variable names to values (equivalent to the Spark SQL command: SET name&#x3D;\&quot;value\&quot;;). |  [optional] |



