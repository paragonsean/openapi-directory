

# RiskMetadata

Risk metadata used for 3DS and risk scoring.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accuracyRadius** | **Integer** | Accuracy radius for specified ipAddress (kilometers). |  [optional] [readonly] |
|**browserData** | [**BrowserData**](BrowserData.md) |  |  [optional] |
|**city** | **String** | City for specified ipAddress. |  [optional] [readonly] |
|**country** | **String** | Country ISO Alpha-2 code for specified ipAddress. |  [optional] [readonly] |
|**deviceVelocity** | **Integer** | Number of transactions for this device (based on fingerprint) in the last 24 hours. |  [optional] [readonly] |
|**distance** | **Integer** | Distance between IP Address and Billing Address geolocation (kilometers). |  [optional] [readonly] |
|**fingerprint** | **String** | The fingerprint. |  [optional] |
|**hasMismatchedBankCountry** | **Boolean** | True if the bank country and geo-IP address are not the same. |  [optional] [readonly] |
|**hasMismatchedBillingAddressCountry** | **Boolean** | True if the billing address country and geo-IP address are not the same. |  [optional] [readonly] |
|**hasMismatchedHolderName** | **Boolean** | True if the customer&#39;s name from billing address and from customer&#39;s primary address are not the same. |  [optional] [readonly] |
|**hasMismatchedTimeZone** | **Boolean** | True if the browser time zone and IP address associated time zone are not the same. |  [optional] [readonly] |
|**httpHeaders** | **Map&lt;String, String&gt;** | The HTTP headers. |  [optional] |
|**ipAddress** | **String** | The customer&#39;s IP. |  [optional] |
|**isHosting** | **Boolean** | True if customer&#39;s ip address is related to hosting. |  [optional] [readonly] |
|**isProxy** | **Boolean** | True if customer&#39;s ip address is related to proxy. |  [optional] [readonly] |
|**isTor** | **Boolean** | True if customer&#39;s ip address is related to TOR. |  [optional] [readonly] |
|**isVpn** | **Boolean** | True if customer&#39;s ip address is related to VPN. |  [optional] [readonly] |
|**isp** | **String** | Internet Service Provider name, if available. |  [optional] [readonly] |
|**latitude** | **Double** | Latitude for specified ipAddress. |  [optional] [readonly] |
|**longitude** | **Double** | Longitude for specified ipAddress. |  [optional] [readonly] |
|**paymentInstrumentVelocity** | **Integer** | Number of transactions for this payment instrument (based on fingerprint) in the last 24 hours. |  [optional] [readonly] |
|**postalCode** | **String** | Postal code for specified ipAddress. |  [optional] [readonly] |
|**region** | **String** | Region for specified ipAddress. |  [optional] [readonly] |
|**score** | **Integer** | Risk score computed per all the factors. |  [optional] [readonly] |
|**timeZone** | **String** | Time zone for specified ipAddress. |  [optional] [readonly] |
|**vpnServiceName** | **String** | VPN service name, if available. |  [optional] [readonly] |



