# CloudRunAdminApi.GoogleCloudRunV2Condition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executionReason** | **String** | A reason for the execution condition. | [optional] 
**lastTransitionTime** | **String** | Last time the condition transitioned from one status to another. | [optional] 
**message** | **String** | Human readable message indicating details about the current status. | [optional] 
**reason** | **String** | A common (service-level) reason for this condition. | [optional] 
**revisionReason** | **String** | A reason for the revision condition. | [optional] 
**severity** | **String** | How to interpret failures of this condition, one of Error, Warning, Info | [optional] 
**state** | **String** | State of the condition. | [optional] 
**type** | **String** | type is used to communicate the status of the reconciliation process. See also: https://github.com/knative/serving/blob/main/docs/spec/errors.md#error-conditions-and-reporting Types common to all resources include: * \&quot;Ready\&quot;: True when the Resource is ready. | [optional] 



## Enum: ExecutionReasonEnum


* `EXECUTION_REASON_UNDEFINED` (value: `"EXECUTION_REASON_UNDEFINED"`)

* `JOB_STATUS_SERVICE_POLLING_ERROR` (value: `"JOB_STATUS_SERVICE_POLLING_ERROR"`)

* `NON_ZERO_EXIT_CODE` (value: `"NON_ZERO_EXIT_CODE"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `CANCELLING` (value: `"CANCELLING"`)

* `DELETED` (value: `"DELETED"`)





## Enum: ReasonEnum


* `COMMON_REASON_UNDEFINED` (value: `"COMMON_REASON_UNDEFINED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `REVISION_FAILED` (value: `"REVISION_FAILED"`)

* `PROGRESS_DEADLINE_EXCEEDED` (value: `"PROGRESS_DEADLINE_EXCEEDED"`)

* `CONTAINER_MISSING` (value: `"CONTAINER_MISSING"`)

* `CONTAINER_PERMISSION_DENIED` (value: `"CONTAINER_PERMISSION_DENIED"`)

* `CONTAINER_IMAGE_UNAUTHORIZED` (value: `"CONTAINER_IMAGE_UNAUTHORIZED"`)

* `CONTAINER_IMAGE_AUTHORIZATION_CHECK_FAILED` (value: `"CONTAINER_IMAGE_AUTHORIZATION_CHECK_FAILED"`)

* `ENCRYPTION_KEY_PERMISSION_DENIED` (value: `"ENCRYPTION_KEY_PERMISSION_DENIED"`)

* `ENCRYPTION_KEY_CHECK_FAILED` (value: `"ENCRYPTION_KEY_CHECK_FAILED"`)

* `SECRETS_ACCESS_CHECK_FAILED` (value: `"SECRETS_ACCESS_CHECK_FAILED"`)

* `WAITING_FOR_OPERATION` (value: `"WAITING_FOR_OPERATION"`)

* `IMMEDIATE_RETRY` (value: `"IMMEDIATE_RETRY"`)

* `POSTPONED_RETRY` (value: `"POSTPONED_RETRY"`)

* `INTERNAL` (value: `"INTERNAL"`)





## Enum: RevisionReasonEnum


* `REVISION_REASON_UNDEFINED` (value: `"REVISION_REASON_UNDEFINED"`)

* `PENDING` (value: `"PENDING"`)

* `RESERVE` (value: `"RESERVE"`)

* `RETIRED` (value: `"RETIRED"`)

* `RETIRING` (value: `"RETIRING"`)

* `RECREATING` (value: `"RECREATING"`)

* `HEALTH_CHECK_CONTAINER_ERROR` (value: `"HEALTH_CHECK_CONTAINER_ERROR"`)

* `CUSTOMIZED_PATH_RESPONSE_PENDING` (value: `"CUSTOMIZED_PATH_RESPONSE_PENDING"`)

* `MIN_INSTANCES_NOT_PROVISIONED` (value: `"MIN_INSTANCES_NOT_PROVISIONED"`)

* `ACTIVE_REVISION_LIMIT_REACHED` (value: `"ACTIVE_REVISION_LIMIT_REACHED"`)

* `NO_DEPLOYMENT` (value: `"NO_DEPLOYMENT"`)

* `HEALTH_CHECK_SKIPPED` (value: `"HEALTH_CHECK_SKIPPED"`)

* `MIN_INSTANCES_WARMING` (value: `"MIN_INSTANCES_WARMING"`)





## Enum: SeverityEnum


* `SEVERITY_UNSPECIFIED` (value: `"SEVERITY_UNSPECIFIED"`)

* `ERROR` (value: `"ERROR"`)

* `WARNING` (value: `"WARNING"`)

* `INFO` (value: `"INFO"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CONDITION_PENDING` (value: `"CONDITION_PENDING"`)

* `CONDITION_RECONCILING` (value: `"CONDITION_RECONCILING"`)

* `CONDITION_FAILED` (value: `"CONDITION_FAILED"`)

* `CONDITION_SUCCEEDED` (value: `"CONDITION_SUCCEEDED"`)




