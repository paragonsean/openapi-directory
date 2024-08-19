

# EnvironmentApprovals

An entry in the reviews log for environment deployments

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comment** | **String** | The comment submitted with the deployment review |  |
|**environments** | [**List&lt;EnvironmentApprovalsEnvironmentsInner&gt;**](EnvironmentApprovalsEnvironmentsInner.md) | The list of environments that were approved or rejected |  |
|**state** | [**StateEnum**](#StateEnum) | Whether deployment to the environment(s) was approved or rejected |  |
|**user** | [**SimpleUser**](SimpleUser.md) |  |  |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| APPROVED | &quot;approved&quot; |
| REJECTED | &quot;rejected&quot; |



