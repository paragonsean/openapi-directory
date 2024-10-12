

# GoogleCloudDataplexV1TaskSparkTaskConfig

User-specified config for running a Spark task.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archiveUris** | **List&lt;String&gt;** | Optional. Cloud Storage URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip. |  [optional] |
|**fileUris** | **List&lt;String&gt;** | Optional. Cloud Storage URIs of files to be placed in the working directory of each executor. |  [optional] |
|**infrastructureSpec** | [**GoogleCloudDataplexV1TaskInfrastructureSpec**](GoogleCloudDataplexV1TaskInfrastructureSpec.md) |  |  [optional] |
|**mainClass** | **String** | The name of the driver&#39;s main class. The jar file that contains the class must be in the default CLASSPATH or specified in jar_file_uris. The execution args are passed in as a sequence of named process arguments (--key&#x3D;value). |  [optional] |
|**mainJarFileUri** | **String** | The Cloud Storage URI of the jar file that contains the main class. The execution args are passed in as a sequence of named process arguments (--key&#x3D;value). |  [optional] |
|**pythonScriptFile** | **String** | The Gcloud Storage URI of the main Python file to use as the driver. Must be a .py file. The execution args are passed in as a sequence of named process arguments (--key&#x3D;value). |  [optional] |
|**sqlScript** | **String** | The query text. The execution args are used to declare a set of script variables (set key&#x3D;\&quot;value\&quot;;). |  [optional] |
|**sqlScriptFile** | **String** | A reference to a query file. This can be the Cloud Storage URI of the query file or it can the path to a SqlScript Content. The execution args are used to declare a set of script variables (set key&#x3D;\&quot;value\&quot;;). |  [optional] |



