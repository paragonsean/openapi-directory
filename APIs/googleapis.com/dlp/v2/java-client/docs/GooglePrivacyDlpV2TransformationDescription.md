

# GooglePrivacyDlpV2TransformationDescription

A flattened description of a `PrimitiveTransformation` or `RecordSuppression`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**condition** | **String** | A human-readable string representation of the &#x60;RecordCondition&#x60; corresponding to this transformation. Set if a &#x60;RecordCondition&#x60; was used to determine whether or not to apply this transformation. Examples: * (age_field &gt; 85) * (age_field &lt;&#x3D; 18) * (zip_field exists) * (zip_field &#x3D;&#x3D; 01234) &amp;&amp; (city_field !&#x3D; \&quot;Springville\&quot;) * (zip_field &#x3D;&#x3D; 01234) &amp;&amp; (age_field &lt;&#x3D; 18) &amp;&amp; (city_field exists) |  [optional] |
|**description** | **String** | A description of the transformation. This is empty for a RECORD_SUPPRESSION, or is the output of calling toString() on the &#x60;PrimitiveTransformation&#x60; protocol buffer message for any other type of transformation. |  [optional] |
|**infoType** | [**GooglePrivacyDlpV2InfoType**](GooglePrivacyDlpV2InfoType.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The transformation type. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TRANSFORMATION_TYPE_UNSPECIFIED | &quot;TRANSFORMATION_TYPE_UNSPECIFIED&quot; |
| RECORD_SUPPRESSION | &quot;RECORD_SUPPRESSION&quot; |
| REPLACE_VALUE | &quot;REPLACE_VALUE&quot; |
| REPLACE_DICTIONARY | &quot;REPLACE_DICTIONARY&quot; |
| REDACT | &quot;REDACT&quot; |
| CHARACTER_MASK | &quot;CHARACTER_MASK&quot; |
| CRYPTO_REPLACE_FFX_FPE | &quot;CRYPTO_REPLACE_FFX_FPE&quot; |
| FIXED_SIZE_BUCKETING | &quot;FIXED_SIZE_BUCKETING&quot; |
| BUCKETING | &quot;BUCKETING&quot; |
| REPLACE_WITH_INFO_TYPE | &quot;REPLACE_WITH_INFO_TYPE&quot; |
| TIME_PART | &quot;TIME_PART&quot; |
| CRYPTO_HASH | &quot;CRYPTO_HASH&quot; |
| DATE_SHIFT | &quot;DATE_SHIFT&quot; |
| CRYPTO_DETERMINISTIC_CONFIG | &quot;CRYPTO_DETERMINISTIC_CONFIG&quot; |
| REDACT_IMAGE | &quot;REDACT_IMAGE&quot; |



