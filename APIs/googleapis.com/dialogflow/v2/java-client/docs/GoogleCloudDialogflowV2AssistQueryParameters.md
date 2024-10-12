

# GoogleCloudDialogflowV2AssistQueryParameters

Represents the parameters of human assist query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documentsMetadataFilters** | **Map&lt;String, String&gt;** | Key-value filters on the metadata of documents returned by article suggestion. If specified, article suggestion only returns suggested documents that match all filters in their Document.metadata. Multiple values for a metadata key should be concatenated by comma. For example, filters to match all documents that have &#39;US&#39; or &#39;CA&#39; in their market metadata values and &#39;agent&#39; in their user metadata values will be &#x60;&#x60;&#x60; documents_metadata_filters { key: \&quot;market\&quot; value: \&quot;US,CA\&quot; } documents_metadata_filters { key: \&quot;user\&quot; value: \&quot;agent\&quot; } &#x60;&#x60;&#x60; |  [optional] |



