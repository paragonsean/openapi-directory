# CrmApi.User

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**companyName** | **String** | The name of the company. | [optional] 
**createdAt** | **String** | The date and time when the user was created. | [optional] [readonly] 
**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. | [optional] 
**department** | **String** | The department the person is currently in. [Deprecated](https://developers.apideck.com/changelog) in favor of the dedicated department_id and department_name field. | [optional] 
**description** | **String** | A description of the object. | [optional] 
**division** | **String** | The division the person is currently in. Usually a collection of departments or teams or regions. | [optional] 
**emails** | [**[Email]**](Email.md) |  | 
**employeeNumber** | **String** | An Employee Number, Employee ID or Employee Code, is a unique number that has been assigned to each individual staff member within a company. | [optional] 
**firstName** | **String** | The first name of the person. | [optional] 
**id** | **String** | The unique identifier for the user | [optional] [readonly] 
**image** | **String** | The URL of the user&#39;s avatar | [optional] 
**language** | **String** | language code according to ISO 639-1. For the United States - EN | [optional] 
**lastName** | **String** | The last name of the person. | [optional] 
**parentId** | **String** | The parent user id | [optional] 
**password** | **String** | The password of the user | [optional] 
**phoneNumbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**status** | **String** | The status of the user | [optional] 
**title** | **String** | The job title of the person. | [optional] 
**updatedAt** | **String** | The date and time when the user was last updated. | [optional] [readonly] 
**username** | **String** | The username of the user | [optional] 


