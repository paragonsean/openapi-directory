# CrmApi.Opportunity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closeDate** | **Date** | The actual closing date for the opportunity. If close_date is null, the opportunity is not closed yet. | [optional] 
**companyId** | **String** | The unique identifier of the company associated with the opportunity. | [optional] 
**companyName** | **String** | The name of the company associated with the opportunity. | [optional] 
**contactId** | **String** | The unique identifier of the contact associated with the opportunity. | [optional] 
**contactIds** | **[String]** | An array of unique identifiers of all contacts associated with the opportunity. | [optional] 
**createdAt** | **Date** | The date and time when the opportunity was created. | [optional] [readonly] 
**createdBy** | **String** | The unique identifier of the user who created the opportunity. | [optional] [readonly] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**customFields** | [**[CustomField]**](CustomField.md) |  | [optional] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**dateLastContacted** | **Date** | The date and time when the opportunity was last contacted. | [optional] [readonly] 
**dateLeadCreated** | **Date** | The date and time when the lead associated with the opportunity was created. | [optional] [readonly] 
**dateStageChanged** | **Date** | The date and time when the stage of the opportunity was last changed. | [optional] [readonly] 
**deleted** | **Boolean** | Indicates whether the opportunity has been deleted. | [optional] [readonly] 
**description** | **String** | A description of the opportunity. | [optional] 
**expectedRevenue** | **Number** | The expected revenue from the opportunity | [optional] [readonly] 
**id** | **String** | A unique identifier for the opportunity. | [optional] [readonly] 
**interactionCount** | **Number** | The number of interactions with the opportunity. | [optional] [readonly] 
**lastActivityAt** | **String** | The date and time of the last activity associated with the opportunity. | [optional] [readonly] 
**leadId** | **String** | The unique identifier of the lead associated with the opportunity. | [optional] 
**leadSource** | **String** | The source of the lead associated with the opportunity. | [optional] 
**lossReason** | **String** | The reason why the opportunity was lost. | [optional] 
**lossReasonId** | **String** | The unique identifier of the reason why the opportunity was lost. | [optional] 
**monetaryAmount** | **Number** | The monetary value associated with the opportunity | [optional] 
**ownerId** | **String** | The unique identifier of the user who owns the opportunity. | [optional] 
**pipelineId** | **String** | The unique identifier of the pipeline associated with the opportunity | [optional] 
**pipelineStageId** | **String** | The unique identifier of the stage in the pipeline associated with the opportunity. | [optional] 
**primaryContactId** | **String** | The unique identifier of the primary contact associated with the opportunity. | 
**priority** | **String** | The priority level of the opportunity. | [optional] 
**sourceId** | **String** | The unique identifier of the source of the opportunity. | [optional] 
**stageLastChangedAt** | **Date** | The date and time when the stage of the opportunity was last changed. | [optional] 
**status** | **String** | The current status of the opportunity. | [optional] 
**statusId** | **String** | The unique identifier of the current status of the opportunity. | [optional] 
**tags** | **[String]** |  | [optional] 
**title** | **String** | The title or name of the opportunity. | 
**type** | **String** | The type of the opportunity | [optional] 
**updatedAt** | **Date** | The date and time when the opportunity was last updated. | [optional] [readonly] 
**updatedBy** | **String** | The unique identifier of the user who last updated the opportunity. | [optional] [readonly] 
**winProbability** | **Number** | The probability of winning the opportunity, expressed as a percentage. | [optional] 
**wonReason** | **String** | The reason why the opportunity was won. | [optional] 
**wonReasonId** | **String** | The unique identifier of the reason why the opportunity was won. | [optional] 


