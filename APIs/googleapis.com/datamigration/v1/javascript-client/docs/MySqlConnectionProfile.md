# DatabaseMigrationApi.MySqlConnectionProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloudSqlId** | **String** | If the source is a Cloud SQL database, use this field to provide the Cloud SQL instance ID of the source. | [optional] 
**host** | **String** | Required. The IP or hostname of the source MySQL database. | [optional] 
**password** | **String** | Required. Input only. The password for the user that Database Migration Service will be using to connect to the database. This field is not returned on request, and the value is encrypted when stored in Database Migration Service. | [optional] 
**passwordSet** | **Boolean** | Output only. Indicates If this connection profile password is stored. | [optional] [readonly] 
**port** | **Number** | Required. The network port of the source MySQL database. | [optional] 
**ssl** | [**SslConfig**](SslConfig.md) |  | [optional] 
**username** | **String** | Required. The username that Database Migration Service will use to connect to the database. The value is encrypted when stored in Database Migration Service. | [optional] 


