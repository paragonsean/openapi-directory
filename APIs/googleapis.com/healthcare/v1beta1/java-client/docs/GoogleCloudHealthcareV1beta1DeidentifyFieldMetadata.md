

# GoogleCloudHealthcareV1beta1DeidentifyFieldMetadata

Specifies the FHIR paths to match and how to handle the de-identification of matching fields.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**characterMaskField** | **Object** | Replace field value with masking character. Supported [types](https://www.hl7.org/fhir/datatypes.html): Code, Decimal, HumanName, Id, LanguageCode, Markdown, Oid, String, Uri, Uuid, Xhtml. |  [optional] |
|**cleanTextField** | **Object** | Inspect text and transform sensitive text. Configure using TextConfig. Supported [types](https://www.hl7.org/fhir/datatypes.html): Code, Date, DateTime, Decimal, HumanName, Id, LanguageCode, Markdown, Oid, String, Uri, Uuid, Xhtml. |  [optional] |
|**cryptoHashField** | **Object** | Replace field value with a hash of that value. Supported [types](https://www.hl7.org/fhir/datatypes.html): Code, Decimal, HumanName, Id, LanguageCode, Markdown, Oid, String, Uri, Uuid, Xhtml. |  [optional] |
|**dateShiftField** | **Object** | Shift the date by a randomized number of days. See [date shifting](https://cloud.google.com/dlp/docs/concepts-date-shifting) for more information. Supported [types](https://www.hl7.org/fhir/datatypes.html): Date, DateTime. |  [optional] |
|**keepField** | **Object** | Keep field unchanged. |  [optional] |
|**paths** | **List&lt;String&gt;** | List of paths to FHIR fields to redact. Each path is a period-separated list where each component is either a field name or FHIR [type](https://www.hl7.org/fhir/datatypes.html) name. All types begin with an upper case letter. For example, the resource field &#x60;Patient.Address.city&#x60;, which uses a [string](https://www.hl7.org/fhir/datatypes-definitions.html#Address.city) type, can be matched by &#x60;Patient.Address.String&#x60;. Partial matching is supported. For example, &#x60;Patient.Address.city&#x60; can be matched by &#x60;Address.city&#x60; (with &#x60;Patient&#x60; omitted). Partial matching and type matching can be combined, for example &#x60;Patient.Address.city&#x60; can be matched by &#x60;Address.String&#x60;. For \&quot;choice\&quot; types (those defined in the FHIR spec with the format &#x60;field[x]&#x60;), use two separate components. For example, &#x60;deceasedAge.unit&#x60; is matched by &#x60;Deceased.Age.unit&#x60;. The following types are supported: AdministrativeGenderCode, Base64Binary, Boolean, Code, Date, DateTime, Decimal, HumanName, Id, Instant, Integer, LanguageCode, Markdown, Oid, PositiveInt, String, UnsignedInt, Uri, Uuid, Xhtml. The sub-type for HumanName (for example &#x60;HumanName.given&#x60;, &#x60;HumanName.family&#x60;) can be omitted. |  [optional] |
|**removeField** | **Object** | Remove field. |  [optional] |



