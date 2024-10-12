

# Filter


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**absoluteMatchOnly** | **Boolean** | If set this will return ChangeEntry values with a path that matches the attribute_path property exactly.  |  [optional] |
|**actorKey** | **String** | The user who made the change. |  [optional] |
|**attributePath** | **String** | A dot-separated / bracket-indexed path to the field changed on the object. &#39;%&#39; may be used as a wildcard.  |  [optional] |
|**attributeValue** | **String** | The value that has been added or removed to the object at the attribute path indicated in path.  |  [optional] |
|**changeTxn** | **String** | A unique identifier for all this transaction. It is shared by all attribute updates within a change.  |  [optional] |
|**changeType** | [**ChangeTypeEnum**](#ChangeTypeEnum) | Whether the value was added or removed to the object. |  [optional] |
|**excludeEmptyValues** | **Boolean** | If set this will exclude ChangeEntry records that save the addition or removal of an empty value.  |  [optional] |
|**negativeMatch** | **Boolean** | If set this filter will match the all ChangeEntry records that do NOT meet the constraints laid out in this Filter object.  |  [optional] |
|**objectKey** | **String** | An ID uniquely identifying the object being changed. |  [optional] |
|**objectType** | [**ObjectTypeEnum**](#ObjectTypeEnum) | The name of the object being being altered. |  [optional] |
|**orgKey** | **String** | The organization the objects being updated belong to. |  [optional] |
|**timeRange** | [**TimeRange**](TimeRange.md) |  |  [optional] |
|**zoneKey** | **String** | The zone this object is located in. |  [optional] |



## Enum: ChangeTypeEnum

| Name | Value |
|---- | -----|
| ADDITION | &quot;addition&quot; |
| REMOVAL | &quot;removal&quot; |



## Enum: ObjectTypeEnum

| Name | Value |
|---- | -----|
| ORG | &quot;org&quot; |
| USER | &quot;user&quot; |
| ZONE | &quot;zone&quot; |
| PROXY | &quot;proxy&quot; |
| DOMAIN | &quot;domain&quot; |
| ROUTE | &quot;route&quot; |
| SHARED_RULES | &quot;shared_rules&quot; |
| CLUSTER | &quot;cluster&quot; |



