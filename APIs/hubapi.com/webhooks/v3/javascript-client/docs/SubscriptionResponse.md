# WebhooksWebhooks.SubscriptionResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** | Determines if the subscription is active or paused. | 
**createdAt** | **Date** | When this subscription was created. Formatted as milliseconds from the [Unix epoch](#). | 
**eventType** | **String** | Type of event to listen for. Can be one of &#x60;create&#x60;, &#x60;delete&#x60;, &#x60;deletedForPrivacy&#x60;, or &#x60;propertyChange&#x60;. | 
**id** | **String** | The unique ID of the subscription. | 
**propertyName** | **String** | The internal name of the property being monitored for changes. Only applies when &#x60;eventType&#x60; is &#x60;propertyChange&#x60;. | [optional] 
**updatedAt** | **Date** | When this subscription was last updated. Formatted as milliseconds from the [Unix epoch](#). | [optional] 



## Enum: EventTypeEnum


* `contact.propertyChange` (value: `"contact.propertyChange"`)

* `company.propertyChange` (value: `"company.propertyChange"`)

* `deal.propertyChange` (value: `"deal.propertyChange"`)

* `ticket.propertyChange` (value: `"ticket.propertyChange"`)

* `product.propertyChange` (value: `"product.propertyChange"`)

* `line_item.propertyChange` (value: `"line_item.propertyChange"`)

* `contact.creation` (value: `"contact.creation"`)

* `contact.deletion` (value: `"contact.deletion"`)

* `contact.privacyDeletion` (value: `"contact.privacyDeletion"`)

* `company.creation` (value: `"company.creation"`)

* `company.deletion` (value: `"company.deletion"`)

* `deal.creation` (value: `"deal.creation"`)

* `deal.deletion` (value: `"deal.deletion"`)

* `ticket.creation` (value: `"ticket.creation"`)

* `ticket.deletion` (value: `"ticket.deletion"`)

* `product.creation` (value: `"product.creation"`)

* `product.deletion` (value: `"product.deletion"`)

* `line_item.creation` (value: `"line_item.creation"`)

* `line_item.deletion` (value: `"line_item.deletion"`)

* `conversation.creation` (value: `"conversation.creation"`)

* `conversation.deletion` (value: `"conversation.deletion"`)

* `conversation.newMessage` (value: `"conversation.newMessage"`)

* `conversation.privacyDeletion` (value: `"conversation.privacyDeletion"`)

* `conversation.propertyChange` (value: `"conversation.propertyChange"`)

* `contact.merge` (value: `"contact.merge"`)

* `company.merge` (value: `"company.merge"`)

* `deal.merge` (value: `"deal.merge"`)

* `ticket.merge` (value: `"ticket.merge"`)

* `product.merge` (value: `"product.merge"`)

* `line_item.merge` (value: `"line_item.merge"`)

* `contact.restore` (value: `"contact.restore"`)

* `company.restore` (value: `"company.restore"`)

* `deal.restore` (value: `"deal.restore"`)

* `ticket.restore` (value: `"ticket.restore"`)

* `product.restore` (value: `"product.restore"`)

* `line_item.restore` (value: `"line_item.restore"`)

* `contact.associationChange` (value: `"contact.associationChange"`)

* `company.associationChange` (value: `"company.associationChange"`)

* `deal.associationChange` (value: `"deal.associationChange"`)

* `ticket.associationChange` (value: `"ticket.associationChange"`)

* `line_item.associationChange` (value: `"line_item.associationChange"`)




