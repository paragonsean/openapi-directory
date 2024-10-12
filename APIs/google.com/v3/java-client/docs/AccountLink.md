

# AccountLink

An account link. Represents the link between a Google Ads customer and a Hotel Ads (Hotel Center) account. An account link defines the set of hotels under the Hotel Center account that is linked to the Google Ads customer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountLinkTarget** | [**AccountLinkTarget**](AccountLinkTarget.md) |  |  [optional] |
|**googleAdsCustomerName** | **String** | Required for CREATE requests. The value representing the Google Ads customer ID in the format &#x60;customers/{google_ads_customer_id}&#x60;. For example: &#x60;customers/0123456789&#x60;. Note that the &#x60;googleAdsCustomerName&#x60; field is not returned in responses to GET requests. |  [optional] |
|**name** | **String** | The resource name for the account link in the format &#x60;accounts/{account_id}/accountLinks/{account_link_id}&#x60;. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of the account link. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACCOUNT_LINK_STATUS_UNSPECIFIED | &quot;ACCOUNT_LINK_STATUS_UNSPECIFIED&quot; |
| ACCOUNT_LINK_STATUS_UNKNOWN | &quot;ACCOUNT_LINK_STATUS_UNKNOWN&quot; |
| REQUESTED_FROM_HOTEL_CENTER | &quot;REQUESTED_FROM_HOTEL_CENTER&quot; |
| REQUESTED_FROM_GOOGLE_ADS | &quot;REQUESTED_FROM_GOOGLE_ADS&quot; |
| APPROVED | &quot;APPROVED&quot; |



