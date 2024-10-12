# CloudDataprocApi.SparkSqlJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jarFileUris** | **[String]** | Optional. HCFS URIs of jar files to be added to the Spark CLASSPATH. | [optional] 
**loggingConfig** | [**LoggingConfig**](LoggingConfig.md) |  | [optional] 
**properties** | **{String: String}** | Optional. A mapping of property names to values, used to configure Spark SQL&#39;s SparkConf. Properties that conflict with values set by the Dataproc API might be overwritten. | [optional] 
**queryFileUri** | **String** | The HCFS URI of the script that contains SQL queries. | [optional] 
**queryList** | [**QueryList**](QueryList.md) |  | [optional] 
**scriptVariables** | **{String: String}** | Optional. Mapping of query variable names to values (equivalent to the Spark SQL command: SET name&#x3D;\&quot;value\&quot;;). | [optional] 


