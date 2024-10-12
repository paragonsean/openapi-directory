# TravelPartnerApi.AccountLink

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountLinkTarget** | [**AccountLinkTarget**](AccountLinkTarget.md) |  | [optional] 
**googleAdsCustomerName** | **String** | Required for CREATE requests. The value representing the Google Ads customer ID in the format &#x60;customers/{google_ads_customer_id}&#x60;. For example: &#x60;customers/0123456789&#x60;. Note that the &#x60;googleAdsCustomerName&#x60; field is not returned in responses to GET requests. | [optional] 
**name** | **String** | The resource name for the account link in the format &#x60;accounts/{account_id}/accountLinks/{account_link_id}&#x60;. | [optional] 
**status** | **String** | The current status of the account link. | [optional] 



## Enum: StatusEnum


* `ACCOUNT_LINK_STATUS_UNSPECIFIED` (value: `"ACCOUNT_LINK_STATUS_UNSPECIFIED"`)

* `ACCOUNT_LINK_STATUS_UNKNOWN` (value: `"ACCOUNT_LINK_STATUS_UNKNOWN"`)

* `REQUESTED_FROM_HOTEL_CENTER` (value: `"REQUESTED_FROM_HOTEL_CENTER"`)

* `REQUESTED_FROM_GOOGLE_ADS` (value: `"REQUESTED_FROM_GOOGLE_ADS"`)

* `APPROVED` (value: `"APPROVED"`)




