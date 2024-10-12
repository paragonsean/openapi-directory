

# InvoiceLine


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **String** |  |  [optional] [readonly] |
|**createdById** | **UUID** |  |  [optional] |
|**deleted** | **String** | Only present if it&#39;s a deleted object |  [optional] [readonly] |
|**description** | **String** |  |  [optional] |
|**discountPercent** | **Integer** |  |  [optional] |
|**discountText** | **String** |  |  [optional] |
|**eanProductId** | **UUID** |  |  [optional] |
|**formId** | **UUID** |  |  [optional] |
|**id** | **UUID** |  |  [optional] |
|**invoiceId** | **UUID** |  |  [optional] |
|**materialId** | **UUID** |  |  [optional] |
|**modified** | **String** |  |  [optional] [readonly] |
|**name** | **String** |  |  [optional] |
|**parentId** | **UUID** |  |  [optional] |
|**productBundleId** | **UUID** |  |  [optional] |
|**productId** | **UUID** |  |  [optional] |
|**quantity** | **Integer** |  |  [optional] |
|**sellingPrice** | **Float** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**userId** | **UUID** |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NORMAL | &quot;normal&quot; |
| TEXT | &quot;text&quot; |
| BUNDLE | &quot;bundle&quot; |



