# OrdersApi.HookFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disableSingleFire** | **Boolean** | Sets a limit to how many times a specific order shows on the hook, after it first meets filtering conditions. Using the &#x60;FromOrders&#x60; type configuration with JSONata filtering expressions might cause orders to appear more than once on a feed, whenever changes are made to that order. If this field is &#x60;false&#x60; orders will appear in the hook only once. Send this field if you want to filter &#x60;FromOrders&#x60;. | [optional] [default to false]
**expression** | **String** | JSONata query expression that defines what conditions must be met for an order to be included in the hook. This should only be used in case &#x60;type&#x60; is &#x60;FromOrders&#x60;. | [optional] 
**status** | **[String]** | List of order statuses that should be included in the hook. This should only be used in case &#x60;type&#x60; is &#x60;FromWorkflow&#x60;. | [optional] 
**type** | **String** | Determines what orders appear in the hook and how they are filtered. As shown in the examples above, there are two ways:     - &#x60;FromWorkflow&#x60;: the hook will receive order updates only when there is a change or update in the [order status](https://help.vtex.com/en/tutorial/order-flow-and-status--tutorials_196). You must send at least one value for the &#x60;status&#x60; field to determine by which status the orders will be filtered.     - &#x60;FromOrders&#x60;: the hook will receive order updates when there is a change in the order. In this case, orders can be filtered by any property, according to JSONata expressions passed in the &#x60;expression&#x60; field. You must send the request with values for the &#x60;expression&#x60; and &#x60;disableSingleFire&#x60; fields. | [default to &#39;FromWorkflow&#39;]


