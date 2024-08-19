# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaAttributionSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquisitionConversionEventLookbackWindow** | **String** | Required. The lookback window configuration for acquisition conversion events. The default window size is 30 days. | [optional] 
**adsWebConversionDataExportScope** | **String** | Required. The Conversion Export Scope for data exported to linked Ads Accounts. | [optional] 
**name** | **String** | Output only. Resource name of this attribution settings resource. Format: properties/{property_id}/attributionSettings Example: \&quot;properties/1000/attributionSettings\&quot; | [optional] [readonly] 
**otherConversionEventLookbackWindow** | **String** | Required. The lookback window for all other, non-acquisition conversion events. The default window size is 90 days. | [optional] 
**reportingAttributionModel** | **String** | Required. The reporting attribution model used to calculate conversion credit in this property&#39;s reports. Changing the attribution model will apply to both historical and future data. These changes will be reflected in reports with conversion and revenue data. User and session data will be unaffected. | [optional] 



## Enum: AcquisitionConversionEventLookbackWindowEnum


* `UNSPECIFIED` (value: `"ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_UNSPECIFIED"`)

* `7_DAYS` (value: `"ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_7_DAYS"`)

* `30_DAYS` (value: `"ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_30_DAYS"`)





## Enum: AdsWebConversionDataExportScopeEnum


* `ADS_WEB_CONVERSION_DATA_EXPORT_SCOPE_UNSPECIFIED` (value: `"ADS_WEB_CONVERSION_DATA_EXPORT_SCOPE_UNSPECIFIED"`)

* `NOT_SELECTED_YET` (value: `"NOT_SELECTED_YET"`)

* `PAID_AND_ORGANIC_CHANNELS` (value: `"PAID_AND_ORGANIC_CHANNELS"`)

* `GOOGLE_PAID_CHANNELS` (value: `"GOOGLE_PAID_CHANNELS"`)





## Enum: OtherConversionEventLookbackWindowEnum


* `UNSPECIFIED` (value: `"OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_UNSPECIFIED"`)

* `30_DAYS` (value: `"OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_30_DAYS"`)

* `60_DAYS` (value: `"OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_60_DAYS"`)

* `90_DAYS` (value: `"OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_90_DAYS"`)





## Enum: ReportingAttributionModelEnum


* `REPORTING_ATTRIBUTION_MODEL_UNSPECIFIED` (value: `"REPORTING_ATTRIBUTION_MODEL_UNSPECIFIED"`)

* `PAID_AND_ORGANIC_CHANNELS_DATA_DRIVEN` (value: `"PAID_AND_ORGANIC_CHANNELS_DATA_DRIVEN"`)

* `PAID_AND_ORGANIC_CHANNELS_LAST_CLICK` (value: `"PAID_AND_ORGANIC_CHANNELS_LAST_CLICK"`)

* `GOOGLE_PAID_CHANNELS_LAST_CLICK` (value: `"GOOGLE_PAID_CHANNELS_LAST_CLICK"`)




