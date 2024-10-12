# CloudDataprocApi.SparkSqlBatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jarFileUris** | **[String]** | Optional. HCFS URIs of jar files to be added to the Spark CLASSPATH. | [optional] 
**queryFileUri** | **String** | Required. The HCFS URI of the script that contains Spark SQL queries to execute. | [optional] 
**queryVariables** | **{String: String}** | Optional. Mapping of query variable names to values (equivalent to the Spark SQL command: SET name&#x3D;\&quot;value\&quot;;). | [optional] 


