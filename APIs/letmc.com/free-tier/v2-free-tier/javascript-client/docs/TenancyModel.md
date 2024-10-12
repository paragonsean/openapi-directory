# LetMcApiV2FreeTier1.TenancyModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertiseFrom** | **Date** | The date to advertise this tenancy from. | [optional] 
**area** | **String** | The area containing the instruction. | [optional] 
**bondRequired** | **Number** | The total bond required. | [optional] 
**branch** | **String** | The branch the tenancy is assigned to.. | [optional] 
**eTag** | **String** | A unique identifier defining the object and change revision. | [optional] 
**furnished** | **String** | The property furnished type. | [optional] 
**globalReference** | **String** | The global reference for a tenancy. | [optional] 
**isShareProperty** | **Boolean** | Is this property a shared property. | [optional] 
**isStudentProperty** | **Boolean** | Is this property a student property. | [optional] 
**isTenancyAdvertised** | **Boolean** | Gets a value indicating whether this tenancy is being advertised. Note              that this will only return true while the tenancy has a valid advertise              date. It will not return true in the proposed phase. | [optional] 
**isTenancyProposed** | **Boolean** | Is the tenancy a proposed tenancy? | [optional] 
**maximumTenants** | **Number** | The maximum number of tenants to advertise for. | [optional] 
**minimumTenants** | **Number** | The minimum number of tenants to advertise for. | [optional] 
**OID** | **String** | The unique Object ID (OID). | [optional] 
**rentAdvertised** | **Number** | The advertised amount of rent for the property. | [optional] 
**rentRecurrence** | **Number** | The rent schedule recurrence | [optional] 
**rentSchedule** | **String** | The tenancy rent schedule | [optional] 
**tenancyProperty** | **String** | The property linked to this tenancy. | [optional] 
**tenantSystemTypes** | **[String]** | The specific tenant type list, or empty if for all types. | [optional] 
**termMaximum** | **Number** | The instruction maximum term. | [optional] 
**termMinimum** | **Number** | The minimum term. | [optional] 
**termStart** | **Date** | The instruction start date. | [optional] 
**utilityCouncilTax** | **String** | Who&#39;s responsible for council tax bills. | [optional] 
**utilityElectricity** | **String** | Who&#39;s responsible for electricity bills. | [optional] 
**utilityGas** | **String** | Who&#39;s responsible for Gas bills. | [optional] 
**utilityTelephone** | **String** | Who&#39;s responsible for telephone bills. | [optional] 
**utilityWater** | **String** | Who&#39;s responsible for water bills. | [optional] 



## Enum: FurnishedEnum


* `Unfurnished` (value: `"Unfurnished"`)

* `PartFurnished` (value: `"PartFurnished"`)

* `Furnished` (value: `"Furnished"`)





## Enum: RentScheduleEnum


* `Once` (value: `"Once"`)

* `Daily` (value: `"Daily"`)

* `Weekly` (value: `"Weekly"`)

* `Monthly` (value: `"Monthly"`)

* `Yearly` (value: `"Yearly"`)





## Enum: [TenantSystemTypesEnum]


* `Employed` (value: `"Employed"`)

* `SelfEmployed` (value: `"SelfEmployed"`)

* `Unemployed` (value: `"Unemployed"`)

* `Student` (value: `"Student"`)

* `OwnMeans` (value: `"OwnMeans"`)

* `Retired` (value: `"Retired"`)

* `Company` (value: `"Company"`)

* `Council` (value: `"Council"`)





## Enum: UtilityCouncilTaxEnum


* `Tenant` (value: `"Tenant"`)

* `Landlord` (value: `"Landlord"`)





## Enum: UtilityElectricityEnum


* `Tenant` (value: `"Tenant"`)

* `Landlord` (value: `"Landlord"`)





## Enum: UtilityGasEnum


* `Tenant` (value: `"Tenant"`)

* `Landlord` (value: `"Landlord"`)





## Enum: UtilityTelephoneEnum


* `Tenant` (value: `"Tenant"`)

* `Landlord` (value: `"Landlord"`)





## Enum: UtilityWaterEnum


* `Tenant` (value: `"Tenant"`)

* `Landlord` (value: `"Landlord"`)




