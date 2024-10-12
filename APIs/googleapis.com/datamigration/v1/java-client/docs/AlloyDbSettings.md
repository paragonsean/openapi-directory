

# AlloyDbSettings

Settings for creating an AlloyDB cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**databaseVersion** | [**DatabaseVersionEnum**](#DatabaseVersionEnum) | Optional. The database engine major version. This is an optional field. If a database version is not supplied at cluster creation time, then a default database version will be used. |  [optional] |
|**encryptionConfig** | [**EncryptionConfig**](EncryptionConfig.md) |  |  [optional] |
|**initialUser** | [**UserPassword**](UserPassword.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels for the AlloyDB cluster created by DMS. An object containing a list of &#39;key&#39;, &#39;value&#39; pairs. |  [optional] |
|**primaryInstanceSettings** | [**PrimaryInstanceSettings**](PrimaryInstanceSettings.md) |  |  [optional] |
|**vpcNetwork** | **String** | Required. The resource link for the VPC network in which cluster resources are created and from which they are accessible via Private IP. The network must belong to the same project as the cluster. It is specified in the form: \&quot;projects/{project_number}/global/networks/{network_id}\&quot;. This is required to create a cluster. |  [optional] |



## Enum: DatabaseVersionEnum

| Name | Value |
|---- | -----|
| DATABASE_VERSION_UNSPECIFIED | &quot;DATABASE_VERSION_UNSPECIFIED&quot; |
| POSTGRES_14 | &quot;POSTGRES_14&quot; |
| POSTGRES_15 | &quot;POSTGRES_15&quot; |



