

# GoogleAnalyticsAdminV1alphaAccountSummary

A virtual resource representing an overview of an account and all its child GA4 properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | **String** | Resource name of account referred to by this account summary Format: accounts/{account_id} Example: \&quot;accounts/1000\&quot; |  [optional] |
|**displayName** | **String** | Display name for the account referred to in this account summary. |  [optional] |
|**name** | **String** | Resource name for this account summary. Format: accountSummaries/{account_id} Example: \&quot;accountSummaries/1000\&quot; |  [optional] |
|**propertySummaries** | [**List&lt;GoogleAnalyticsAdminV1alphaPropertySummary&gt;**](GoogleAnalyticsAdminV1alphaPropertySummary.md) | List of summaries for child accounts of this account. |  [optional] |



