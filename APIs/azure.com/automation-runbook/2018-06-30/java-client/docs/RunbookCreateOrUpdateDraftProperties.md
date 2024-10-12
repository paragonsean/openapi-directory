

# RunbookCreateOrUpdateDraftProperties

The parameters supplied to the create or update draft runbook properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Gets or sets the description of the runbook. |  [optional] |
|**draft** | [**RunbookDraft**](RunbookDraft.md) |  |  |
|**logActivityTrace** | **Integer** | Gets or sets the activity-level tracing options of the runbook. |  [optional] |
|**logProgress** | **Boolean** | Gets or sets progress log option. |  [optional] |
|**logVerbose** | **Boolean** | Gets or sets verbose log option. |  [optional] |
|**runbookType** | [**RunbookTypeEnum**](#RunbookTypeEnum) | Gets or sets the type of the runbook. |  |



## Enum: RunbookTypeEnum

| Name | Value |
|---- | -----|
| SCRIPT | &quot;Script&quot; |
| GRAPH | &quot;Graph&quot; |
| POWER_SHELL_WORKFLOW | &quot;PowerShellWorkflow&quot; |
| POWER_SHELL | &quot;PowerShell&quot; |
| GRAPH_POWER_SHELL_WORKFLOW | &quot;GraphPowerShellWorkflow&quot; |
| GRAPH_POWER_SHELL | &quot;GraphPowerShell&quot; |



