

# SparkRBatch

A configuration for running an Apache SparkR (https://spark.apache.org/docs/latest/sparkr.html) batch workload.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archiveUris** | **List&lt;String&gt;** | Optional. HCFS URIs of archives to be extracted into the working directory of each executor. Supported file types: .jar, .tar, .tar.gz, .tgz, and .zip. |  [optional] |
|**args** | **List&lt;String&gt;** | Optional. The arguments to pass to the Spark driver. Do not include arguments that can be set as batch properties, such as --conf, since a collision can occur that causes an incorrect batch submission. |  [optional] |
|**fileUris** | **List&lt;String&gt;** | Optional. HCFS URIs of files to be placed in the working directory of each executor. |  [optional] |
|**mainRFileUri** | **String** | Required. The HCFS URI of the main R file to use as the driver. Must be a .R or .r file. |  [optional] |



