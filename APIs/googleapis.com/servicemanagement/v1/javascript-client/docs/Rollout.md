# ServiceManagementApi.Rollout

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Creation time of the rollout. Readonly. | [optional] 
**createdBy** | **String** | The user who created the Rollout. Readonly. | [optional] 
**deleteServiceStrategy** | **Object** | Strategy used to delete a service. This strategy is a placeholder only used by the system generated rollout to delete a service. | [optional] 
**rolloutId** | **String** | Optional. Unique identifier of this Rollout. Must be no longer than 63 characters and only lower case letters, digits, &#39;.&#39;, &#39;_&#39; and &#39;-&#39; are allowed. If not specified by client, the server will generate one. The generated id will have the form of , where \&quot;date\&quot; is the create date in ISO 8601 format. \&quot;revision number\&quot; is a monotonically increasing positive number that is reset every day for each service. An example of the generated rollout_id is &#39;2016-02-16r1&#39; | [optional] 
**serviceName** | **String** | The name of the service associated with this Rollout. | [optional] 
**status** | **String** | The status of this rollout. Readonly. In case of a failed rollout, the system will automatically rollback to the current Rollout version. Readonly. | [optional] 
**trafficPercentStrategy** | [**TrafficPercentStrategy**](TrafficPercentStrategy.md) |  | [optional] 



## Enum: StatusEnum


* `ROLLOUT_STATUS_UNSPECIFIED` (value: `"ROLLOUT_STATUS_UNSPECIFIED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `SUCCESS` (value: `"SUCCESS"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `FAILED` (value: `"FAILED"`)

* `PENDING` (value: `"PENDING"`)

* `FAILED_ROLLED_BACK` (value: `"FAILED_ROLLED_BACK"`)




