

# GoogleAnalyticsAdminV1alphaAccount

A resource message representing a Google Analytics account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Time when this account was originally created. |  [optional] [readonly] |
|**deleted** | **Boolean** | Output only. Indicates whether this Account is soft-deleted or not. Deleted accounts are excluded from List results unless specifically requested. |  [optional] [readonly] |
|**displayName** | **String** | Required. Human-readable display name for this account. |  [optional] |
|**name** | **String** | Output only. Resource name of this account. Format: accounts/{account} Example: \&quot;accounts/100\&quot; |  [optional] [readonly] |
|**regionCode** | **String** | Country of business. Must be a Unicode CLDR region code. |  [optional] |
|**updateTime** | **String** | Output only. Time when account payload fields were last updated. |  [optional] [readonly] |



