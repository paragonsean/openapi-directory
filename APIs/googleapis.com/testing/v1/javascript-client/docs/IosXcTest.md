# CloudTestingApi.IosXcTest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appBundleId** | **String** | Output only. The bundle id for the application under test. | [optional] 
**testSpecialEntitlements** | **Boolean** | The option to test special app entitlements. Setting this would re-sign the app having special entitlements with an explicit application-identifier. Currently supports testing aps-environment entitlement. | [optional] 
**testsZip** | [**FileReference**](FileReference.md) |  | [optional] 
**xcodeVersion** | **String** | The Xcode version that should be used for the test. Use the TestEnvironmentDiscoveryService to get supported options. Defaults to the latest Xcode version Firebase Test Lab supports. | [optional] 
**xctestrun** | [**FileReference**](FileReference.md) |  | [optional] 


