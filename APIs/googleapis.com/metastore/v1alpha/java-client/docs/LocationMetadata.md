

# LocationMetadata

Metadata about the service in a location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**multiRegionMetadata** | [**MultiRegionMetadata**](MultiRegionMetadata.md) |  |  [optional] |
|**supportedHiveMetastoreVersions** | [**List&lt;HiveMetastoreVersion&gt;**](HiveMetastoreVersion.md) | The versions of Hive Metastore that can be used when creating a new metastore service in this location. The server guarantees that exactly one HiveMetastoreVersion in the list will set is_default. |  [optional] |



