

# EntityMention

An entity mention in the document.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certaintyAssessment** | [**Feature**](Feature.md) |  |  [optional] |
|**confidence** | **Double** | The model&#39;s confidence in this entity mention annotation. A number between 0 and 1. |  [optional] |
|**linkedEntities** | [**List&lt;LinkedEntity&gt;**](LinkedEntity.md) | linked_entities are candidate ontological concepts that this entity mention may refer to. They are sorted by decreasing confidence. |  [optional] |
|**mentionId** | **String** | mention_id uniquely identifies each entity mention in a single response. |  [optional] |
|**subject** | [**Feature**](Feature.md) |  |  [optional] |
|**temporalAssessment** | [**Feature**](Feature.md) |  |  [optional] |
|**text** | [**TextSpan**](TextSpan.md) |  |  [optional] |
|**type** | **String** | The semantic type of the entity: UNKNOWN_ENTITY_TYPE, ALONE, ANATOMICAL_STRUCTURE, ASSISTED_LIVING, BF_RESULT, BM_RESULT, BM_UNIT, BM_VALUE, BODY_FUNCTION, BODY_MEASUREMENT, COMPLIANT, DOESNOT_FOLLOWUP, FAMILY, FOLLOWSUP, LABORATORY_DATA, LAB_RESULT, LAB_UNIT, LAB_VALUE, MEDICAL_DEVICE, MEDICINE, MED_DOSE, MED_DURATION, MED_FORM, MED_FREQUENCY, MED_ROUTE, MED_STATUS, MED_STRENGTH, MED_TOTALDOSE, MED_UNIT, NON_COMPLIANT, OTHER_LIVINGSTATUS, PROBLEM, PROCEDURE, PROCEDURE_RESULT, PROC_METHOD, REASON_FOR_NONCOMPLIANCE, SEVERITY, SUBSTANCE_ABUSE, UNCLEAR_FOLLOWUP. |  [optional] |



