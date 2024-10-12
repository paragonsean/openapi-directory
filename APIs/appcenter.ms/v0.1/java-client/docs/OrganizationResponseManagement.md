

# OrganizationResponseManagement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**avatarUrl** | **String** | The URL to a user-uploaded Avatar image |  [optional] |
|**createdAt** | **String** | The date when the organization was created |  |
|**displayName** | **String** | The display name of the organization |  |
|**id** | **UUID** | The internal unique id (UUID) of the organization. |  |
|**name** | **String** | The slug name of the organization |  |
|**origin** | [**OriginEnum**](#OriginEnum) | The creation origin of this organization |  |
|**updatedAt** | **String** | The date when the organization was updated |  |
|**featureFlags** | **List&lt;String&gt;** | The feature flags that are enabled for this organization |  [optional] |
|**email** | **String** | The organization email, if the app was synced from HockeyApp |  [optional] |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| APPCENTER | &quot;appcenter&quot; |
| HOCKEYAPP | &quot;hockeyapp&quot; |



