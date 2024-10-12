# AwsStorageGateway.DescribeSMBSettingsOutput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gatewayARN** | **String** | The Amazon Resource Name (ARN) of the gateway. Use the &lt;a&gt;ListGateways&lt;/a&gt; operation to return a list of gateways for your account and Amazon Web Services Region. | [optional] 
**domainName** | **String** |  | [optional] 
**activeDirectoryStatus** | [**ActiveDirectoryStatus**](ActiveDirectoryStatus.md) |  | [optional] 
**sMBGuestPasswordSet** | **Boolean** |  | [optional] 
**sMBSecurityStrategy** | [**SMBSecurityStrategy**](SMBSecurityStrategy.md) |  | [optional] 
**fileSharesVisible** | **Boolean** |  | [optional] 
**sMBLocalGroups** | [**DescribeSMBSettingsOutputSMBLocalGroups**](DescribeSMBSettingsOutputSMBLocalGroups.md) |  | [optional] 


