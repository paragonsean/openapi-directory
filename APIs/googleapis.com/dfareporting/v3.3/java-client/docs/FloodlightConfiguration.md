

# FloodlightConfiguration

Contains properties of a Floodlight configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Account ID of this floodlight configuration. This is a read-only field that can be left blank. |  [optional] |
|**advertiserId** | **String** | Advertiser ID of the parent advertiser of this floodlight configuration. |  [optional] |
|**advertiserIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**analyticsDataSharingEnabled** | **Boolean** | Whether advertiser data is shared with Google Analytics. |  [optional] |
|**customViewabilityMetric** | [**CustomViewabilityMetric**](CustomViewabilityMetric.md) |  |  [optional] |
|**exposureToConversionEnabled** | **Boolean** | Whether the exposure-to-conversion report is enabled. This report shows detailed pathway information on up to 10 of the most recent ad exposures seen by a user before converting. |  [optional] |
|**firstDayOfWeek** | [**FirstDayOfWeekEnum**](#FirstDayOfWeekEnum) | Day that will be counted as the first day of the week in reports. This is a required field. |  [optional] |
|**id** | **String** | ID of this floodlight configuration. This is a read-only, auto-generated field. |  [optional] |
|**idDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**inAppAttributionTrackingEnabled** | **Boolean** | Whether in-app attribution tracking is enabled. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#floodlightConfiguration\&quot;. |  [optional] |
|**lookbackConfiguration** | [**LookbackConfiguration**](LookbackConfiguration.md) |  |  [optional] |
|**naturalSearchConversionAttributionOption** | [**NaturalSearchConversionAttributionOptionEnum**](#NaturalSearchConversionAttributionOptionEnum) | Types of attribution options for natural search conversions. |  [optional] |
|**omnitureSettings** | [**OmnitureSettings**](OmnitureSettings.md) |  |  [optional] |
|**subaccountId** | **String** | Subaccount ID of this floodlight configuration. This is a read-only field that can be left blank. |  [optional] |
|**tagSettings** | [**TagSettings**](TagSettings.md) |  |  [optional] |
|**thirdPartyAuthenticationTokens** | [**List&lt;ThirdPartyAuthenticationToken&gt;**](ThirdPartyAuthenticationToken.md) | List of third-party authentication tokens enabled for this configuration. |  [optional] |
|**userDefinedVariableConfigurations** | [**List&lt;UserDefinedVariableConfiguration&gt;**](UserDefinedVariableConfiguration.md) | List of user defined variables enabled for this configuration. |  [optional] |



## Enum: FirstDayOfWeekEnum

| Name | Value |
|---- | -----|
| MONDAY | &quot;MONDAY&quot; |
| SUNDAY | &quot;SUNDAY&quot; |



## Enum: NaturalSearchConversionAttributionOptionEnum

| Name | Value |
|---- | -----|
| EXCLUDE_NATURAL_SEARCH_CONVERSION_ATTRIBUTION | &quot;EXCLUDE_NATURAL_SEARCH_CONVERSION_ATTRIBUTION&quot; |
| INCLUDE_NATURAL_SEARCH_CONVERSION_ATTRIBUTION | &quot;INCLUDE_NATURAL_SEARCH_CONVERSION_ATTRIBUTION&quot; |
| INCLUDE_NATURAL_SEARCH_TIERED_CONVERSION_ATTRIBUTION | &quot;INCLUDE_NATURAL_SEARCH_TIERED_CONVERSION_ATTRIBUTION&quot; |



