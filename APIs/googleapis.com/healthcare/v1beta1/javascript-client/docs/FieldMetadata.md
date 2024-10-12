# CloudHealthcareApi.FieldMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | Deidentify action for one field. | [optional] 
**paths** | **[String]** | List of paths to FHIR fields to redact. Each path is a period-separated list where each component is either a field name or FHIR type name. All types begin with an upper case letter. For example, the resource field \&quot;Patient.Address.city\&quot;, which uses a string type, can be matched by \&quot;Patient.Address.String\&quot;. Path also supports partial matching. For example, \&quot;Patient.Address.city\&quot; can be matched by \&quot;Address.city\&quot; (Patient omitted). Partial matching and type matching can be combined. For example, \&quot;Patient.Address.city\&quot; can be matched by \&quot;Address.String\&quot;. For \&quot;choice\&quot; types (those defined in the FHIR spec with the form: field[x]), use two separate components. For example, \&quot;deceasedAge.unit\&quot; is matched by \&quot;Deceased.Age.unit\&quot;. Supported types are: AdministrativeGenderCode, Base64Binary, Boolean, Code, Date, DateTime, Decimal, HumanName, Id, Instant, Integer, LanguageCode, Markdown, Oid, PositiveInt, String, UnsignedInt, Uri, Uuid, Xhtml. The sub-type for HumanName(for example HumanName.given, HumanName.family) can be omitted. | [optional] 



## Enum: ActionEnum


* `ACTION_UNSPECIFIED` (value: `"ACTION_UNSPECIFIED"`)

* `TRANSFORM` (value: `"TRANSFORM"`)

* `INSPECT_AND_TRANSFORM` (value: `"INSPECT_AND_TRANSFORM"`)

* `DO_NOT_TRANSFORM` (value: `"DO_NOT_TRANSFORM"`)




