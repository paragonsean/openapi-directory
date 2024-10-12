# CloudTestingApi.TestMatrix

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientInfo** | [**ClientInfo**](ClientInfo.md) |  | [optional] 
**environmentMatrix** | [**EnvironmentMatrix**](EnvironmentMatrix.md) |  | [optional] 
**extendedInvalidMatrixDetails** | [**[MatrixErrorDetail]**](MatrixErrorDetail.md) | Output only. Details about why a matrix was deemed invalid. If multiple checks can be safely performed, they will be reported but no assumptions should be made about the length of this list. | [optional] [readonly] 
**failFast** | **Boolean** | If true, only a single attempt at most will be made to run each execution/shard in the matrix. Flaky test attempts are not affected. Normally, 2 or more attempts are made if a potential infrastructure issue is detected. This feature is for latency sensitive workloads. The incidence of execution failures may be significantly greater for fail-fast matrices and support is more limited because of that expectation. | [optional] 
**flakyTestAttempts** | **Number** | The number of times a TestExecution should be re-attempted if one or more of its test cases fail for any reason. The maximum number of reruns allowed is 10. Default is 0, which implies no reruns. | [optional] 
**invalidMatrixDetails** | **String** | Output only. Describes why the matrix is considered invalid. Only useful for matrices in the INVALID state. | [optional] 
**outcomeSummary** | **String** | Output Only. The overall outcome of the test. Only set when the test matrix state is FINISHED. | [optional] 
**projectId** | **String** | The cloud project that owns the test matrix. | [optional] 
**resultStorage** | [**ResultStorage**](ResultStorage.md) |  | [optional] 
**state** | **String** | Output only. Indicates the current progress of the test matrix. | [optional] 
**testExecutions** | [**[TestExecution]**](TestExecution.md) | Output only. The list of test executions that the service creates for this matrix. | [optional] 
**testMatrixId** | **String** | Output only. Unique id set by the service. | [optional] 
**testSpecification** | [**TestSpecification**](TestSpecification.md) |  | [optional] 
**timestamp** | **String** | Output only. The time this test matrix was initially created. | [optional] 



## Enum: InvalidMatrixDetailsEnum


* `INVALID_MATRIX_DETAILS_UNSPECIFIED` (value: `"INVALID_MATRIX_DETAILS_UNSPECIFIED"`)

* `DETAILS_UNAVAILABLE` (value: `"DETAILS_UNAVAILABLE"`)

* `MALFORMED_APK` (value: `"MALFORMED_APK"`)

* `MALFORMED_TEST_APK` (value: `"MALFORMED_TEST_APK"`)

* `NO_MANIFEST` (value: `"NO_MANIFEST"`)

* `NO_PACKAGE_NAME` (value: `"NO_PACKAGE_NAME"`)

* `INVALID_PACKAGE_NAME` (value: `"INVALID_PACKAGE_NAME"`)

* `TEST_SAME_AS_APP` (value: `"TEST_SAME_AS_APP"`)

* `NO_INSTRUMENTATION` (value: `"NO_INSTRUMENTATION"`)

* `NO_SIGNATURE` (value: `"NO_SIGNATURE"`)

* `INSTRUMENTATION_ORCHESTRATOR_INCOMPATIBLE` (value: `"INSTRUMENTATION_ORCHESTRATOR_INCOMPATIBLE"`)

* `NO_TEST_RUNNER_CLASS` (value: `"NO_TEST_RUNNER_CLASS"`)

* `NO_LAUNCHER_ACTIVITY` (value: `"NO_LAUNCHER_ACTIVITY"`)

* `FORBIDDEN_PERMISSIONS` (value: `"FORBIDDEN_PERMISSIONS"`)

* `INVALID_ROBO_DIRECTIVES` (value: `"INVALID_ROBO_DIRECTIVES"`)

* `INVALID_RESOURCE_NAME` (value: `"INVALID_RESOURCE_NAME"`)

* `INVALID_DIRECTIVE_ACTION` (value: `"INVALID_DIRECTIVE_ACTION"`)

* `TEST_LOOP_INTENT_FILTER_NOT_FOUND` (value: `"TEST_LOOP_INTENT_FILTER_NOT_FOUND"`)

* `SCENARIO_LABEL_NOT_DECLARED` (value: `"SCENARIO_LABEL_NOT_DECLARED"`)

* `SCENARIO_LABEL_MALFORMED` (value: `"SCENARIO_LABEL_MALFORMED"`)

* `SCENARIO_NOT_DECLARED` (value: `"SCENARIO_NOT_DECLARED"`)

* `DEVICE_ADMIN_RECEIVER` (value: `"DEVICE_ADMIN_RECEIVER"`)

* `MALFORMED_XC_TEST_ZIP` (value: `"MALFORMED_XC_TEST_ZIP"`)

* `BUILT_FOR_IOS_SIMULATOR` (value: `"BUILT_FOR_IOS_SIMULATOR"`)

* `NO_TESTS_IN_XC_TEST_ZIP` (value: `"NO_TESTS_IN_XC_TEST_ZIP"`)

* `USE_DESTINATION_ARTIFACTS` (value: `"USE_DESTINATION_ARTIFACTS"`)

* `TEST_NOT_APP_HOSTED` (value: `"TEST_NOT_APP_HOSTED"`)

* `PLIST_CANNOT_BE_PARSED` (value: `"PLIST_CANNOT_BE_PARSED"`)

* `TEST_ONLY_APK` (value: `"TEST_ONLY_APK"`)

* `MALFORMED_IPA` (value: `"MALFORMED_IPA"`)

* `MISSING_URL_SCHEME` (value: `"MISSING_URL_SCHEME"`)

* `MALFORMED_APP_BUNDLE` (value: `"MALFORMED_APP_BUNDLE"`)

* `NO_CODE_APK` (value: `"NO_CODE_APK"`)

* `INVALID_INPUT_APK` (value: `"INVALID_INPUT_APK"`)

* `INVALID_APK_PREVIEW_SDK` (value: `"INVALID_APK_PREVIEW_SDK"`)

* `MATRIX_TOO_LARGE` (value: `"MATRIX_TOO_LARGE"`)

* `TEST_QUOTA_EXCEEDED` (value: `"TEST_QUOTA_EXCEEDED"`)

* `SERVICE_NOT_ACTIVATED` (value: `"SERVICE_NOT_ACTIVATED"`)

* `UNKNOWN_PERMISSION_ERROR` (value: `"UNKNOWN_PERMISSION_ERROR"`)





## Enum: OutcomeSummaryEnum


* `OUTCOME_SUMMARY_UNSPECIFIED` (value: `"OUTCOME_SUMMARY_UNSPECIFIED"`)

* `SUCCESS` (value: `"SUCCESS"`)

* `FAILURE` (value: `"FAILURE"`)

* `INCONCLUSIVE` (value: `"INCONCLUSIVE"`)

* `SKIPPED` (value: `"SKIPPED"`)





## Enum: StateEnum


* `TEST_STATE_UNSPECIFIED` (value: `"TEST_STATE_UNSPECIFIED"`)

* `VALIDATING` (value: `"VALIDATING"`)

* `PENDING` (value: `"PENDING"`)

* `RUNNING` (value: `"RUNNING"`)

* `FINISHED` (value: `"FINISHED"`)

* `ERROR` (value: `"ERROR"`)

* `UNSUPPORTED_ENVIRONMENT` (value: `"UNSUPPORTED_ENVIRONMENT"`)

* `INCOMPATIBLE_ENVIRONMENT` (value: `"INCOMPATIBLE_ENVIRONMENT"`)

* `INCOMPATIBLE_ARCHITECTURE` (value: `"INCOMPATIBLE_ARCHITECTURE"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `INVALID` (value: `"INVALID"`)




