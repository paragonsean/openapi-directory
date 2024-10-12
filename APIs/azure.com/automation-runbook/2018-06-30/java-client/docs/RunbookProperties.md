

# RunbookProperties

Definition of the runbook property type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **OffsetDateTime** | Gets or sets the creation time. |  [optional] |
|**description** | **String** | Gets or sets the description. |  [optional] |
|**draft** | [**RunbookDraft**](RunbookDraft.md) |  |  [optional] |
|**jobCount** | **Integer** | Gets or sets the job count of the runbook. |  [optional] |
|**lastModifiedBy** | **String** | Gets or sets the last modified by. |  [optional] |
|**lastModifiedTime** | **OffsetDateTime** | Gets or sets the last modified time. |  [optional] |
|**logActivityTrace** | **Integer** | Gets or sets the option to log activity trace of the runbook. |  [optional] |
|**logProgress** | **Boolean** | Gets or sets progress log option. |  [optional] |
|**logVerbose** | **Boolean** | Gets or sets verbose log option. |  [optional] |
|**outputTypes** | **List&lt;String&gt;** | Gets or sets the runbook output types. |  [optional] |
|**parameters** | [**Map&lt;String, RunbookParameter&gt;**](RunbookParameter.md) | Gets or sets the runbook parameters. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Gets or sets the provisioning state of the runbook. |  [optional] |
|**publishContentLink** | [**ContentLink**](ContentLink.md) |  |  [optional] |
|**runbookType** | [**RunbookTypeEnum**](#RunbookTypeEnum) | Gets or sets the type of the runbook. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Gets or sets the state of the runbook. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |



## Enum: RunbookTypeEnum

| Name | Value |
|---- | -----|
| SCRIPT | &quot;Script&quot; |
| GRAPH | &quot;Graph&quot; |
| POWER_SHELL_WORKFLOW | &quot;PowerShellWorkflow&quot; |
| POWER_SHELL | &quot;PowerShell&quot; |
| GRAPH_POWER_SHELL_WORKFLOW | &quot;GraphPowerShellWorkflow&quot; |
| GRAPH_POWER_SHELL | &quot;GraphPowerShell&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| NEW | &quot;New&quot; |
| EDIT | &quot;Edit&quot; |
| PUBLISHED | &quot;Published&quot; |



