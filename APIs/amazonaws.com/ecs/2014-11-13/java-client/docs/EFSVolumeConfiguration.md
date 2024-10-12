

# EFSVolumeConfiguration

This parameter is specified when you're using an Amazon Elastic File System file system for task storage. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/efs-volumes.html\">Amazon EFS volumes</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileSystemId** | [**String**](String.md) |  |  |
|**rootDirectory** | [**String**](String.md) |  |  [optional] |
|**transitEncryption** | [**EFSTransitEncryption**](EFSTransitEncryption.md) |  |  [optional] |
|**transitEncryptionPort** | [**Integer**](Integer.md) |  |  [optional] |
|**authorizationConfig** | [**EFSVolumeConfigurationAuthorizationConfig**](EFSVolumeConfigurationAuthorizationConfig.md) |  |  [optional] |



