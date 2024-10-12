

# Attachment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**embedded** | [**List&lt;AttachmentEmbeddedInner&gt;**](AttachmentEmbeddedInner.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. |  [optional] [readonly] |
|**links** | [**List&lt;AttachmentLinksInner&gt;**](AttachmentLinksInner.md) | The links related to resource. |  [optional] [readonly] |
|**createdTime** | **OffsetDateTime** | Creation date/time. |  [optional] [readonly] |
|**description** | **String** | The Attachment description. |  [optional] |
|**fileId** | **String** | Linked File object id. |  |
|**id** | **String** | The resource ID. Defaults to UUID v4. |  [optional] [readonly] |
|**name** | **String** | The Original Attachment name. |  [optional] |
|**relatedId** | **String** | Linked object Id. |  |
|**relatedType** | [**RelatedTypeEnum**](#RelatedTypeEnum) | Linked object type. |  |
|**updatedTime** | **OffsetDateTime** | Latest update date/time. |  [optional] [readonly] |



## Enum: RelatedTypeEnum

| Name | Value |
|---- | -----|
| CUSTOMER | &quot;customer&quot; |
| DISPUTE | &quot;dispute&quot; |
| GATEWAY_TIMELINE_COMMENT | &quot;gateway-timeline-comment&quot; |
| INVOICE | &quot;invoice&quot; |
| ORGANIZATION | &quot;organization&quot; |
| PAYMENT | &quot;payment&quot; |
| PLAN | &quot;plan&quot; |
| PRODUCT | &quot;product&quot; |
| SUBSCRIPTION | &quot;subscription&quot; |
| TRANSACTION | &quot;transaction&quot; |
| CUSTOMER_TIMELINE_COMMENT | &quot;customer-timeline-comment&quot; |
| TRANSACTION_TIMELINE_COMMENT | &quot;transaction-timeline-comment&quot; |
| ORDER_TIMELINE_COMMENT | &quot;order-timeline-comment&quot; |



