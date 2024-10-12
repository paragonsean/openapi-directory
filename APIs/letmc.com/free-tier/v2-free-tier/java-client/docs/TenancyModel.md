

# TenancyModel

Represents a single tenancy on a property structure. This class may              be considered to be the context of the tenancy strategy pattern. The              strategy is the tenancy service, that dictates the algorithm applied              to the tenancy. This class therefore holds the raw data of a tenancy,              and ignores any tenancy service (fully managed, let only) parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertiseFrom** | **OffsetDateTime** | The date to advertise this tenancy from. |  [optional] |
|**area** | **String** | The area containing the instruction. |  [optional] |
|**bondRequired** | **Double** | The total bond required. |  [optional] |
|**branch** | **String** | The branch the tenancy is assigned to.. |  [optional] |
|**etag** | **String** | A unique identifier defining the object and change revision. |  [optional] |
|**furnished** | [**FurnishedEnum**](#FurnishedEnum) | The property furnished type. |  [optional] |
|**globalReference** | **String** | The global reference for a tenancy. |  [optional] |
|**isShareProperty** | **Boolean** | Is this property a shared property. |  [optional] |
|**isStudentProperty** | **Boolean** | Is this property a student property. |  [optional] |
|**isTenancyAdvertised** | **Boolean** | Gets a value indicating whether this tenancy is being advertised. Note              that this will only return true while the tenancy has a valid advertise              date. It will not return true in the proposed phase. |  [optional] |
|**isTenancyProposed** | **Boolean** | Is the tenancy a proposed tenancy? |  [optional] |
|**maximumTenants** | **Integer** | The maximum number of tenants to advertise for. |  [optional] |
|**minimumTenants** | **Integer** | The minimum number of tenants to advertise for. |  [optional] |
|**OID** | **String** | The unique Object ID (OID). |  [optional] |
|**rentAdvertised** | **Double** | The advertised amount of rent for the property. |  [optional] |
|**rentRecurrence** | **Integer** | The rent schedule recurrence |  [optional] |
|**rentSchedule** | [**RentScheduleEnum**](#RentScheduleEnum) | The tenancy rent schedule |  [optional] |
|**tenancyProperty** | **String** | The property linked to this tenancy. |  [optional] |
|**tenantSystemTypes** | [**List&lt;TenantSystemTypesEnum&gt;**](#List&lt;TenantSystemTypesEnum&gt;) | The specific tenant type list, or empty if for all types. |  [optional] |
|**termMaximum** | **Integer** | The instruction maximum term. |  [optional] |
|**termMinimum** | **Integer** | The minimum term. |  [optional] |
|**termStart** | **OffsetDateTime** | The instruction start date. |  [optional] |
|**utilityCouncilTax** | [**UtilityCouncilTaxEnum**](#UtilityCouncilTaxEnum) | Who&#39;s responsible for council tax bills. |  [optional] |
|**utilityElectricity** | [**UtilityElectricityEnum**](#UtilityElectricityEnum) | Who&#39;s responsible for electricity bills. |  [optional] |
|**utilityGas** | [**UtilityGasEnum**](#UtilityGasEnum) | Who&#39;s responsible for Gas bills. |  [optional] |
|**utilityTelephone** | [**UtilityTelephoneEnum**](#UtilityTelephoneEnum) | Who&#39;s responsible for telephone bills. |  [optional] |
|**utilityWater** | [**UtilityWaterEnum**](#UtilityWaterEnum) | Who&#39;s responsible for water bills. |  [optional] |



## Enum: FurnishedEnum

| Name | Value |
|---- | -----|
| UNFURNISHED | &quot;Unfurnished&quot; |
| PART_FURNISHED | &quot;PartFurnished&quot; |
| FURNISHED | &quot;Furnished&quot; |



## Enum: RentScheduleEnum

| Name | Value |
|---- | -----|
| ONCE | &quot;Once&quot; |
| DAILY | &quot;Daily&quot; |
| WEEKLY | &quot;Weekly&quot; |
| MONTHLY | &quot;Monthly&quot; |
| YEARLY | &quot;Yearly&quot; |



## Enum: List&lt;TenantSystemTypesEnum&gt;

| Name | Value |
|---- | -----|
| EMPLOYED | &quot;Employed&quot; |
| SELF_EMPLOYED | &quot;SelfEmployed&quot; |
| UNEMPLOYED | &quot;Unemployed&quot; |
| STUDENT | &quot;Student&quot; |
| OWN_MEANS | &quot;OwnMeans&quot; |
| RETIRED | &quot;Retired&quot; |
| COMPANY | &quot;Company&quot; |
| COUNCIL | &quot;Council&quot; |



## Enum: UtilityCouncilTaxEnum

| Name | Value |
|---- | -----|
| TENANT | &quot;Tenant&quot; |
| LANDLORD | &quot;Landlord&quot; |



## Enum: UtilityElectricityEnum

| Name | Value |
|---- | -----|
| TENANT | &quot;Tenant&quot; |
| LANDLORD | &quot;Landlord&quot; |



## Enum: UtilityGasEnum

| Name | Value |
|---- | -----|
| TENANT | &quot;Tenant&quot; |
| LANDLORD | &quot;Landlord&quot; |



## Enum: UtilityTelephoneEnum

| Name | Value |
|---- | -----|
| TENANT | &quot;Tenant&quot; |
| LANDLORD | &quot;Landlord&quot; |



## Enum: UtilityWaterEnum

| Name | Value |
|---- | -----|
| TENANT | &quot;Tenant&quot; |
| LANDLORD | &quot;Landlord&quot; |



