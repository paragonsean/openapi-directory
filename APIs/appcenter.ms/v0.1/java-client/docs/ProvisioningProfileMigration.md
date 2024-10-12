

# ProvisioningProfileMigration

Describes the migration schema for a provisioning profile defined in HockeyApp.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bundleId** | **String** | The bundle/application identifier. |  |
|**expiredAt** | **String** | The provisioning profile&#39;s expiration date in RFC 3339 format, i.e. 2017-07-21T17:32:28Z. |  [optional] |
|**isAppex** | **Boolean** | A boolean value that indicates whether the provisioning profile represents an app extension. |  |
|**name** | **String** | The name of the provisioning profile. |  |
|**teamIdentifier** | **String** | The team identifier. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of provisoning profile. |  |
|**udids** | **List&lt;String&gt;** | A list of UDIDs of provisioned devices. |  [optional] |
|**url** | **String** | A provisioning profile URL that indicates where to download it from. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |



