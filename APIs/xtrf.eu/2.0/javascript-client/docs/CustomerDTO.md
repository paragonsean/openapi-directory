# XtrfHomePortalApi.CustomerDTO

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountOnCustomerServer** | **String** |  | [optional] 
**accounting** | [**CustomerAccountingDTO**](CustomerAccountingDTO.md) |  | [optional] 
**billingAddress** | [**AddressDTO**](AddressDTO.md) |  | [optional] 
**branchId** | **Number** |  | [optional] 
**categoriesIds** | **[Number]** |  | [optional] 
**clientFirstProjectDate** | **Date** |  | [optional] 
**clientFirstQuoteDate** | **Date** |  | [optional] 
**clientLastProjectDate** | **Date** |  | [optional] 
**clientLastQuoteDate** | **Date** |  | [optional] 
**clientNumberOfProjects** | **Number** |  | [optional] 
**clientNumberOfQuotes** | **Number** |  | [optional] 
**contact** | [**ContactDTO**](ContactDTO.md) |  | [optional] 
**contractNumber** | **String** |  | [optional] 
**correspondenceAddress** | [**AddressDTO**](AddressDTO.md) |  | [optional] 
**customFields** | [**[CustomFieldDTO]**](CustomFieldDTO.md) |  | [optional] 
**fullName** | **String** |  | [optional] 
**id** | **Number** |  | [optional] 
**idNumber** | **String** |  | [optional] 
**industriesIds** | **[Number]** |  | [optional] 
**leadSourceId** | **Number** |  | [optional] 
**limitAccessToPeopleResponsible** | **Boolean** |  | [optional] 
**name** | **String** |  | [optional] 
**notes** | **String** |  | [optional] 
**persons** | [**[CustomerPersonDTO]**](CustomerPersonDTO.md) |  | [optional] 
**responsiblePersons** | [**CustomerResponsiblePersonsDTO**](CustomerResponsiblePersonsDTO.md) |  | [optional] 
**salesNotes** | **String** |  | [optional] 
**status** | **String** |  | [optional] 



## Enum: StatusEnum


* `ACTIVE` (value: `"ACTIVE"`)

* `INACTIVE` (value: `"INACTIVE"`)

* `POTENTIAL` (value: `"POTENTIAL"`)




