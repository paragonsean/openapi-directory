# CloudSqlAdminApi.DemoteMasterContext

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **String** | This is always &#x60;sql#demoteMasterContext&#x60;. | [optional] 
**masterInstanceName** | **String** | The name of the instance which will act as on-premises primary instance in the replication setup. | [optional] 
**replicaConfiguration** | [**DemoteMasterConfiguration**](DemoteMasterConfiguration.md) |  | [optional] 
**skipReplicationSetup** | **Boolean** | Flag to skip replication setup on the instance. | [optional] 
**verifyGtidConsistency** | **Boolean** | Verify the GTID consistency for demote operation. Default value: &#x60;True&#x60;. Setting this flag to &#x60;false&#x60; enables you to bypass the GTID consistency check between on-premises primary instance and Cloud SQL instance during the demotion operation but also exposes you to the risk of future replication failures. Change the value only if you know the reason for the GTID divergence and are confident that doing so will not cause any replication issues. | [optional] 


