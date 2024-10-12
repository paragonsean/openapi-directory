# SqlManagementClient.FailoverGroupProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**databases** | **[String]** | List of databases in the failover group. | [optional] 
**partnerServers** | [**[PartnerInfo]**](PartnerInfo.md) | List of partner server information for the failover group. | 
**readOnlyEndpoint** | [**FailoverGroupReadOnlyEndpoint**](FailoverGroupReadOnlyEndpoint.md) |  | [optional] 
**readWriteEndpoint** | [**FailoverGroupReadWriteEndpoint**](FailoverGroupReadWriteEndpoint.md) |  | 
**replicationRole** | **String** | Local replication role of the failover group instance. | [optional] [readonly] 
**replicationState** | **String** | Replication state of the failover group instance. | [optional] [readonly] 



## Enum: ReplicationRoleEnum


* `Primary` (value: `"Primary"`)

* `Secondary` (value: `"Secondary"`)




