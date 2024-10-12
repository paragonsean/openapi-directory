

# SearchOrdersFulfillmentFilter

Filter based on [order fulfillment](https://developer.squareup.com/reference/square_2021-08-18/objects/OrderFulfillment) information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fulfillmentStates** | **List&lt;String&gt;** | A list of [fulfillment states](https://developer.squareup.com/reference/square_2021-08-18/objects/OrderFulfillmentState) to filter for. The list returns orders if any of its fulfillments match any of the fulfillment states listed in this field. |  [optional] |
|**fulfillmentTypes** | **List&lt;String&gt;** | A list of [fulfillment types](https://developer.squareup.com/reference/square_2021-08-18/enums/OrderFulfillmentType) to filter for. The list returns orders if any of its fulfillments match any of the fulfillment types listed in this field. |  [optional] |



