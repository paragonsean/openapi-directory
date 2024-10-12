

# IosXcTest

A test of an iOS application that uses the XCTest framework. Xcode supports the option to \"build for testing\", which generates an .xctestrun file that contains a test specification (arguments, test methods, etc). This test type accepts a zip file containing the .xctestrun file and the corresponding contents of the Build/Products directory that contains all the binaries needed to run the tests.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appBundleId** | **String** | Output only. The bundle id for the application under test. |  [optional] |
|**testSpecialEntitlements** | **Boolean** | The option to test special app entitlements. Setting this would re-sign the app having special entitlements with an explicit application-identifier. Currently supports testing aps-environment entitlement. |  [optional] |
|**testsZip** | [**FileReference**](FileReference.md) |  |  [optional] |
|**xcodeVersion** | **String** | The Xcode version that should be used for the test. Use the TestEnvironmentDiscoveryService to get supported options. Defaults to the latest Xcode version Firebase Test Lab supports. |  [optional] |
|**xctestrun** | [**FileReference**](FileReference.md) |  |  [optional] |



