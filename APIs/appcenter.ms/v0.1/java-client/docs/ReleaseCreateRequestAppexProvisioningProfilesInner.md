

# ReleaseCreateRequestAppexProvisioningProfilesInner

An object containing information about an iOS provisioning profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationIdentifier** | **String** | The application identifier. |  |
|**expiredAt** | **String** | The profile&#39;s expiration date in RFC 3339 format, i.e. 2017-07-21T17:32:28Z |  |
|**name** | **String** | The name of the provisioning profile. |  |
|**profileType** | [**ProfileTypeEnum**](#ProfileTypeEnum) |  |  |
|**teamIdentifier** | **String** | The team identifier. |  |
|**udids** | **List&lt;String&gt;** |  |  [optional] |



## Enum: ProfileTypeEnum

| Name | Value |
|---- | -----|
| ADHOC | &quot;adhoc&quot; |
| ENTERPRISE | &quot;enterprise&quot; |
| OTHER | &quot;other&quot; |



