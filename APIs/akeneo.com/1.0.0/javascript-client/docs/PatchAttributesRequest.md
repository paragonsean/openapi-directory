# AkeneoPimRestApi.PatchAttributesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedExtensions** | **[String]** | Extensions allowed when the attribute type is &#x60;pim_catalog_file&#x60; or &#x60;pim_catalog_image&#x60; | [optional] 
**availableLocales** | **[String]** | To make the attribute locale specfic, specify here for which locales it is specific | [optional] 
**code** | **String** | Attribute code | 
**dateMax** | **Date** | Maximum date allowed when the attribute type is &#x60;pim_catalog_date&#x60; | [optional] 
**dateMin** | **Date** | Minimum date allowed when the attribute type is &#x60;pim_catalog_date&#x60; | [optional] 
**decimalsAllowed** | **Boolean** | Whether decimals are allowed when the attribute type is &#x60;pim_catalog_metric&#x60;, &#x60;pim_catalog_price&#x60; or &#x60;pim_catalog_number&#x60; | [optional] 
**defaultMetricUnit** | **String** | Default metric unit when the attribute type is &#x60;pim_catalog_metric&#x60; | [optional] 
**defaultValue** | **Boolean** | Default value for a Yes/No attribute, applied when creating a new product or product model (only available since the 5.0) | [optional] 
**group** | **String** | Attribute group | 
**groupLabels** | [**AttributesAllOfEmbeddedItemsInnerAllOfGroupLabels**](AttributesAllOfEmbeddedItemsInnerAllOfGroupLabels.md) |  | [optional] 
**labels** | [**GetAssetFamiliesCodeAttributes200ResponseInnerLabels**](GetAssetFamiliesCodeAttributes200ResponseInnerLabels.md) |  | [optional] 
**localizable** | **Boolean** | Whether the attribute is localizable, i.e. can have one value by locale | [optional] [default to false]
**maxCharacters** | **Number** | Number maximum of characters allowed for the value of the attribute when the attribute type is &#x60;pim_catalog_text&#x60;, &#x60;pim_catalog_textarea&#x60; or &#x60;pim_catalog_identifier&#x60; | [optional] 
**maxFileSize** | **String** | Max file size in MB when the attribute type is &#x60;pim_catalog_file&#x60; or &#x60;pim_catalog_image&#x60; | [optional] 
**metricFamily** | **String** | Metric family when the attribute type is &#x60;pim_catalog_metric&#x60; | [optional] 
**negativeAllowed** | **Boolean** | Whether negative values are allowed when the attribute type is &#x60;pim_catalog_metric&#x60; or &#x60;pim_catalog_number&#x60; | [optional] 
**numberMax** | **String** | Maximum integer value allowed when the attribute type is &#x60;pim_catalog_metric&#x60;, &#x60;pim_catalog_price&#x60; or &#x60;pim_catalog_number&#x60; | [optional] 
**numberMin** | **String** | Minimum integer value allowed when the attribute type is &#x60;pim_catalog_metric&#x60;, &#x60;pim_catalog_price&#x60; or &#x60;pim_catalog_number&#x60; | [optional] 
**referenceDataName** | **String** | Reference entity code when the attribute type is &#x60;akeneo_reference_entity&#x60; or &#x60;akeneo_reference_entity_collection&#x60; OR Asset family code when the attribute type is &#x60;pim_catalog_asset_collection&#x60; | [optional] 
**scopable** | **Boolean** | Whether the attribute is scopable, i.e. can have one value by channel | [optional] [default to false]
**sortOrder** | **Number** | Order of the attribute in its group | [optional] 
**tableConfiguration** | [**[AttributesAllOfEmbeddedItemsInnerAllOfTableConfigurationInner]**](AttributesAllOfEmbeddedItemsInnerAllOfTableConfigurationInner.md) | Configuration of the Table attribute (columns) | [optional] 
**type** | **String** | Attribute type. See &lt;a href&#x3D;&#39;/concepts/catalog-structure.html#attribute&#39;&gt;type&lt;/a&gt; section for more details. | 
**unique** | **Boolean** | Whether two values for the attribute cannot be the same | [optional] 
**useableAsGridFilter** | **Boolean** | Whether the attribute can be used as a filter for the product grid in the PIM user interface | [optional] 
**validationRegexp** | **String** | Regexp expression used to validate any attribute value when the attribute type is &#x60;pim_catalog_text&#x60; or &#x60;pim_catalog_identifier&#x60; | [optional] 
**validationRule** | **String** | Validation rule type used to validate any attribute value when the attribute type is &#x60;pim_catalog_text&#x60; or &#x60;pim_catalog_identifier&#x60; | [optional] 
**wysiwygEnabled** | **Boolean** | Whether the WYSIWYG interface is shown when the attribute type is &#x60;pim_catalog_textarea&#x60; | [optional] 



## Enum: TypeEnum


* `pim_catalog_identifier` (value: `"pim_catalog_identifier"`)

* `pim_catalog_metric` (value: `"pim_catalog_metric"`)

* `pim_catalog_number` (value: `"pim_catalog_number"`)

* `pim_catalog_reference_data_multi_select` (value: `"pim_catalog_reference_data_multi_select"`)

* `pim_catalog_reference_data_simple_select` (value: `"pim_catalog_reference_data_simple_select"`)

* `pim_catalog_simpleselect` (value: `"pim_catalog_simpleselect"`)

* `pim_catalog_multiselect` (value: `"pim_catalog_multiselect"`)

* `pim_catalog_date` (value: `"pim_catalog_date"`)

* `pim_catalog_textarea` (value: `"pim_catalog_textarea"`)

* `pim_catalog_text` (value: `"pim_catalog_text"`)

* `pim_catalog_file` (value: `"pim_catalog_file"`)

* `pim_catalog_image` (value: `"pim_catalog_image"`)

* `pim_catalog_price_collection` (value: `"pim_catalog_price_collection"`)

* `pim_catalog_boolean` (value: `"pim_catalog_boolean"`)

* `akeneo_reference_entity` (value: `"akeneo_reference_entity"`)

* `akeneo_reference_entity_collection` (value: `"akeneo_reference_entity_collection"`)

* `pim_catalog_asset_collection` (value: `"pim_catalog_asset_collection"`)




