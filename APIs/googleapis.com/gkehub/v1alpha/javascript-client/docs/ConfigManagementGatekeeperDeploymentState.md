# GkeHubApi.ConfigManagementGatekeeperDeploymentState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gatekeeperAudit** | **String** | Status of gatekeeper-audit deployment. | [optional] 
**gatekeeperControllerManagerState** | **String** | Status of gatekeeper-controller-manager pod. | [optional] 
**gatekeeperMutation** | **String** | Status of the pod serving the mutation webhook. | [optional] 



## Enum: GatekeeperAuditEnum


* `DEPLOYMENT_STATE_UNSPECIFIED` (value: `"DEPLOYMENT_STATE_UNSPECIFIED"`)

* `NOT_INSTALLED` (value: `"NOT_INSTALLED"`)

* `INSTALLED` (value: `"INSTALLED"`)

* `ERROR` (value: `"ERROR"`)

* `PENDING` (value: `"PENDING"`)





## Enum: GatekeeperControllerManagerStateEnum


* `DEPLOYMENT_STATE_UNSPECIFIED` (value: `"DEPLOYMENT_STATE_UNSPECIFIED"`)

* `NOT_INSTALLED` (value: `"NOT_INSTALLED"`)

* `INSTALLED` (value: `"INSTALLED"`)

* `ERROR` (value: `"ERROR"`)

* `PENDING` (value: `"PENDING"`)





## Enum: GatekeeperMutationEnum


* `DEPLOYMENT_STATE_UNSPECIFIED` (value: `"DEPLOYMENT_STATE_UNSPECIFIED"`)

* `NOT_INSTALLED` (value: `"NOT_INSTALLED"`)

* `INSTALLED` (value: `"INSTALLED"`)

* `ERROR` (value: `"ERROR"`)

* `PENDING` (value: `"PENDING"`)




