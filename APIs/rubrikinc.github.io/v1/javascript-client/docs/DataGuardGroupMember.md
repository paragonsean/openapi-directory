# RubrikRestApi.DataGuardGroupMember

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dbUniqueName** | **String** | Unique name of the member Oracle database. | 
**racId** | **String** | Rubrik ID of the RAC on which this database is hosted. This field is empty when the database is not hosted on a RAC environment. | [optional] 
**racName** | **String** | Cluster name assigned to the Oracle RAC. | [optional] 
**role** | **String** | Current role of the member Oracle database. | 
**standaloneHostId** | **String** | Rubrik ID of the standalone Oracle host on which this database is hosted. This field is empty when the database is not hosted on a standalone system. | [optional] 
**standaloneHostName** | **String** | Name of the standalone Oracle database host. | [optional] 


