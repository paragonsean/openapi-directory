# RubrikRestApi.OracleRacSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuredSlaDomainId** | **String** | The ID of the SLA Domain configured directly on the Rubrik object. | 
**configuredSlaDomainName** | **String** | The name of the SLA Domain configured directly on the Rubrik object. | 
**configuredSlaDomainType** | [**ConfiguredSlaType**](ConfiguredSlaType.md) |  | [optional] 
**id** | **String** | ID assigned to the Oracle RAC. | 
**isConfiguredSlaDomainRetentionLocked** | **Boolean** | Indicates whether the configured SLA Domain is Retention Locked. When this value is &#39;true&#39;, the configured SLA Domain is a Retention Lock SLA Domain. | [optional] 
**name** | **String** | Cluster name assigned to the Oracle RAC. | 
**primaryClusterId** | **String** |  | 
**slaLastUpdateTime** | **Date** | The UTC time when the SLA Domain was last updated. | [optional] 
**nodeOrder** | [**[OracleNodeOrder]**](OracleNodeOrder.md) | Specifies an order for the RAC nodes. Automated Oracle backups use the RAC nodes in the specified order. | 
**nodes** | [**[OracleNodeProperties]**](OracleNodeProperties.md) | Details of the nodes of this Oracle RAC. | 
**numDbs** | **Number** | Count of the number of databases on the Oracle RAC. | 
**numNodes** | **Number** | Count of the number of nodes on the Oracle RAC. | 
**status** | **String** | Connectivity status of the Oracle RAC. | 


