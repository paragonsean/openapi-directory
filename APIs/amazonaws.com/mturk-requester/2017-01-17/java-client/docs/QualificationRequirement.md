

# QualificationRequirement

 The QualificationRequirement data structure describes a Qualification that a Worker must have before the Worker is allowed to accept a HIT. A requirement may optionally state that a Worker must have the Qualification in order to preview the HIT, or see the HIT in search results. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**qualificationTypeId** | [**String**](String.md) |  |  |
|**comparator** | [**Comparator**](Comparator.md) |  |  |
|**integerValues** | [**List**](List.md) |  |  [optional] |
|**localeValues** | [**List**](List.md) |  |  [optional] |
|**requiredToPreview** | [**Boolean**](Boolean.md) |  |  [optional] |
|**actionsGuarded** | [**HITAccessActions**](HITAccessActions.md) |  |  [optional] |



