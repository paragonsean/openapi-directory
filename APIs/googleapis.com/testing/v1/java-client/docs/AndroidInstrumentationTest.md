

# AndroidInstrumentationTest

A test of an Android application that can control an Android component independently of its normal lifecycle. Android instrumentation tests run an application APK and test APK inside the same process on a virtual or physical AndroidDevice. They also specify a test runner class, such as com.google.GoogleTestRunner, which can vary on the specific instrumentation framework chosen. See for more information on types of Android tests.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appApk** | [**FileReference**](FileReference.md) |  |  [optional] |
|**appBundle** | [**AppBundle**](AppBundle.md) |  |  [optional] |
|**appPackageId** | **String** | The java package for the application under test. The default value is determined by examining the application&#39;s manifest. |  [optional] |
|**orchestratorOption** | [**OrchestratorOptionEnum**](#OrchestratorOptionEnum) | The option of whether running each test within its own invocation of instrumentation with Android Test Orchestrator or not. ** Orchestrator is only compatible with AndroidJUnitRunner version 1.1 or higher! ** Orchestrator offers the following benefits: - No shared state - Crashes are isolated - Logs are scoped per test See for more information about Android Test Orchestrator. If not set, the test will be run without the orchestrator. |  [optional] |
|**shardingOption** | [**ShardingOption**](ShardingOption.md) |  |  [optional] |
|**testApk** | [**FileReference**](FileReference.md) |  |  [optional] |
|**testPackageId** | **String** | The java package for the test to be executed. The default value is determined by examining the application&#39;s manifest. |  [optional] |
|**testRunnerClass** | **String** | The InstrumentationTestRunner class. The default value is determined by examining the application&#39;s manifest. |  [optional] |
|**testTargets** | **List&lt;String&gt;** | Each target must be fully qualified with the package name or class name, in one of these formats: - \&quot;package package_name\&quot; - \&quot;class package_name.class_name\&quot; - \&quot;class package_name.class_name#method_name\&quot; If empty, all targets in the module will be run. |  [optional] |



## Enum: OrchestratorOptionEnum

| Name | Value |
|---- | -----|
| ORCHESTRATOR_OPTION_UNSPECIFIED | &quot;ORCHESTRATOR_OPTION_UNSPECIFIED&quot; |
| USE_ORCHESTRATOR | &quot;USE_ORCHESTRATOR&quot; |
| DO_NOT_USE_ORCHESTRATOR | &quot;DO_NOT_USE_ORCHESTRATOR&quot; |



