

# GoogleCloudRecommendationengineV1beta1PurgeUserEventsResponse

Response of the PurgeUserEventsRequest. If the long running operation is successfully done, then this message is returned by the google.longrunning.Operations.response field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**purgedEventsCount** | **String** | The total count of events purged as a result of the operation. |  [optional] |
|**userEventsSample** | [**List&lt;GoogleCloudRecommendationengineV1beta1UserEvent&gt;**](GoogleCloudRecommendationengineV1beta1UserEvent.md) | A sampling of events deleted (or will be deleted) depending on the &#x60;force&#x60; property in the request. Max of 500 items will be returned. |  [optional] |



