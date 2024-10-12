# SensitiveDataProtectionDlp.GooglePrivacyDlpV2TransformationDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **String** | A human-readable string representation of the &#x60;RecordCondition&#x60; corresponding to this transformation. Set if a &#x60;RecordCondition&#x60; was used to determine whether or not to apply this transformation. Examples: * (age_field &gt; 85) * (age_field &lt;&#x3D; 18) * (zip_field exists) * (zip_field &#x3D;&#x3D; 01234) &amp;&amp; (city_field !&#x3D; \&quot;Springville\&quot;) * (zip_field &#x3D;&#x3D; 01234) &amp;&amp; (age_field &lt;&#x3D; 18) &amp;&amp; (city_field exists) | [optional] 
**description** | **String** | A description of the transformation. This is empty for a RECORD_SUPPRESSION, or is the output of calling toString() on the &#x60;PrimitiveTransformation&#x60; protocol buffer message for any other type of transformation. | [optional] 
**infoType** | [**GooglePrivacyDlpV2InfoType**](GooglePrivacyDlpV2InfoType.md) |  | [optional] 
**type** | **String** | The transformation type. | [optional] 



## Enum: TypeEnum


* `TRANSFORMATION_TYPE_UNSPECIFIED` (value: `"TRANSFORMATION_TYPE_UNSPECIFIED"`)

* `RECORD_SUPPRESSION` (value: `"RECORD_SUPPRESSION"`)

* `REPLACE_VALUE` (value: `"REPLACE_VALUE"`)

* `REPLACE_DICTIONARY` (value: `"REPLACE_DICTIONARY"`)

* `REDACT` (value: `"REDACT"`)

* `CHARACTER_MASK` (value: `"CHARACTER_MASK"`)

* `CRYPTO_REPLACE_FFX_FPE` (value: `"CRYPTO_REPLACE_FFX_FPE"`)

* `FIXED_SIZE_BUCKETING` (value: `"FIXED_SIZE_BUCKETING"`)

* `BUCKETING` (value: `"BUCKETING"`)

* `REPLACE_WITH_INFO_TYPE` (value: `"REPLACE_WITH_INFO_TYPE"`)

* `TIME_PART` (value: `"TIME_PART"`)

* `CRYPTO_HASH` (value: `"CRYPTO_HASH"`)

* `DATE_SHIFT` (value: `"DATE_SHIFT"`)

* `CRYPTO_DETERMINISTIC_CONFIG` (value: `"CRYPTO_DETERMINISTIC_CONFIG"`)

* `REDACT_IMAGE` (value: `"REDACT_IMAGE"`)




