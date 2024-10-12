# CloudDataprocApi.SparkJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archiveUris** | **[String]** | Optional. HCFS URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip. | [optional] 
**args** | **[String]** | Optional. The arguments to pass to the driver. Do not include arguments, such as --conf, that can be set as job properties, since a collision may occur that causes an incorrect job submission. | [optional] 
**fileUris** | **[String]** | Optional. HCFS URIs of files to be placed in the working directory of each executor. Useful for naively parallel tasks. | [optional] 
**jarFileUris** | **[String]** | Optional. HCFS URIs of jar files to add to the CLASSPATHs of the Spark driver and tasks. | [optional] 
**loggingConfig** | [**LoggingConfig**](LoggingConfig.md) |  | [optional] 
**mainClass** | **String** | The name of the driver&#39;s main class. The jar file that contains the class must be in the default CLASSPATH or specified in SparkJob.jar_file_uris. | [optional] 
**mainJarFileUri** | **String** | The HCFS URI of the jar file that contains the main class. | [optional] 
**properties** | **{String: String}** | Optional. A mapping of property names to values, used to configure Spark. Properties that conflict with values set by the Dataproc API might be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code. | [optional] 


