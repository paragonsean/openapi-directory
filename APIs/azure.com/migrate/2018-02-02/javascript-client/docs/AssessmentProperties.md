# AzureMigrate.AssessmentProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azureHybridUseBenefit** | **String** | AHUB discount on windows virtual machines. | 
**azureLocation** | **String** | Target Azure location for which the machines should be assessed. These enums are the same as used by Compute API. | 
**azureOfferCode** | **String** | Offer code according to which cost estimation is done. | 
**azurePricingTier** | **String** | Pricing tier for Size evaluation. | 
**azureStorageRedundancy** | **String** | Storage Redundancy type offered by Azure. | 
**confidenceRatingInPercentage** | **Number** | Confidence rating percentage for assessment. Can be in the range [0, 100]. | [optional] [readonly] 
**createdTimestamp** | **Date** | Time when this project was created. Date-Time represented in ISO-8601 format. | [optional] [readonly] 
**currency** | **String** | Currency to report prices in. | 
**discountPercentage** | **Number** | Custom discount percentage to be applied on final costs. Can be in the range [0, 100]. | 
**monthlyBandwidthCost** | **Number** | Monthly network cost estimate for the machines that are part of this assessment as a group, for a 31-day month. | [optional] [readonly] 
**monthlyComputeCost** | **Number** | Monthly compute cost estimate for the machines that are part of this assessment as a group, for a 31-day month. | [optional] [readonly] 
**monthlyStorageCost** | **Number** | Monthly storage cost estimate for the machines that are part of this assessment as a group, for a 31-day month. | [optional] [readonly] 
**numberOfMachines** | **Number** | Number of assessed machines part of this assessment. | [optional] [readonly] 
**percentile** | **String** | Percentile of performance data used to recommend Azure size. | 
**pricesTimestamp** | **Date** | Time when the Azure Prices were queried. Date-Time represented in ISO-8601 format. | [optional] [readonly] 
**scalingFactor** | **Number** | Scaling factor used over utilization data to add a performance buffer for new machines to be created in Azure. Min Value &#x3D; 1.0, Max value &#x3D; 1.9, Default &#x3D; 1.3. | 
**sizingCriterion** | **String** | Assessment sizing criterion. | 
**stage** | **String** | User configurable setting that describes the status of the assessment. | 
**status** | **String** | Whether the assessment has been created and is valid. | [optional] [readonly] 
**timeRange** | **String** | Time range of performance data used to recommend a size. | 
**updatedTimestamp** | **Date** | Time when this project was last updated. Date-Time represented in ISO-8601 format. | [optional] [readonly] 



## Enum: AzureHybridUseBenefitEnum


* `Unknown` (value: `"Unknown"`)

* `Yes` (value: `"Yes"`)

* `No` (value: `"No"`)





## Enum: AzureLocationEnum


* `Unknown` (value: `"Unknown"`)

* `EastAsia` (value: `"EastAsia"`)

* `SoutheastAsia` (value: `"SoutheastAsia"`)

* `AustraliaEast` (value: `"AustraliaEast"`)

* `AustraliaSoutheast` (value: `"AustraliaSoutheast"`)

* `BrazilSouth` (value: `"BrazilSouth"`)

* `CanadaCentral` (value: `"CanadaCentral"`)

* `CanadaEast` (value: `"CanadaEast"`)

* `WestEurope` (value: `"WestEurope"`)

* `NorthEurope` (value: `"NorthEurope"`)

* `CentralIndia` (value: `"CentralIndia"`)

* `SouthIndia` (value: `"SouthIndia"`)

* `WestIndia` (value: `"WestIndia"`)

* `JapanEast` (value: `"JapanEast"`)

* `JapanWest` (value: `"JapanWest"`)

* `KoreaCentral` (value: `"KoreaCentral"`)

* `KoreaSouth` (value: `"KoreaSouth"`)

* `UkWest` (value: `"UkWest"`)

* `UkSouth` (value: `"UkSouth"`)

* `NorthCentralUs` (value: `"NorthCentralUs"`)

* `EastUs` (value: `"EastUs"`)

* `WestUs2` (value: `"WestUs2"`)

* `SouthCentralUs` (value: `"SouthCentralUs"`)

* `CentralUs` (value: `"CentralUs"`)

* `EastUs2` (value: `"EastUs2"`)

* `WestUs` (value: `"WestUs"`)

* `WestCentralUs` (value: `"WestCentralUs"`)

* `GermanyCentral` (value: `"GermanyCentral"`)

* `GermanyNortheast` (value: `"GermanyNortheast"`)

* `ChinaNorth` (value: `"ChinaNorth"`)

* `ChinaEast` (value: `"ChinaEast"`)





## Enum: AzureOfferCodeEnum


* `Unknown` (value: `"Unknown"`)

* `MSAZR0003P` (value: `"MSAZR0003P"`)

* `MSAZR0044P` (value: `"MSAZR0044P"`)

* `MSAZR0059P` (value: `"MSAZR0059P"`)

* `MSAZR0060P` (value: `"MSAZR0060P"`)

* `MSAZR0062P` (value: `"MSAZR0062P"`)

* `MSAZR0063P` (value: `"MSAZR0063P"`)

* `MSAZR0064P` (value: `"MSAZR0064P"`)

* `MSAZR0029P` (value: `"MSAZR0029P"`)

* `MSAZR0022P` (value: `"MSAZR0022P"`)

* `MSAZR0023P` (value: `"MSAZR0023P"`)

* `MSAZR0148P` (value: `"MSAZR0148P"`)

* `MSAZR0025P` (value: `"MSAZR0025P"`)

* `MSAZR0036P` (value: `"MSAZR0036P"`)

* `MSAZR0120P` (value: `"MSAZR0120P"`)

* `MSAZR0121P` (value: `"MSAZR0121P"`)

* `MSAZR0122P` (value: `"MSAZR0122P"`)

* `MSAZR0123P` (value: `"MSAZR0123P"`)

* `MSAZR0124P` (value: `"MSAZR0124P"`)

* `MSAZR0125P` (value: `"MSAZR0125P"`)

* `MSAZR0126P` (value: `"MSAZR0126P"`)

* `MSAZR0127P` (value: `"MSAZR0127P"`)

* `MSAZR0128P` (value: `"MSAZR0128P"`)

* `MSAZR0129P` (value: `"MSAZR0129P"`)

* `MSAZR0130P` (value: `"MSAZR0130P"`)

* `MSAZR0111P` (value: `"MSAZR0111P"`)

* `MSAZR0144P` (value: `"MSAZR0144P"`)

* `MSAZR0149P` (value: `"MSAZR0149P"`)

* `MSMCAZR0044P` (value: `"MSMCAZR0044P"`)

* `MSMCAZR0059P` (value: `"MSMCAZR0059P"`)

* `MSMCAZR0060P` (value: `"MSMCAZR0060P"`)

* `MSMCAZR0063P` (value: `"MSMCAZR0063P"`)

* `MSMCAZR0120P` (value: `"MSMCAZR0120P"`)

* `MSMCAZR0121P` (value: `"MSMCAZR0121P"`)

* `MSMCAZR0125P` (value: `"MSMCAZR0125P"`)

* `MSMCAZR0128P` (value: `"MSMCAZR0128P"`)

* `MSAZRDE0003P` (value: `"MSAZRDE0003P"`)

* `MSAZRDE0044P` (value: `"MSAZRDE0044P"`)





## Enum: AzurePricingTierEnum


* `Standard` (value: `"Standard"`)

* `Basic` (value: `"Basic"`)





## Enum: AzureStorageRedundancyEnum


* `Unknown` (value: `"Unknown"`)

* `LocallyRedundant` (value: `"LocallyRedundant"`)

* `ZoneRedundant` (value: `"ZoneRedundant"`)

* `GeoRedundant` (value: `"GeoRedundant"`)

* `ReadAccessGeoRedundant` (value: `"ReadAccessGeoRedundant"`)





## Enum: CurrencyEnum


* `Unknown` (value: `"Unknown"`)

* `USD` (value: `"USD"`)

* `DKK` (value: `"DKK"`)

* `CAD` (value: `"CAD"`)

* `IDR` (value: `"IDR"`)

* `JPY` (value: `"JPY"`)

* `KRW` (value: `"KRW"`)

* `NZD` (value: `"NZD"`)

* `NOK` (value: `"NOK"`)

* `RUB` (value: `"RUB"`)

* `SAR` (value: `"SAR"`)

* `ZAR` (value: `"ZAR"`)

* `SEK` (value: `"SEK"`)

* `TRY` (value: `"TRY"`)

* `GBP` (value: `"GBP"`)

* `MXN` (value: `"MXN"`)

* `MYR` (value: `"MYR"`)

* `INR` (value: `"INR"`)

* `HKD` (value: `"HKD"`)

* `BRL` (value: `"BRL"`)

* `TWD` (value: `"TWD"`)

* `EUR` (value: `"EUR"`)

* `CHF` (value: `"CHF"`)

* `ARS` (value: `"ARS"`)

* `AUD` (value: `"AUD"`)

* `CNY` (value: `"CNY"`)





## Enum: PercentileEnum


* `Percentile50` (value: `"Percentile50"`)

* `Percentile90` (value: `"Percentile90"`)

* `Percentile95` (value: `"Percentile95"`)

* `Percentile99` (value: `"Percentile99"`)





## Enum: SizingCriterionEnum


* `PerformanceBased` (value: `"PerformanceBased"`)

* `AsOnPremises` (value: `"AsOnPremises"`)





## Enum: StageEnum


* `InProgress` (value: `"InProgress"`)

* `UnderReview` (value: `"UnderReview"`)

* `Approved` (value: `"Approved"`)





## Enum: StatusEnum


* `Created` (value: `"Created"`)

* `Updated` (value: `"Updated"`)

* `Running` (value: `"Running"`)

* `Completed` (value: `"Completed"`)

* `Invalid` (value: `"Invalid"`)





## Enum: TimeRangeEnum


* `Day` (value: `"Day"`)

* `Week` (value: `"Week"`)

* `Month` (value: `"Month"`)




