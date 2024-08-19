# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaSKAdNetworkConversionValueSchema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applyConversionValues** | **Boolean** | If enabled, the GA SDK will set conversion values using this schema definition, and schema will be exported to any Google Ads accounts linked to this property. If disabled, the GA SDK will not automatically set conversion values, and also the schema will not be exported to Ads. | [optional] 
**name** | **String** | Output only. Resource name of the schema. This will be child of ONLY an iOS stream, and there can be at most one such child under an iOS stream. Format: properties/{property}/dataStreams/{dataStream}/sKAdNetworkConversionValueSchema | [optional] [readonly] 
**postbackWindowOne** | [**GoogleAnalyticsAdminV1alphaPostbackWindow**](GoogleAnalyticsAdminV1alphaPostbackWindow.md) |  | [optional] 
**postbackWindowThree** | [**GoogleAnalyticsAdminV1alphaPostbackWindow**](GoogleAnalyticsAdminV1alphaPostbackWindow.md) |  | [optional] 
**postbackWindowTwo** | [**GoogleAnalyticsAdminV1alphaPostbackWindow**](GoogleAnalyticsAdminV1alphaPostbackWindow.md) |  | [optional] 


