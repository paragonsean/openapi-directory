# TwilioWireless.WirelessV1AccountUsageRecord

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the AccountUsageRecord resource. | [optional] 
**commands** | **Object** | An object that describes the aggregated Commands usage for all SIMs during the specified period. See [Commands Usage Object](https://www.twilio.com/docs/iot/wireless/api/account-usagerecord-resource#commands-usage-object). | [optional] 
**data** | **Object** | An object that describes the aggregated Data usage for all SIMs over the period. See [Data Usage Object](https://www.twilio.com/docs/iot/wireless/api/account-usagerecord-resource#data-usage-object). | [optional] 
**period** | **Object** | The time period for which usage is reported. Contains &#x60;start&#x60; and &#x60;end&#x60; properties that describe the period using GMT date-time values specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. | [optional] 


