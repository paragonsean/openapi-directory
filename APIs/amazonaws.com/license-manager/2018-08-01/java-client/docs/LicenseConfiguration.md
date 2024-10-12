

# LicenseConfiguration

A license configuration is an abstraction of a customer license agreement that can be consumed and enforced by License Manager. Components include specifications for the license type (licensing by instance, socket, CPU, or vCPU), allowed tenancy (shared tenancy, Dedicated Instance, Dedicated Host, or all of these), host affinity (how long a VM must be associated with a host), and the number of licenses purchased and used.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**licenseConfigurationId** | [**String**](String.md) |  |  [optional] |
|**licenseConfigurationArn** | [**String**](String.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**description** | [**String**](String.md) |  |  [optional] |
|**licenseCountingType** | [**LicenseCountingType**](LicenseCountingType.md) |  |  [optional] |
|**licenseRules** | [**List**](List.md) |  |  [optional] |
|**licenseCount** | [**Integer**](Integer.md) |  |  [optional] |
|**licenseCountHardLimit** | [**Boolean**](Boolean.md) |  |  [optional] |
|**disassociateWhenNotFound** | [**Boolean**](Boolean.md) |  |  [optional] |
|**consumedLicenses** | [**Integer**](Integer.md) |  |  [optional] |
|**status** | [**String**](String.md) |  |  [optional] |
|**ownerAccountId** | [**String**](String.md) |  |  [optional] |
|**consumedLicenseSummaryList** | [**List**](List.md) |  |  [optional] |
|**managedResourceSummaryList** | [**List**](List.md) |  |  [optional] |
|**productInformationList** | [**List**](List.md) |  |  [optional] |
|**automatedDiscoveryInformation** | [**GetLicenseConfigurationResponseAutomatedDiscoveryInformation**](GetLicenseConfigurationResponseAutomatedDiscoveryInformation.md) |  |  [optional] |



