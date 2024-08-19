# CloudTestingApi.AndroidInstrumentationTest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appApk** | [**FileReference**](FileReference.md) |  | [optional] 
**appBundle** | [**AppBundle**](AppBundle.md) |  | [optional] 
**appPackageId** | **String** | The java package for the application under test. The default value is determined by examining the application&#39;s manifest. | [optional] 
**orchestratorOption** | **String** | The option of whether running each test within its own invocation of instrumentation with Android Test Orchestrator or not. ** Orchestrator is only compatible with AndroidJUnitRunner version 1.1 or higher! ** Orchestrator offers the following benefits: - No shared state - Crashes are isolated - Logs are scoped per test See for more information about Android Test Orchestrator. If not set, the test will be run without the orchestrator. | [optional] 
**shardingOption** | [**ShardingOption**](ShardingOption.md) |  | [optional] 
**testApk** | [**FileReference**](FileReference.md) |  | [optional] 
**testPackageId** | **String** | The java package for the test to be executed. The default value is determined by examining the application&#39;s manifest. | [optional] 
**testRunnerClass** | **String** | The InstrumentationTestRunner class. The default value is determined by examining the application&#39;s manifest. | [optional] 
**testTargets** | **[String]** | Each target must be fully qualified with the package name or class name, in one of these formats: - \&quot;package package_name\&quot; - \&quot;class package_name.class_name\&quot; - \&quot;class package_name.class_name#method_name\&quot; If empty, all targets in the module will be run. | [optional] 



## Enum: OrchestratorOptionEnum


* `ORCHESTRATOR_OPTION_UNSPECIFIED` (value: `"ORCHESTRATOR_OPTION_UNSPECIFIED"`)

* `USE_ORCHESTRATOR` (value: `"USE_ORCHESTRATOR"`)

* `DO_NOT_USE_ORCHESTRATOR` (value: `"DO_NOT_USE_ORCHESTRATOR"`)




