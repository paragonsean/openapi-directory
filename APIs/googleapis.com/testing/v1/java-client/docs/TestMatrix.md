

# TestMatrix

TestMatrix captures all details about a test. It contains the environment configuration, test specification, test executions and overall state and outcome.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientInfo** | [**ClientInfo**](ClientInfo.md) |  |  [optional] |
|**environmentMatrix** | [**EnvironmentMatrix**](EnvironmentMatrix.md) |  |  [optional] |
|**extendedInvalidMatrixDetails** | [**List&lt;MatrixErrorDetail&gt;**](MatrixErrorDetail.md) | Output only. Details about why a matrix was deemed invalid. If multiple checks can be safely performed, they will be reported but no assumptions should be made about the length of this list. |  [optional] [readonly] |
|**failFast** | **Boolean** | If true, only a single attempt at most will be made to run each execution/shard in the matrix. Flaky test attempts are not affected. Normally, 2 or more attempts are made if a potential infrastructure issue is detected. This feature is for latency sensitive workloads. The incidence of execution failures may be significantly greater for fail-fast matrices and support is more limited because of that expectation. |  [optional] |
|**flakyTestAttempts** | **Integer** | The number of times a TestExecution should be re-attempted if one or more of its test cases fail for any reason. The maximum number of reruns allowed is 10. Default is 0, which implies no reruns. |  [optional] |
|**invalidMatrixDetails** | [**InvalidMatrixDetailsEnum**](#InvalidMatrixDetailsEnum) | Output only. Describes why the matrix is considered invalid. Only useful for matrices in the INVALID state. |  [optional] |
|**outcomeSummary** | [**OutcomeSummaryEnum**](#OutcomeSummaryEnum) | Output Only. The overall outcome of the test. Only set when the test matrix state is FINISHED. |  [optional] |
|**projectId** | **String** | The cloud project that owns the test matrix. |  [optional] |
|**resultStorage** | [**ResultStorage**](ResultStorage.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Indicates the current progress of the test matrix. |  [optional] |
|**testExecutions** | [**List&lt;TestExecution&gt;**](TestExecution.md) | Output only. The list of test executions that the service creates for this matrix. |  [optional] |
|**testMatrixId** | **String** | Output only. Unique id set by the service. |  [optional] |
|**testSpecification** | [**TestSpecification**](TestSpecification.md) |  |  [optional] |
|**timestamp** | **String** | Output only. The time this test matrix was initially created. |  [optional] |



## Enum: InvalidMatrixDetailsEnum

| Name | Value |
|---- | -----|
| INVALID_MATRIX_DETAILS_UNSPECIFIED | &quot;INVALID_MATRIX_DETAILS_UNSPECIFIED&quot; |
| DETAILS_UNAVAILABLE | &quot;DETAILS_UNAVAILABLE&quot; |
| MALFORMED_APK | &quot;MALFORMED_APK&quot; |
| MALFORMED_TEST_APK | &quot;MALFORMED_TEST_APK&quot; |
| NO_MANIFEST | &quot;NO_MANIFEST&quot; |
| NO_PACKAGE_NAME | &quot;NO_PACKAGE_NAME&quot; |
| INVALID_PACKAGE_NAME | &quot;INVALID_PACKAGE_NAME&quot; |
| TEST_SAME_AS_APP | &quot;TEST_SAME_AS_APP&quot; |
| NO_INSTRUMENTATION | &quot;NO_INSTRUMENTATION&quot; |
| NO_SIGNATURE | &quot;NO_SIGNATURE&quot; |
| INSTRUMENTATION_ORCHESTRATOR_INCOMPATIBLE | &quot;INSTRUMENTATION_ORCHESTRATOR_INCOMPATIBLE&quot; |
| NO_TEST_RUNNER_CLASS | &quot;NO_TEST_RUNNER_CLASS&quot; |
| NO_LAUNCHER_ACTIVITY | &quot;NO_LAUNCHER_ACTIVITY&quot; |
| FORBIDDEN_PERMISSIONS | &quot;FORBIDDEN_PERMISSIONS&quot; |
| INVALID_ROBO_DIRECTIVES | &quot;INVALID_ROBO_DIRECTIVES&quot; |
| INVALID_RESOURCE_NAME | &quot;INVALID_RESOURCE_NAME&quot; |
| INVALID_DIRECTIVE_ACTION | &quot;INVALID_DIRECTIVE_ACTION&quot; |
| TEST_LOOP_INTENT_FILTER_NOT_FOUND | &quot;TEST_LOOP_INTENT_FILTER_NOT_FOUND&quot; |
| SCENARIO_LABEL_NOT_DECLARED | &quot;SCENARIO_LABEL_NOT_DECLARED&quot; |
| SCENARIO_LABEL_MALFORMED | &quot;SCENARIO_LABEL_MALFORMED&quot; |
| SCENARIO_NOT_DECLARED | &quot;SCENARIO_NOT_DECLARED&quot; |
| DEVICE_ADMIN_RECEIVER | &quot;DEVICE_ADMIN_RECEIVER&quot; |
| MALFORMED_XC_TEST_ZIP | &quot;MALFORMED_XC_TEST_ZIP&quot; |
| BUILT_FOR_IOS_SIMULATOR | &quot;BUILT_FOR_IOS_SIMULATOR&quot; |
| NO_TESTS_IN_XC_TEST_ZIP | &quot;NO_TESTS_IN_XC_TEST_ZIP&quot; |
| USE_DESTINATION_ARTIFACTS | &quot;USE_DESTINATION_ARTIFACTS&quot; |
| TEST_NOT_APP_HOSTED | &quot;TEST_NOT_APP_HOSTED&quot; |
| PLIST_CANNOT_BE_PARSED | &quot;PLIST_CANNOT_BE_PARSED&quot; |
| TEST_ONLY_APK | &quot;TEST_ONLY_APK&quot; |
| MALFORMED_IPA | &quot;MALFORMED_IPA&quot; |
| MISSING_URL_SCHEME | &quot;MISSING_URL_SCHEME&quot; |
| MALFORMED_APP_BUNDLE | &quot;MALFORMED_APP_BUNDLE&quot; |
| NO_CODE_APK | &quot;NO_CODE_APK&quot; |
| INVALID_INPUT_APK | &quot;INVALID_INPUT_APK&quot; |
| INVALID_APK_PREVIEW_SDK | &quot;INVALID_APK_PREVIEW_SDK&quot; |
| MATRIX_TOO_LARGE | &quot;MATRIX_TOO_LARGE&quot; |
| TEST_QUOTA_EXCEEDED | &quot;TEST_QUOTA_EXCEEDED&quot; |
| SERVICE_NOT_ACTIVATED | &quot;SERVICE_NOT_ACTIVATED&quot; |
| UNKNOWN_PERMISSION_ERROR | &quot;UNKNOWN_PERMISSION_ERROR&quot; |



## Enum: OutcomeSummaryEnum

| Name | Value |
|---- | -----|
| OUTCOME_SUMMARY_UNSPECIFIED | &quot;OUTCOME_SUMMARY_UNSPECIFIED&quot; |
| SUCCESS | &quot;SUCCESS&quot; |
| FAILURE | &quot;FAILURE&quot; |
| INCONCLUSIVE | &quot;INCONCLUSIVE&quot; |
| SKIPPED | &quot;SKIPPED&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| TEST_STATE_UNSPECIFIED | &quot;TEST_STATE_UNSPECIFIED&quot; |
| VALIDATING | &quot;VALIDATING&quot; |
| PENDING | &quot;PENDING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| FINISHED | &quot;FINISHED&quot; |
| ERROR | &quot;ERROR&quot; |
| UNSUPPORTED_ENVIRONMENT | &quot;UNSUPPORTED_ENVIRONMENT&quot; |
| INCOMPATIBLE_ENVIRONMENT | &quot;INCOMPATIBLE_ENVIRONMENT&quot; |
| INCOMPATIBLE_ARCHITECTURE | &quot;INCOMPATIBLE_ARCHITECTURE&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| INVALID | &quot;INVALID&quot; |



