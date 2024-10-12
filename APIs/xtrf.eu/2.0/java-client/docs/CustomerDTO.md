

# CustomerDTO


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountOnCustomerServer** | **String** |  |  [optional] |
|**accounting** | [**CustomerAccountingDTO**](CustomerAccountingDTO.md) |  |  [optional] |
|**billingAddress** | [**AddressDTO**](AddressDTO.md) |  |  [optional] |
|**branchId** | **Long** |  |  [optional] |
|**categoriesIds** |  |  |  [optional] |
|**clientFirstProjectDate** | **OffsetDateTime** |  |  [optional] |
|**clientFirstQuoteDate** | **OffsetDateTime** |  |  [optional] |
|**clientLastProjectDate** | **OffsetDateTime** |  |  [optional] |
|**clientLastQuoteDate** | **OffsetDateTime** |  |  [optional] |
|**clientNumberOfProjects** | **Integer** |  |  [optional] |
|**clientNumberOfQuotes** | **Integer** |  |  [optional] |
|**contact** | [**ContactDTO**](ContactDTO.md) |  |  [optional] |
|**contractNumber** | **String** |  |  [optional] |
|**correspondenceAddress** | [**AddressDTO**](AddressDTO.md) |  |  [optional] |
|**customFields** |  |  |  [optional] |
|**fullName** | **String** |  |  [optional] |
|**id** | **Long** |  |  [optional] |
|**idNumber** | **String** |  |  [optional] |
|**industriesIds** |  |  |  [optional] |
|**leadSourceId** | **Long** |  |  [optional] |
|**limitAccessToPeopleResponsible** | **Boolean** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**notes** | **String** |  |  [optional] |
|**persons** | [**List&lt;CustomerPersonDTO&gt;**](CustomerPersonDTO.md) |  |  [optional] |
|**responsiblePersons** | [**CustomerResponsiblePersonsDTO**](CustomerResponsiblePersonsDTO.md) |  |  [optional] |
|**salesNotes** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| INACTIVE | &quot;INACTIVE&quot; |
| POTENTIAL | &quot;POTENTIAL&quot; |



