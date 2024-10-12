

# AccountUserProfile

AccountUserProfiles contains properties of a Campaign Manager user profile. This resource is specifically for managing user profiles, whereas UserProfiles is for accessing the API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Account ID of the user profile. This is a read-only field that can be left blank. |  [optional] |
|**active** | **Boolean** | Whether this user profile is active. This defaults to false, and must be set true on insert for the user profile to be usable. |  [optional] |
|**advertiserFilter** | [**ObjectFilter**](ObjectFilter.md) |  |  [optional] |
|**campaignFilter** | [**ObjectFilter**](ObjectFilter.md) |  |  [optional] |
|**comments** | **String** | Comments for this user profile. |  [optional] |
|**email** | **String** | Email of the user profile. The email addresss must be linked to a Google Account. This field is required on insertion and is read-only after insertion. |  [optional] |
|**id** | **String** | ID of the user profile. This is a read-only, auto-generated field. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#accountUserProfile\&quot;. |  [optional] |
|**locale** | **String** | Locale of the user profile. This is a required field. Acceptable values are: - \&quot;cs\&quot; (Czech) - \&quot;de\&quot; (German) - \&quot;en\&quot; (English) - \&quot;en-GB\&quot; (English United Kingdom) - \&quot;es\&quot; (Spanish) - \&quot;fr\&quot; (French) - \&quot;it\&quot; (Italian) - \&quot;ja\&quot; (Japanese) - \&quot;ko\&quot; (Korean) - \&quot;pl\&quot; (Polish) - \&quot;pt-BR\&quot; (Portuguese Brazil) - \&quot;ru\&quot; (Russian) - \&quot;sv\&quot; (Swedish) - \&quot;tr\&quot; (Turkish) - \&quot;zh-CN\&quot; (Chinese Simplified) - \&quot;zh-TW\&quot; (Chinese Traditional)  |  [optional] |
|**name** | **String** | Name of the user profile. This is a required field. Must be less than 64 characters long, must be globally unique, and cannot contain whitespace or any of the following characters: \&quot;&amp;;&lt;&gt;\&quot;#%,\&quot;. |  [optional] |
|**siteFilter** | [**ObjectFilter**](ObjectFilter.md) |  |  [optional] |
|**subaccountId** | **String** | Subaccount ID of the user profile. This is a read-only field that can be left blank. |  [optional] |
|**traffickerType** | [**TraffickerTypeEnum**](#TraffickerTypeEnum) | Trafficker type of this user profile. This is a read-only field. |  [optional] |
|**userAccessType** | [**UserAccessTypeEnum**](#UserAccessTypeEnum) | User type of the user profile. This is a read-only field that can be left blank. |  [optional] |
|**userRoleFilter** | [**ObjectFilter**](ObjectFilter.md) |  |  [optional] |
|**userRoleId** | **String** | User role ID of the user profile. This is a required field. |  [optional] |



## Enum: TraffickerTypeEnum

| Name | Value |
|---- | -----|
| INTERNAL_NON_TRAFFICKER | &quot;INTERNAL_NON_TRAFFICKER&quot; |
| INTERNAL_TRAFFICKER | &quot;INTERNAL_TRAFFICKER&quot; |
| EXTERNAL_TRAFFICKER | &quot;EXTERNAL_TRAFFICKER&quot; |



## Enum: UserAccessTypeEnum

| Name | Value |
|---- | -----|
| NORMAL_USER | &quot;NORMAL_USER&quot; |
| SUPER_USER | &quot;SUPER_USER&quot; |
| INTERNAL_ADMINISTRATOR | &quot;INTERNAL_ADMINISTRATOR&quot; |
| READ_ONLY_SUPER_USER | &quot;READ_ONLY_SUPER_USER&quot; |



