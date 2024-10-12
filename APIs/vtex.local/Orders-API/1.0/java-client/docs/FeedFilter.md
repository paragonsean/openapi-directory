

# FeedFilter

Object with type and status that will filter feed orders.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disableSingleFire** | **Boolean** | Sets a limit to how many times a specific order shows on the feed, after it first meets filtering conditions. Using the &#x60;FromOrders&#x60; type configuration with JSONata filtering expressions might cause orders to appear more than once on a feed, whenever changes are made to that order. If this field is &#x60;false&#x60; orders will appear in the feed only once. |  [optional] |
|**expression** | **String** | JSONata query expression that defines what conditions must be met for an order to be included in the feed. This should only be used in case &#x60;type&#x60; is set to &#x60;FromOrders&#x60;. |  [optional] |
|**status** | **List&lt;String&gt;** | List of order statuses that should be included in the feed. This should only be used in case &#x60;type&#x60; is set to &#x60;FromWorkflow&#x60;. The status event will be removed, if it can&#39;t deliver a message more than 100 times, 4 days progressively.     **Status available to filter**     - order-created    - on-order-completed    - on-order-completed-ffm    - payment-pending    - waiting-for-order-authorization    - approve-payment    - payment-approved    - request-cancel    - waiting-for-seller-decision    - waiting-ffmt-authorization    - waiting-for-authorization    - waiting-for-manual-authorization    - authorize-fulfillment    - order-create-error    - order-creation-error    - window-to-cancel    - window-to-change-seller    - waiting-for-mkt-authorization    - waiting-seller-handling    - ready-for-handling    - start-handling    - handling    - invoice-after-cancellation-deny    - order-accepted    - invoice    - invoiced    - replaced    - cancellation-requested    - cancel    - canceled |  [optional] |
|**type** | **String** | Determines what orders appear in the feed and how they are filtered. There are two possible values:    -&#x60;FromWorkflow&#x60;: the feed will receive order updates only when order’s statuses change and orders can be filtered by status, using the &#x60;status&#x60; field described below.    -&#x60;FromOrders&#x60;: the feed gets updates whenever any change is made to an order. in this case, orders can be filtered by any property, according to JSONata expressions passed in the &#x60;expression&#x60; field described below. |  |



