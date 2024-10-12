

# SapDiscovery

The schema of SAP system discovery data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationLayer** | [**SapDiscoveryComponent**](SapDiscoveryComponent.md) |  |  [optional] |
|**databaseLayer** | [**SapDiscoveryComponent**](SapDiscoveryComponent.md) |  |  [optional] |
|**metadata** | [**SapDiscoveryMetadata**](SapDiscoveryMetadata.md) |  |  [optional] |
|**projectNumber** | **String** | Optional. The GCP project number that this SapSystem belongs to. |  [optional] |
|**systemId** | **String** | Output only. A combination of database SID, database instance URI and tenant DB name to make a unique identifier per-system. |  [optional] [readonly] |
|**updateTime** | **String** | Required. Unix timestamp this system has been updated last. |  [optional] |
|**workloadProperties** | [**SapDiscoveryWorkloadProperties**](SapDiscoveryWorkloadProperties.md) |  |  [optional] |



