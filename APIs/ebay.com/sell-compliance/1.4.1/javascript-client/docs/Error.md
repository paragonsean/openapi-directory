# ComplianceApi.Error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | Identifies the type of erro. | [optional] 
**domain** | **String** | Name for the primary system where the error occurred. This is relevant for application errors. | [optional] 
**errorId** | **Number** | A unique number to identify the error. | [optional] 
**inputRefIds** | **[String]** | An array of request elements most closely associated to the error. | [optional] 
**longMessage** | **String** | A more detailed explanation of the error. | [optional] 
**message** | **String** | Information on how to correct the problem, in the end user&#39;s terms and language where applicable. | [optional] 
**outputRefIds** | **[String]** | An array of request elements most closely associated to the error. | [optional] 
**parameters** | [**[ErrorParameter]**](ErrorParameter.md) | An array of name/value pairs that describe details the error condition. These are useful when multiple errors are returned. | [optional] 
**subdomain** | **String** | Further helps indicate which subsystem the error is coming from. System subcategories include: Initialization, Serialization, Security, Monitoring, Rate Limiting, etc. | [optional] 


