

# GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicy

FeaturePolicy defines features allowed to be used on RBE instances, as well as instance-wide behavior changes that take effect without opt-in or opt-out at usage time.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionHermeticity** | [**ActionHermeticityEnum**](#ActionHermeticityEnum) | Defines the hermeticity policy for actions on this instance. DO NOT USE: Experimental / unlaunched feature. |  [optional] |
|**actionIsolation** | [**ActionIsolationEnum**](#ActionIsolationEnum) | Defines the isolation policy for actions on this instance. DO NOT USE: Experimental / unlaunched feature. |  [optional] |
|**containerImageSources** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature.md) |  |  [optional] |
|**dockerAddCapabilities** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature.md) |  |  [optional] |
|**dockerChrootPath** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature.md) |  |  [optional] |
|**dockerNetwork** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature.md) |  |  [optional] |
|**dockerPrivileged** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature.md) |  |  [optional] |
|**dockerRunAsContainerProvidedUser** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature.md) |  |  [optional] |
|**dockerRunAsRoot** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature.md) |  |  [optional] |
|**dockerRuntime** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature.md) |  |  [optional] |
|**dockerSiblingContainers** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature.md) |  |  [optional] |
|**dockerUlimits** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature.md) |  |  [optional] |
|**linuxExecution** | [**LinuxExecutionEnum**](#LinuxExecutionEnum) | Defines how Linux actions are allowed to execute. DO NOT USE: Experimental / unlaunched feature. |  [optional] |
|**linuxIsolation** | [**LinuxIsolationEnum**](#LinuxIsolationEnum) | linux_isolation allows overriding the docker runtime used for containers started on Linux. |  [optional] |
|**macExecution** | [**MacExecutionEnum**](#MacExecutionEnum) | Defines how Windows actions are allowed to execute. DO NOT USE: Experimental / unlaunched feature. |  [optional] |
|**vmVerification** | [**VmVerificationEnum**](#VmVerificationEnum) | Whether to verify CreateBotSession and UpdateBotSession from the bot. |  [optional] |
|**windowsExecution** | [**WindowsExecutionEnum**](#WindowsExecutionEnum) | Defines how Windows actions are allowed to execute. DO NOT USE: Experimental / unlaunched feature. |  [optional] |



## Enum: ActionHermeticityEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ACTION_HERMETICITY_UNSPECIFIED&quot; |
| OFF | &quot;ACTION_HERMETICITY_OFF&quot; |
| ENFORCED | &quot;ACTION_HERMETICITY_ENFORCED&quot; |
| BEST_EFFORT | &quot;ACTION_HERMETICITY_BEST_EFFORT&quot; |



## Enum: ActionIsolationEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ACTION_ISOLATION_UNSPECIFIED&quot; |
| OFF | &quot;ACTION_ISOLATION_OFF&quot; |
| ENFORCED | &quot;ACTION_ISOLATION_ENFORCED&quot; |



## Enum: LinuxExecutionEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;LINUX_EXECUTION_UNSPECIFIED&quot; |
| FORBIDDEN | &quot;LINUX_EXECUTION_FORBIDDEN&quot; |
| UNRESTRICTED | &quot;LINUX_EXECUTION_UNRESTRICTED&quot; |
| HARDENED_GVISOR | &quot;LINUX_EXECUTION_HARDENED_GVISOR&quot; |
| HARDENED_GVISOR_OR_TERMINAL | &quot;LINUX_EXECUTION_HARDENED_GVISOR_OR_TERMINAL&quot; |



## Enum: LinuxIsolationEnum

| Name | Value |
|---- | -----|
| LINUX_ISOLATION_UNSPECIFIED | &quot;LINUX_ISOLATION_UNSPECIFIED&quot; |
| GVISOR | &quot;GVISOR&quot; |
| FALSE | &quot;false&quot; |



## Enum: MacExecutionEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;MAC_EXECUTION_UNSPECIFIED&quot; |
| FORBIDDEN | &quot;MAC_EXECUTION_FORBIDDEN&quot; |



## Enum: VmVerificationEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;VM_VERIFICATION_UNSPECIFIED&quot; |
| GCP_TOKEN | &quot;VM_VERIFICATION_GCP_TOKEN&quot; |
| OFF | &quot;VM_VERIFICATION_OFF&quot; |



## Enum: WindowsExecutionEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;WINDOWS_EXECUTION_UNSPECIFIED&quot; |
| FORBIDDEN | &quot;WINDOWS_EXECUTION_FORBIDDEN&quot; |
| UNRESTRICTED | &quot;WINDOWS_EXECUTION_UNRESTRICTED&quot; |
| TERMINAL | &quot;WINDOWS_EXECUTION_TERMINAL&quot; |



