# KustoManagementClient.AttachedDatabaseConfigurationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachedDatabaseNames** | **[String]** | The list of databases from the clusterResourceId which are currently attached to the cluster. | [optional] [readonly] 
**clusterResourceId** | **String** | The resource id of the cluster where the databases you would like to attach reside. | 
**databaseName** | **String** | The name of the database which you would like to attach, use * if you want to follow all current and future databases. | 
**defaultPrincipalsModificationKind** | **String** | The default principals modification kind | 
**provisioningState** | **String** | The provisioned state of the resource. | [optional] [readonly] 



## Enum: DefaultPrincipalsModificationKindEnum


* `Union` (value: `"Union"`)

* `Replace` (value: `"Replace"`)

* `None` (value: `"None"`)





## Enum: ProvisioningStateEnum


* `Running` (value: `"Running"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Moving` (value: `"Moving"`)




