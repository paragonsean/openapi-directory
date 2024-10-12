

# AttributeSuggestionsUpdateConfig

<p>Updates the configuration information for the document fields/attributes that you want to base query suggestions on.</p> <p>To deactivate using documents fields for query suggestions, set the mode to <code>INACTIVE</code>. You must also set <code>SuggestionTypes</code> as either <code>QUERY</code> or <code>DOCUMENT_ATTRIBUTES</code> and then call <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/API_GetQuerySuggestions.html\">GetQuerySuggestions</a>. If you set to <code>QUERY</code>, then Amazon Kendra uses the query history to base suggestions on. If you set to <code>DOCUMENT_ATTRIBUTES</code>, then Amazon Kendra uses the contents of document fields to base suggestions on.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**suggestableConfigList** | [**List**](List.md) |  |  [optional] |
|**attributeSuggestionsMode** | [**AttributeSuggestionsMode**](AttributeSuggestionsMode.md) |  |  [optional] |



