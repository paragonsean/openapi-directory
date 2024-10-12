

# AssessmentProperties

Properties of an assessment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**azureDiskType** | [**AzureDiskTypeEnum**](#AzureDiskTypeEnum) | Storage type selected for this disk. |  |
|**azureHybridUseBenefit** | [**AzureHybridUseBenefitEnum**](#AzureHybridUseBenefitEnum) | AHUB discount on windows virtual machines. |  |
|**azureLocation** | [**AzureLocationEnum**](#AzureLocationEnum) | Target Azure location for which the machines should be assessed. These enums are the same as used by Compute API. |  |
|**azureOfferCode** | [**AzureOfferCodeEnum**](#AzureOfferCodeEnum) | Offer code according to which cost estimation is done. |  |
|**azurePricingTier** | [**AzurePricingTierEnum**](#AzurePricingTierEnum) | Pricing tier for Size evaluation. |  |
|**azureStorageRedundancy** | [**AzureStorageRedundancyEnum**](#AzureStorageRedundancyEnum) | Storage Redundancy type offered by Azure. |  |
|**azureVmFamilies** | [**List&lt;AzureVmFamiliesEnum&gt;**](#List&lt;AzureVmFamiliesEnum&gt;) | List of azure VM families. |  |
|**confidenceRatingInPercentage** | **Double** | Confidence rating percentage for assessment. Can be in the range [0, 100]. |  [optional] [readonly] |
|**createdTimestamp** | **OffsetDateTime** | Time when this project was created. Date-Time represented in ISO-8601 format. |  [optional] [readonly] |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | Currency to report prices in. |  |
|**discountPercentage** | **Double** | Custom discount percentage to be applied on final costs. Can be in the range [0, 100]. |  |
|**eaSubscriptionId** | **String** | Enterprise agreement subscription arm id. |  [optional] [readonly] |
|**monthlyBandwidthCost** | **Double** | Monthly network cost estimate for the machines that are part of this assessment as a group, for a 31-day month. |  [optional] [readonly] |
|**monthlyComputeCost** | **Double** | Monthly compute cost estimate for the machines that are part of this assessment as a group, for a 31-day month. |  [optional] [readonly] |
|**monthlyPremiumStorageCost** | **Double** | Monthly premium storage cost estimate for the machines that are part of this assessment as a group, for a 31-day month. |  [optional] [readonly] |
|**monthlyStandardSSDStorageCost** | **Double** | Monthly standard SSD storage cost estimate for the machines that are part of this assessment as a group, for a 31-day month. |  [optional] [readonly] |
|**monthlyStorageCost** | **Double** | Monthly storage cost estimate for the machines that are part of this assessment as a group, for a 31-day month. |  [optional] [readonly] |
|**numberOfMachines** | **Integer** | Number of assessed machines part of this assessment. |  [optional] [readonly] |
|**percentile** | [**PercentileEnum**](#PercentileEnum) | Percentile of performance data used to recommend Azure size. |  |
|**perfDataEndTime** | **OffsetDateTime** | End time to consider performance data for assessment |  [optional] [readonly] |
|**perfDataStartTime** | **OffsetDateTime** | Start time to consider performance data for assessment |  [optional] [readonly] |
|**pricesTimestamp** | **OffsetDateTime** | Time when the Azure Prices were queried. Date-Time represented in ISO-8601 format. |  [optional] [readonly] |
|**reservedInstance** | [**ReservedInstanceEnum**](#ReservedInstanceEnum) | Azure reserved instance. |  |
|**scalingFactor** | **Double** | Scaling factor used over utilization data to add a performance buffer for new machines to be created in Azure. Min Value &#x3D; 1.0, Max value &#x3D; 1.9, Default &#x3D; 1.3. |  |
|**sizingCriterion** | [**SizingCriterionEnum**](#SizingCriterionEnum) | Assessment sizing criterion. |  |
|**stage** | [**StageEnum**](#StageEnum) | User configurable setting that describes the status of the assessment. |  |
|**status** | [**StatusEnum**](#StatusEnum) | Whether the assessment has been created and is valid. |  [optional] [readonly] |
|**timeRange** | [**TimeRangeEnum**](#TimeRangeEnum) | Time range of performance data used to recommend a size. |  |
|**updatedTimestamp** | **OffsetDateTime** | Time when this project was last updated. Date-Time represented in ISO-8601 format. |  [optional] [readonly] |
|**vmUptime** | [**VmUptime**](VmUptime.md) |  |  |



## Enum: AzureDiskTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |
| STANDARD_SSD | &quot;StandardSSD&quot; |
| STANDARD_OR_PREMIUM | &quot;StandardOrPremium&quot; |



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
| GERMANY_CENTRAL | &quot;GermanyCentral&quot; |
| GERMANY_NORTHEAST | &quot;GermanyNortheast&quot; |
| CHINA_NORTH | &quot;ChinaNorth&quot; |
| CHINA_EAST | &quot;ChinaEast&quot; |
| US_GOV_ARIZONA | &quot;USGovArizona&quot; |
| US_GOV_TEXAS | &quot;USGovTexas&quot; |
| US_GOV_IOWA | &quot;USGovIowa&quot; |
| US_GOV_VIRGINIA | &quot;USGovVirginia&quot; |
| USDO_D_CENTRAL | &quot;USDoDCentral&quot; |
| USDO_D_EAST | &quot;USDoDEast&quot; |



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
| MSMCAZR0044_P | &quot;MSMCAZR0044P&quot; |
| MSMCAZR0059_P | &quot;MSMCAZR0059P&quot; |
| MSMCAZR0060_P | &quot;MSMCAZR0060P&quot; |
| MSMCAZR0063_P | &quot;MSMCAZR0063P&quot; |
| MSMCAZR0120_P | &quot;MSMCAZR0120P&quot; |
| MSMCAZR0121_P | &quot;MSMCAZR0121P&quot; |
| MSMCAZR0125_P | &quot;MSMCAZR0125P&quot; |
| MSMCAZR0128_P | &quot;MSMCAZR0128P&quot; |
| MSAZRDE0003_P | &quot;MSAZRDE0003P&quot; |
| MSAZRDE0044_P | &quot;MSAZRDE0044P&quot; |
| MSAZRUSGOV0003_P | &quot;MSAZRUSGOV0003P&quot; |
| EA | &quot;EA&quot; |



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



## Enum: List&lt;AzureVmFamiliesEnum&gt;

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| BASIC_A0_A4 | &quot;Basic_A0_A4&quot; |
| STANDARD_A0_A7 | &quot;Standard_A0_A7&quot; |
| STANDARD_A8_A11 | &quot;Standard_A8_A11&quot; |
| AV2_SERIES | &quot;Av2_series&quot; |
| D_SERIES | &quot;D_series&quot; |
| DV2_SERIES | &quot;Dv2_series&quot; |
| DS_SERIES | &quot;DS_series&quot; |
| DSV2_SERIES | &quot;DSv2_series&quot; |
| F_SERIES | &quot;F_series&quot; |
| FS_SERIES | &quot;Fs_series&quot; |
| G_SERIES | &quot;G_series&quot; |
| GS_SERIES | &quot;GS_series&quot; |
| H_SERIES | &quot;H_series&quot; |
| LS_SERIES | &quot;Ls_series&quot; |
| DSV3_SERIES | &quot;Dsv3_series&quot; |
| DV3_SERIES | &quot;Dv3_series&quot; |
| FSV2_SERIES | &quot;Fsv2_series&quot; |
| EV3_SERIES | &quot;Ev3_series&quot; |
| ESV3_SERIES | &quot;Esv3_series&quot; |
| M_SERIES | &quot;M_series&quot; |
| DC_SERIES | &quot;DC_Series&quot; |



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
| CNY | &quot;CNY&quot; |



## Enum: PercentileEnum

| Name | Value |
|---- | -----|
| PERCENTILE50 | &quot;Percentile50&quot; |
| PERCENTILE90 | &quot;Percentile90&quot; |
| PERCENTILE95 | &quot;Percentile95&quot; |
| PERCENTILE99 | &quot;Percentile99&quot; |



## Enum: ReservedInstanceEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| RI1_YEAR | &quot;RI1Year&quot; |
| RI3_YEAR | &quot;RI3Year&quot; |



## Enum: SizingCriterionEnum

| Name | Value |
|---- | -----|
| PERFORMANCE_BASED | &quot;PerformanceBased&quot; |
| AS_ON_PREMISES | &quot;AsOnPremises&quot; |



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
| OUT_OF_SYNC | &quot;OutOfSync&quot; |
| OUT_DATED | &quot;OutDated&quot; |



## Enum: TimeRangeEnum

| Name | Value |
|---- | -----|
| DAY | &quot;Day&quot; |
| WEEK | &quot;Week&quot; |
| MONTH | &quot;Month&quot; |
| CUSTOM | &quot;Custom&quot; |



