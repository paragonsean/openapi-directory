# DatabaseMigrationApi.PostgreSqlConnectionProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alloydbClusterId** | **String** | Optional. If the destination is an AlloyDB database, use this field to provide the AlloyDB cluster ID. | [optional] 
**cloudSqlId** | **String** | If the source is a Cloud SQL database, use this field to provide the Cloud SQL instance ID of the source. | [optional] 
**host** | **String** | Required. The IP or hostname of the source PostgreSQL database. | [optional] 
**networkArchitecture** | **String** | Output only. If the source is a Cloud SQL database, this field indicates the network architecture it&#39;s associated with. | [optional] [readonly] 
**password** | **String** | Required. Input only. The password for the user that Database Migration Service will be using to connect to the database. This field is not returned on request, and the value is encrypted when stored in Database Migration Service. | [optional] 
**passwordSet** | **Boolean** | Output only. Indicates If this connection profile password is stored. | [optional] [readonly] 
**port** | **Number** | Required. The network port of the source PostgreSQL database. | [optional] 
**privateServiceConnectConnectivity** | [**PrivateServiceConnectConnectivity**](PrivateServiceConnectConnectivity.md) |  | [optional] 
**ssl** | [**SslConfig**](SslConfig.md) |  | [optional] 
**staticIpConnectivity** | **Object** | The source database will allow incoming connections from the public IP of the destination database. You can retrieve the public IP of the Cloud SQL instance from the Cloud SQL console or using Cloud SQL APIs. No additional configuration is required. | [optional] 
**username** | **String** | Required. The username that Database Migration Service will use to connect to the database. The value is encrypted when stored in Database Migration Service. | [optional] 



## Enum: NetworkArchitectureEnum


* `UNSPECIFIED` (value: `"NETWORK_ARCHITECTURE_UNSPECIFIED"`)

* `OLD_CSQL_PRODUCER` (value: `"NETWORK_ARCHITECTURE_OLD_CSQL_PRODUCER"`)

* `NEW_CSQL_PRODUCER` (value: `"NETWORK_ARCHITECTURE_NEW_CSQL_PRODUCER"`)




