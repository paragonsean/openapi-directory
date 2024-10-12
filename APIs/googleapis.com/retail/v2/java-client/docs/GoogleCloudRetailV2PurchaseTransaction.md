

# GoogleCloudRetailV2PurchaseTransaction

A transaction represents the entire purchase transaction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cost** | **Float** | All the costs associated with the products. These can be manufacturing costs, shipping expenses not borne by the end user, or any other costs, such that: * Profit &#x3D; revenue - tax - cost |  [optional] |
|**currencyCode** | **String** | Required. Currency code. Use three-character ISO-4217 code. |  [optional] |
|**id** | **String** | The transaction ID with a length limit of 128 characters. |  [optional] |
|**revenue** | **Float** | Required. Total non-zero revenue or grand total associated with the transaction. This value include shipping, tax, or other adjustments to total revenue that you want to include as part of your revenue calculations. |  [optional] |
|**tax** | **Float** | All the taxes associated with the transaction. |  [optional] |



