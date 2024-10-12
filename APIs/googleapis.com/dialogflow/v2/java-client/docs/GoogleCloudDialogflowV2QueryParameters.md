

# GoogleCloudDialogflowV2QueryParameters

Represents the parameters of the conversational query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contexts** | [**List&lt;GoogleCloudDialogflowV2Context&gt;**](GoogleCloudDialogflowV2Context.md) | The collection of contexts to be activated before this query is executed. |  [optional] |
|**geoLocation** | [**GoogleTypeLatLng**](GoogleTypeLatLng.md) |  |  [optional] |
|**payload** | **Map&lt;String, Object&gt;** | This field can be used to pass custom data to your webhook. Arbitrary JSON objects are supported. If supplied, the value is used to populate the &#x60;WebhookRequest.original_detect_intent_request.payload&#x60; field sent to your webhook. |  [optional] |
|**platform** | **String** | The platform of the virtual agent response messages. If not empty, only emits messages from this platform in the response. Valid values are the enum names of platform. |  [optional] |
|**resetContexts** | **Boolean** | Specifies whether to delete all contexts in the current session before the new ones are activated. |  [optional] |
|**sentimentAnalysisRequestConfig** | [**GoogleCloudDialogflowV2SentimentAnalysisRequestConfig**](GoogleCloudDialogflowV2SentimentAnalysisRequestConfig.md) |  |  [optional] |
|**sessionEntityTypes** | [**List&lt;GoogleCloudDialogflowV2SessionEntityType&gt;**](GoogleCloudDialogflowV2SessionEntityType.md) | Additional session entity types to replace or extend developer entity types with. The entity synonyms apply to all languages and persist for the session of this query. |  [optional] |
|**timeZone** | **String** | The time zone of this conversational query from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris. If not provided, the time zone specified in agent settings is used. |  [optional] |
|**webhookHeaders** | **Map&lt;String, String&gt;** | This field can be used to pass HTTP headers for a webhook call. These headers will be sent to webhook along with the headers that have been configured through the Dialogflow web console. The headers defined within this field will overwrite the headers configured through the Dialogflow console if there is a conflict. Header names are case-insensitive. Google&#39;s specified headers are not allowed. Including: \&quot;Host\&quot;, \&quot;Content-Length\&quot;, \&quot;Connection\&quot;, \&quot;From\&quot;, \&quot;User-Agent\&quot;, \&quot;Accept-Encoding\&quot;, \&quot;If-Modified-Since\&quot;, \&quot;If-None-Match\&quot;, \&quot;X-Forwarded-For\&quot;, etc. |  [optional] |



