

# DeployServicePackageToNodeDescription

Defines description for downloading packages associated with a service manifest to image cache on a Service Fabric node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationTypeName** | **String** | The application type name as defined in the application manifest. |  |
|**applicationTypeVersion** | **String** | The version of the application type as defined in the application manifest. |  |
|**nodeName** | **String** | The name of a Service Fabric node. |  |
|**packageSharingPolicy** | [**List&lt;PackageSharingPolicyInfo&gt;**](PackageSharingPolicyInfo.md) | List of package sharing policy information. |  [optional] |
|**serviceManifestName** | **String** | The name of the service manifest. |  |



