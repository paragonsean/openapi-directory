

# DBClusterSnapshot

<p>Contains the details for an Amazon Neptune DB cluster snapshot</p> <p>This data type is used as a response element in the <a>DescribeDBClusterSnapshots</a> action.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availabilityZones** | [**List**](List.md) |  |  [optional] |
|**dbClusterSnapshotIdentifier** | [**String**](String.md) |  |  [optional] |
|**dbClusterIdentifier** | [**String**](String.md) |  |  [optional] |
|**snapshotCreateTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**engine** | [**String**](String.md) |  |  [optional] |
|**allocatedStorage** | [**Integer**](Integer.md) |  |  [optional] |
|**status** | [**String**](String.md) |  |  [optional] |
|**port** | [**Integer**](Integer.md) |  |  [optional] |
|**vpcId** | [**String**](String.md) |  |  [optional] |
|**clusterCreateTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**masterUsername** | [**String**](String.md) |  |  [optional] |
|**engineVersion** | [**String**](String.md) |  |  [optional] |
|**licenseModel** | [**String**](String.md) |  |  [optional] |
|**snapshotType** | [**String**](String.md) |  |  [optional] |
|**percentProgress** | [**Integer**](Integer.md) |  |  [optional] |
|**storageEncrypted** | [**Boolean**](Boolean.md) |  |  [optional] |
|**kmsKeyId** | [**String**](String.md) |  |  [optional] |
|**dbClusterSnapshotArn** | [**String**](String.md) |  |  [optional] |
|**sourceDBClusterSnapshotArn** | [**String**](String.md) |  |  [optional] |
|**iaMDatabaseAuthenticationEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |



