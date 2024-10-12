

# ReplicaInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultLeaderLocation** | **Boolean** | If true, this location is designated as the default leader location where leader replicas are placed. See the [region types documentation](https://cloud.google.com/spanner/docs/instances#region_types) for more details. |  [optional] |
|**location** | **String** | The location of the serving resources, e.g., \&quot;us-central1\&quot;. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of replica. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| READ_WRITE | &quot;READ_WRITE&quot; |
| READ_ONLY | &quot;READ_ONLY&quot; |
| WITNESS | &quot;WITNESS&quot; |



