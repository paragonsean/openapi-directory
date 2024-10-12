# CustomerInsightsManagementClient.EnrichingKpi

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**[KpiAlias]**](KpiAlias.md) | The aliases. | [optional] 
**calculationWindow** | **String** | The calculation window. | 
**calculationWindowFieldName** | **String** | Name of calculation window field. | [optional] 
**description** | **{String: String}** | Localized description for the KPI. | [optional] 
**displayName** | **{String: String}** | Localized display name for the KPI. | [optional] 
**entityType** | **String** | The mapping entity type. | 
**entityTypeName** | **String** | The mapping entity name. | 
**expression** | **String** | The computation expression for the KPI. | 
**extracts** | [**[KpiExtract]**](KpiExtract.md) | The KPI extracts. | [optional] 
**filter** | **String** | The filter expression for the KPI. | [optional] 
**_function** | **String** | The computation function for the KPI. | 
**groupBy** | **[String]** | the group by properties for the KPI. | [optional] 
**groupByMetadata** | [**[KpiGroupByMetadata]**](KpiGroupByMetadata.md) | The KPI GroupByMetadata. | [optional] [readonly] 
**kpiName** | **String** | The KPI name. | [optional] [readonly] 
**participantProfilesMetadata** | [**[KpiParticipantProfilesMetadata]**](KpiParticipantProfilesMetadata.md) | The participant profiles. | [optional] [readonly] 
**provisioningState** | [**ProvisioningState**](ProvisioningState.md) |  | [optional] 
**tenantId** | **String** | The hub name. | [optional] [readonly] 
**thresHolds** | [**KpiThresholds**](KpiThresholds.md) |  | [optional] 
**unit** | **String** | The unit of measurement for the KPI. | [optional] 



## Enum: CalculationWindowEnum


* `Lifetime` (value: `"Lifetime"`)

* `Hour` (value: `"Hour"`)

* `Day` (value: `"Day"`)

* `Week` (value: `"Week"`)

* `Month` (value: `"Month"`)





## Enum: EntityTypeEnum


* `None` (value: `"None"`)

* `Profile` (value: `"Profile"`)

* `Interaction` (value: `"Interaction"`)

* `Relationship` (value: `"Relationship"`)





## Enum: FunctionEnum


* `Sum` (value: `"Sum"`)

* `Avg` (value: `"Avg"`)

* `Min` (value: `"Min"`)

* `Max` (value: `"Max"`)

* `Last` (value: `"Last"`)

* `Count` (value: `"Count"`)

* `None` (value: `"None"`)

* `CountDistinct` (value: `"CountDistinct"`)




