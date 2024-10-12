

# WatchCreativesResponse

A response for the request to receive push notification when a bidder's creatives change status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**subscription** | **String** | The Pub/Sub subscription that can be used to pull creative status notifications. This would be of the format &#x60;projects/{project_id}/subscriptions/{subscription_id}&#x60;. Subscription is created with pull delivery. All service accounts belonging to the bidder will have read access to this subscription. Subscriptions that are inactive for more than 90 days will be disabled. Use watchCreatives to re-enable the subscription. |  [optional] |
|**topic** | **String** | The Pub/Sub topic that will be used to publish creative serving status notifications. This would be of the format &#x60;projects/{project_id}/topics/{topic_id}&#x60;. |  [optional] |



