

# OracleConnectionProfile

Specifies connection parameters required specifically for Oracle databases.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**databaseService** | **String** | Required. Database service for the Oracle connection. |  [optional] |
|**forwardSshConnectivity** | [**ForwardSshTunnelConnectivity**](ForwardSshTunnelConnectivity.md) |  |  [optional] |
|**host** | **String** | Required. The IP or hostname of the source Oracle database. |  [optional] |
|**password** | **String** | Required. Input only. The password for the user that Database Migration Service will be using to connect to the database. This field is not returned on request, and the value is encrypted when stored in Database Migration Service. |  [optional] |
|**passwordSet** | **Boolean** | Output only. Indicates whether a new password is included in the request. |  [optional] [readonly] |
|**port** | **Integer** | Required. The network port of the source Oracle database. |  [optional] |
|**privateConnectivity** | [**PrivateConnectivity**](PrivateConnectivity.md) |  |  [optional] |
|**ssl** | [**SslConfig**](SslConfig.md) |  |  [optional] |
|**staticServiceIpConnectivity** | **Object** | Static IP address connectivity configured on service project. |  [optional] |
|**username** | **String** | Required. The username that Database Migration Service will use to connect to the database. The value is encrypted when stored in Database Migration Service. |  [optional] |



