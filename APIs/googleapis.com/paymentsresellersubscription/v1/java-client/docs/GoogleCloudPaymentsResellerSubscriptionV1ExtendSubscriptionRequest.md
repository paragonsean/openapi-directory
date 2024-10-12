

# GoogleCloudPaymentsResellerSubscriptionV1ExtendSubscriptionRequest

Request message for extending a Subscription resource. A new recurrence will be made based on the subscription schedule defined by the original product.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**extension** | [**GoogleCloudPaymentsResellerSubscriptionV1Extension**](GoogleCloudPaymentsResellerSubscriptionV1Extension.md) |  |  [optional] |
|**requestId** | **String** | Required. Restricted to 36 ASCII characters. A random UUID is recommended. The idempotency key for the request. The ID generation logic is controlled by the partner. request_id should be the same as on retries of the same request. A different request_id must be used for a extension of a different cycle. |  [optional] |



