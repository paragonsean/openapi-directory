

# Federation

Represents a federation of multiple backend metastores.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendMetastores** | [**Map&lt;String, BackendMetastore&gt;**](BackendMetastore.md) | A map from BackendMetastore rank to BackendMetastores from which the federation service serves metadata at query time. The map key represents the order in which BackendMetastores should be evaluated to resolve database names at query time and should be greater than or equal to zero. A BackendMetastore with a lower number will be evaluated before a BackendMetastore with a higher number. |  [optional] |
|**createTime** | **String** | Output only. The time when the metastore federation was created. |  [optional] [readonly] |
|**endpointUri** | **String** | Output only. The federation endpoint. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | User-defined labels for the metastore federation. |  [optional] |
|**name** | **String** | Immutable. The relative resource name of the federation, of the form: projects/{project_number}/locations/{location_id}/federations/{federation_id}&#x60;. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of the federation. |  [optional] [readonly] |
|**stateMessage** | **String** | Output only. Additional information about the current state of the metastore federation, if available. |  [optional] [readonly] |
|**uid** | **String** | Output only. The globally unique resource identifier of the metastore federation. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The time when the metastore federation was last updated. |  [optional] [readonly] |
|**version** | **String** | Immutable. The Apache Hive metastore version of the federation. All backend metastore versions must be compatible with the federation version. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| UPDATING | &quot;UPDATING&quot; |
| DELETING | &quot;DELETING&quot; |
| ERROR | &quot;ERROR&quot; |



