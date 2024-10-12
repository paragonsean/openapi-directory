

# JobStatus


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorResult** | [**ErrorProto**](ErrorProto.md) |  |  [optional] |
|**errors** | [**List&lt;ErrorProto&gt;**](ErrorProto.md) | Output only. The first errors encountered during the running of the job. The final message includes the number of errors that caused the process to stop. Errors here do not necessarily mean that the job has not completed or was unsuccessful. |  [optional] [readonly] |
|**state** | **String** | Output only. Running state of the job. Valid states include &#39;PENDING&#39;, &#39;RUNNING&#39;, and &#39;DONE&#39;. |  [optional] [readonly] |



