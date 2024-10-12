

# RDSMetadata

The datasource details that are specific to Amazon RDS.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**database** | [**RDSMetadataDatabase**](RDSMetadataDatabase.md) |  |  [optional] |
|**databaseUserName** | **String** | The username to be used by Amazon ML to connect to database on an Amazon RDS instance. The username should have sufficient permissions to execute an &lt;code&gt;RDSSelectSqlQuery&lt;/code&gt; query. |  [optional] |
|**selectSqlQuery** | [**String**](String.md) |  |  [optional] |
|**resourceRole** | [**String**](String.md) |  |  [optional] |
|**serviceRole** | [**String**](String.md) |  |  [optional] |
|**dataPipelineId** | [**String**](String.md) |  |  [optional] |



