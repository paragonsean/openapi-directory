# SalesLoftPlatform.CrmActivityField

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | Datetime of when the CrmActivityField was created | [optional] 
**crmObjectType** | **String** | The CRM object type that this field maps to. Valid object types are CRM dependent: Task, Phonecall, Email.  | [optional] 
**field** | **String** | The CRM field name | [optional] 
**fieldType** | **String** | The type of this field in your CRM. Certain field types can only accept structured input. | [optional] 
**id** | **Number** | ID of CrmActivityField | [optional] 
**picklistValues** | **Object** | Valid picklist values, if present for this field. The format is {label &#x3D;&gt; value}. If present, only values in the picklist structure can be used as a crm param.  | [optional] 
**salesforceObjectType** | **String** | The Salesforce object type that this field maps to. Valid object types are: Task. More object types may be added in the future.  | [optional] 
**source** | **String** | SalesLoft object that this field is mapped for. Valid sources are: email, phone | [optional] 
**title** | **String** | A human friendly title for this field | [optional] 
**updatedAt** | **Date** | Datetime of when the CrmActivityField was last updated | [optional] 
**value** | **String** | A value to always be written. This value does not need to be sent to other endpoints&#39; crm params, but must be the exact value if sent. Email source fields will always have a value present.  | [optional] 


