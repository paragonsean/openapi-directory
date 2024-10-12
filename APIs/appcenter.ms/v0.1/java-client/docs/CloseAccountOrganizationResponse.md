

# CloseAccountOrganizationResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**avatarUrl** | **String** | The URL to a user-uploaded Avatar image |  [optional] |
|**createdAt** | **String** | The creation date of this organization |  |
|**displayName** | **String** | The display name of the organization |  |
|**id** | **UUID** | The internal unique id (UUID) of the organization. |  |
|**name** | **String** | The slug name of the organization |  |
|**origin** | [**OriginEnum**](#OriginEnum) | The creation origin of this organization |  |
|**updatedAt** | **String** | The date the organization was last updated at |  |
|**collaboratorsCount** | **BigDecimal** | The number of collaborators from the organization |  |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| APPCENTER | &quot;appcenter&quot; |
| HOCKEYAPP | &quot;hockeyapp&quot; |



