# CloudDataprocApi.SparkBatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archiveUris** | **[String]** | Optional. HCFS URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip. | [optional] 
**args** | **[String]** | Optional. The arguments to pass to the driver. Do not include arguments that can be set as batch properties, such as --conf, since a collision can occur that causes an incorrect batch submission. | [optional] 
**fileUris** | **[String]** | Optional. HCFS URIs of files to be placed in the working directory of each executor. | [optional] 
**jarFileUris** | **[String]** | Optional. HCFS URIs of jar files to add to the classpath of the Spark driver and tasks. | [optional] 
**mainClass** | **String** | Optional. The name of the driver main class. The jar file that contains the class must be in the classpath or specified in jar_file_uris. | [optional] 
**mainJarFileUri** | **String** | Optional. The HCFS URI of the jar file that contains the main class. | [optional] 


