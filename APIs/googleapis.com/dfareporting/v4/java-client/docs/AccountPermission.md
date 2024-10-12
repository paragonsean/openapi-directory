

# AccountPermission

AccountPermissions contains information about a particular account permission. Some features of Campaign Manager require an account permission to be present in the account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountProfiles** | [**List&lt;AccountProfilesEnum&gt;**](#List&lt;AccountProfilesEnum&gt;) | Account profiles associated with this account permission. Possible values are: - \&quot;ACCOUNT_PROFILE_BASIC\&quot; - \&quot;ACCOUNT_PROFILE_STANDARD\&quot;  |  [optional] |
|**id** | **String** | ID of this account permission. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#accountPermission\&quot;. |  [optional] |
|**level** | [**LevelEnum**](#LevelEnum) | Administrative level required to enable this account permission. |  [optional] |
|**name** | **String** | Name of this account permission. |  [optional] |
|**permissionGroupId** | **String** | Permission group of this account permission. |  [optional] |



## Enum: List&lt;AccountProfilesEnum&gt;

| Name | Value |
|---- | -----|
| BASIC | &quot;ACCOUNT_PROFILE_BASIC&quot; |
| STANDARD | &quot;ACCOUNT_PROFILE_STANDARD&quot; |



## Enum: LevelEnum

| Name | Value |
|---- | -----|
| USER | &quot;USER&quot; |
| ADMINISTRATOR | &quot;ADMINISTRATOR&quot; |



