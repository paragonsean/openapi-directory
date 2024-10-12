

# ClusterConfig

Container for the cluster configuration of an OpenSearch Service domain. For more information, see <a href=\"https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html\">Creating and managing Amazon OpenSearch Service domains</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instanceType** | [**OpenSearchPartitionInstanceType**](OpenSearchPartitionInstanceType.md) |  |  [optional] |
|**instanceCount** | [**Integer**](Integer.md) |  |  [optional] |
|**dedicatedMasterEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**zoneAwarenessEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**zoneAwarenessConfig** | [**CreateDomainRequestClusterConfigZoneAwarenessConfig**](CreateDomainRequestClusterConfigZoneAwarenessConfig.md) |  |  [optional] |
|**dedicatedMasterType** | [**OpenSearchPartitionInstanceType**](OpenSearchPartitionInstanceType.md) |  |  [optional] |
|**dedicatedMasterCount** | [**Integer**](Integer.md) |  |  [optional] |
|**warmEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**warmType** | [**OpenSearchWarmPartitionInstanceType**](OpenSearchWarmPartitionInstanceType.md) |  |  [optional] |
|**warmCount** | [**Integer**](Integer.md) |  |  [optional] |
|**coldStorageOptions** | [**CreateDomainRequestClusterConfigColdStorageOptions**](CreateDomainRequestClusterConfigColdStorageOptions.md) |  |  [optional] |
|**multiAZWithStandbyEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |



