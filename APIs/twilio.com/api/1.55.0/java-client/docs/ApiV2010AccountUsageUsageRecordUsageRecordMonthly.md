

# ApiV2010AccountUsageUsageRecordUsageRecordMonthly


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that accrued the usage. |  [optional] |
|**apiVersion** | **String** | The API version used to create the resource. |  [optional] |
|**asOf** | **String** | Usage records up to date as of this timestamp, formatted as YYYY-MM-DDTHH:MM:SS+00:00. All timestamps are in GMT |  [optional] |
|**category** | **UsageRecordMonthlyEnumCategory** |  |  [optional] |
|**count** | **String** | The number of usage events, such as the number of calls. |  [optional] |
|**countUnit** | **String** | The units in which &#x60;count&#x60; is measured, such as &#x60;calls&#x60; for calls or &#x60;messages&#x60; for SMS. |  [optional] |
|**description** | **String** | A plain-language description of the usage category. |  [optional] |
|**endDate** | **LocalDate** | The last date for which usage is included in the UsageRecord. The date is specified in GMT and formatted as &#x60;YYYY-MM-DD&#x60;. |  [optional] |
|**price** | **BigDecimal** | The total price of the usage in the currency specified in &#x60;price_unit&#x60; and associated with the account. |  [optional] |
|**priceUnit** | **String** | The currency in which &#x60;price&#x60; is measured, in [ISO 4127](https://www.iso.org/iso/home/standards/currency_codes.htm) format, such as &#x60;usd&#x60;, &#x60;eur&#x60;, and &#x60;jpy&#x60;. |  [optional] |
|**startDate** | **LocalDate** | The first date for which usage is included in this UsageRecord. The date is specified in GMT and formatted as &#x60;YYYY-MM-DD&#x60;. |  [optional] |
|**subresourceUris** | **Object** | A list of related resources identified by their URIs. For more information, see [List Subresources](https://www.twilio.com/docs/usage/api/usage-record#list-subresources). |  [optional] |
|**uri** | **String** | The URI of the resource, relative to &#x60;https://api.twilio.com&#x60;. |  [optional] |
|**usage** | **String** | The amount used to bill usage and measured in units described in &#x60;usage_unit&#x60;. |  [optional] |
|**usageUnit** | **String** | The units in which &#x60;usage&#x60; is measured, such as &#x60;minutes&#x60; for calls or &#x60;messages&#x60; for SMS. |  [optional] |



