

# WirelessV1RatePlan


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the RatePlan resource. |  [optional] |
|**dataEnabled** | **Boolean** | Whether SIMs can use GPRS/3G/4G/LTE data connectivity. |  [optional] |
|**dataLimit** | **Integer** | The total data usage (download and upload combined) in Megabytes that the Network allows during one month on the home network (T-Mobile USA). The metering period begins the day of activation and ends on the same day in the following month. Can be up to 2TB. |  [optional] |
|**dataMetering** | **String** | The model used to meter data usage. Can be: &#x60;payg&#x60; and &#x60;quota-1&#x60;, &#x60;quota-10&#x60;, and &#x60;quota-50&#x60;. Learn more about the available [data metering models](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource#payg-vs-quota-data-plans). |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. |  [optional] |
|**friendlyName** | **String** | The string that you assigned to describe the resource. |  [optional] |
|**internationalRoaming** | **List&lt;String&gt;** | The list of services that SIMs capable of using GPRS/3G/4G/LTE data connectivity can use outside of the United States. Can contain: &#x60;data&#x60; and &#x60;messaging&#x60;. |  [optional] |
|**internationalRoamingDataLimit** | **Integer** | The total data usage (download and upload combined) in Megabytes that the Network allows during one month when roaming outside the United States. Can be up to 2TB. |  [optional] |
|**messagingEnabled** | **Boolean** | Whether SIMs can make, send, and receive SMS using [Commands](https://www.twilio.com/docs/iot/wireless/api/command-resource). |  [optional] |
|**nationalRoamingDataLimit** | **Integer** | The total data usage (download and upload combined) in Megabytes that the Network allows during one month on non-home networks in the United States. The metering period begins the day of activation and ends on the same day in the following month. Can be up to 2TB. |  [optional] |
|**nationalRoamingEnabled** | **Boolean** | Whether SIMs can roam on networks other than the home network (T-Mobile USA) in the United States. See [national roaming](https://www.twilio.com/docs/iot/wireless/api/rateplan-resource#national-roaming). |  [optional] |
|**sid** | **String** | The unique string that we created to identify the RatePlan resource. |  [optional] |
|**uniqueName** | **String** | An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource. |  [optional] |
|**url** | **URI** | The absolute URL of the resource. |  [optional] |
|**voiceEnabled** | **Boolean** | Deprecated. Whether SIMs can make and receive voice calls. |  [optional] |



