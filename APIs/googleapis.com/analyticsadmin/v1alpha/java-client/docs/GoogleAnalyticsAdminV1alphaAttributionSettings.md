

# GoogleAnalyticsAdminV1alphaAttributionSettings

The attribution settings used for a given property. This is a singleton resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acquisitionConversionEventLookbackWindow** | [**AcquisitionConversionEventLookbackWindowEnum**](#AcquisitionConversionEventLookbackWindowEnum) | Required. The lookback window configuration for acquisition conversion events. The default window size is 30 days. |  [optional] |
|**adsWebConversionDataExportScope** | [**AdsWebConversionDataExportScopeEnum**](#AdsWebConversionDataExportScopeEnum) | Required. The Conversion Export Scope for data exported to linked Ads Accounts. |  [optional] |
|**name** | **String** | Output only. Resource name of this attribution settings resource. Format: properties/{property_id}/attributionSettings Example: \&quot;properties/1000/attributionSettings\&quot; |  [optional] [readonly] |
|**otherConversionEventLookbackWindow** | [**OtherConversionEventLookbackWindowEnum**](#OtherConversionEventLookbackWindowEnum) | Required. The lookback window for all other, non-acquisition conversion events. The default window size is 90 days. |  [optional] |
|**reportingAttributionModel** | [**ReportingAttributionModelEnum**](#ReportingAttributionModelEnum) | Required. The reporting attribution model used to calculate conversion credit in this property&#39;s reports. Changing the attribution model will apply to both historical and future data. These changes will be reflected in reports with conversion and revenue data. User and session data will be unaffected. |  [optional] |



## Enum: AcquisitionConversionEventLookbackWindowEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_UNSPECIFIED&quot; |
| _7_DAYS | &quot;ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_7_DAYS&quot; |
| _30_DAYS | &quot;ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_30_DAYS&quot; |



## Enum: AdsWebConversionDataExportScopeEnum

| Name | Value |
|---- | -----|
| ADS_WEB_CONVERSION_DATA_EXPORT_SCOPE_UNSPECIFIED | &quot;ADS_WEB_CONVERSION_DATA_EXPORT_SCOPE_UNSPECIFIED&quot; |
| NOT_SELECTED_YET | &quot;NOT_SELECTED_YET&quot; |
| PAID_AND_ORGANIC_CHANNELS | &quot;PAID_AND_ORGANIC_CHANNELS&quot; |
| GOOGLE_PAID_CHANNELS | &quot;GOOGLE_PAID_CHANNELS&quot; |



## Enum: OtherConversionEventLookbackWindowEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_UNSPECIFIED&quot; |
| _30_DAYS | &quot;OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_30_DAYS&quot; |
| _60_DAYS | &quot;OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_60_DAYS&quot; |
| _90_DAYS | &quot;OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_90_DAYS&quot; |



## Enum: ReportingAttributionModelEnum

| Name | Value |
|---- | -----|
| REPORTING_ATTRIBUTION_MODEL_UNSPECIFIED | &quot;REPORTING_ATTRIBUTION_MODEL_UNSPECIFIED&quot; |
| PAID_AND_ORGANIC_CHANNELS_DATA_DRIVEN | &quot;PAID_AND_ORGANIC_CHANNELS_DATA_DRIVEN&quot; |
| PAID_AND_ORGANIC_CHANNELS_LAST_CLICK | &quot;PAID_AND_ORGANIC_CHANNELS_LAST_CLICK&quot; |
| GOOGLE_PAID_CHANNELS_LAST_CLICK | &quot;GOOGLE_PAID_CHANNELS_LAST_CLICK&quot; |



