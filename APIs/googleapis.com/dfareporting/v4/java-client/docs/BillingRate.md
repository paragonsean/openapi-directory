

# BillingRate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currencyCode** | **String** | Billing currency code in ISO 4217 format. |  [optional] |
|**endDate** | **String** | End date of this billing rate. |  [optional] |
|**id** | **String** | ID of this billing rate. |  [optional] |
|**name** | **String** | Name of this billing rate. This must be less than 256 characters long. |  [optional] |
|**rateInMicros** | **String** | Flat rate in micros of this billing rate. This cannot co-exist with tiered rate. |  [optional] |
|**startDate** | **String** | Start date of this billing rate. |  [optional] |
|**tieredRates** | [**List&lt;BillingRateTieredRate&gt;**](BillingRateTieredRate.md) | Tiered rate of this billing rate. This cannot co-exist with flat rate. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of this billing rate. |  [optional] |
|**unitOfMeasure** | [**UnitOfMeasureEnum**](#UnitOfMeasureEnum) | Unit of measure for this billing rate. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AD_SERVING | &quot;AD_SERVING&quot; |
| CLICKS | &quot;CLICKS&quot; |
| MINIMUM_SERVICE | &quot;MINIMUM_SERVICE&quot; |
| PATH_TO_CONVERSION | &quot;PATH_TO_CONVERSION&quot; |
| RICH_MEDIA_INPAGE | &quot;RICH_MEDIA_INPAGE&quot; |
| RICH_MEDIA_EXPANDING | &quot;RICH_MEDIA_EXPANDING&quot; |
| RICH_MEDIA_FLOATING | &quot;RICH_MEDIA_FLOATING&quot; |
| RICH_MEDIA_VIDEO | &quot;RICH_MEDIA_VIDEO&quot; |
| RICH_MEDIA_TEASER | &quot;RICH_MEDIA_TEASER&quot; |
| RICH_MEDIA_VPAID | &quot;RICH_MEDIA_VPAID&quot; |
| INSTREAM_VIDEO | &quot;INSTREAM_VIDEO&quot; |
| PIXEL | &quot;PIXEL&quot; |
| TRACKING | &quot;TRACKING&quot; |
| TRAFFICKING_FEATURE | &quot;TRAFFICKING_FEATURE&quot; |
| CUSTOM_REPORTS | &quot;CUSTOM_REPORTS&quot; |
| EXPOSURE_TO_CONVERSION | &quot;EXPOSURE_TO_CONVERSION&quot; |
| DATA_TRANSFER | &quot;DATA_TRANSFER&quot; |
| DATA_TRANSFER_SETUP | &quot;DATA_TRANSFER_SETUP&quot; |
| STARTUP | &quot;STARTUP&quot; |
| STATEMENT_OF_WORK | &quot;STATEMENT_OF_WORK&quot; |
| PROVIDED_LIST | &quot;PROVIDED_LIST&quot; |
| PROVIDED_LIST_SETUP | &quot;PROVIDED_LIST_SETUP&quot; |
| ENHANCED_FORMATS | &quot;ENHANCED_FORMATS&quot; |
| TRACKING_AD_IMPRESSIONS | &quot;TRACKING_AD_IMPRESSIONS&quot; |
| TRACKING_AD_CLICKS | &quot;TRACKING_AD_CLICKS&quot; |
| NIELSEN_DIGITAL_AD_RATINGS_FEE | &quot;NIELSEN_DIGITAL_AD_RATINGS_FEE&quot; |
| INSTREAM_VIDEO_REDIRECT | &quot;INSTREAM_VIDEO_REDIRECT&quot; |
| INSTREAM_VIDEO_VPAID | &quot;INSTREAM_VIDEO_VPAID&quot; |
| DISPLAY_AD_SERVING | &quot;DISPLAY_AD_SERVING&quot; |
| VIDEO_AD_SERVING | &quot;VIDEO_AD_SERVING&quot; |
| AUDIO_AD_SERVING | &quot;AUDIO_AD_SERVING&quot; |
| ADVANCED_DISPLAY_AD_SERVING | &quot;ADVANCED_DISPLAY_AD_SERVING&quot; |



## Enum: UnitOfMeasureEnum

| Name | Value |
|---- | -----|
| CPM | &quot;CPM&quot; |
| CPC | &quot;CPC&quot; |
| EA | &quot;EA&quot; |
| P2_C | &quot;P2C&quot; |



