# AkeneoPimRestApi.ReferenceEntityAttribute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedExtensions** | **[String]** | Extensions allowed when the attribute type is &#x60;image&#x60; | [optional] 
**code** | **String** | Attribute code | 
**decimalsAllowed** | **Boolean** | Whether decimals are allowed when the attribute type is &#x60;number&#x60; | [optional] [default to false]
**isRequiredForCompleteness** | **Boolean** | Whether the attribute should be part of the record&#39;s completeness calculation | [optional] [default to false]
**isRichTextEditor** | **Boolean** | Whether the UI should display a rich text editor instead of a simple text area when the attribute type is &#x60;text&#x60; | [optional] 
**isTextarea** | **Boolean** | Whether the UI should display a text area instead of a simple field when the attribute type is &#x60;text&#x60; | [optional] [default to false]
**labels** | [**GetAssetFamiliesCodeAttributes200ResponseInnerLabels**](GetAssetFamiliesCodeAttributes200ResponseInnerLabels.md) |  | [optional] 
**maxCharacters** | **Number** | Maximum number of characters allowed for the value of the attribute when the attribute type is &#x60;text&#x60; | [optional] 
**maxFileSize** | **String** | Max file size in MB when the attribute type is &#x60;image&#x60; | [optional] 
**maxValue** | **String** | Maximum value allowed when the attribute type is &#x60;number&#x60; | [optional] 
**minValue** | **String** | Minimum value allowed when the attribute type is &#x60;number&#x60; | [optional] 
**referenceEntityCode** | **String** | Code of the linked reference entity when the attribute type is &#x60;reference_entity_single_link&#x60; or &#x60;reference_entity_multiple_links&#x60; | [optional] 
**type** | **String** | Attribute type. See &lt;a href&#x3D;&#39;/concepts/reference-entities.html#reference-entity-attribute&#39;&gt;type&lt;/a&gt; section for more details. | 
**validationRegexp** | **String** | Regexp expression used to validate the attribute value when the attribute type is &#x60;text&#x60; | [optional] 
**validationRule** | **String** | Validation rule type used to validate the attribute value when the attribute type is &#x60;text&#x60; | [optional] [default to &#39;none&#39;]
**valuePerChannel** | **Boolean** | Whether the attribute is scopable, i.e. can have one value by channel | [optional] [default to false]
**valuePerLocale** | **Boolean** | Whether the attribute is localizable, i.e. can have one value by locale | [optional] [default to false]



## Enum: TypeEnum


* `text` (value: `"text"`)

* `image` (value: `"image"`)

* `number` (value: `"number"`)

* `single_option` (value: `"single_option"`)

* `multiple_options` (value: `"multiple_options"`)

* `reference_entity_single_link` (value: `"reference_entity_single_link"`)

* `reference_entity_multiple_links` (value: `"reference_entity_multiple_links"`)





## Enum: ValidationRuleEnum


* `email` (value: `"email"`)

* `url` (value: `"url"`)

* `regexp` (value: `"regexp"`)

* `none` (value: `"none"`)




