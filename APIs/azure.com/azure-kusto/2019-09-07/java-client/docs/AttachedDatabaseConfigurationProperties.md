

# AttachedDatabaseConfigurationProperties

Class representing the an attached database configuration properties of kind specific.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachedDatabaseNames** | **List&lt;String&gt;** | The list of databases from the clusterResourceId which are currently attached to the cluster. |  [optional] [readonly] |
|**clusterResourceId** | **String** | The resource id of the cluster where the databases you would like to attach reside. |  |
|**databaseName** | **String** | The name of the database which you would like to attach, use * if you want to follow all current and future databases. |  |
|**defaultPrincipalsModificationKind** | [**DefaultPrincipalsModificationKindEnum**](#DefaultPrincipalsModificationKindEnum) | The default principals modification kind |  |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioned state of the resource. |  [optional] [readonly] |



## Enum: DefaultPrincipalsModificationKindEnum

| Name | Value |
|---- | -----|
| UNION | &quot;Union&quot; |
| REPLACE | &quot;Replace&quot; |
| NONE | &quot;None&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;Running&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| MOVING | &quot;Moving&quot; |



