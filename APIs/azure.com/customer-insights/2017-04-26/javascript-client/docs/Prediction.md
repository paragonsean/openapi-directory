# CustomerInsightsManagementClient.Prediction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoAnalyze** | **Boolean** | Whether do auto analyze. | 
**description** | **{String: String}** | Description of the prediction. | [optional] 
**displayName** | **{String: String}** | Display name of the prediction. | [optional] 
**grades** | [**[PredictionGradesInner]**](PredictionGradesInner.md) | The prediction grades. | [optional] 
**involvedInteractionTypes** | **[String]** | Interaction types involved in the prediction. | [optional] 
**involvedKpiTypes** | **[String]** | KPI types involved in the prediction. | [optional] 
**involvedRelationships** | **[String]** | Relationships involved in the prediction. | [optional] 
**mappings** | [**PredictionMappings**](PredictionMappings.md) |  | 
**negativeOutcomeExpression** | **String** | Negative outcome expression. | 
**positiveOutcomeExpression** | **String** | Positive outcome expression. | 
**predictionName** | **String** | Name of the prediction. | [optional] 
**primaryProfileType** | **String** | Primary profile type. | 
**provisioningState** | [**ProvisioningState**](ProvisioningState.md) |  | [optional] 
**scopeExpression** | **String** | Scope expression. | 
**scoreLabel** | **String** | Score label. | 
**systemGeneratedEntities** | [**PredictionSystemGeneratedEntities**](PredictionSystemGeneratedEntities.md) |  | [optional] 
**tenantId** | **String** | The hub name. | [optional] [readonly] 


