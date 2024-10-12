

# DomainStatus

The current status of an OpenSearch Service domain.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domainId** | [**String**](String.md) |  |  |
|**domainName** | [**String**](String.md) |  |  |
|**ARN** | [**String**](String.md) |  |  |
|**created** | [**Boolean**](Boolean.md) |  |  [optional] |
|**deleted** | [**Boolean**](Boolean.md) |  |  [optional] |
|**endpoint** | [**String**](String.md) |  |  [optional] |
|**endpoints** | [**Map**](Map.md) |  |  [optional] |
|**processing** | [**Boolean**](Boolean.md) |  |  [optional] |
|**upgradeProcessing** | [**Boolean**](Boolean.md) |  |  [optional] |
|**engineVersion** | [**String**](String.md) |  |  [optional] |
|**clusterConfig** | [**DomainStatusClusterConfig**](DomainStatusClusterConfig.md) |  |  |
|**ebSOptions** | [**DomainStatusEBSOptions**](DomainStatusEBSOptions.md) |  |  [optional] |
|**accessPolicies** | [**String**](String.md) |  |  [optional] |
|**snapshotOptions** | [**DomainStatusSnapshotOptions**](DomainStatusSnapshotOptions.md) |  |  [optional] |
|**vpCOptions** | [**DomainStatusVPCOptions**](DomainStatusVPCOptions.md) |  |  [optional] |
|**cognitoOptions** | [**DomainStatusCognitoOptions**](DomainStatusCognitoOptions.md) |  |  [optional] |
|**encryptionAtRestOptions** | [**DomainStatusEncryptionAtRestOptions**](DomainStatusEncryptionAtRestOptions.md) |  |  [optional] |
|**nodeToNodeEncryptionOptions** | [**DomainStatusNodeToNodeEncryptionOptions**](DomainStatusNodeToNodeEncryptionOptions.md) |  |  [optional] |
|**advancedOptions** | [**Map**](Map.md) |  |  [optional] |
|**logPublishingOptions** | [**Map**](Map.md) |  |  [optional] |
|**serviceSoftwareOptions** | [**DomainStatusServiceSoftwareOptions**](DomainStatusServiceSoftwareOptions.md) |  |  [optional] |
|**domainEndpointOptions** | [**CreateDomainRequestDomainEndpointOptions**](CreateDomainRequestDomainEndpointOptions.md) |  |  [optional] |
|**advancedSecurityOptions** | [**DomainStatusAdvancedSecurityOptions**](DomainStatusAdvancedSecurityOptions.md) |  |  [optional] |
|**autoTuneOptions** | [**DomainStatusAutoTuneOptions**](DomainStatusAutoTuneOptions.md) |  |  [optional] |
|**changeProgressDetails** | [**DomainStatusChangeProgressDetails**](DomainStatusChangeProgressDetails.md) |  |  [optional] |
|**offPeakWindowOptions** | [**DomainStatusOffPeakWindowOptions**](DomainStatusOffPeakWindowOptions.md) |  |  [optional] |
|**softwareUpdateOptions** | [**DomainStatusSoftwareUpdateOptions**](DomainStatusSoftwareUpdateOptions.md) |  |  [optional] |



