

# GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomy

Encapsulates geographic metadata, such as regions and multi-regions like `us-east4` or `European Union`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**globalMetadata** | **Object** | Encapsulates a global geographic taxonomy. |  [optional] |
|**multiRegionalMetadata** | [**GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyMultiRegional**](GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyMultiRegional.md) |  |  [optional] |
|**regionalMetadata** | [**GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyRegional**](GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomyRegional.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of geographic taxonomy associated with the billing account SKU. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| GLOBAL | &quot;TYPE_GLOBAL&quot; |
| REGIONAL | &quot;TYPE_REGIONAL&quot; |
| MULTI_REGIONAL | &quot;TYPE_MULTI_REGIONAL&quot; |



