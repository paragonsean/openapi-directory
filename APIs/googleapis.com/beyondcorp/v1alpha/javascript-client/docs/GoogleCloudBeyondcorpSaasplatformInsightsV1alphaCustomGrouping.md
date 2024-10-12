# BeyondCorpApi.GoogleCloudBeyondcorpSaasplatformInsightsV1alphaCustomGrouping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fieldFilter** | **String** | Optional. Filterable parameters to be added to the grouping clause. Available fields could be fetched by calling insight list and get APIs in &#x60;BASIC&#x60; view. &#x60;&#x3D;&#x60; is the only comparison operator supported. &#x60;AND&#x60; is the only logical operator supported. Usage: field_filter&#x3D;\&quot;fieldName1&#x3D;fieldVal1 AND fieldName2&#x3D;fieldVal2\&quot;. NOTE: Only &#x60;AND&#x60; conditions are allowed. NOTE: Use the &#x60;filter_alias&#x60; from &#x60;Insight.Metadata.Field&#x60; message for the filtering the corresponding fields in this filter field. (These expressions are based on the filter language described at https://google.aip.dev/160). | [optional] 
**groupFields** | **[String]** | Required. Fields to be used for grouping. NOTE: Use the &#x60;filter_alias&#x60; from &#x60;Insight.Metadata.Field&#x60; message for declaring the fields to be grouped-by here. | [optional] 


