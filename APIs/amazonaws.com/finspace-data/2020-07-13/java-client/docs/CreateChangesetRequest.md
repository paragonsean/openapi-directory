

# CreateChangesetRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientToken** | **String** | Idempotence Token for API operations |  [optional] |
|**changeType** | [**ChangeTypeEnum**](#ChangeTypeEnum) | Indicates how the given change will be applied to the dataset. |  |
|**sourceParams** | **Map&lt;String, String&gt;** | Source Parameters of a Changeset |  |
|**formatParams** | **Map&lt;String, String&gt;** | Format Parameters of a Changeset |  |



## Enum: ChangeTypeEnum

| Name | Value |
|---- | -----|
| REPLACE | &quot;REPLACE&quot; |
| APPEND | &quot;APPEND&quot; |
| MODIFY | &quot;MODIFY&quot; |



