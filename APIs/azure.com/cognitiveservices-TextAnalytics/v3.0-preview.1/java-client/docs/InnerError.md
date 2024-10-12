

# InnerError


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | Error code. |  |
|**details** | **Map&lt;String, String&gt;** | Error details. |  [optional] |
|**innerError** | [**InnerError**](InnerError.md) |  |  [optional] |
|**message** | **String** | Error message. |  |
|**target** | **String** | Error target. |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| INVALID_PARAMETER_VALUE | &quot;invalidParameterValue&quot; |
| INVALID_REQUEST_BODY_FORMAT | &quot;invalidRequestBodyFormat&quot; |
| EMPTY_REQUEST | &quot;emptyRequest&quot; |
| MISSING_INPUT_RECORDS | &quot;missingInputRecords&quot; |
| INVALID_DOCUMENT | &quot;invalidDocument&quot; |
| MODEL_VERSION_INCORRECT | &quot;modelVersionIncorrect&quot; |
| INVALID_DOCUMENT_BATCH | &quot;invalidDocumentBatch&quot; |
| UNSUPPORTED_LANGUAGE_CODE | &quot;unsupportedLanguageCode&quot; |
| INVALID_COUNTRY_HINT | &quot;invalidCountryHint&quot; |



