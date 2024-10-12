# RebillyRestApi.Attachment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**[AttachmentEmbeddedInner]**](AttachmentEmbeddedInner.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. | [optional] [readonly] 
**links** | [**[AttachmentLinksInner]**](AttachmentLinksInner.md) | The links related to resource. | [optional] [readonly] 
**createdTime** | **Date** | Creation date/time. | [optional] [readonly] 
**description** | **String** | The Attachment description. | [optional] 
**fileId** | **String** | Linked File object id. | 
**id** | **String** | The resource ID. Defaults to UUID v4. | [optional] [readonly] 
**name** | **String** | The Original Attachment name. | [optional] 
**relatedId** | **String** | Linked object Id. | 
**relatedType** | **String** | Linked object type. | 
**updatedTime** | **Date** | Latest update date/time. | [optional] [readonly] 



## Enum: RelatedTypeEnum


* `customer` (value: `"customer"`)

* `dispute` (value: `"dispute"`)

* `gateway-timeline-comment` (value: `"gateway-timeline-comment"`)

* `invoice` (value: `"invoice"`)

* `organization` (value: `"organization"`)

* `payment` (value: `"payment"`)

* `plan` (value: `"plan"`)

* `product` (value: `"product"`)

* `subscription` (value: `"subscription"`)

* `transaction` (value: `"transaction"`)

* `customer-timeline-comment` (value: `"customer-timeline-comment"`)

* `transaction-timeline-comment` (value: `"transaction-timeline-comment"`)

* `order-timeline-comment` (value: `"order-timeline-comment"`)




