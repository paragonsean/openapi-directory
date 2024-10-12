

# Prediction

The prediction definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoAnalyze** | **Boolean** | Whether do auto analyze. |  |
|**description** | **Map&lt;String, String&gt;** | Description of the prediction. |  [optional] |
|**displayName** | **Map&lt;String, String&gt;** | Display name of the prediction. |  [optional] |
|**grades** | [**List&lt;PredictionGradesInner&gt;**](PredictionGradesInner.md) | The prediction grades. |  [optional] |
|**involvedInteractionTypes** | **List&lt;String&gt;** | Interaction types involved in the prediction. |  [optional] |
|**involvedKpiTypes** | **List&lt;String&gt;** | KPI types involved in the prediction. |  [optional] |
|**involvedRelationships** | **List&lt;String&gt;** | Relationships involved in the prediction. |  [optional] |
|**mappings** | [**PredictionMappings**](PredictionMappings.md) |  |  |
|**negativeOutcomeExpression** | **String** | Negative outcome expression. |  |
|**positiveOutcomeExpression** | **String** | Positive outcome expression. |  |
|**predictionName** | **String** | Name of the prediction. |  [optional] |
|**primaryProfileType** | **String** | Primary profile type. |  |
|**provisioningState** | **ProvisioningState** |  |  [optional] |
|**scopeExpression** | **String** | Scope expression. |  |
|**scoreLabel** | **String** | Score label. |  |
|**systemGeneratedEntities** | [**PredictionSystemGeneratedEntities**](PredictionSystemGeneratedEntities.md) |  |  [optional] |
|**tenantId** | **String** | The hub name. |  [optional] [readonly] |



