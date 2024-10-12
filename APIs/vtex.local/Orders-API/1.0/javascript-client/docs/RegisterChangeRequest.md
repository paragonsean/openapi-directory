# OrdersApi.RegisterChangeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discountValue** | **Number** | This field can be used to apply a discount to the total value of the order. Value in cents. | [default to 100]
**incrementValue** | **Number** | This field can be used to increment the total value of the order. Value in cents. | [default to 100]
**itemsAdded** | [**[RegisterChangeRequestItemsAddedInner]**](RegisterChangeRequestItemsAddedInner.md) | List of items that should be added to the order. | [optional] 
**itemsRemoved** | [**[RegisterChangeRequestItemsRemovedInner]**](RegisterChangeRequestItemsRemovedInner.md) | List of items that should be removed from the order. | [optional] 
**reason** | **String** | Reason for order change. This may be shown to the shopper in the UI or transactional emails. | [default to &#39;Stock shortage&#39;]
**requestId** | **String** | Request identification of the change. Only the first change made with each &#x60;requestId&#x60; will be effective on a given order. Use different IDs for different changes to the same order. | [default to &#39;change-request-0123&#39;]


