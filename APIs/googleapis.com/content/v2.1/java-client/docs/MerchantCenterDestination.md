

# MerchantCenterDestination

\"Merchant Center Destination\" sources can be used to send conversion events from a website using a Google tag directly to a Merchant Center account where the source is created.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributionSettings** | [**AttributionSettings**](AttributionSettings.md) |  |  [optional] |
|**currencyCode** | **String** | Required. Three-letter currency code (ISO 4217). The currency code defines in which currency the conversions sent to this destination will be reported in Merchant Center. |  [optional] |
|**destinationId** | **String** | Output only. Merchant Center Destination ID. |  [optional] [readonly] |
|**displayName** | **String** | Required. Merchant-specified display name for the destination. This is the name that identifies the conversion source within the Merchant Center UI. Limited to 64 characters. |  [optional] |



