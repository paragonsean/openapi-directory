

# GoogleCloudDiscoveryengineV1alphaWidgetConfig

WidgetConfig captures configs at the Widget level.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowPublicAccess** | **Boolean** | Whether allow no-auth integration with widget. If set true, public access to search or other solutions from widget is allowed without authenication token provided by customer hosted backend server. |  [optional] |
|**allowlistedDomains** | **List&lt;String&gt;** | Allowlisted domains that can load this widget. |  [optional] |
|**configId** | **String** | Output only. Unique obfuscated identifier of a WidgetConfig. |  [optional] [readonly] |
|**contentSearchSpec** | [**GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpec**](GoogleCloudDiscoveryengineV1alphaSearchRequestContentSearchSpec.md) |  |  [optional] |
|**createTime** | **String** | Output only. Timestamp the WidgetConfig was created. |  [optional] [readonly] |
|**dataStoreType** | [**DataStoreTypeEnum**](#DataStoreTypeEnum) | Output only. The type of the parent data store. |  [optional] [readonly] |
|**displayName** | **String** | Required. The human readable widget config display name. Used in Discovery UI. This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned. |  [optional] |
|**enableAutocomplete** | **Boolean** | Whether or not to enable autocomplete. |  [optional] |
|**enableConversationalSearch** | **Boolean** | Whether to allow conversational search (LLM, multi-turn) or not (non-LLM, single-turn). |  [optional] |
|**enableQualityFeedback** | **Boolean** | Turn on or off collecting the search result quality feedback from end users. |  [optional] |
|**enableResultScore** | **Boolean** | Whether to show the result score. |  [optional] |
|**enableSafeSearch** | **Boolean** | Whether to enable safe search. |  [optional] |
|**enableSnippetResultSummary** | **Boolean** | Turn on or off summary for each snippets result. |  [optional] |
|**enableSummarization** | **Boolean** | Turn on or off summarization for the search response. |  [optional] |
|**enableWebApp** | **Boolean** | Whether to enable standalone web app. |  [optional] |
|**facetField** | [**List&lt;GoogleCloudDiscoveryengineV1alphaWidgetConfigFacetField&gt;**](GoogleCloudDiscoveryengineV1alphaWidgetConfigFacetField.md) | The configuration and appearance of facets in the end user view. |  [optional] |
|**fieldsUiComponentsMap** | [**Map&lt;String, GoogleCloudDiscoveryengineV1alphaWidgetConfigUIComponentField&gt;**](GoogleCloudDiscoveryengineV1alphaWidgetConfigUIComponentField.md) | The key is the UI component. Mock. Currently supported &#x60;title&#x60;, &#x60;thumbnail&#x60;, &#x60;url&#x60;, &#x60;custom1&#x60;, &#x60;custom2&#x60;, &#x60;custom3&#x60;. The value is the name of the field along with its device visibility. The 3 custom fields are optional and can be added or removed. &#x60;title&#x60;, &#x60;thumbnail&#x60;, &#x60;url&#x60; are required UI components that cannot be removed. |  [optional] |
|**industryVertical** | [**IndustryVerticalEnum**](#IndustryVerticalEnum) | Output only. The industry vertical that the WidgetConfig registers. The WidgetConfig industry vertical is based on the associated Engine. |  [optional] [readonly] |
|**llmEnabled** | **Boolean** | Output only. Whether LLM is enabled in the corresponding data store. |  [optional] [readonly] |
|**minimumDataTermAccepted** | **Boolean** | Output only. Whether the customer accepted data use terms. |  [optional] [readonly] |
|**name** | **String** | Immutable. The full resource name of the widget config. Format: &#x60;projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}/widgetConfigs/{widget_config_id}&#x60;. This field must be a UTF-8 encoded string with a length limit of 1024 characters. |  [optional] |
|**resultDisplayType** | [**ResultDisplayTypeEnum**](#ResultDisplayTypeEnum) | The type of snippet to display in UCS widget. - RESULT_DISPLAY_TYPE_UNSPECIFIED for existing users. - SNIPPET for new non-enterprise search users. - EXTRACTIVE_ANSWER for new enterprise search users. |  [optional] |
|**solutionType** | [**SolutionTypeEnum**](#SolutionTypeEnum) | Required. Immutable. Specifies the solution type that this WidgetConfig can be used for. |  [optional] |
|**updateTime** | **String** | Output only. Timestamp the WidgetConfig was updated. |  [optional] [readonly] |



## Enum: DataStoreTypeEnum

| Name | Value |
|---- | -----|
| DATA_STORE_TYPE_UNSPECIFIED | &quot;DATA_STORE_TYPE_UNSPECIFIED&quot; |
| SITE_SEARCH | &quot;SITE_SEARCH&quot; |
| STRUCTURED | &quot;STRUCTURED&quot; |
| UNSTRUCTURED | &quot;UNSTRUCTURED&quot; |
| BLENDED | &quot;BLENDED&quot; |



## Enum: IndustryVerticalEnum

| Name | Value |
|---- | -----|
| INDUSTRY_VERTICAL_UNSPECIFIED | &quot;INDUSTRY_VERTICAL_UNSPECIFIED&quot; |
| GENERIC | &quot;GENERIC&quot; |
| MEDIA | &quot;MEDIA&quot; |



## Enum: ResultDisplayTypeEnum

| Name | Value |
|---- | -----|
| RESULT_DISPLAY_TYPE_UNSPECIFIED | &quot;RESULT_DISPLAY_TYPE_UNSPECIFIED&quot; |
| SNIPPET | &quot;SNIPPET&quot; |
| EXTRACTIVE_ANSWER | &quot;EXTRACTIVE_ANSWER&quot; |



## Enum: SolutionTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SOLUTION_TYPE_UNSPECIFIED&quot; |
| RECOMMENDATION | &quot;SOLUTION_TYPE_RECOMMENDATION&quot; |
| SEARCH | &quot;SOLUTION_TYPE_SEARCH&quot; |
| CHAT | &quot;SOLUTION_TYPE_CHAT&quot; |



