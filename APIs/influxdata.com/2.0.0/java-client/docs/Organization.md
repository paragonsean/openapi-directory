

# Organization


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**description** | **String** |  |  [optional] |
|**id** | **String** |  |  [optional] [readonly] |
|**links** | [**OrganizationLinks**](OrganizationLinks.md) |  |  [optional] |
|**name** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) | If inactive the organization is inactive. |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |



