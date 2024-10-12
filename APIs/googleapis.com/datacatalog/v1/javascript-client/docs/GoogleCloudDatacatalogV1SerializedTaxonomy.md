# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1SerializedTaxonomy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activatedPolicyTypes** | **[String]** | A list of policy types that are activated per taxonomy. | [optional] 
**description** | **String** | Description of the serialized taxonomy. At most 2000 bytes when encoded in UTF-8. If not set, defaults to an empty description. | [optional] 
**displayName** | **String** | Required. Display name of the taxonomy. At most 200 bytes when encoded in UTF-8. | [optional] 
**policyTags** | [**[GoogleCloudDatacatalogV1SerializedPolicyTag]**](GoogleCloudDatacatalogV1SerializedPolicyTag.md) | Top level policy tags associated with the taxonomy, if any. | [optional] 



## Enum: [ActivatedPolicyTypesEnum]


* `POLICY_TYPE_UNSPECIFIED` (value: `"POLICY_TYPE_UNSPECIFIED"`)

* `FINE_GRAINED_ACCESS_CONTROL` (value: `"FINE_GRAINED_ACCESS_CONTROL"`)




