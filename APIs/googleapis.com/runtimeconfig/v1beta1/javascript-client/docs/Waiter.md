# CloudRuntimeConfigurationApi.Waiter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The instant at which this Waiter resource was created. Adding the value of &#x60;timeout&#x60; to this instant yields the timeout deadline for the waiter. | [optional] 
**done** | **Boolean** | Output only. If the value is &#x60;false&#x60;, it means the waiter is still waiting for one of its conditions to be met. If true, the waiter has finished. If the waiter finished due to a timeout or failure, &#x60;error&#x60; will be set. | [optional] 
**error** | [**Status**](Status.md) |  | [optional] 
**failure** | [**EndCondition**](EndCondition.md) |  | [optional] 
**name** | **String** | The name of the Waiter resource, in the format: projects/[PROJECT_ID]/configs/[CONFIG_NAME]/waiters/[WAITER_NAME] The &#x60;[PROJECT_ID]&#x60; must be a valid Google Cloud project ID, the &#x60;[CONFIG_NAME]&#x60; must be a valid RuntimeConfig resource, the &#x60;[WAITER_NAME]&#x60; must match RFC 1035 segment specification, and the length of &#x60;[WAITER_NAME]&#x60; must be less than 64 bytes. After you create a Waiter resource, you cannot change the resource name. | [optional] 
**success** | [**EndCondition**](EndCondition.md) |  | [optional] 
**timeout** | **String** | [Required] Specifies the timeout of the waiter in seconds, beginning from the instant that &#x60;waiters().create&#x60; method is called. If this time elapses before the success or failure conditions are met, the waiter fails and sets the &#x60;error&#x60; code to &#x60;DEADLINE_EXCEEDED&#x60;. | [optional] 


