

# AvailableVendorsFilter


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**corporateId** | **BigDecimal** | Corporate account ID to filter for vendor authorization |  [optional] |
|**manualWorkPermission** | **Boolean** | Filter vendors for manual work permission |  [optional] |
|**sourceLanguage** | **String** | Source language code |  [optional] |
|**targetLanguages** | **List&lt;String&gt;** | List of target language codes. |  [optional] |
|**types** | [**List&lt;TypesEnum&gt;**](#List&lt;TypesEnum&gt;) | List of vendor types |  [optional] |



## Enum: List&lt;TypesEnum&gt;

| Name | Value |
|---- | -----|
| TRANSLATOR | &quot;translator&quot; |
| PROOFREADER | &quot;proofreader&quot; |
| BOTH | &quot;both&quot; |



