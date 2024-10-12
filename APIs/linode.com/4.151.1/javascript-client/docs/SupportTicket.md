# LinodeApi.SupportTicket

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | **[String]** | A list of filenames representing attached files associated with this Ticket.  | [optional] [readonly] 
**closable** | **Boolean** | Whether the Support Ticket may be closed.  | [optional] 
**closed** | **Date** | The date and time this Ticket was closed.  | [optional] [readonly] 
**description** | **String** | The full details of the issue or question.  | [optional] [readonly] 
**entity** | [**SupportTicketEntity**](SupportTicketEntity.md) |  | [optional] 
**gravatarId** | **String** | The Gravatar ID of the User who opened this Ticket.  | [optional] [readonly] 
**id** | **Number** | The ID of the Support Ticket.  | [optional] [readonly] 
**opened** | **Date** | The date and time this Ticket was created.  | [optional] [readonly] 
**openedBy** | **String** | The User who opened this Ticket.  | [optional] [readonly] 
**status** | **String** | The current status of this Ticket. | [optional] [readonly] 
**summary** | **String** | The summary or title for this Ticket.  | [optional] [readonly] 
**updated** | **Date** | The date and time this Ticket was last updated.  | [optional] [readonly] 
**updatedBy** | **String** | The User who last updated this Ticket.  | [optional] [readonly] 



## Enum: StatusEnum


* `closed` (value: `"closed"`)

* `new` (value: `"new"`)

* `open` (value: `"open"`)




