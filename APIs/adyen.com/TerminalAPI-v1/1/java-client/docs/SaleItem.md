

# SaleItem

In loyalty or value added payment card transaction, the items of the sale are entering in the processing of the transaction. Sale items of a transaction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalProductInfo** | **String** | If data sent, POI has to store it and send it if the host protocol allows it. |  [optional] |
|**eanUpc** | **Integer** | If data sent, POI has to store it and send it if the host protocol allows it. |  [optional] |
|**itemAmount** | **BigDecimal** | Total amount of the item line. |  |
|**itemID** | **Integer** | Item identification inside a transaction (0 to n). |  |
|**productCode** | **Integer** | Product code of item purchased with the transaction. |  |
|**productLabel** | **String** |  |  [optional] |
|**quantity** | **String** | If data sent, POI has to store it and send it if the host protocol allows it. |  [optional] |
|**saleChannel** | **Integer** | If data sent, POI has to store it and send it if the host protocol allows it. |  [optional] |
|**taxCode** | **Integer** | If data sent, POI has to store it and send it if the host protocol allows it. |  [optional] |
|**unitOfMeasure** | **UnitOfMeasure** |  |  [optional] |
|**unitPrice** | **BigDecimal** | if Quantity present. |  [optional] |



