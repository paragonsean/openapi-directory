

# AndroidMatrix

A set of Android device configuration permutations is defined by the the cross-product of the given axes. Internally, the given AndroidMatrix will be expanded into a set of AndroidDevices. Only supported permutations will be instantiated. Invalid permutations (e.g., incompatible models/versions) are ignored.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**androidModelIds** | **List&lt;String&gt;** | Required. The ids of the set of Android device to be used. Use the TestEnvironmentDiscoveryService to get supported options. |  [optional] |
|**androidVersionIds** | **List&lt;String&gt;** | Required. The ids of the set of Android OS version to be used. Use the TestEnvironmentDiscoveryService to get supported options. |  [optional] |
|**locales** | **List&lt;String&gt;** | Required. The set of locales the test device will enable for testing. Use the TestEnvironmentDiscoveryService to get supported options. |  [optional] |
|**orientations** | **List&lt;String&gt;** | Required. The set of orientations to test with. Use the TestEnvironmentDiscoveryService to get supported options. |  [optional] |



