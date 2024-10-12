

# OrderableDBInstanceOption

<p>Contains a list of available options for a DB instance.</p> <p> This data type is used as a response element in the <a>DescribeOrderableDBInstanceOptions</a> action.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**engine** | [**String**](String.md) |  |  [optional] |
|**engineVersion** | [**String**](String.md) |  |  [optional] |
|**dbInstanceClass** | [**String**](String.md) |  |  [optional] |
|**licenseModel** | [**String**](String.md) |  |  [optional] |
|**availabilityZones** | [**List**](List.md) |  |  [optional] |
|**multiAZCapable** | [**Boolean**](Boolean.md) |  |  [optional] |
|**readReplicaCapable** | [**Boolean**](Boolean.md) |  |  [optional] |
|**vpc** | [**Boolean**](Boolean.md) |  |  [optional] |
|**supportsStorageEncryption** | [**Boolean**](Boolean.md) |  |  [optional] |
|**storageType** | [**String**](String.md) |  |  [optional] |
|**supportsIops** | [**Boolean**](Boolean.md) |  |  [optional] |
|**supportsEnhancedMonitoring** | [**Boolean**](Boolean.md) |  |  [optional] |
|**supportsIAMDatabaseAuthentication** | [**Boolean**](Boolean.md) |  |  [optional] |
|**supportsPerformanceInsights** | [**Boolean**](Boolean.md) |  |  [optional] |
|**minStorageSize** | [**Integer**](Integer.md) |  |  [optional] |
|**maxStorageSize** | [**Integer**](Integer.md) |  |  [optional] |
|**minIopsPerDbInstance** | [**Integer**](Integer.md) |  |  [optional] |
|**maxIopsPerDbInstance** | [**Integer**](Integer.md) |  |  [optional] |
|**minIopsPerGib** | [**Double**](Double.md) |  |  [optional] |
|**maxIopsPerGib** | [**Double**](Double.md) |  |  [optional] |
|**supportsGlobalDatabases** | [**Boolean**](Boolean.md) |  |  [optional] |



