

# GoogleMapsPlayablelocationsV3LogImpressionsRequest

A request for logging impressions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientInfo** | [**GoogleMapsUnityClientInfo**](GoogleMapsUnityClientInfo.md) |  |  [optional] |
|**impressions** | [**List&lt;GoogleMapsPlayablelocationsV3Impression&gt;**](GoogleMapsPlayablelocationsV3Impression.md) | Required. Impression event details. The maximum number of impression reports that you can log at once is 50. |  [optional] |
|**requestId** | **String** | Required. A string that uniquely identifies the log impressions request. This allows you to detect duplicate requests. We recommend that you use UUIDs for this value. The value must not exceed 50 characters. You should reuse the &#x60;request_id&#x60; only when retrying a request in case of failure. In this case, the request must be identical to the one that failed. |  [optional] |



