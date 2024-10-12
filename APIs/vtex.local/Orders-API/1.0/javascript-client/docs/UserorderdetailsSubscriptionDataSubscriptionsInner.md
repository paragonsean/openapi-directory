# OrdersApi.UserorderdetailsSubscriptionDataSubscriptionsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executionCount** | **Number** | Position of the order in the subscription cycle. The first order will have the value &#x60;0&#x60;, the second will have the value &#x60;1&#x60;, and so on. | 
**itemIndex** | **Number** | Each item in the subscriptions&#39; order is identified by an index. The position starts in&#x60;0&#x60;, followed by &#x60;1&#x60;, &#x60;2&#x60;, and so on. | 
**plan** | [**UserorderdetailsSubscriptionDataSubscriptionsInnerPlan**](UserorderdetailsSubscriptionDataSubscriptionsInnerPlan.md) |  | 
**priceAtSubscriptionDate** | **Number** | Price of the order when the customer signed up for subscriptions. Subscriptions created from Admin UI or APIs do not have an original order, so the field returns &#x60;0.0&#x60;. This field was valid only for Subscriptions v2 and is deprecated in Subscriptions v3. | 


