

# PolicyRequest1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) |  |  |
|**name** | **String** | User-friendly policy name |  |
|**owner** | **Boolean** | Whether policy applies to resource owner or not |  |
|**priority** | **Integer** | Policy priority |  |
|**resources** | **List&lt;String&gt;** | List of resources to apply policy to |  |
|**roles** | **List&lt;String&gt;** | List of roles to apply policy to |  |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| DENY | &quot;Deny&quot; |
| ALLOW | &quot;Allow&quot; |



