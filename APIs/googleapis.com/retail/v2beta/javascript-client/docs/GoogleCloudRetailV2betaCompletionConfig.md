# VertexAiSearchForRetailApi.GoogleCloudRetailV2betaCompletionConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowlistInputConfig** | [**GoogleCloudRetailV2betaCompletionDataInputConfig**](GoogleCloudRetailV2betaCompletionDataInputConfig.md) |  | [optional] 
**autoLearning** | **Boolean** | If set to true, the auto learning function is enabled. Auto learning uses user data to generate suggestions using ML techniques. Default value is false. Only after enabling auto learning can users use &#x60;cloud-retail&#x60; data in CompleteQueryRequest. | [optional] 
**denylistInputConfig** | [**GoogleCloudRetailV2betaCompletionDataInputConfig**](GoogleCloudRetailV2betaCompletionDataInputConfig.md) |  | [optional] 
**lastAllowlistImportOperation** | **String** | Output only. Name of the LRO corresponding to the latest allowlist import. Can use GetOperation API to retrieve the latest state of the Long Running Operation. | [optional] [readonly] 
**lastDenylistImportOperation** | **String** | Output only. Name of the LRO corresponding to the latest denylist import. Can use GetOperation API to retrieve the latest state of the Long Running Operation. | [optional] [readonly] 
**lastSuggestionsImportOperation** | **String** | Output only. Name of the LRO corresponding to the latest suggestion terms list import. Can use GetOperation API method to retrieve the latest state of the Long Running Operation. | [optional] [readonly] 
**matchingOrder** | **String** | Specifies the matching order for autocomplete suggestions, e.g., a query consisting of &#39;sh&#39; with &#39;out-of-order&#39; specified would suggest \&quot;women&#39;s shoes\&quot;, whereas a query of &#39;red s&#39; with &#39;exact-prefix&#39; specified would suggest \&quot;red shoes\&quot;. Currently supported values: * &#39;out-of-order&#39; * &#39;exact-prefix&#39; Default value: &#39;exact-prefix&#39;. | [optional] 
**maxSuggestions** | **Number** | The maximum number of autocomplete suggestions returned per term. Default value is 20. If left unset or set to 0, then will fallback to default value. Value range is 1 to 20. | [optional] 
**minPrefixLength** | **Number** | The minimum number of characters needed to be typed in order to get suggestions. Default value is 2. If left unset or set to 0, then will fallback to default value. Value range is 1 to 20. | [optional] 
**name** | **String** | Required. Immutable. Fully qualified name &#x60;projects/_*_/locations/_*_/catalogs/_*_/completionConfig&#x60; | [optional] 
**suggestionsInputConfig** | [**GoogleCloudRetailV2betaCompletionDataInputConfig**](GoogleCloudRetailV2betaCompletionDataInputConfig.md) |  | [optional] 


