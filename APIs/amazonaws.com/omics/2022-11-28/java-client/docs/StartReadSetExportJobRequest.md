

# StartReadSetExportJobRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destination** | **String** | A location for exported files in Amazon S3. |  |
|**roleArn** | **String** | A service role for the job. |  |
|**clientToken** | **String** | To ensure that jobs don&#39;t run multiple times, specify a unique token for each job. |  [optional] |
|**sources** | [**List&lt;ExportReadSet&gt;**](ExportReadSet.md) | The job&#39;s source files. |  |



