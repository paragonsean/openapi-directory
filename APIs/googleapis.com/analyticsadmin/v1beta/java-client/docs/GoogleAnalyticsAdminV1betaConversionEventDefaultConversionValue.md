

# GoogleAnalyticsAdminV1betaConversionEventDefaultConversionValue

Defines a default value/currency for a conversion event. Both value and currency must be provided.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currencyCode** | **String** | When a conversion event for this event_name has no set currency, this currency will be applied as the default. Must be in ISO 4217 currency code format. See https://en.wikipedia.org/wiki/ISO_4217 for more information. |  [optional] |
|**value** | **Double** | This value will be used to populate the value for all conversions of the specified event_name where the event \&quot;value\&quot; parameter is unset. |  [optional] |



