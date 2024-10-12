# OrdersApi.GetFeedConfiguration200ResponseFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disableSingleFire** | **Boolean** | Sets a limit to how many times a specific order shows on the feed, after it first meets filtering conditions. Using the &#x60;FromOrders&#x60; type configuration with JSONata filtering expressions might cause orders to appear more than once on a feed, whenever changes are made to that order. If this field is &#x60;false&#x60; orders will appear in the feed only once. | [optional] 
**expression** | **String** | JSONata query expression that defines what conditions must be met for an order to be included in the feed. This should only be used in case &#x60;type&#x60; is &#x60;FromOrders&#x60;. | [optional] 
**status** | **[String]** | List of order statuses that should be included in the feed. This should only be used in case &#x60;type&#x60; is &#x60;FromWorkflow&#x60;. | [optional] 
**type** | **String** | Determines what orders appear in the feed and how they are filtered. If a feed has the &#x60;FromWorkflow&#x60; type configuration, it will receive order updates only when order’s statuses change and orders can be filtered by status, using the &#x60;status&#x60; field. A feed with the &#x60;FromOrders&#x60; type configuration gets updates whenever any change is made to an order. in this case, orders can be filtered by any property, according to JSONata expressions set in the &#x60;expression&#x60; field. | [optional] 


