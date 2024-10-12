# CloudSpannerApi.ReplicaInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultLeaderLocation** | **Boolean** | If true, this location is designated as the default leader location where leader replicas are placed. See the [region types documentation](https://cloud.google.com/spanner/docs/instances#region_types) for more details. | [optional] 
**location** | **String** | The location of the serving resources, e.g., \&quot;us-central1\&quot;. | [optional] 
**type** | **String** | The type of replica. | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `READ_WRITE` (value: `"READ_WRITE"`)

* `READ_ONLY` (value: `"READ_ONLY"`)

* `WITNESS` (value: `"WITNESS"`)




