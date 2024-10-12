

# MultiRegionConfiguration

<p>Describes the configuration of this multi-Region key. This field appears only when the KMS key is a primary or replica of a multi-Region key.</p> <p>For more information about any listed KMS key, use the <a>DescribeKey</a> operation.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**multiRegionKeyType** | [**MultiRegionKeyType**](MultiRegionKeyType.md) |  |  [optional] |
|**primaryKey** | [**MultiRegionConfigurationPrimaryKey**](MultiRegionConfigurationPrimaryKey.md) |  |  [optional] |
|**replicaKeys** | [**List**](List.md) |  |  [optional] |



