# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1ReconcileTagsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forceDeleteMissing** | **Boolean** | If set to &#x60;true&#x60;, deletes entry tags related to a tag template not listed in the tags source from an entry. If set to &#x60;false&#x60;, unlisted tags are retained. | [optional] 
**tagTemplate** | **String** | Required. The name of the tag template, which is used for reconciliation. | [optional] 
**tags** | [**[GoogleCloudDatacatalogV1Tag]**](GoogleCloudDatacatalogV1Tag.md) | A list of tags to apply to an entry. A tag can specify a tag template, which must be the template specified in the &#x60;ReconcileTagsRequest&#x60;. The sole entry and each of its columns must be mentioned at most once. | [optional] 


