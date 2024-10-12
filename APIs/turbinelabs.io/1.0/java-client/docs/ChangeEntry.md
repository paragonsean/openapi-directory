

# ChangeEntry


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**changeType** | [**ChangeTypeEnum**](#ChangeTypeEnum) | Whether the value was added or removed to the object. |  [optional] |
|**objectKey** | **String** | An ID uniquely identifying the object being changed. |  [optional] |
|**objectType** | [**ObjectTypeEnum**](#ObjectTypeEnum) | The name of the object being being altered. |  [optional] |
|**path** | **String** | A dot-separated / bracket-indexed path to the field changed on the object. |  [optional] |
|**value** | **String** | The value that has been added or removed to the object at the attribute path indicated in path.  |  [optional] |
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



