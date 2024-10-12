

# GoogleCloudDiscoveryengineV1DocumentProcessingConfig

A singleton resource of DataStore. It's empty when DataStore is created, which defaults to digital parser. The first call to DataStoreService.UpdateDocumentProcessingConfig method will initialize the config.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultParsingConfig** | [**GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfig**](GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfig.md) |  |  [optional] |
|**name** | **String** | The full resource name of the Document Processing Config. Format: &#x60;projects/_*_/locations/_*_/collections/_*_/dataStores/_*_/documentProcessingConfig&#x60;. |  [optional] |
|**parsingConfigOverrides** | [**Map&lt;String, GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfig&gt;**](GoogleCloudDiscoveryengineV1DocumentProcessingConfigParsingConfig.md) | Map from file type to override the default parsing configuration based on the file type. Supported keys: * &#x60;pdf&#x60;: Override parsing config for PDF files, either digital parsing, ocr parsing or layout parsing is supported. * &#x60;html&#x60;: Override parsing config for HTML files, only digital parsing and or layout parsing are supported. * &#x60;docx&#x60;: Override parsing config for DOCX files, only digital parsing and or layout parsing are supported. |  [optional] |



