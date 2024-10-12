# KubernetesEngineApi.BlueGreenInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blueInstanceGroupUrls** | **[String]** | The resource URLs of the [managed instance groups] (/compute/docs/instance-groups/creating-groups-of-managed-instances) associated with blue pool. | [optional] 
**bluePoolDeletionStartTime** | **String** | Time to start deleting blue pool to complete blue-green upgrade, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format. | [optional] 
**greenInstanceGroupUrls** | **[String]** | The resource URLs of the [managed instance groups] (/compute/docs/instance-groups/creating-groups-of-managed-instances) associated with green pool. | [optional] 
**greenPoolVersion** | **String** | Version of green pool. | [optional] 
**phase** | **String** | Current blue-green upgrade phase. | [optional] 



## Enum: PhaseEnum


* `PHASE_UNSPECIFIED` (value: `"PHASE_UNSPECIFIED"`)

* `UPDATE_STARTED` (value: `"UPDATE_STARTED"`)

* `CREATING_GREEN_POOL` (value: `"CREATING_GREEN_POOL"`)

* `CORDONING_BLUE_POOL` (value: `"CORDONING_BLUE_POOL"`)

* `DRAINING_BLUE_POOL` (value: `"DRAINING_BLUE_POOL"`)

* `NODE_POOL_SOAKING` (value: `"NODE_POOL_SOAKING"`)

* `DELETING_BLUE_POOL` (value: `"DELETING_BLUE_POOL"`)

* `ROLLBACK_STARTED` (value: `"ROLLBACK_STARTED"`)




