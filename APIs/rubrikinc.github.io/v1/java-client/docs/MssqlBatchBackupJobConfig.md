

# MssqlBatchBackupJobConfig


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**slaId** | **String** |  |  [optional] |
|**availabilityGroupIds** | **List&lt;String&gt;** | IDs of the Microsoft SQL availability groups. All databases with a &#x60;rootId&#x60; belonging to this list are considered for taking an on demand snapshot. |  [optional] |
|**databaseIds** | **List&lt;String&gt;** | IDs of the Microsoft SQL databases. All databases in this list are considered for taking an on demand snapshot. |  [optional] |
|**forceFullSnapshot** | **Boolean** | Determines whether to force a full or incremental snapshot. |  [optional] |
|**hostIds** | **List&lt;String&gt;** | IDs of the hosts. All databases with a &#x60;rootId&#x60; belonging to this list are considered for taking an on demand snapshot. |  [optional] |
|**instanceIds** | **List&lt;String&gt;** | IDs of the Microsoft SQL instances. All non-availability databases on these instances are considered for taking an on demand snapshot. |  [optional] |
|**windowsClusterIds** | **List&lt;String&gt;** | IDs of the Windows clusters. All databases with a &#x60;rootId&#x60; belonging to this list are considered for taking an on demand snapshot. |  [optional] |



