

# KeyRangeLocation

Location information for a specific key-range of a sharded computation. Currently we only support UTF-8 character splits to simplify encoding into JSON.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataDisk** | **String** | The name of the data disk where data for this range is stored. This name is local to the Google Cloud Platform project and uniquely identifies the disk within that project, for example \&quot;myproject-1014-104817-4c2-harness-0-disk-1\&quot;. |  [optional] |
|**deliveryEndpoint** | **String** | The physical location of this range assignment to be used for streaming computation cross-worker message delivery. |  [optional] |
|**deprecatedPersistentDirectory** | **String** | DEPRECATED. The location of the persistent state for this range, as a persistent directory in the worker local filesystem. |  [optional] |
|**end** | **String** | The end (exclusive) of the key range. |  [optional] |
|**start** | **String** | The start (inclusive) of the key range. |  [optional] |



