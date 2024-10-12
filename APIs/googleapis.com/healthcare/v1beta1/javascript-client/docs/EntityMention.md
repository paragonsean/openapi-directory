# CloudHealthcareApi.EntityMention

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalInfo** | [**[Feature]**](Feature.md) | Additional information about the entity mention. For example, for an entity mention of type &#x60;DATE&#x60; this can be its more specific date types from the following list: &#x60;ADMISSION_DATE&#x60;, &#x60;CONSULTATION_DATE&#x60;, &#x60;DISCHARGE_DATE&#x60;, &#x60;SERVICE_DATE&#x60;, &#x60;VISIT_DATE&#x60;, &#x60;DIAGNOSIS_DATE&#x60;, &#x60;MED_STARTED_DATE&#x60;, &#x60;MED_ENDED_DATE&#x60;, &#x60;NOTE_DATE&#x60;, &#x60;PROCEDURE_DATE&#x60;, &#x60;RADIATION_STARTED_DATE&#x60;, &#x60;RADIATION_ENDED_DATE&#x60;, &#x60;STAGE_DATE&#x60; | [optional] 
**certaintyAssessment** | [**Feature**](Feature.md) |  | [optional] 
**confidence** | **Number** | The model&#39;s confidence in this entity mention annotation. A number between 0 and 1. | [optional] 
**linkedEntities** | [**[LinkedEntity]**](LinkedEntity.md) | linked_entities are candidate ontological concepts that this entity mention may refer to. They are sorted by decreasing confidence. | [optional] 
**mentionId** | **String** | mention_id uniquely identifies each entity mention in a single response. | [optional] 
**subject** | [**Feature**](Feature.md) |  | [optional] 
**temporalAssessment** | [**Feature**](Feature.md) |  | [optional] 
**text** | [**TextSpan**](TextSpan.md) |  | [optional] 
**type** | **String** | The semantic type of the entity: UNKNOWN_ENTITY_TYPE, ALONE, ANATOMICAL_STRUCTURE, ASSISTED_LIVING, BF_RESULT, BM_RESULT, BM_UNIT, BM_VALUE, BODY_FUNCTION, BODY_MEASUREMENT, COMPLIANT, DOESNOT_FOLLOWUP, FAMILY, FOLLOWSUP, LABORATORY_DATA, LAB_RESULT, LAB_UNIT, LAB_VALUE, MEDICAL_DEVICE, MEDICINE, MED_DOSE, MED_DURATION, MED_FORM, MED_FREQUENCY, MED_ROUTE, MED_STATUS, MED_STRENGTH, MED_TOTALDOSE, MED_UNIT, NON_COMPLIANT, OTHER_LIVINGSTATUS, PROBLEM, PROCEDURE, PROCEDURE_RESULT, PROC_METHOD, REASON_FOR_NONCOMPLIANCE, SEVERITY, SUBSTANCE_ABUSE, UNCLEAR_FOLLOWUP. | [optional] 


