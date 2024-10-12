# AdvicentFactFinderService.ILifeInsurancePolicyDomainObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beneficiary** | **String** |  | [optional] 
**beneficiaryDependentId** | **Number** |  | [optional] 
**benefit** | **Number** |  | [optional] 
**description** | **String** |  | [optional] 
**externalDestinationId** | **String** |  | [optional] 
**factFinderId** | **Number** |  | [optional] 
**frequency** | **Number** |  | [optional] 
**generalAccountMarketValue** | **Number** |  | [optional] 
**insured** | **String** |  | [optional] 
**lifeInsurancePolicyId** | **Number** |  | [optional] 
**payer** | **String** |  | [optional] 
**policyType** | **Number** |  | [optional] 
**premium** | **Number** |  | [optional] 
**subaccounts** | [**[LifeInsurancePolicySubaccountDomainObject]**](LifeInsurancePolicySubaccountDomainObject.md) |  | [optional] 



## Enum: BeneficiaryEnum


* `Client` (value: `"Client"`)

* `CoClient` (value: `"CoClient"`)

* `Dependent` (value: `"Dependent"`)

* `Other` (value: `"Other"`)





## Enum: InsuredEnum


* `Client` (value: `"Client"`)

* `CoClient` (value: `"CoClient"`)

* `FirstToDie` (value: `"FirstToDie"`)

* `SecondToDie` (value: `"SecondToDie"`)

* `Other` (value: `"Other"`)





## Enum: PayerEnum


* `Client` (value: `"Client"`)

* `CoClient` (value: `"CoClient"`)

* `Joint` (value: `"Joint"`)

* `Other` (value: `"Other"`)




