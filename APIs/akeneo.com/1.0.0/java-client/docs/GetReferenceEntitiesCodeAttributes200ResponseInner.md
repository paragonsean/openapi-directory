

# GetReferenceEntitiesCodeAttributes200ResponseInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedExtensions** | **List&lt;String&gt;** | Extensions allowed when the attribute type is &#x60;image&#x60; |  [optional] |
|**code** | **String** | Attribute code |  |
|**decimalsAllowed** | **Boolean** | Whether decimals are allowed when the attribute type is &#x60;number&#x60; |  [optional] |
|**isRequiredForCompleteness** | **Boolean** | Whether the attribute should be part of the record&#39;s completeness calculation |  [optional] |
|**isRichTextEditor** | **Boolean** | Whether the UI should display a rich text editor instead of a simple text area when the attribute type is &#x60;text&#x60; |  [optional] |
|**isTextarea** | **Boolean** | Whether the UI should display a text area instead of a simple field when the attribute type is &#x60;text&#x60; |  [optional] |
|**labels** | [**GetAssetFamiliesCodeAttributes200ResponseInnerLabels**](GetAssetFamiliesCodeAttributes200ResponseInnerLabels.md) |  |  [optional] |
|**maxCharacters** | **Integer** | Maximum number of characters allowed for the value of the attribute when the attribute type is &#x60;text&#x60; |  [optional] |
|**maxFileSize** | **String** | Max file size in MB when the attribute type is &#x60;image&#x60; |  [optional] |
|**maxValue** | **String** | Maximum value allowed when the attribute type is &#x60;number&#x60; |  [optional] |
|**minValue** | **String** | Minimum value allowed when the attribute type is &#x60;number&#x60; |  [optional] |
|**referenceEntityCode** | **String** | Code of the linked reference entity when the attribute type is &#x60;reference_entity_single_link&#x60; or &#x60;reference_entity_multiple_links&#x60; |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Attribute type. See &lt;a href&#x3D;&#39;/concepts/reference-entities.html#reference-entity-attribute&#39;&gt;type&lt;/a&gt; section for more details. |  |
|**validationRegexp** | **String** | Regexp expression used to validate the attribute value when the attribute type is &#x60;text&#x60; |  [optional] |
|**validationRule** | [**ValidationRuleEnum**](#ValidationRuleEnum) | Validation rule type used to validate the attribute value when the attribute type is &#x60;text&#x60; |  [optional] |
|**valuePerChannel** | **Boolean** | Whether the attribute is scopable, i.e. can have one value by channel |  [optional] |
|**valuePerLocale** | **Boolean** | Whether the attribute is localizable, i.e. can have one value by locale |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TEXT | &quot;text&quot; |
| IMAGE | &quot;image&quot; |
| NUMBER | &quot;number&quot; |
| SINGLE_OPTION | &quot;single_option&quot; |
| MULTIPLE_OPTIONS | &quot;multiple_options&quot; |
| REFERENCE_ENTITY_SINGLE_LINK | &quot;reference_entity_single_link&quot; |
| REFERENCE_ENTITY_MULTIPLE_LINKS | &quot;reference_entity_multiple_links&quot; |



## Enum: ValidationRuleEnum

| Name | Value |
|---- | -----|
| EMAIL | &quot;email&quot; |
| URL | &quot;url&quot; |
| REGEXP | &quot;regexp&quot; |
| NONE | &quot;none&quot; |



