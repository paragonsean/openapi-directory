# MotaWordApi.DocumentUpdates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents** | **[File]** | You can add as many files as you want in documents[] parameter. | [optional] 
**schemes** | **String** | JSON string. If your documents have a scheme, as in cases of CSV files, use the same array index keys for &#x60;schemes&#x60; parameter to specify their schemes. See &#x60;Document Schemes&#x60; title in the API documentation. | [optional] 
**sourceLinks** | [**[LinkedSourceDocument]**](LinkedSourceDocument.md) | When provided, we will download the files from these URLs, in addition to files provded in &#x60;documents&#x60; parameter and then save as source documents | [optional] 


