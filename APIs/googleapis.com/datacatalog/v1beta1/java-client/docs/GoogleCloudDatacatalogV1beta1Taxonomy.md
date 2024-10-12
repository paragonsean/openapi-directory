

# GoogleCloudDatacatalogV1beta1Taxonomy

A taxonomy is a collection of policy tags that classify data along a common axis. For instance a data *sensitivity* taxonomy could contain policy tags denoting PII such as age, zipcode, and SSN. A data *origin* taxonomy could contain policy tags to distinguish user data, employee data, partner data, public data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activatedPolicyTypes** | [**List&lt;ActivatedPolicyTypesEnum&gt;**](#List&lt;ActivatedPolicyTypesEnum&gt;) | Optional. A list of policy types that are activated for this taxonomy. If not set, defaults to an empty list. |  [optional] |
|**description** | **String** | Optional. Description of this taxonomy. It must: contain only unicode characters, tabs, newlines, carriage returns and page breaks; and be at most 2000 bytes long when encoded in UTF-8. If not set, defaults to an empty description. |  [optional] |
|**displayName** | **String** | Required. User defined name of this taxonomy. It must: contain only unicode letters, numbers, underscores, dashes and spaces; not start or end with spaces; and be at most 200 bytes long when encoded in UTF-8. The taxonomy display name must be unique within an organization. |  [optional] |
|**name** | **String** | Identifier. Resource name of this taxonomy, whose format is: \&quot;projects/{project_number}/locations/{location_id}/taxonomies/{id}\&quot;. |  [optional] |
|**policyTagCount** | **Integer** | Output only. Number of policy tags contained in this taxonomy. |  [optional] [readonly] |
|**service** | [**GoogleCloudDatacatalogV1beta1TaxonomyService**](GoogleCloudDatacatalogV1beta1TaxonomyService.md) |  |  [optional] |
|**taxonomyTimestamps** | [**GoogleCloudDatacatalogV1beta1SystemTimestamps**](GoogleCloudDatacatalogV1beta1SystemTimestamps.md) |  |  [optional] |



## Enum: List&lt;ActivatedPolicyTypesEnum&gt;

| Name | Value |
|---- | -----|
| POLICY_TYPE_UNSPECIFIED | &quot;POLICY_TYPE_UNSPECIFIED&quot; |
| FINE_GRAINED_ACCESS_CONTROL | &quot;FINE_GRAINED_ACCESS_CONTROL&quot; |



