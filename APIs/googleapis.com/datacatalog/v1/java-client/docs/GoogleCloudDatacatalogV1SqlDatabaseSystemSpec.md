

# GoogleCloudDatacatalogV1SqlDatabaseSystemSpec

Specification that applies to entries that are part `SQL_DATABASE` system (user_specified_type)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**databaseVersion** | **String** | Version of the database engine. |  [optional] |
|**instanceHost** | **String** | Host of the SQL database enum InstanceHost { UNDEFINED &#x3D; 0; SELF_HOSTED &#x3D; 1; CLOUD_SQL &#x3D; 2; AMAZON_RDS &#x3D; 3; AZURE_SQL &#x3D; 4; } Host of the enclousing database instance. |  [optional] |
|**sqlEngine** | **String** | SQL Database Engine. enum SqlEngine { UNDEFINED &#x3D; 0; MY_SQL &#x3D; 1; POSTGRE_SQL &#x3D; 2; SQL_SERVER &#x3D; 3; } Engine of the enclosing database instance. |  [optional] |



