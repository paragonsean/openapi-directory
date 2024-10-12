

# SubscriptionResponse

Complete details for an event subscription.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | Determines if the subscription is active or paused. |  |
|**createdAt** | **OffsetDateTime** | When this subscription was created. Formatted as milliseconds from the [Unix epoch](#). |  |
|**eventType** | [**EventTypeEnum**](#EventTypeEnum) | Type of event to listen for. Can be one of &#x60;create&#x60;, &#x60;delete&#x60;, &#x60;deletedForPrivacy&#x60;, or &#x60;propertyChange&#x60;. |  |
|**id** | **String** | The unique ID of the subscription. |  |
|**propertyName** | **String** | The internal name of the property being monitored for changes. Only applies when &#x60;eventType&#x60; is &#x60;propertyChange&#x60;. |  [optional] |
|**updatedAt** | **OffsetDateTime** | When this subscription was last updated. Formatted as milliseconds from the [Unix epoch](#). |  [optional] |



## Enum: EventTypeEnum

| Name | Value |
|---- | -----|
| CONTACT_PROPERTY_CHANGE | &quot;contact.propertyChange&quot; |
| COMPANY_PROPERTY_CHANGE | &quot;company.propertyChange&quot; |
| DEAL_PROPERTY_CHANGE | &quot;deal.propertyChange&quot; |
| TICKET_PROPERTY_CHANGE | &quot;ticket.propertyChange&quot; |
| PRODUCT_PROPERTY_CHANGE | &quot;product.propertyChange&quot; |
| LINE_ITEM_PROPERTY_CHANGE | &quot;line_item.propertyChange&quot; |
| CONTACT_CREATION | &quot;contact.creation&quot; |
| CONTACT_DELETION | &quot;contact.deletion&quot; |
| CONTACT_PRIVACY_DELETION | &quot;contact.privacyDeletion&quot; |
| COMPANY_CREATION | &quot;company.creation&quot; |
| COMPANY_DELETION | &quot;company.deletion&quot; |
| DEAL_CREATION | &quot;deal.creation&quot; |
| DEAL_DELETION | &quot;deal.deletion&quot; |
| TICKET_CREATION | &quot;ticket.creation&quot; |
| TICKET_DELETION | &quot;ticket.deletion&quot; |
| PRODUCT_CREATION | &quot;product.creation&quot; |
| PRODUCT_DELETION | &quot;product.deletion&quot; |
| LINE_ITEM_CREATION | &quot;line_item.creation&quot; |
| LINE_ITEM_DELETION | &quot;line_item.deletion&quot; |
| CONVERSATION_CREATION | &quot;conversation.creation&quot; |
| CONVERSATION_DELETION | &quot;conversation.deletion&quot; |
| CONVERSATION_NEW_MESSAGE | &quot;conversation.newMessage&quot; |
| CONVERSATION_PRIVACY_DELETION | &quot;conversation.privacyDeletion&quot; |
| CONVERSATION_PROPERTY_CHANGE | &quot;conversation.propertyChange&quot; |
| CONTACT_MERGE | &quot;contact.merge&quot; |
| COMPANY_MERGE | &quot;company.merge&quot; |
| DEAL_MERGE | &quot;deal.merge&quot; |
| TICKET_MERGE | &quot;ticket.merge&quot; |
| PRODUCT_MERGE | &quot;product.merge&quot; |
| LINE_ITEM_MERGE | &quot;line_item.merge&quot; |
| CONTACT_RESTORE | &quot;contact.restore&quot; |
| COMPANY_RESTORE | &quot;company.restore&quot; |
| DEAL_RESTORE | &quot;deal.restore&quot; |
| TICKET_RESTORE | &quot;ticket.restore&quot; |
| PRODUCT_RESTORE | &quot;product.restore&quot; |
| LINE_ITEM_RESTORE | &quot;line_item.restore&quot; |
| CONTACT_ASSOCIATION_CHANGE | &quot;contact.associationChange&quot; |
| COMPANY_ASSOCIATION_CHANGE | &quot;company.associationChange&quot; |
| DEAL_ASSOCIATION_CHANGE | &quot;deal.associationChange&quot; |
| TICKET_ASSOCIATION_CHANGE | &quot;ticket.associationChange&quot; |
| LINE_ITEM_ASSOCIATION_CHANGE | &quot;line_item.associationChange&quot; |



