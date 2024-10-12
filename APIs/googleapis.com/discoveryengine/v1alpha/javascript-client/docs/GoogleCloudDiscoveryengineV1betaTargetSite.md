# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1betaTargetSite

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exactMatch** | **Boolean** | Input only. If set to false, a uri_pattern is generated to include all pages whose address contains the provided_uri_pattern. If set to true, an uri_pattern is generated to try to be an exact match of the provided_uri_pattern or just the specific page if the provided_uri_pattern is a specific one. provided_uri_pattern is always normalized to generate the URI pattern to be used by the search engine. | [optional] 
**failureReason** | [**GoogleCloudDiscoveryengineV1betaTargetSiteFailureReason**](GoogleCloudDiscoveryengineV1betaTargetSiteFailureReason.md) |  | [optional] 
**generatedUriPattern** | **String** | Output only. This is system-generated based on the provided_uri_pattern. | [optional] [readonly] 
**indexingStatus** | **String** | Output only. Indexing status. | [optional] [readonly] 
**name** | **String** | Output only. The fully qualified resource name of the target site. &#x60;projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine/targetSites/{target_site}&#x60; The &#x60;target_site_id&#x60; is system-generated. | [optional] [readonly] 
**providedUriPattern** | **String** | Required. Input only. The user provided URI pattern from which the &#x60;generated_uri_pattern&#x60; is generated. | [optional] 
**siteVerificationInfo** | [**GoogleCloudDiscoveryengineV1betaSiteVerificationInfo**](GoogleCloudDiscoveryengineV1betaSiteVerificationInfo.md) |  | [optional] 
**type** | **String** | The type of the target site, e.g., whether the site is to be included or excluded. | [optional] 
**updateTime** | **String** | Output only. The target site&#39;s last updated time. | [optional] [readonly] 



## Enum: IndexingStatusEnum


* `INDEXING_STATUS_UNSPECIFIED` (value: `"INDEXING_STATUS_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `FAILED` (value: `"FAILED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `DELETING` (value: `"DELETING"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `INCLUDE` (value: `"INCLUDE"`)

* `EXCLUDE` (value: `"EXCLUDE"`)




