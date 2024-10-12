

# SupersimV1UsageRecord


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that incurred the usage. |  [optional] |
|**billedUnit** | **String** | The currency in which the billed amounts are measured, specified in the 3 letter ISO 4127 format (e.g. &#x60;USD&#x60;, &#x60;EUR&#x60;, &#x60;JPY&#x60;). This can be null when data_toal_billed is 0 and we do not yet have billing information for the corresponding data usage. Refer to [Data Usage Processing](https://www.twilio.com/docs/iot/supersim/api/usage-record-resource#data-usage-processing) for more details. |  [optional] |
|**dataDownload** | **Long** | Total data downloaded in bytes, aggregated by the query parameters. |  [optional] |
|**dataTotal** | **Long** | Total of data_upload and data_download. |  [optional] |
|**dataTotalBilled** | **BigDecimal** | Total amount in the &#x60;billed_unit&#x60; that was charged for the data uploaded or downloaded. Will return 0 for usage prior to February 1, 2022. Value may be 0 despite &#x60;data_total&#x60; being greater than 0 if the data usage is still being processed by Twilio&#39;s billing system. Refer to [Data Usage Processing](https://www.twilio.com/docs/iot/supersim/api/usage-record-resource#data-usage-processing) for more details. |  [optional] |
|**dataUpload** | **Long** | Total data uploaded in bytes, aggregated by the query parameters. |  [optional] |
|**fleetSid** | **String** | SID of the Fleet resource the usage occurred on. Value will only be present when either a value for the &#x60;Fleet&#x60; query parameter is provided or when UsageRecords are grouped by &#x60;fleet&#x60;. Otherwise, the value will be &#x60;null&#x60;. |  [optional] |
|**isoCountry** | **String** | Alpha-2 ISO Country Code that the usage occurred in. Value will only be present when either a value for the &#x60;IsoCountry&#x60; query parameter is provided or when UsageRecords are grouped by &#x60;isoCountry&#x60;. Otherwise, the value will be &#x60;null&#x60;. |  [optional] |
|**networkSid** | **String** | SID of the Network resource the usage occurred on. Value will only be present when either a value for the &#x60;Network&#x60; query parameter is provided or when UsageRecords are grouped by &#x60;network&#x60;. Otherwise, the value will be &#x60;null&#x60;. |  [optional] |
|**period** | **Object** | The time period for which the usage is reported. The period is represented as a pair of &#x60;start_time&#x60; and &#x60;end_time&#x60; timestamps specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**simSid** | **String** | SID of a Sim resource to which the UsageRecord belongs. Value will only be present when either a value for the &#x60;Sim&#x60; query parameter is provided or when UsageRecords are grouped by &#x60;sim&#x60;. Otherwise, the value will be &#x60;null&#x60;. |  [optional] |



