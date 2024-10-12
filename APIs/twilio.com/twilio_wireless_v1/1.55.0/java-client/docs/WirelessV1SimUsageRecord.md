

# WirelessV1SimUsageRecord


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resource. |  [optional] |
|**commands** | **Object** | An object that describes the SIM&#39;s usage of Commands during the specified period. See [Commands Usage Object](https://www.twilio.com/docs/iot/wireless/api/sim-usagerecord-resource#commands-usage-object). |  [optional] |
|**data** | **Object** | An object that describes the SIM&#39;s data usage during the specified period. See [Data Usage Object](https://www.twilio.com/docs/iot/wireless/api/sim-usagerecord-resource#data-usage-object). |  [optional] |
|**period** | **Object** | The time period for which the usage is reported. Contains &#x60;start&#x60; and &#x60;end&#x60; datetime values given as GMT in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. |  [optional] |
|**simSid** | **String** | The SID of the [Sim resource](https://www.twilio.com/docs/iot/wireless/api/sim-resource) that this Usage Record is for. |  [optional] |



