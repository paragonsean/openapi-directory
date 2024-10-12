

# GetAssetFamiliesCodeAttributes200ResponseInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedExtensions** | **List&lt;String&gt;** | Extensions allowed when the attribute type is &#x60;media_file&#x60; |  [optional] |
|**code** | **String** | Attribute code |  |
|**decimalsAllowed** | **Boolean** | Whether decimals are allowed when the attribute type is &#x60;number&#x60; |  [optional] |
|**isReadOnly** | **Boolean** | Whether the attribute should be in read only mode only in the UI, but you can still update it with the API |  [optional] |
|**isRequiredForCompleteness** | **Boolean** | Whether the attribute should be part of the record&#39;s completeness calculation |  [optional] |
|**isRichTextEditor** | **Boolean** | Whether the UI should display a rich text editor instead of a simple text area when the attribute type is &#x60;text&#x60; |  [optional] |
|**isTextarea** | **Boolean** | Whether the UI should display a text area instead of a simple field when the attribute type is &#x60;text&#x60; |  [optional] |
|**labels** | [**GetAssetFamiliesCodeAttributes200ResponseInnerLabels**](GetAssetFamiliesCodeAttributes200ResponseInnerLabels.md) |  |  [optional] |
|**maxCharacters** | **Integer** | Maximum number of characters allowed for the value of the attribute when the attribute type is &#x60;text&#x60; |  [optional] |
|**maxFileSize** | **String** | Max file size in MB when the attribute type is &#x60;media_file&#x60; |  [optional] |
|**maxValue** | **String** | Maximum value allowed when the attribute type is &#x60;number&#x60; |  [optional] |
|**mediaType** | [**MediaTypeEnum**](#MediaTypeEnum) | For the &#x60;media_link&#x60; attribute type, it is the type of the media behind the url, to allow its preview in the PIM. For the &#x60;media_file&#x60; attribute type, it is the type of the file. |  |
|**minValue** | **String** | Minimum value allowed when the attribute type is &#x60;number&#x60; |  [optional] |
|**prefix** | **String** | Prefix of the &#x60;media_link&#x60; attribute type. The common url root that prefixes the link to the media |  [optional] |
|**suffix** | **String** | Suffix of the &#x60;media_link&#x60; attribute type. The common url suffix for the media |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Attribute type. See &lt;a href&#x3D;&#39;/concepts/asset-manager.html#asset-attribute&#39;&gt;type&lt;/a&gt; section for more details. |  |
|**validationRegexp** | **String** | Regexp expression used to validate the attribute value when the attribute type is &#x60;text&#x60; |  [optional] |
|**validationRule** | [**ValidationRuleEnum**](#ValidationRuleEnum) | Validation rule type used to validate the attribute value when the attribute type is &#x60;text&#x60; |  [optional] |
|**valuePerChannel** | **Boolean** | Whether the attribute is scopable, i.e. can have one value by channel |  [optional] |
|**valuePerLocale** | **Boolean** | Whether the attribute is localizable, i.e. can have one value by locale |  [optional] |



## Enum: MediaTypeEnum

| Name | Value |
|---- | -----|
| IMAGE | &quot;image&quot; |
| PDF | &quot;pdf&quot; |
| YOUTUBE | &quot;youtube&quot; |
| VIMEO | &quot;vimeo&quot; |
| OTHER | &quot;other&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TEXT | &quot;text&quot; |
| MEDIA_LINK | &quot;media_link&quot; |
| NUMBER | &quot;number&quot; |
| MEDIA_FILE | &quot;media_file&quot; |
| SINGLE_OPTION | &quot;single_option&quot; |
| MULTIPLE_OPTIONS | &quot;multiple_options&quot; |
| REFERENCE_ENTITY_SINGLE_LINK | &quot;reference_entity_single_link&quot; |
| REFERENCE_ENTITY_MULTIPLE_LINKS | &quot;reference_entity_multiple_links&quot; |
| BOOLEAN | &quot;boolean&quot; |



## Enum: ValidationRuleEnum

| Name | Value |
|---- | -----|
| EMAIL | &quot;email&quot; |
| URL | &quot;url&quot; |
| REGEXP | &quot;regexp&quot; |
| NONE | &quot;none&quot; |



