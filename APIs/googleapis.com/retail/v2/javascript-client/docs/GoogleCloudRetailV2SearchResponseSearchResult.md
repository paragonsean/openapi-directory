# VertexAiSearchForRetailApi.GoogleCloudRetailV2SearchResponseSearchResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Product.id of the searched Product. | [optional] 
**matchingVariantCount** | **Number** | The count of matched variant Products. | [optional] 
**matchingVariantFields** | **{String: String}** | If a variant Product matches the search query, this map indicates which Product fields are matched. The key is the Product.name, the value is a field mask of the matched Product fields. If matched attributes cannot be determined, this map will be empty. For example, a key \&quot;sku1\&quot; with field mask \&quot;products.color_info\&quot; indicates there is a match between \&quot;sku1\&quot; ColorInfo and the query. | [optional] 
**personalLabels** | **[String]** | Specifies previous events related to this product for this user based on UserEvent with same SearchRequest.visitor_id or UserInfo.user_id. This is set only when SearchRequest.PersonalizationSpec.mode is SearchRequest.PersonalizationSpec.Mode.AUTO. Possible values: * &#x60;purchased&#x60;: Indicates that this product has been purchased before. | [optional] 
**product** | [**GoogleCloudRetailV2Product**](GoogleCloudRetailV2Product.md) |  | [optional] 
**variantRollupValues** | **{String: Object}** | The rollup matching variant Product attributes. The key is one of the SearchRequest.variant_rollup_keys. The values are the merged and de-duplicated Product attributes. Notice that the rollup values are respect filter. For example, when filtering by \&quot;colorFamilies:ANY(\\\&quot;red\\\&quot;)\&quot; and rollup \&quot;colorFamilies\&quot;, only \&quot;red\&quot; is returned. For textual and numerical attributes, the rollup values is a list of string or double values with type google.protobuf.ListValue. For example, if there are two variants with colors \&quot;red\&quot; and \&quot;blue\&quot;, the rollup values are { key: \&quot;colorFamilies\&quot; value { list_value { values { string_value: \&quot;red\&quot; } values { string_value: \&quot;blue\&quot; } } } } For FulfillmentInfo, the rollup values is a double value with type google.protobuf.Value. For example, &#x60;{key: \&quot;pickupInStore.store1\&quot; value { number_value: 10 }}&#x60; means a there are 10 variants in this product are available in the store \&quot;store1\&quot;. | [optional] 


