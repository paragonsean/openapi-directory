

# CalculationUnitDTO


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | should this value be available on the XTRF selection lists |  [optional] |
|**canBeUsedInCatAnalysis** | **Boolean** |  |  [optional] |
|**catQuantityConversionExpression** | **String** |  |  [optional] |
|**_default** | **Boolean** | should this value be set by default in XTRF selection lists |  [optional] |
|**exchangeRatio** | **BigDecimal** |  |  [optional] |
|**fileStatsConversionExpression** | **String** |  |  [optional] |
|**id** | **Long** | internal identifier |  [optional] |
|**jobTypeIds** | **List&lt;Long&gt;** |  |  [optional] |
|**name** | **String** | localised name (formatted in the current user&#39;s locale) |  [optional] |
|**preferred** | **Boolean** | should this value be available on the top of XTRF selection lists, in the Preferred section |  [optional] |
|**symbol** | **String** |  |  [optional] |
|**timeToQuantityConversionExpression** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TIME | &quot;TIME&quot; |
| VOLUME | &quot;VOLUME&quot; |
| PERCENT | &quot;PERCENT&quot; |



