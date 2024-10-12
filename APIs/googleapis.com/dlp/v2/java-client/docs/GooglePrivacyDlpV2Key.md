

# GooglePrivacyDlpV2Key

A unique identifier for a Datastore entity. If a key's partition ID or any of its path kinds or names are reserved/read-only, the key is reserved/read-only. A reserved/read-only key is forbidden in certain documented contexts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**partitionId** | [**GooglePrivacyDlpV2PartitionId**](GooglePrivacyDlpV2PartitionId.md) |  |  [optional] |
|**path** | [**List&lt;GooglePrivacyDlpV2PathElement&gt;**](GooglePrivacyDlpV2PathElement.md) | The entity path. An entity path consists of one or more elements composed of a kind and a string or numerical identifier, which identify entities. The first element identifies a _root entity_, the second element identifies a _child_ of the root entity, the third element identifies a child of the second entity, and so forth. The entities identified by all prefixes of the path are called the element&#39;s _ancestors_. A path can never be empty, and a path can have at most 100 elements. |  [optional] |



