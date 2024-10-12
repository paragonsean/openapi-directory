

# KpiDefinition

Defines the KPI Threshold limits.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aliases** | [**List&lt;KpiAlias&gt;**](KpiAlias.md) | The aliases. |  [optional] |
|**calculationWindow** | [**CalculationWindowEnum**](#CalculationWindowEnum) | The calculation window. |  |
|**calculationWindowFieldName** | **String** | Name of calculation window field. |  [optional] |
|**description** | **Map&lt;String, String&gt;** | Localized description for the KPI. |  [optional] |
|**displayName** | **Map&lt;String, String&gt;** | Localized display name for the KPI. |  [optional] |
|**entityType** | [**EntityTypeEnum**](#EntityTypeEnum) | The mapping entity type. |  |
|**entityTypeName** | **String** | The mapping entity name. |  |
|**expression** | **String** | The computation expression for the KPI. |  |
|**extracts** | [**List&lt;KpiExtract&gt;**](KpiExtract.md) | The KPI extracts. |  [optional] |
|**filter** | **String** | The filter expression for the KPI. |  [optional] |
|**function** | [**FunctionEnum**](#FunctionEnum) | The computation function for the KPI. |  |
|**groupBy** | **List&lt;String&gt;** | the group by properties for the KPI. |  [optional] |
|**groupByMetadata** | [**List&lt;KpiGroupByMetadata&gt;**](KpiGroupByMetadata.md) | The KPI GroupByMetadata. |  [optional] [readonly] |
|**kpiName** | **String** | The KPI name. |  [optional] [readonly] |
|**participantProfilesMetadata** | [**List&lt;KpiParticipantProfilesMetadata&gt;**](KpiParticipantProfilesMetadata.md) | The participant profiles. |  [optional] [readonly] |
|**provisioningState** | **ProvisioningState** |  |  [optional] |
|**tenantId** | **String** | The hub name. |  [optional] [readonly] |
|**thresHolds** | [**KpiThresholds**](KpiThresholds.md) |  |  [optional] |
|**unit** | **String** | The unit of measurement for the KPI. |  [optional] |



## Enum: CalculationWindowEnum

| Name | Value |
|---- | -----|
| LIFETIME | &quot;Lifetime&quot; |
| HOUR | &quot;Hour&quot; |
| DAY | &quot;Day&quot; |
| WEEK | &quot;Week&quot; |
| MONTH | &quot;Month&quot; |



## Enum: EntityTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| PROFILE | &quot;Profile&quot; |
| INTERACTION | &quot;Interaction&quot; |
| RELATIONSHIP | &quot;Relationship&quot; |



## Enum: FunctionEnum

| Name | Value |
|---- | -----|
| SUM | &quot;Sum&quot; |
| AVG | &quot;Avg&quot; |
| MIN | &quot;Min&quot; |
| MAX | &quot;Max&quot; |
| LAST | &quot;Last&quot; |
| COUNT | &quot;Count&quot; |
| NONE | &quot;None&quot; |
| COUNT_DISTINCT | &quot;CountDistinct&quot; |



