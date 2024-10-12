

# EventHealthEvaluation

Represents health evaluation of a HealthEvent that was reported on the entity. The health evaluation is returned when evaluating health of an entity results in Error or Warning. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**considerWarningAsError** | **Boolean** | Indicates whether warnings are treated with the same severity as errors. The field is specified in the health policy used to evaluate the entity. |  [optional] |
|**unhealthyEvent** | [**HealthEvent**](HealthEvent.md) |  |  [optional] |



