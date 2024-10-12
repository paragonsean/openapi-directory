

# ConfigManagementGatekeeperDeploymentState

State of Policy Controller installation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gatekeeperAudit** | [**GatekeeperAuditEnum**](#GatekeeperAuditEnum) | Status of gatekeeper-audit deployment. |  [optional] |
|**gatekeeperControllerManagerState** | [**GatekeeperControllerManagerStateEnum**](#GatekeeperControllerManagerStateEnum) | Status of gatekeeper-controller-manager pod. |  [optional] |
|**gatekeeperMutation** | [**GatekeeperMutationEnum**](#GatekeeperMutationEnum) | Status of the pod serving the mutation webhook. |  [optional] |



## Enum: GatekeeperAuditEnum

| Name | Value |
|---- | -----|
| DEPLOYMENT_STATE_UNSPECIFIED | &quot;DEPLOYMENT_STATE_UNSPECIFIED&quot; |
| NOT_INSTALLED | &quot;NOT_INSTALLED&quot; |
| INSTALLED | &quot;INSTALLED&quot; |
| ERROR | &quot;ERROR&quot; |
| PENDING | &quot;PENDING&quot; |



## Enum: GatekeeperControllerManagerStateEnum

| Name | Value |
|---- | -----|
| DEPLOYMENT_STATE_UNSPECIFIED | &quot;DEPLOYMENT_STATE_UNSPECIFIED&quot; |
| NOT_INSTALLED | &quot;NOT_INSTALLED&quot; |
| INSTALLED | &quot;INSTALLED&quot; |
| ERROR | &quot;ERROR&quot; |
| PENDING | &quot;PENDING&quot; |



## Enum: GatekeeperMutationEnum

| Name | Value |
|---- | -----|
| DEPLOYMENT_STATE_UNSPECIFIED | &quot;DEPLOYMENT_STATE_UNSPECIFIED&quot; |
| NOT_INSTALLED | &quot;NOT_INSTALLED&quot; |
| INSTALLED | &quot;INSTALLED&quot; |
| ERROR | &quot;ERROR&quot; |
| PENDING | &quot;PENDING&quot; |



