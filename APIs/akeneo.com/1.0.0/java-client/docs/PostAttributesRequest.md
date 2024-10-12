

# PostAttributesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedExtensions** | **List&lt;String&gt;** | Extensions allowed when the attribute type is &#x60;pim_catalog_file&#x60; or &#x60;pim_catalog_image&#x60; |  [optional] |
|**availableLocales** | **List&lt;String&gt;** | To make the attribute locale specfic, specify here for which locales it is specific |  [optional] |
|**code** | **String** | Attribute code |  |
|**dateMax** | **OffsetDateTime** | Maximum date allowed when the attribute type is &#x60;pim_catalog_date&#x60; |  [optional] |
|**dateMin** | **OffsetDateTime** | Minimum date allowed when the attribute type is &#x60;pim_catalog_date&#x60; |  [optional] |
|**decimalsAllowed** | **Boolean** | Whether decimals are allowed when the attribute type is &#x60;pim_catalog_metric&#x60;, &#x60;pim_catalog_price&#x60; or &#x60;pim_catalog_number&#x60; |  [optional] |
|**defaultMetricUnit** | **String** | Default metric unit when the attribute type is &#x60;pim_catalog_metric&#x60; |  [optional] |
|**defaultValue** | **Boolean** | Default value for a Yes/No attribute, applied when creating a new product or product model (only available since the 5.0) |  [optional] |
|**group** | **String** | Attribute group |  |
|**groupLabels** | [**AttributesAllOfEmbeddedItemsInnerAllOfGroupLabels**](AttributesAllOfEmbeddedItemsInnerAllOfGroupLabels.md) |  |  [optional] |
|**labels** | [**GetAssetFamiliesCodeAttributes200ResponseInnerLabels**](GetAssetFamiliesCodeAttributes200ResponseInnerLabels.md) |  |  [optional] |
|**localizable** | **Boolean** | Whether the attribute is localizable, i.e. can have one value by locale |  [optional] |
|**maxCharacters** | **Integer** | Number maximum of characters allowed for the value of the attribute when the attribute type is &#x60;pim_catalog_text&#x60;, &#x60;pim_catalog_textarea&#x60; or &#x60;pim_catalog_identifier&#x60; |  [optional] |
|**maxFileSize** | **String** | Max file size in MB when the attribute type is &#x60;pim_catalog_file&#x60; or &#x60;pim_catalog_image&#x60; |  [optional] |
|**metricFamily** | **String** | Metric family when the attribute type is &#x60;pim_catalog_metric&#x60; |  [optional] |
|**negativeAllowed** | **Boolean** | Whether negative values are allowed when the attribute type is &#x60;pim_catalog_metric&#x60; or &#x60;pim_catalog_number&#x60; |  [optional] |
|**numberMax** | **String** | Maximum integer value allowed when the attribute type is &#x60;pim_catalog_metric&#x60;, &#x60;pim_catalog_price&#x60; or &#x60;pim_catalog_number&#x60; |  [optional] |
|**numberMin** | **String** | Minimum integer value allowed when the attribute type is &#x60;pim_catalog_metric&#x60;, &#x60;pim_catalog_price&#x60; or &#x60;pim_catalog_number&#x60; |  [optional] |
|**referenceDataName** | **String** | Reference entity code when the attribute type is &#x60;akeneo_reference_entity&#x60; or &#x60;akeneo_reference_entity_collection&#x60; OR Asset family code when the attribute type is &#x60;pim_catalog_asset_collection&#x60; |  [optional] |
|**scopable** | **Boolean** | Whether the attribute is scopable, i.e. can have one value by channel |  [optional] |
|**sortOrder** | **Integer** | Order of the attribute in its group |  [optional] |
|**tableConfiguration** | [**List&lt;AttributesAllOfEmbeddedItemsInnerAllOfTableConfigurationInner&gt;**](AttributesAllOfEmbeddedItemsInnerAllOfTableConfigurationInner.md) | Configuration of the Table attribute (columns) |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Attribute type. See &lt;a href&#x3D;&#39;/concepts/catalog-structure.html#attribute&#39;&gt;type&lt;/a&gt; section for more details. |  |
|**unique** | **Boolean** | Whether two values for the attribute cannot be the same |  [optional] |
|**useableAsGridFilter** | **Boolean** | Whether the attribute can be used as a filter for the product grid in the PIM user interface |  [optional] |
|**validationRegexp** | **String** | Regexp expression used to validate any attribute value when the attribute type is &#x60;pim_catalog_text&#x60; or &#x60;pim_catalog_identifier&#x60; |  [optional] |
|**validationRule** | **String** | Validation rule type used to validate any attribute value when the attribute type is &#x60;pim_catalog_text&#x60; or &#x60;pim_catalog_identifier&#x60; |  [optional] |
|**wysiwygEnabled** | **Boolean** | Whether the WYSIWYG interface is shown when the attribute type is &#x60;pim_catalog_textarea&#x60; |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PIM_CATALOG_IDENTIFIER | &quot;pim_catalog_identifier&quot; |
| PIM_CATALOG_METRIC | &quot;pim_catalog_metric&quot; |
| PIM_CATALOG_NUMBER | &quot;pim_catalog_number&quot; |
| PIM_CATALOG_REFERENCE_DATA_MULTI_SELECT | &quot;pim_catalog_reference_data_multi_select&quot; |
| PIM_CATALOG_REFERENCE_DATA_SIMPLE_SELECT | &quot;pim_catalog_reference_data_simple_select&quot; |
| PIM_CATALOG_SIMPLESELECT | &quot;pim_catalog_simpleselect&quot; |
| PIM_CATALOG_MULTISELECT | &quot;pim_catalog_multiselect&quot; |
| PIM_CATALOG_DATE | &quot;pim_catalog_date&quot; |
| PIM_CATALOG_TEXTAREA | &quot;pim_catalog_textarea&quot; |
| PIM_CATALOG_TEXT | &quot;pim_catalog_text&quot; |
| PIM_CATALOG_FILE | &quot;pim_catalog_file&quot; |
| PIM_CATALOG_IMAGE | &quot;pim_catalog_image&quot; |
| PIM_CATALOG_PRICE_COLLECTION | &quot;pim_catalog_price_collection&quot; |
| PIM_CATALOG_BOOLEAN | &quot;pim_catalog_boolean&quot; |
| AKENEO_REFERENCE_ENTITY | &quot;akeneo_reference_entity&quot; |
| AKENEO_REFERENCE_ENTITY_COLLECTION | &quot;akeneo_reference_entity_collection&quot; |
| PIM_CATALOG_ASSET_COLLECTION | &quot;pim_catalog_asset_collection&quot; |



