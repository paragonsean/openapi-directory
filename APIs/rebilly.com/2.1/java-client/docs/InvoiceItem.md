

# InvoiceItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**embedded** | [**List&lt;InvoiceItemEmbeddedInner&gt;**](InvoiceItemEmbeddedInner.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. |  [optional] [readonly] |
|**links** | [**List&lt;InvoiceItemLinksInner&gt;**](InvoiceItemLinksInner.md) | The links related to resource. |  [optional] [readonly] |
|**createdTime** | **OffsetDateTime** | Invoice item created time. |  [optional] [readonly] |
|**description** | **String** | Invoice item&#39;s description. |  [optional] |
|**discountAmount** | **Double** | Invoice item discount amount. |  [optional] [readonly] |
|**id** | **String** | The website identifier string. |  [optional] [readonly] |
|**periodEndTime** | **OffsetDateTime** | End time. |  [optional] |
|**periodNumber** | **Integer** | Invoice item subscription order period number. |  [optional] |
|**periodStartTime** | **OffsetDateTime** | Start time. |  [optional] |
|**price** | **Double** | Invoice item&#39;s total price. |  [optional] [readonly] |
|**productId** | **String** | The product&#39;s ID. |  [optional] |
|**quantity** | **Integer** | Invoice item&#39;s quantity. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Invoice item&#39;s type. |  |
|**unitPrice** | **Double** | Invoice item&#39;s price. |  |
|**updatedTime** | **OffsetDateTime** | Invoice item updated time. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DEBIT | &quot;debit&quot; |
| CREDIT | &quot;credit&quot; |



