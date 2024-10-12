# AmazonConnectCustomerProfiles.ListWorkflowsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflowType** | **String** | The type of workflow. The only supported value is APPFLOW_INTEGRATION. | [optional] 
**status** | **String** | Status of workflow execution. | [optional] 
**queryStartDate** | **Date** | Retrieve workflows started after timestamp. | [optional] 
**queryEndDate** | **Date** | Retrieve workflows ended after timestamp. | [optional] 



## Enum: WorkflowTypeEnum


* `APPFLOW_INTEGRATION` (value: `"APPFLOW_INTEGRATION"`)





## Enum: StatusEnum


* `NOT_STARTED` (value: `"NOT_STARTED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `COMPLETE` (value: `"COMPLETE"`)

* `FAILED` (value: `"FAILED"`)

* `SPLIT` (value: `"SPLIT"`)

* `RETRY` (value: `"RETRY"`)

* `CANCELLED` (value: `"CANCELLED"`)




