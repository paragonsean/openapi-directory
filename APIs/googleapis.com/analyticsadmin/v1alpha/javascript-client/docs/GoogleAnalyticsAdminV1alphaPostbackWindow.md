# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaPostbackWindow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversionValues** | [**[GoogleAnalyticsAdminV1alphaConversionValues]**](GoogleAnalyticsAdminV1alphaConversionValues.md) | Ordering of the repeated field will be used to prioritize the conversion value settings. Lower indexed entries are prioritized higher. The first conversion value setting that evaluates to true will be selected. It must have at least one entry if enable_postback_window_settings is set to true. It can have maximum of 128 entries. | [optional] 
**postbackWindowSettingsEnabled** | **Boolean** | If enable_postback_window_settings is true, conversion_values must be populated and will be used for determining when and how to set the Conversion Value on a client device and exporting schema to linked Ads accounts. If false, the settings are not used, but are retained in case they may be used in the future. This must always be true for postback_window_one. | [optional] 


