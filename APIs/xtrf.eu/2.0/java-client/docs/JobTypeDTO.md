

# JobTypeDTO


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | should this value be available on the XTRF selection lists |  [optional] |
|**calculationUnitIds** | **List&lt;Long&gt;** |  |  [optional] |
|**_default** | **Boolean** | should this value be set by default in XTRF selection lists |  [optional] |
|**filesNeeded** | **Boolean** |  |  [optional] |
|**id** | **Long** | internal identifier |  [optional] |
|**name** | **String** | localised name (formatted in the current user&#39;s locale) |  [optional] |
|**preferred** | **Boolean** | should this value be available on the top of XTRF selection lists, in the Preferred section |  [optional] |
|**providedByClient** | **Boolean** |  |  [optional] |
|**relationToLanguage** | [**RelationToLanguageEnum**](#RelationToLanguageEnum) |  |  [optional] |
|**vendorProductivity** | **BigDecimal** |  |  [optional] |
|**vendorProductivityCalculationUnitId** | **Long** |  |  [optional] |



## Enum: RelationToLanguageEnum

| Name | Value |
|---- | -----|
| LANGUAGE_COMBINATION_RELATED | &quot;LANGUAGE_COMBINATION_RELATED&quot; |
| SOURCE_LANGUAGE_RELATED_ONLY | &quot;SOURCE_LANGUAGE_RELATED_ONLY&quot; |
| TARGET_LANGUAGE_RELATED_ONLY | &quot;TARGET_LANGUAGE_RELATED_ONLY&quot; |
| LANGUAGE_INDEPENDENT | &quot;LANGUAGE_INDEPENDENT&quot; |



