# CloudRunAdminApi.JobCondition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lastTransitionTime** | **String** | Optional. Last time the condition transitioned from one status to another. | [optional] 
**message** | **String** | Optional. Human readable message indicating details about the current status. | [optional] 
**reason** | **String** | Optional. One-word CamelCase reason for the condition&#39;s last transition. | [optional] 
**severity** | **String** | Optional. How to interpret failures of this condition, one of Error, Warning, Info | [optional] 
**status** | **String** | Required. Status of the condition, one of True, False, Unknown. | [optional] 
**type** | **String** | Required. Type is used to communicate the status of the reconciliation process. See also: https://github.com/knative/serving/blob/main/docs/spec/errors.md#error-conditions-and-reporting Types include: * \&quot;Completed\&quot;: True when the Job has successfully completed. * \&quot;Started\&quot;: True when the Job has successfully started running. * \&quot;ResourcesAvailable\&quot;: True when underlying resources have been provisioned. | [optional] 


