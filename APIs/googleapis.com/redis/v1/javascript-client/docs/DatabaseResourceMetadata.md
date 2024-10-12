# GoogleCloudMemorystoreForRedisApi.DatabaseResourceMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availabilityConfiguration** | [**AvailabilityConfiguration**](AvailabilityConfiguration.md) |  | [optional] 
**backupConfiguration** | [**BackupConfiguration**](BackupConfiguration.md) |  | [optional] 
**backupRun** | [**BackupRun**](BackupRun.md) |  | [optional] 
**creationTime** | **String** | The creation time of the resource, i.e. the time when resource is created and recorded in partner service. | [optional] 
**currentState** | **String** | Current state of the instance. | [optional] 
**customMetadata** | [**CustomMetadataData**](CustomMetadataData.md) |  | [optional] 
**entitlements** | [**[Entitlement]**](Entitlement.md) | Entitlements associated with the resource | [optional] 
**expectedState** | **String** | The state that the instance is expected to be in. For example, an instance state can transition to UNHEALTHY due to wrong patch update, while the expected state will remain at the HEALTHY. | [optional] 
**id** | [**DatabaseResourceId**](DatabaseResourceId.md) |  | [optional] 
**instanceType** | **String** | The type of the instance. Specified at creation time. | [optional] 
**location** | **String** | The resource location. REQUIRED | [optional] 
**primaryResourceId** | [**DatabaseResourceId**](DatabaseResourceId.md) |  | [optional] 
**product** | [**Product**](Product.md) |  | [optional] 
**resourceContainer** | **String** | Closest parent Cloud Resource Manager container of this resource. It must be resource name of a Cloud Resource Manager project with the format of \&quot;/\&quot;, such as \&quot;projects/123\&quot;. For GCP provided resources, number should be project number. | [optional] 
**resourceName** | **String** | Required. Different from DatabaseResourceId.unique_id, a resource name can be reused over time. That is, after a resource named \&quot;ABC\&quot; is deleted, the name \&quot;ABC\&quot; can be used to to create a new resource within the same source. Resource name to follow CAIS resource_name format as noted here go/condor-common-datamodel | [optional] 
**updationTime** | **String** | The time at which the resource was updated and recorded at partner service. | [optional] 
**userLabels** | **{String: String}** | User-provided labels, represented as a dictionary where each label is a single key value pair. | [optional] 



## Enum: CurrentStateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `HEALTHY` (value: `"HEALTHY"`)

* `UNHEALTHY` (value: `"UNHEALTHY"`)

* `SUSPENDED` (value: `"SUSPENDED"`)

* `DELETED` (value: `"DELETED"`)

* `STATE_OTHER` (value: `"STATE_OTHER"`)





## Enum: ExpectedStateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `HEALTHY` (value: `"HEALTHY"`)

* `UNHEALTHY` (value: `"UNHEALTHY"`)

* `SUSPENDED` (value: `"SUSPENDED"`)

* `DELETED` (value: `"DELETED"`)

* `STATE_OTHER` (value: `"STATE_OTHER"`)





## Enum: InstanceTypeEnum


* `INSTANCE_TYPE_UNSPECIFIED` (value: `"INSTANCE_TYPE_UNSPECIFIED"`)

* `SUB_RESOURCE_TYPE_UNSPECIFIED` (value: `"SUB_RESOURCE_TYPE_UNSPECIFIED"`)

* `PRIMARY` (value: `"PRIMARY"`)

* `SECONDARY` (value: `"SECONDARY"`)

* `READ_REPLICA` (value: `"READ_REPLICA"`)

* `OTHER` (value: `"OTHER"`)

* `SUB_RESOURCE_TYPE_PRIMARY` (value: `"SUB_RESOURCE_TYPE_PRIMARY"`)

* `SUB_RESOURCE_TYPE_SECONDARY` (value: `"SUB_RESOURCE_TYPE_SECONDARY"`)

* `SUB_RESOURCE_TYPE_READ_REPLICA` (value: `"SUB_RESOURCE_TYPE_READ_REPLICA"`)

* `SUB_RESOURCE_TYPE_OTHER` (value: `"SUB_RESOURCE_TYPE_OTHER"`)




