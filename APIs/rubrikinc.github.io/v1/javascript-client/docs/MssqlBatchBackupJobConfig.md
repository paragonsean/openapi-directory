# RubrikRestApi.MssqlBatchBackupJobConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slaId** | **String** |  | [optional] 
**availabilityGroupIds** | **[String]** | IDs of the Microsoft SQL availability groups. All databases with a &#x60;rootId&#x60; belonging to this list are considered for taking an on demand snapshot. | [optional] 
**databaseIds** | **[String]** | IDs of the Microsoft SQL databases. All databases in this list are considered for taking an on demand snapshot. | [optional] 
**forceFullSnapshot** | **Boolean** | Determines whether to force a full or incremental snapshot. | [optional] 
**hostIds** | **[String]** | IDs of the hosts. All databases with a &#x60;rootId&#x60; belonging to this list are considered for taking an on demand snapshot. | [optional] 
**instanceIds** | **[String]** | IDs of the Microsoft SQL instances. All non-availability databases on these instances are considered for taking an on demand snapshot. | [optional] 
**windowsClusterIds** | **[String]** | IDs of the Windows clusters. All databases with a &#x60;rootId&#x60; belonging to this list are considered for taking an on demand snapshot. | [optional] 


