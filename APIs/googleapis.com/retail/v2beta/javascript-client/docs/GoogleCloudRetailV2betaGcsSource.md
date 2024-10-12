# VertexAiSearchForRetailApi.GoogleCloudRetailV2betaGcsSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataSchema** | **String** | The schema to use when parsing the data from the source. Supported values for product imports: * &#x60;product&#x60; (default): One JSON Product per line. Each product must have a valid Product.id. * &#x60;product_merchant_center&#x60;: See [Importing catalog data from Merchant Center](https://cloud.google.com/retail/recommendations-ai/docs/upload-catalog#mc). Supported values for user events imports: * &#x60;user_event&#x60; (default): One JSON UserEvent per line. * &#x60;user_event_ga360&#x60;: Using https://support.google.com/analytics/answer/3437719. Supported values for control imports: * &#x60;control&#x60; (default): One JSON Control per line. Supported values for catalog attribute imports: * &#x60;catalog_attribute&#x60; (default): One CSV CatalogAttribute per line. | [optional] 
**inputUris** | **[String]** | Required. Google Cloud Storage URIs to input files. URI can be up to 2000 characters long. URIs can match the full object path (for example, &#x60;gs://bucket/directory/object.json&#x60;) or a pattern matching one or more files, such as &#x60;gs://bucket/directory/_*.json&#x60;. A request can contain at most 100 files, and each file can be up to 2 GB. See [Importing product information](https://cloud.google.com/retail/recommendations-ai/docs/upload-catalog) for the expected file format and setup instructions. | [optional] 


