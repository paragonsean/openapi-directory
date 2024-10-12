

# AssessmentProperties

Properties of an assessment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**azureHybridUseBenefit** | [**AzureHybridUseBenefitEnum**](#AzureHybridUseBenefitEnum) | AHUB discount on windows virtual machines. |  |
|**azureLocation** | [**AzureLocationEnum**](#AzureLocationEnum) | Target Azure location for which the machines should be assessed. These enums are the same as used by Compute API. |  |
|**azureOfferCode** | [**AzureOfferCodeEnum**](#AzureOfferCodeEnum) | Offer code according to which cost estimation is done. |  |
|**azurePricingTier** | [**AzurePricingTierEnum**](#AzurePricingTierEnum) | Pricing tier for Size evaluation. |  |
|**azureStorageRedundancy** | [**AzureStorageRedundancyEnum**](#AzureStorageRedundancyEnum) | Storage Redundancy type offered by Azure. |  |
|**createdTimestamp** | **OffsetDateTime** | Time when this project was created. Date-Time represented in ISO-8601 format. |  [optional] [readonly] |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | Currency to report prices in. |  |
|**discountPercentage** | **Double** | Custom discount percentage to be applied on final costs. Can be in the range [0, 100]. |  |
|**monthlyBandwidthCost** | **Double** | Monthly network cost estimate for the machines that are part of this assessment as a group, for a 31-day month. |  [optional] [readonly] |
|**monthlyComputeCost** | **Double** | Monthly compute cost estimate for the machines that are part of this assessment as a group, for a 31-day month. |  [optional] [readonly] |
|**monthlyStorageCost** | **Double** | Monthly storage cost estimate for the machines that are part of this assessment as a group, for a 31-day month. |  [optional] [readonly] |
|**numberOfMachines** | **Integer** | Number of assessed machines part of this assessment. |  [optional] [readonly] |
|**percentile** | [**PercentileEnum**](#PercentileEnum) | Percentile of performance data used to recommend Azure size. |  |
|**pricesTimestamp** | **OffsetDateTime** | Time when the Azure Prices were queried. Date-Time represented in ISO-8601 format. |  [optional] [readonly] |
|**scalingFactor** | **Double** | Scaling factor used over utilization data to add a performance buffer for new machines to be created in Azure. Min Value &#x3D; 1.0, Max value &#x3D; 1.9, Default &#x3D; 1.3. |  |
|**stage** | [**StageEnum**](#StageEnum) | User configurable setting that describes the status of the assessment. |  |
|**status** | [**StatusEnum**](#StatusEnum) | Whether the assessment has been created and is valid. |  [optional] [readonly] |
|**timeRange** | [**TimeRangeEnum**](#TimeRangeEnum) | Time range of performance data used to recommend a size. |  |
|**updatedTimestamp** | **OffsetDateTime** | Time when this project was last updated. Date-Time represented in ISO-8601 format. |  [optional] [readonly] |



## Enum: AzureHybridUseBenefitEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| YES | &quot;Yes&quot; |
| NO | &quot;No&quot; |



## Enum: AzureLocationEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| EAST_ASIA | &quot;EastAsia&quot; |
| SOUTHEAST_ASIA | &quot;SoutheastAsia&quot; |
| AUSTRALIA_EAST | &quot;AustraliaEast&quot; |
| AUSTRALIA_SOUTHEAST | &quot;AustraliaSoutheast&quot; |
| BRAZIL_SOUTH | &quot;BrazilSouth&quot; |
| CANADA_CENTRAL | &quot;CanadaCentral&quot; |
| CANADA_EAST | &quot;CanadaEast&quot; |
| WEST_EUROPE | &quot;WestEurope&quot; |
| NORTH_EUROPE | &quot;NorthEurope&quot; |
| CENTRAL_INDIA | &quot;CentralIndia&quot; |
| SOUTH_INDIA | &quot;SouthIndia&quot; |
| WEST_INDIA | &quot;WestIndia&quot; |
| JAPAN_EAST | &quot;JapanEast&quot; |
| JAPAN_WEST | &quot;JapanWest&quot; |
| KOREA_CENTRAL | &quot;KoreaCentral&quot; |
| KOREA_SOUTH | &quot;KoreaSouth&quot; |
| UK_WEST | &quot;UkWest&quot; |
| UK_SOUTH | &quot;UkSouth&quot; |
| NORTH_CENTRAL_US | &quot;NorthCentralUs&quot; |
| EAST_US | &quot;EastUs&quot; |
| WEST_US2 | &quot;WestUs2&quot; |
| SOUTH_CENTRAL_US | &quot;SouthCentralUs&quot; |
| CENTRAL_US | &quot;CentralUs&quot; |
| EAST_US2 | &quot;EastUs2&quot; |
| WEST_US | &quot;WestUs&quot; |
| WEST_CENTRAL_US | &quot;WestCentralUs&quot; |



## Enum: AzureOfferCodeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| MSAZR0003_P | &quot;MSAZR0003P&quot; |
| MSAZR0044_P | &quot;MSAZR0044P&quot; |
| MSAZR0059_P | &quot;MSAZR0059P&quot; |
| MSAZR0060_P | &quot;MSAZR0060P&quot; |
| MSAZR0062_P | &quot;MSAZR0062P&quot; |
| MSAZR0063_P | &quot;MSAZR0063P&quot; |
| MSAZR0064_P | &quot;MSAZR0064P&quot; |
| MSAZR0029_P | &quot;MSAZR0029P&quot; |
| MSAZR0022_P | &quot;MSAZR0022P&quot; |
| MSAZR0023_P | &quot;MSAZR0023P&quot; |
| MSAZR0148_P | &quot;MSAZR0148P&quot; |
| MSAZR0025_P | &quot;MSAZR0025P&quot; |
| MSAZR0036_P | &quot;MSAZR0036P&quot; |
| MSAZR0120_P | &quot;MSAZR0120P&quot; |
| MSAZR0121_P | &quot;MSAZR0121P&quot; |
| MSAZR0122_P | &quot;MSAZR0122P&quot; |
| MSAZR0123_P | &quot;MSAZR0123P&quot; |
| MSAZR0124_P | &quot;MSAZR0124P&quot; |
| MSAZR0125_P | &quot;MSAZR0125P&quot; |
| MSAZR0126_P | &quot;MSAZR0126P&quot; |
| MSAZR0127_P | &quot;MSAZR0127P&quot; |
| MSAZR0128_P | &quot;MSAZR0128P&quot; |
| MSAZR0129_P | &quot;MSAZR0129P&quot; |
| MSAZR0130_P | &quot;MSAZR0130P&quot; |
| MSAZR0111_P | &quot;MSAZR0111P&quot; |
| MSAZR0144_P | &quot;MSAZR0144P&quot; |
| MSAZR0149_P | &quot;MSAZR0149P&quot; |



## Enum: AzurePricingTierEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |
| BASIC | &quot;Basic&quot; |



## Enum: AzureStorageRedundancyEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| LOCALLY_REDUNDANT | &quot;LocallyRedundant&quot; |
| ZONE_REDUNDANT | &quot;ZoneRedundant&quot; |
| GEO_REDUNDANT | &quot;GeoRedundant&quot; |
| READ_ACCESS_GEO_REDUNDANT | &quot;ReadAccessGeoRedundant&quot; |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| USD | &quot;USD&quot; |
| DKK | &quot;DKK&quot; |
| CAD | &quot;CAD&quot; |
| IDR | &quot;IDR&quot; |
| JPY | &quot;JPY&quot; |
| KRW | &quot;KRW&quot; |
| NZD | &quot;NZD&quot; |
| NOK | &quot;NOK&quot; |
| RUB | &quot;RUB&quot; |
| SAR | &quot;SAR&quot; |
| ZAR | &quot;ZAR&quot; |
| SEK | &quot;SEK&quot; |
| TRY | &quot;TRY&quot; |
| GBP | &quot;GBP&quot; |
| MXN | &quot;MXN&quot; |
| MYR | &quot;MYR&quot; |
| INR | &quot;INR&quot; |
| HKD | &quot;HKD&quot; |
| BRL | &quot;BRL&quot; |
| TWD | &quot;TWD&quot; |
| EUR | &quot;EUR&quot; |
| CHF | &quot;CHF&quot; |
| ARS | &quot;ARS&quot; |
| AUD | &quot;AUD&quot; |



## Enum: PercentileEnum

| Name | Value |
|---- | -----|
| PERCENTILE50 | &quot;Percentile50&quot; |
| PERCENTILE90 | &quot;Percentile90&quot; |
| PERCENTILE95 | &quot;Percentile95&quot; |
| PERCENTILE99 | &quot;Percentile99&quot; |



## Enum: StageEnum

| Name | Value |
|---- | -----|
| IN_PROGRESS | &quot;InProgress&quot; |
| UNDER_REVIEW | &quot;UnderReview&quot; |
| APPROVED | &quot;Approved&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;Created&quot; |
| UPDATED | &quot;Updated&quot; |
| RUNNING | &quot;Running&quot; |
| COMPLETED | &quot;Completed&quot; |
| INVALID | &quot;Invalid&quot; |



## Enum: TimeRangeEnum

| Name | Value |
|---- | -----|
| DAY | &quot;Day&quot; |
| WEEK | &quot;Week&quot; |
| MONTH | &quot;Month&quot; |



