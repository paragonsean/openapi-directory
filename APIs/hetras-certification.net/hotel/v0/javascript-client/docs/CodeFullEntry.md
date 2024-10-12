# HetrasHotelApiVersion0.CodeFullEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**{String: LinkObject}**](LinkObject.md) | Collection of links to related resources | [optional] 
**code** | **String** | The code value. This value you will see in reservations as market code and in other              resources like the revenue buckets in transactions | [optional] 
**comment** | **String** | The comment for this code | [optional] 
**_default** | **Boolean** | This attribute tells you if this code is the default code for the specific type or not.              Not all the types of codes need to have a default code | [optional] 
**id** | **String** | The id of the code | [optional] 
**name** | **String** | The name of the code that usually is more human readable | [optional] 
**parent** | [**CodeBaseEntry**](CodeBaseEntry.md) |  | [optional] 
**type** | **String** | The type or category of the code | [optional] 



## Enum: TypeEnum


* `GuestRequest` (value: `"GuestRequest"`)

* `RequestDietary` (value: `"RequestDietary"`)

* `VIPStatus` (value: `"VIPStatus"`)

* `ReasonForRateChange` (value: `"ReasonForRateChange"`)

* `Regrets` (value: `"Regrets"`)

* `MarketSegments` (value: `"MarketSegments"`)

* `SourceOfBusiness` (value: `"SourceOfBusiness"`)

* `LoyaltyProgram` (value: `"LoyaltyProgram"`)

* `CancellationReason` (value: `"CancellationReason"`)

* `AccountType` (value: `"AccountType"`)

* `AccountRank` (value: `"AccountRank"`)

* `VIPLevel` (value: `"VIPLevel"`)

* `Title` (value: `"Title"`)

* `ContactFunction` (value: `"ContactFunction"`)

* `Territory` (value: `"Territory"`)

* `CorrespondenceType` (value: `"CorrespondenceType"`)

* `ExternalProgramType` (value: `"ExternalProgramType"`)

* `RevenueBucket` (value: `"RevenueBucket"`)

* `AdditionalRevenueBucket` (value: `"AdditionalRevenueBucket"`)

* `AdditionalStatisticsBuckets` (value: `"AdditionalStatisticsBuckets"`)

* `MealPeriod` (value: `"MealPeriod"`)

* `BillingCycle` (value: `"BillingCycle"`)

* `ReminderCycle` (value: `"ReminderCycle"`)

* `MajorMarketSegments` (value: `"MajorMarketSegments"`)

* `DocumentType` (value: `"DocumentType"`)

* `ActivityType` (value: `"ActivityType"`)

* `ReservationLabels` (value: `"ReservationLabels"`)




