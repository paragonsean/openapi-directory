

# AssetFamilyList


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**PAMAssetCategoriesAllOfEmbeddedItemsInnerAllOfLinks**](PAMAssetCategoriesAllOfEmbeddedItemsInnerAllOfLinks.md) |  |  [optional] |
|**attributeAsMainMedia** | **String** | Attribute code that is used as the main media of the asset family. |  [optional] |
|**code** | **String** | Asset family code |  |
|**labels** | [**AssetFamiliesAllOfEmbeddedItemsInnerAllOfLabels**](AssetFamiliesAllOfEmbeddedItemsInnerAllOfLabels.md) |  |  [optional] |
|**namingConvention** | [**AssetFamilyListAllOfNamingConvention**](AssetFamilyListAllOfNamingConvention.md) |  |  [optional] |
|**productLinkRules** | [**List&lt;AssetFamiliesAllOfEmbeddedItemsInnerAllOfProductLinkRulesInner&gt;**](AssetFamiliesAllOfEmbeddedItemsInnerAllOfProductLinkRulesInner.md) | The rules that will be run after the asset creation, in order to automatically link the assets of this family to a set of products. To understand the format of this property, see &lt;a href&#x3D;&#39;/concepts/asset-manager.html#focus-on-the-product-link-rule&#39;&gt;here&lt;/a&gt;. |  [optional] |
|**transformations** | [**List&lt;AssetFamiliesAllOfEmbeddedItemsInnerAllOfTransformationsInner&gt;**](AssetFamiliesAllOfEmbeddedItemsInnerAllOfTransformationsInner.md) | The transformations to perform on source files in order to generate new files into your asset attributes (only available since v4.0). To understand the format of this property, see &lt;a href&#x3D;&#39;/concepts/asset-manager.html#focus-on-the-transformations&#39;&gt;here&lt;/a&gt;. |  [optional] |



