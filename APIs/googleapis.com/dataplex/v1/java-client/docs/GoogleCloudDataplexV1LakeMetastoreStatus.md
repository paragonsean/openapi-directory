

# GoogleCloudDataplexV1LakeMetastoreStatus

Status of Lake and Dataproc Metastore service instance association.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endpoint** | **String** | The URI of the endpoint used to access the Metastore service. |  [optional] |
|**message** | **String** | Additional information about the current status. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Current state of association. |  [optional] |
|**updateTime** | **String** | Last update time of the metastore status of the lake. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| NONE | &quot;NONE&quot; |
| READY | &quot;READY&quot; |
| UPDATING | &quot;UPDATING&quot; |
| ERROR | &quot;ERROR&quot; |



