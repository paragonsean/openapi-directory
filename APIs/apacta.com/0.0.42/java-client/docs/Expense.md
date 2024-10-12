

# Expense


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activityId** | **UUID** |  |  [optional] |
|**comment** | **String** |  |  [optional] |
|**companyId** | **UUID** | Read-only |  [optional] |
|**contactId** | **UUID** |  |  [optional] |
|**created** | **String** |  |  [optional] [readonly] |
|**createdById** | **UUID** | Read-only |  [optional] |
|**currencyId** | **UUID** |  |  [optional] |
|**deleted** | **String** | Only present if it&#39;s a deleted object |  [optional] [readonly] |
|**deliveryDate** | **LocalDate** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**dueDate** | **LocalDate** |  |  [optional] |
|**fileReference** | **String** |  |  [optional] |
|**id** | **UUID** | Read-only |  [optional] |
|**isImported** | **String** |  |  [optional] |
|**modified** | **String** |  |  [optional] [readonly] |
|**orderNumber** | **String** |  |  [optional] |
|**projectId** | **UUID** |  |  [optional] |
|**readsoftId** | **String** |  |  [optional] |
|**reference** | **String** |  |  [optional] |
|**rogerId** | **UUID** |  |  [optional] |
|**sentToEmail** | **String** |  |  [optional] |
|**shortText** | **String** |  |  [optional] |
|**status** | **String** |  |  [optional] |
|**supplierInvoiceNumber** | **String** |  |  [optional] |
|**totalBuyingPrice** | **Float** | Sum of all &#x60;buying_price&#x60; from expense lines |  [optional] |
|**totalSellingPrice** | **Float** | Sum of all &#x60;selling_price&#x60; from expense lines |  [optional] |



