

# GlobalCluster

<p>Contains the details of an Amazon Neptune global database.</p> <p>This data type is used as a response element for the <a>CreateGlobalCluster</a>, <a>DescribeGlobalClusters</a>, <a>ModifyGlobalCluster</a>, <a>DeleteGlobalCluster</a>, <a>FailoverGlobalCluster</a>, and <a>RemoveFromGlobalCluster</a> actions.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**globalClusterIdentifier** | [**String**](String.md) |  |  [optional] |
|**globalClusterResourceId** | [**String**](String.md) |  |  [optional] |
|**globalClusterArn** | [**String**](String.md) |  |  [optional] |
|**status** | [**String**](String.md) |  |  [optional] |
|**engine** | [**String**](String.md) |  |  [optional] |
|**engineVersion** | [**String**](String.md) |  |  [optional] |
|**storageEncrypted** | [**Boolean**](Boolean.md) |  |  [optional] |
|**deletionProtection** | [**Boolean**](Boolean.md) |  |  [optional] |
|**globalClusterMembers** | [**List**](List.md) |  |  [optional] |



