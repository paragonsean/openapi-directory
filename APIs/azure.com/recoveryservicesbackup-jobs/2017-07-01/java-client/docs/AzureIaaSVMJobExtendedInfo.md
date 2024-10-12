

# AzureIaaSVMJobExtendedInfo

Azure IaaS VM workload-specific additional information for job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dynamicErrorMessage** | **String** | Non localized error message on job execution. |  [optional] |
|**progressPercentage** | **Double** | Indicates progress of the job. Null if it has not started or completed. |  [optional] |
|**propertyBag** | **Map&lt;String, String&gt;** | Job properties. |  [optional] |
|**tasksList** | [**List&lt;AzureIaaSVMJobTaskDetails&gt;**](AzureIaaSVMJobTaskDetails.md) | List of tasks associated with this job. |  [optional] |



