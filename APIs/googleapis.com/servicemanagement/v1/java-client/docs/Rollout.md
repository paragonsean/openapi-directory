

# Rollout

A rollout resource that defines how service configuration versions are pushed to control plane systems. Typically, you create a new version of the service config, and then create a Rollout to push the service config.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Creation time of the rollout. Readonly. |  [optional] |
|**createdBy** | **String** | The user who created the Rollout. Readonly. |  [optional] |
|**deleteServiceStrategy** | **Object** | Strategy used to delete a service. This strategy is a placeholder only used by the system generated rollout to delete a service. |  [optional] |
|**rolloutId** | **String** | Optional. Unique identifier of this Rollout. Must be no longer than 63 characters and only lower case letters, digits, &#39;.&#39;, &#39;_&#39; and &#39;-&#39; are allowed. If not specified by client, the server will generate one. The generated id will have the form of , where \&quot;date\&quot; is the create date in ISO 8601 format. \&quot;revision number\&quot; is a monotonically increasing positive number that is reset every day for each service. An example of the generated rollout_id is &#39;2016-02-16r1&#39; |  [optional] |
|**serviceName** | **String** | The name of the service associated with this Rollout. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of this rollout. Readonly. In case of a failed rollout, the system will automatically rollback to the current Rollout version. Readonly. |  [optional] |
|**trafficPercentStrategy** | [**TrafficPercentStrategy**](TrafficPercentStrategy.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ROLLOUT_STATUS_UNSPECIFIED | &quot;ROLLOUT_STATUS_UNSPECIFIED&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| SUCCESS | &quot;SUCCESS&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| FAILED | &quot;FAILED&quot; |
| PENDING | &quot;PENDING&quot; |
| FAILED_ROLLED_BACK | &quot;FAILED_ROLLED_BACK&quot; |



