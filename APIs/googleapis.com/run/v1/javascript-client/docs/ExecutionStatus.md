# CloudRunAdminApi.ExecutionStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelledCount** | **Number** | Optional. The number of tasks which reached phase Cancelled. | [optional] 
**completionTime** | **String** | Optional. Represents the time that the execution was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC. +optional | [optional] 
**conditions** | [**[GoogleCloudRunV1Condition]**](GoogleCloudRunV1Condition.md) | Optional. Conditions communicate information about ongoing/complete reconciliation processes that bring the \&quot;spec\&quot; inline with the observed state of the world. Execution-specific conditions include: * &#x60;ResourcesAvailable&#x60;: &#x60;True&#x60; when underlying resources have been provisioned. * &#x60;Started&#x60;: &#x60;True&#x60; when the execution has started to execute. * &#x60;Completed&#x60;: &#x60;True&#x60; when the execution has succeeded. &#x60;False&#x60; when the execution has failed. | [optional] 
**failedCount** | **Number** | Optional. The number of tasks which reached phase Failed. | [optional] 
**logUri** | **String** | Optional. URI where logs for this execution can be found in Cloud Console. | [optional] 
**observedGeneration** | **Number** | Optional. The &#39;generation&#39; of the execution that was last processed by the controller. | [optional] 
**retriedCount** | **Number** | Optional. The number of tasks which have retried at least once. | [optional] 
**runningCount** | **Number** | Optional. The number of actively running tasks. | [optional] 
**startTime** | **String** | Optional. Represents the time that the execution started to run. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC. | [optional] 
**succeededCount** | **Number** | Optional. The number of tasks which reached phase Succeeded. | [optional] 


