

# DatabaseResourceMetadata

Common model for database resource instance metadata.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availabilityConfiguration** | [**AvailabilityConfiguration**](AvailabilityConfiguration.md) |  |  [optional] |
|**backupConfiguration** | [**BackupConfiguration**](BackupConfiguration.md) |  |  [optional] |
|**backupRun** | [**BackupRun**](BackupRun.md) |  |  [optional] |
|**creationTime** | **String** | The creation time of the resource, i.e. the time when resource is created and recorded in partner service. |  [optional] |
|**currentState** | [**CurrentStateEnum**](#CurrentStateEnum) | Current state of the instance. |  [optional] |
|**customMetadata** | [**CustomMetadataData**](CustomMetadataData.md) |  |  [optional] |
|**entitlements** | [**List&lt;Entitlement&gt;**](Entitlement.md) | Entitlements associated with the resource |  [optional] |
|**expectedState** | [**ExpectedStateEnum**](#ExpectedStateEnum) | The state that the instance is expected to be in. For example, an instance state can transition to UNHEALTHY due to wrong patch update, while the expected state will remain at the HEALTHY. |  [optional] |
|**id** | [**DatabaseResourceId**](DatabaseResourceId.md) |  |  [optional] |
|**instanceType** | [**InstanceTypeEnum**](#InstanceTypeEnum) | The type of the instance. Specified at creation time. |  [optional] |
|**location** | **String** | The resource location. REQUIRED |  [optional] |
|**primaryResourceId** | [**DatabaseResourceId**](DatabaseResourceId.md) |  |  [optional] |
|**product** | [**Product**](Product.md) |  |  [optional] |
|**resourceContainer** | **String** | Closest parent Cloud Resource Manager container of this resource. It must be resource name of a Cloud Resource Manager project with the format of \&quot;/\&quot;, such as \&quot;projects/123\&quot;. For GCP provided resources, number should be project number. |  [optional] |
|**resourceName** | **String** | Required. Different from DatabaseResourceId.unique_id, a resource name can be reused over time. That is, after a resource named \&quot;ABC\&quot; is deleted, the name \&quot;ABC\&quot; can be used to to create a new resource within the same source. Resource name to follow CAIS resource_name format as noted here go/condor-common-datamodel |  [optional] |
|**updationTime** | **String** | The time at which the resource was updated and recorded at partner service. |  [optional] |
|**userLabels** | **Map&lt;String, String&gt;** | User-provided labels, represented as a dictionary where each label is a single key value pair. |  [optional] |



## Enum: CurrentStateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| HEALTHY | &quot;HEALTHY&quot; |
| UNHEALTHY | &quot;UNHEALTHY&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |
| DELETED | &quot;DELETED&quot; |
| STATE_OTHER | &quot;STATE_OTHER&quot; |



## Enum: ExpectedStateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| HEALTHY | &quot;HEALTHY&quot; |
| UNHEALTHY | &quot;UNHEALTHY&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |
| DELETED | &quot;DELETED&quot; |
| STATE_OTHER | &quot;STATE_OTHER&quot; |



## Enum: InstanceTypeEnum

| Name | Value |
|---- | -----|
| INSTANCE_TYPE_UNSPECIFIED | &quot;INSTANCE_TYPE_UNSPECIFIED&quot; |
| SUB_RESOURCE_TYPE_UNSPECIFIED | &quot;SUB_RESOURCE_TYPE_UNSPECIFIED&quot; |
| PRIMARY | &quot;PRIMARY&quot; |
| SECONDARY | &quot;SECONDARY&quot; |
| READ_REPLICA | &quot;READ_REPLICA&quot; |
| OTHER | &quot;OTHER&quot; |
| SUB_RESOURCE_TYPE_PRIMARY | &quot;SUB_RESOURCE_TYPE_PRIMARY&quot; |
| SUB_RESOURCE_TYPE_SECONDARY | &quot;SUB_RESOURCE_TYPE_SECONDARY&quot; |
| SUB_RESOURCE_TYPE_READ_REPLICA | &quot;SUB_RESOURCE_TYPE_READ_REPLICA&quot; |
| SUB_RESOURCE_TYPE_OTHER | &quot;SUB_RESOURCE_TYPE_OTHER&quot; |



