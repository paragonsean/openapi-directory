

# GooglePrivacyDlpV2TransformationConfig

User specified templates and configs for how to deidentify structured, unstructures, and image files. User must provide either a unstructured deidentify template or at least one redact image config.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deidentifyTemplate** | **String** | De-identify template. If this template is specified, it will serve as the default de-identify template. This template cannot contain &#x60;record_transformations&#x60; since it can be used for unstructured content such as free-form text files. If this template is not set, a default &#x60;ReplaceWithInfoTypeConfig&#x60; will be used to de-identify unstructured content. |  [optional] |
|**imageRedactTemplate** | **String** | Image redact template. If this template is specified, it will serve as the de-identify template for images. If this template is not set, all findings in the image will be redacted with a black box. |  [optional] |
|**structuredDeidentifyTemplate** | **String** | Structured de-identify template. If this template is specified, it will serve as the de-identify template for structured content such as delimited files and tables. If this template is not set but the &#x60;deidentify_template&#x60; is set, then &#x60;deidentify_template&#x60; will also apply to the structured content. If neither template is set, a default &#x60;ReplaceWithInfoTypeConfig&#x60; will be used to de-identify structured content. |  [optional] |



