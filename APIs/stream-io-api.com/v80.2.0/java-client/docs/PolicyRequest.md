

# PolicyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) |  |  [optional] |
|**name** | **String** | User-friendly policy name |  |
|**owner** | **Boolean** | Whether policy applies to resource owner or not |  [optional] |
|**priority** | **Integer** | Policy priority |  |
|**resources** | **List&lt;String&gt;** | List of resources to apply policy to |  [optional] |
|**roles** | **List&lt;String&gt;** | List of roles to apply policy to |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| DENY | &quot;Deny&quot; |
| ALLOW | &quot;Allow&quot; |



