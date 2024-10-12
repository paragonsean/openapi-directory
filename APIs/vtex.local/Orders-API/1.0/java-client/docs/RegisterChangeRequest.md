

# RegisterChangeRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**discountValue** | **Integer** | This field can be used to apply a discount to the total value of the order. Value in cents. |  |
|**incrementValue** | **Integer** | This field can be used to increment the total value of the order. Value in cents. |  |
|**itemsAdded** | [**List&lt;RegisterChangeRequestItemsAddedInner&gt;**](RegisterChangeRequestItemsAddedInner.md) | List of items that should be added to the order. |  [optional] |
|**itemsRemoved** | [**List&lt;RegisterChangeRequestItemsRemovedInner&gt;**](RegisterChangeRequestItemsRemovedInner.md) | List of items that should be removed from the order. |  [optional] |
|**reason** | **String** | Reason for order change. This may be shown to the shopper in the UI or transactional emails. |  |
|**requestId** | **String** | Request identification of the change. Only the first change made with each &#x60;requestId&#x60; will be effective on a given order. Use different IDs for different changes to the same order. |  |



