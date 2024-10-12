

# IosTestLoop

A test of an iOS application that implements one or more game loop scenarios. This test type accepts an archived application (.ipa file) and a list of integer scenarios that will be executed on the app sequentially.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appBundleId** | **String** | Output only. The bundle id for the application under test. |  [optional] |
|**appIpa** | [**FileReference**](FileReference.md) |  |  [optional] |
|**scenarios** | **List&lt;Integer&gt;** | The list of scenarios that should be run during the test. Defaults to the single scenario 0 if unspecified. |  [optional] |



