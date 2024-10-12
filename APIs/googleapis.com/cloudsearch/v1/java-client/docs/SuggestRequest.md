

# SuggestRequest

Request of suggest API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSourceRestrictions** | [**List&lt;DataSourceRestriction&gt;**](DataSourceRestriction.md) | The sources to use for suggestions. If not specified, the data sources are taken from the current search application. NOTE: Suggestions are only supported for the following sources: * Third-party data sources * PredefinedSource.PERSON * PredefinedSource.GOOGLE_DRIVE |  [optional] |
|**query** | **String** | Partial query for which autocomplete suggestions will be shown. For example, if the query is \&quot;sea\&quot;, then the server might return \&quot;season\&quot;, \&quot;search\&quot;, \&quot;seagull\&quot; and so on. |  [optional] |
|**requestOptions** | [**RequestOptions**](RequestOptions.md) |  |  [optional] |



