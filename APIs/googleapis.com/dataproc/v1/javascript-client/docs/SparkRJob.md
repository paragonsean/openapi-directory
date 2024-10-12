# CloudDataprocApi.SparkRJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archiveUris** | **[String]** | Optional. HCFS URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip. | [optional] 
**args** | **[String]** | Optional. The arguments to pass to the driver. Do not include arguments, such as --conf, that can be set as job properties, since a collision may occur that causes an incorrect job submission. | [optional] 
**fileUris** | **[String]** | Optional. HCFS URIs of files to be placed in the working directory of each executor. Useful for naively parallel tasks. | [optional] 
**loggingConfig** | [**LoggingConfig**](LoggingConfig.md) |  | [optional] 
**mainRFileUri** | **String** | Required. The HCFS URI of the main R file to use as the driver. Must be a .R file. | [optional] 
**properties** | **{String: String}** | Optional. A mapping of property names to values, used to configure SparkR. Properties that conflict with values set by the Dataproc API might be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code. | [optional] 


