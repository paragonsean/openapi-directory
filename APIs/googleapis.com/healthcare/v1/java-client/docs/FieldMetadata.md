

# FieldMetadata

Specifies FHIR paths to match, and how to handle de-identification of matching fields.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | Deidentify action for one field. |  [optional] |
|**paths** | **List&lt;String&gt;** | List of paths to FHIR fields to be redacted. Each path is a period-separated list where each component is either a field name or FHIR type name, for example: Patient, HumanName. For \&quot;choice\&quot; types (those defined in the FHIR spec with the form: field[x]) we use two separate components. For example, \&quot;deceasedAge.unit\&quot; is matched by \&quot;Deceased.Age.unit\&quot;. Supported types are: AdministrativeGenderCode, Base64Binary, Boolean, Code, Date, DateTime, Decimal, HumanName, Id, Instant, Integer, LanguageCode, Markdown, Oid, PositiveInt, String, UnsignedInt, Uri, Uuid, Xhtml. |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| ACTION_UNSPECIFIED | &quot;ACTION_UNSPECIFIED&quot; |
| TRANSFORM | &quot;TRANSFORM&quot; |
| INSPECT_AND_TRANSFORM | &quot;INSPECT_AND_TRANSFORM&quot; |
| DO_NOT_TRANSFORM | &quot;DO_NOT_TRANSFORM&quot; |



