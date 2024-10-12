# VertexAiSearchForRetailApi.GoogleCloudRetailV2ProductLevelConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingestionProductType** | **String** | The type of Products allowed to be ingested into the catalog. Acceptable values are: * &#x60;primary&#x60; (default): You can ingest Products of all types. When ingesting a Product, its type will default to Product.Type.PRIMARY if unset. * &#x60;variant&#x60; (incompatible with Retail Search): You can only ingest Product.Type.VARIANT Products. This means Product.primary_product_id cannot be empty. If this field is set to an invalid value other than these, an INVALID_ARGUMENT error is returned. If this field is &#x60;variant&#x60; and merchant_center_product_id_field is &#x60;itemGroupId&#x60;, an INVALID_ARGUMENT error is returned. See [Product levels](https://cloud.google.com/retail/docs/catalog#product-levels) for more details. | [optional] 
**merchantCenterProductIdField** | **String** | Which field of [Merchant Center Product](/bigquery-transfer/docs/merchant-center-products-schema) should be imported as Product.id. Acceptable values are: * &#x60;offerId&#x60; (default): Import &#x60;offerId&#x60; as the product ID. * &#x60;itemGroupId&#x60;: Import &#x60;itemGroupId&#x60; as the product ID. Notice that Retail API will choose one item from the ones with the same &#x60;itemGroupId&#x60;, and use it to represent the item group. If this field is set to an invalid value other than these, an INVALID_ARGUMENT error is returned. If this field is &#x60;itemGroupId&#x60; and ingestion_product_type is &#x60;variant&#x60;, an INVALID_ARGUMENT error is returned. See [Product levels](https://cloud.google.com/retail/docs/catalog#product-levels) for more details. | [optional] 


