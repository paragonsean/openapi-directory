

# GiftCard

Represents a Square gift card.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**balanceMoney** | [**Money**](Money.md) |  |  [optional] |
|**createdAt** | **String** | The timestamp when the gift card was created, in RFC 3339 format.  In the case of a digital gift card, it is the time when you create a card  (using the Square Point of Sale application, Seller Dashboard, or Gift Cards API).   In the case of a plastic gift card, it is the time when Square associates the card with the  seller at the time of activation. |  [optional] |
|**customerIds** | **List&lt;String&gt;** | The IDs of the customers to whom this gift card is linked. |  [optional] |
|**gan** | **String** | The gift card account number. |  [optional] |
|**ganSource** | **Object** |  |  [optional] |
|**id** | **String** | The Square-assigned ID of the gift card. |  [optional] |
|**state** | **Object** |  |  [optional] |
|**type** | **Object** |  |  |



