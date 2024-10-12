# RemoteBuildExecutionApi.GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionHermeticity** | **String** | Defines the hermeticity policy for actions on this instance. DO NOT USE: Experimental / unlaunched feature. | [optional] 
**actionIsolation** | **String** | Defines the isolation policy for actions on this instance. DO NOT USE: Experimental / unlaunched feature. | [optional] 
**containerImageSources** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature.md) |  | [optional] 
**dockerAddCapabilities** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature.md) |  | [optional] 
**dockerChrootPath** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature.md) |  | [optional] 
**dockerNetwork** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature.md) |  | [optional] 
**dockerPrivileged** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature.md) |  | [optional] 
**dockerRunAsContainerProvidedUser** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature.md) |  | [optional] 
**dockerRunAsRoot** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature.md) |  | [optional] 
**dockerRuntime** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature.md) |  | [optional] 
**dockerSiblingContainers** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature.md) |  | [optional] 
**dockerUlimits** | [**GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature**](GoogleDevtoolsRemotebuildexecutionAdminV1alphaFeaturePolicyFeature.md) |  | [optional] 
**linuxExecution** | **String** | Defines how Linux actions are allowed to execute. DO NOT USE: Experimental / unlaunched feature. | [optional] 
**linuxIsolation** | **String** | linux_isolation allows overriding the docker runtime used for containers started on Linux. | [optional] 
**macExecution** | **String** | Defines how Windows actions are allowed to execute. DO NOT USE: Experimental / unlaunched feature. | [optional] 
**vmVerification** | **String** | Whether to verify CreateBotSession and UpdateBotSession from the bot. | [optional] 
**windowsExecution** | **String** | Defines how Windows actions are allowed to execute. DO NOT USE: Experimental / unlaunched feature. | [optional] 



## Enum: ActionHermeticityEnum


* `UNSPECIFIED` (value: `"ACTION_HERMETICITY_UNSPECIFIED"`)

* `OFF` (value: `"ACTION_HERMETICITY_OFF"`)

* `ENFORCED` (value: `"ACTION_HERMETICITY_ENFORCED"`)

* `BEST_EFFORT` (value: `"ACTION_HERMETICITY_BEST_EFFORT"`)





## Enum: ActionIsolationEnum


* `UNSPECIFIED` (value: `"ACTION_ISOLATION_UNSPECIFIED"`)

* `OFF` (value: `"ACTION_ISOLATION_OFF"`)

* `ENFORCED` (value: `"ACTION_ISOLATION_ENFORCED"`)





## Enum: LinuxExecutionEnum


* `UNSPECIFIED` (value: `"LINUX_EXECUTION_UNSPECIFIED"`)

* `FORBIDDEN` (value: `"LINUX_EXECUTION_FORBIDDEN"`)

* `UNRESTRICTED` (value: `"LINUX_EXECUTION_UNRESTRICTED"`)

* `HARDENED_GVISOR` (value: `"LINUX_EXECUTION_HARDENED_GVISOR"`)

* `HARDENED_GVISOR_OR_TERMINAL` (value: `"LINUX_EXECUTION_HARDENED_GVISOR_OR_TERMINAL"`)





## Enum: LinuxIsolationEnum


* `LINUX_ISOLATION_UNSPECIFIED` (value: `"LINUX_ISOLATION_UNSPECIFIED"`)

* `GVISOR` (value: `"GVISOR"`)

* `false` (value: `"false"`)





## Enum: MacExecutionEnum


* `UNSPECIFIED` (value: `"MAC_EXECUTION_UNSPECIFIED"`)

* `FORBIDDEN` (value: `"MAC_EXECUTION_FORBIDDEN"`)





## Enum: VmVerificationEnum


* `UNSPECIFIED` (value: `"VM_VERIFICATION_UNSPECIFIED"`)

* `GCP_TOKEN` (value: `"VM_VERIFICATION_GCP_TOKEN"`)

* `OFF` (value: `"VM_VERIFICATION_OFF"`)





## Enum: WindowsExecutionEnum


* `UNSPECIFIED` (value: `"WINDOWS_EXECUTION_UNSPECIFIED"`)

* `FORBIDDEN` (value: `"WINDOWS_EXECUTION_FORBIDDEN"`)

* `UNRESTRICTED` (value: `"WINDOWS_EXECUTION_UNRESTRICTED"`)

* `TERMINAL` (value: `"WINDOWS_EXECUTION_TERMINAL"`)




