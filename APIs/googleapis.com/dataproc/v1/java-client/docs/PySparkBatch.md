

# PySparkBatch

A configuration for running an Apache PySpark (https://spark.apache.org/docs/latest/api/python/getting_started/quickstart.html) batch workload.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archiveUris** | **List&lt;String&gt;** | Optional. HCFS URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip. |  [optional] |
|**args** | **List&lt;String&gt;** | Optional. The arguments to pass to the driver. Do not include arguments that can be set as batch properties, such as --conf, since a collision can occur that causes an incorrect batch submission. |  [optional] |
|**fileUris** | **List&lt;String&gt;** | Optional. HCFS URIs of files to be placed in the working directory of each executor. |  [optional] |
|**jarFileUris** | **List&lt;String&gt;** | Optional. HCFS URIs of jar files to add to the classpath of the Spark driver and tasks. |  [optional] |
|**mainPythonFileUri** | **String** | Required. The HCFS URI of the main Python file to use as the Spark driver. Must be a .py file. |  [optional] |
|**pythonFileUris** | **List&lt;String&gt;** | Optional. HCFS file URIs of Python files to pass to the PySpark framework. Supported file types: .py, .egg, and .zip. |  [optional] |



