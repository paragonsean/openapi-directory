# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1Taxonomy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activatedPolicyTypes** | **[String]** | Optional. A list of policy types that are activated for this taxonomy. If not set, defaults to an empty list. | [optional] 
**description** | **String** | Optional. Description of this taxonomy. If not set, defaults to empty. The description must contain only Unicode characters, tabs, newlines, carriage returns, and page breaks, and be at most 2000 bytes long when encoded in UTF-8. | [optional] 
**displayName** | **String** | Required. User-defined name of this taxonomy. The name can&#39;t start or end with spaces, must contain only Unicode letters, numbers, underscores, dashes, and spaces, and be at most 200 bytes long when encoded in UTF-8. The taxonomy display name must be unique within an organization. | [optional] 
**name** | **String** | Identifier. Resource name of this taxonomy in URL format. Note: Policy tag manager generates unique taxonomy IDs. | [optional] 
**policyTagCount** | **Number** | Output only. Number of policy tags in this taxonomy. | [optional] [readonly] 
**service** | [**GoogleCloudDatacatalogV1TaxonomyService**](GoogleCloudDatacatalogV1TaxonomyService.md) |  | [optional] 
**taxonomyTimestamps** | [**GoogleCloudDatacatalogV1SystemTimestamps**](GoogleCloudDatacatalogV1SystemTimestamps.md) |  | [optional] 



## Enum: [ActivatedPolicyTypesEnum]


* `POLICY_TYPE_UNSPECIFIED` (value: `"POLICY_TYPE_UNSPECIFIED"`)

* `FINE_GRAINED_ACCESS_CONTROL` (value: `"FINE_GRAINED_ACCESS_CONTROL"`)




