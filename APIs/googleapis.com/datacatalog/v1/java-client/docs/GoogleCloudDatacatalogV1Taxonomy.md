

# GoogleCloudDatacatalogV1Taxonomy

A taxonomy is a collection of hierarchical policy tags that classify data along a common axis. For example, a \"data sensitivity\" taxonomy might contain the following policy tags: ``` + PII + Account number + Age + SSN + Zipcode + Financials + Revenue ``` A \"data origin\" taxonomy might contain the following policy tags: ``` + User data + Employee data + Partner data + Public data ```

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activatedPolicyTypes** | [**List&lt;ActivatedPolicyTypesEnum&gt;**](#List&lt;ActivatedPolicyTypesEnum&gt;) | Optional. A list of policy types that are activated for this taxonomy. If not set, defaults to an empty list. |  [optional] |
|**description** | **String** | Optional. Description of this taxonomy. If not set, defaults to empty. The description must contain only Unicode characters, tabs, newlines, carriage returns, and page breaks, and be at most 2000 bytes long when encoded in UTF-8. |  [optional] |
|**displayName** | **String** | Required. User-defined name of this taxonomy. The name can&#39;t start or end with spaces, must contain only Unicode letters, numbers, underscores, dashes, and spaces, and be at most 200 bytes long when encoded in UTF-8. The taxonomy display name must be unique within an organization. |  [optional] |
|**name** | **String** | Identifier. Resource name of this taxonomy in URL format. Note: Policy tag manager generates unique taxonomy IDs. |  [optional] |
|**policyTagCount** | **Integer** | Output only. Number of policy tags in this taxonomy. |  [optional] [readonly] |
|**service** | [**GoogleCloudDatacatalogV1TaxonomyService**](GoogleCloudDatacatalogV1TaxonomyService.md) |  |  [optional] |
|**taxonomyTimestamps** | [**GoogleCloudDatacatalogV1SystemTimestamps**](GoogleCloudDatacatalogV1SystemTimestamps.md) |  |  [optional] |



## Enum: List&lt;ActivatedPolicyTypesEnum&gt;

| Name | Value |
|---- | -----|
| POLICY_TYPE_UNSPECIFIED | &quot;POLICY_TYPE_UNSPECIFIED&quot; |
| FINE_GRAINED_ACCESS_CONTROL | &quot;FINE_GRAINED_ACCESS_CONTROL&quot; |



