# CloudHealthcareApi.FieldMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | Deidentify action for one field. | [optional] 
**paths** | **[String]** | List of paths to FHIR fields to be redacted. Each path is a period-separated list where each component is either a field name or FHIR type name, for example: Patient, HumanName. For \&quot;choice\&quot; types (those defined in the FHIR spec with the form: field[x]) we use two separate components. For example, \&quot;deceasedAge.unit\&quot; is matched by \&quot;Deceased.Age.unit\&quot;. Supported types are: AdministrativeGenderCode, Base64Binary, Boolean, Code, Date, DateTime, Decimal, HumanName, Id, Instant, Integer, LanguageCode, Markdown, Oid, PositiveInt, String, UnsignedInt, Uri, Uuid, Xhtml. | [optional] 



## Enum: ActionEnum


* `ACTION_UNSPECIFIED` (value: `"ACTION_UNSPECIFIED"`)

* `TRANSFORM` (value: `"TRANSFORM"`)

* `INSPECT_AND_TRANSFORM` (value: `"INSPECT_AND_TRANSFORM"`)

* `DO_NOT_TRANSFORM` (value: `"DO_NOT_TRANSFORM"`)




