

# GoogleCloudRunV1Condition

Conditions show the status of reconciliation progress on a given resource. Most resource use a top-level condition type \"Ready\" or \"Completed\" to show overall status with other conditions to checkpoint each stage of reconciliation. Note that if metadata.Generation does not equal status.ObservedGeneration, the conditions shown may not be relevant for the current spec.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lastTransitionTime** | **String** | Optional. Last time the condition transitioned from one status to another. |  [optional] |
|**message** | **String** | Optional. Human readable message indicating details about the current status. |  [optional] |
|**reason** | **String** | Optional. One-word CamelCase reason for the condition&#39;s last transition. These are intended to be stable, unique values which the client may use to trigger error handling logic, whereas messages which may be changed later by the server. |  [optional] |
|**severity** | **String** | Optional. How to interpret this condition. One of Error, Warning, or Info. Conditions of severity Info do not contribute to resource readiness. |  [optional] |
|**status** | **String** | Status of the condition, one of True, False, Unknown. |  [optional] |
|**type** | **String** | type is used to communicate the status of the reconciliation process. Types common to all resources include: * \&quot;Ready\&quot; or \&quot;Completed\&quot;: True when the Resource is ready. |  [optional] |



