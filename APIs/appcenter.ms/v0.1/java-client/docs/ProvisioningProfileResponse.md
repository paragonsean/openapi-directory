

# ProvisioningProfileResponse

A response containing information about an iOS provisioning profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appexProfiles** | [**List&lt;ProvisioningProfileResponse&gt;**](ProvisioningProfileResponse.md) | Array of provisioning profiles for any app extensions |  [optional] |
|**provisioningBundleId** | **String** | The bundle identifier associated with the profile. |  [optional] |
|**provisioningProfileName** | **String** | The name of the provisioning profile. |  [optional] |
|**provisioningProfileType** | [**ProvisioningProfileTypeEnum**](#ProvisioningProfileTypeEnum) |  |  |
|**teamIdentifier** | **String** | The team identifier. |  [optional] |
|**udids** | **List&lt;String&gt;** |  |  [optional] |



## Enum: ProvisioningProfileTypeEnum

| Name | Value |
|---- | -----|
| ADHOC | &quot;adhoc&quot; |
| ENTERPRISE | &quot;enterprise&quot; |
| OTHER | &quot;other&quot; |



