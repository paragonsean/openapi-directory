

# GoogleCloudRunV2Condition

Defines a status condition for a resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**executionReason** | [**ExecutionReasonEnum**](#ExecutionReasonEnum) | A reason for the execution condition. |  [optional] |
|**lastTransitionTime** | **String** | Last time the condition transitioned from one status to another. |  [optional] |
|**message** | **String** | Human readable message indicating details about the current status. |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | A common (service-level) reason for this condition. |  [optional] |
|**revisionReason** | [**RevisionReasonEnum**](#RevisionReasonEnum) | A reason for the revision condition. |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | How to interpret failures of this condition, one of Error, Warning, Info |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of the condition. |  [optional] |
|**type** | **String** | type is used to communicate the status of the reconciliation process. See also: https://github.com/knative/serving/blob/main/docs/spec/errors.md#error-conditions-and-reporting Types common to all resources include: * \&quot;Ready\&quot;: True when the Resource is ready. |  [optional] |



## Enum: ExecutionReasonEnum

| Name | Value |
|---- | -----|
| EXECUTION_REASON_UNDEFINED | &quot;EXECUTION_REASON_UNDEFINED&quot; |
| JOB_STATUS_SERVICE_POLLING_ERROR | &quot;JOB_STATUS_SERVICE_POLLING_ERROR&quot; |
| NON_ZERO_EXIT_CODE | &quot;NON_ZERO_EXIT_CODE&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| CANCELLING | &quot;CANCELLING&quot; |
| DELETED | &quot;DELETED&quot; |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| COMMON_REASON_UNDEFINED | &quot;COMMON_REASON_UNDEFINED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| REVISION_FAILED | &quot;REVISION_FAILED&quot; |
| PROGRESS_DEADLINE_EXCEEDED | &quot;PROGRESS_DEADLINE_EXCEEDED&quot; |
| CONTAINER_MISSING | &quot;CONTAINER_MISSING&quot; |
| CONTAINER_PERMISSION_DENIED | &quot;CONTAINER_PERMISSION_DENIED&quot; |
| CONTAINER_IMAGE_UNAUTHORIZED | &quot;CONTAINER_IMAGE_UNAUTHORIZED&quot; |
| CONTAINER_IMAGE_AUTHORIZATION_CHECK_FAILED | &quot;CONTAINER_IMAGE_AUTHORIZATION_CHECK_FAILED&quot; |
| ENCRYPTION_KEY_PERMISSION_DENIED | &quot;ENCRYPTION_KEY_PERMISSION_DENIED&quot; |
| ENCRYPTION_KEY_CHECK_FAILED | &quot;ENCRYPTION_KEY_CHECK_FAILED&quot; |
| SECRETS_ACCESS_CHECK_FAILED | &quot;SECRETS_ACCESS_CHECK_FAILED&quot; |
| WAITING_FOR_OPERATION | &quot;WAITING_FOR_OPERATION&quot; |
| IMMEDIATE_RETRY | &quot;IMMEDIATE_RETRY&quot; |
| POSTPONED_RETRY | &quot;POSTPONED_RETRY&quot; |
| INTERNAL | &quot;INTERNAL&quot; |



## Enum: RevisionReasonEnum

| Name | Value |
|---- | -----|
| REVISION_REASON_UNDEFINED | &quot;REVISION_REASON_UNDEFINED&quot; |
| PENDING | &quot;PENDING&quot; |
| RESERVE | &quot;RESERVE&quot; |
| RETIRED | &quot;RETIRED&quot; |
| RETIRING | &quot;RETIRING&quot; |
| RECREATING | &quot;RECREATING&quot; |
| HEALTH_CHECK_CONTAINER_ERROR | &quot;HEALTH_CHECK_CONTAINER_ERROR&quot; |
| CUSTOMIZED_PATH_RESPONSE_PENDING | &quot;CUSTOMIZED_PATH_RESPONSE_PENDING&quot; |
| MIN_INSTANCES_NOT_PROVISIONED | &quot;MIN_INSTANCES_NOT_PROVISIONED&quot; |
| ACTIVE_REVISION_LIMIT_REACHED | &quot;ACTIVE_REVISION_LIMIT_REACHED&quot; |
| NO_DEPLOYMENT | &quot;NO_DEPLOYMENT&quot; |
| HEALTH_CHECK_SKIPPED | &quot;HEALTH_CHECK_SKIPPED&quot; |
| MIN_INSTANCES_WARMING | &quot;MIN_INSTANCES_WARMING&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| SEVERITY_UNSPECIFIED | &quot;SEVERITY_UNSPECIFIED&quot; |
| ERROR | &quot;ERROR&quot; |
| WARNING | &quot;WARNING&quot; |
| INFO | &quot;INFO&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CONDITION_PENDING | &quot;CONDITION_PENDING&quot; |
| CONDITION_RECONCILING | &quot;CONDITION_RECONCILING&quot; |
| CONDITION_FAILED | &quot;CONDITION_FAILED&quot; |
| CONDITION_SUCCEEDED | &quot;CONDITION_SUCCEEDED&quot; |



