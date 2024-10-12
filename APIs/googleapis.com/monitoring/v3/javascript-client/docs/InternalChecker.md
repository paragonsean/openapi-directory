# CloudMonitoringApi.InternalChecker

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | The checker&#39;s human-readable name. The display name should be unique within a Cloud Monitoring Metrics Scope in order to make it easier to identify; however, uniqueness is not enforced. | [optional] 
**gcpZone** | **String** | The GCP zone the Uptime check should egress from. Only respected for internal Uptime checks, where internal_network is specified. | [optional] 
**name** | **String** | A unique resource name for this InternalChecker. The format is: projects/[PROJECT_ID_OR_NUMBER]/internalCheckers/[INTERNAL_CHECKER_ID] [PROJECT_ID_OR_NUMBER] is the Cloud Monitoring Metrics Scope project for the Uptime check config associated with the internal checker. | [optional] 
**network** | **String** | The GCP VPC network (https://cloud.google.com/vpc/docs/vpc) where the internal resource lives (ex: \&quot;default\&quot;). | [optional] 
**peerProjectId** | **String** | The GCP project ID where the internal checker lives. Not necessary the same as the Metrics Scope project. | [optional] 
**state** | **String** | The current operational state of the internal checker. | [optional] 



## Enum: StateEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `RUNNING` (value: `"RUNNING"`)




