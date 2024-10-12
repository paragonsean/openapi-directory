

# PySparkJob

A Dataproc job for running Apache PySpark (https://spark.apache.org/docs/0.9.0/python-programming-guide.html) applications on YARN.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archiveUris** | **List&lt;String&gt;** | Optional. HCFS URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip. |  [optional] |
|**args** | **List&lt;String&gt;** | Optional. The arguments to pass to the driver. Do not include arguments, such as --conf, that can be set as job properties, since a collision may occur that causes an incorrect job submission. |  [optional] |
|**fileUris** | **List&lt;String&gt;** | Optional. HCFS URIs of files to be placed in the working directory of each executor. Useful for naively parallel tasks. |  [optional] |
|**jarFileUris** | **List&lt;String&gt;** | Optional. HCFS URIs of jar files to add to the CLASSPATHs of the Python driver and tasks. |  [optional] |
|**loggingConfig** | [**LoggingConfig**](LoggingConfig.md) |  |  [optional] |
|**mainPythonFileUri** | **String** | Required. The HCFS URI of the main Python file to use as the driver. Must be a .py file. |  [optional] |
|**properties** | **Map&lt;String, String&gt;** | Optional. A mapping of property names to values, used to configure PySpark. Properties that conflict with values set by the Dataproc API might be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code. |  [optional] |
|**pythonFileUris** | **List&lt;String&gt;** | Optional. HCFS file URIs of Python files to pass to the PySpark framework. Supported file types: .py, .egg, and .zip. |  [optional] |



