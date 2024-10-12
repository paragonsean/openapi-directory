

# Response

Defines a response. All schemas that return at the root of the response must inherit from this object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adaptiveCard** | **String** |  |  [optional] [readonly] |
|**immediateAction** | [**List&lt;Action&gt;**](Action.md) |  |  [optional] [readonly] |
|**potentialAction** | [**List&lt;Action&gt;**](Action.md) |  |  [optional] [readonly] |
|**preferredClickthroughUrl** | **String** |  |  [optional] [readonly] |
|**readLink** | **String** | The URL that returns this resource. |  [optional] [readonly] |
|**webSearchUrl** | **String** | The URL to Bing&#39;s search result for this item. |  [optional] [readonly] |



