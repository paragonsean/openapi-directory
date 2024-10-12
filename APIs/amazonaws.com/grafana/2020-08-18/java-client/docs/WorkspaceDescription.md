

# WorkspaceDescription

A structure containing information about an Amazon Managed Grafana workspace in your account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountAccessType** | [**AccountAccessType**](AccountAccessType.md) |  |  [optional] |
|**authentication** | [**WorkspaceDescriptionAuthentication**](WorkspaceDescriptionAuthentication.md) |  |  |
|**created** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**dataSources** | [**List**](List.md) |  |  |
|**description** | [**String**](String.md) |  |  [optional] |
|**endpoint** | [**String**](String.md) |  |  |
|**freeTrialConsumed** | [**Boolean**](Boolean.md) |  |  [optional] |
|**freeTrialExpiration** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**grafanaVersion** | [**String**](String.md) |  |  |
|**id** | [**String**](String.md) |  |  |
|**licenseExpiration** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**licenseType** | [**LicenseType**](LicenseType.md) |  |  [optional] |
|**modified** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**name** | [**String**](String.md) |  |  [optional] |
|**networkAccessControl** | [**WorkspaceDescriptionNetworkAccessControl**](WorkspaceDescriptionNetworkAccessControl.md) |  |  [optional] |
|**notificationDestinations** | [**List**](List.md) |  |  [optional] |
|**organizationRoleName** | [**String**](String.md) |  |  [optional] |
|**organizationalUnits** | [**List**](List.md) |  |  [optional] |
|**permissionType** | [**PermissionType**](PermissionType.md) |  |  [optional] |
|**stackSetName** | [**String**](String.md) |  |  [optional] |
|**status** | [**WorkspaceStatus**](WorkspaceStatus.md) |  |  |
|**tags** | [**Map**](Map.md) |  |  [optional] |
|**vpcConfiguration** | [**WorkspaceDescriptionVpcConfiguration**](WorkspaceDescriptionVpcConfiguration.md) |  |  [optional] |
|**workspaceRoleArn** | [**String**](String.md) |  |  [optional] |



