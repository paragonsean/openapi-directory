

# AccountTax

The tax settings of a merchant account. All methods require the admin role.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Required. The ID of the account to which these account tax settings belong. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;&#x60;content#accountTax&#x60;\&quot;. |  [optional] |
|**rules** | [**List&lt;AccountTaxTaxRule&gt;**](AccountTaxTaxRule.md) | Tax rules. Updating the tax rules will enable \&quot;US\&quot; taxes (not reversible). Defining no rules is equivalent to not charging tax at all. |  [optional] |



