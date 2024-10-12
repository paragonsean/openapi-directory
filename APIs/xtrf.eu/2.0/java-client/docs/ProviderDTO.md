

# ProviderDTO


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAddress** | [**AddressDTO**](AddressDTO.md) |  |  [optional] |
|**branchId** | **Long** |  |  [optional] |
|**competencies** | [**CompetenciesDTO**](CompetenciesDTO.md) |  |  [optional] |
|**contact** | [**ContactDTO**](ContactDTO.md) |  |  [optional] |
|**correspondenceAddress** | [**AddressDTO**](AddressDTO.md) |  |  [optional] |
|**customFields** |  |  |  [optional] |
|**fullName** | **String** |  |  [optional] |
|**id** | **Long** |  |  [optional] |
|**idNumber** | **String** |  |  [optional] |
|**leadSourceId** | **Long** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**notes** | **String** |  |  [optional] |
|**persons** | [**List&lt;ProviderPersonDTO&gt;**](ProviderPersonDTO.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| INACTIVE | &quot;INACTIVE&quot; |
| WAITING_FOR_APPROVAL | &quot;WAITING_FOR_APPROVAL&quot; |
| REJECTED | &quot;REJECTED&quot; |
| TOO_EXPENSIVE | &quot;TOO_EXPENSIVE&quot; |
| INCOMPLETE_DATA | &quot;INCOMPLETE_DATA&quot; |
| POTENTIAL | &quot;POTENTIAL&quot; |
| NOT_CONFIRMED | &quot;NOT_CONFIRMED&quot; |



