# CloudSqlAdminApi.DemoteMasterMySqlReplicaConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caCertificate** | **String** | PEM representation of the trusted CA&#39;s x509 certificate. | [optional] 
**clientCertificate** | **String** | PEM representation of the replica&#39;s x509 certificate. | [optional] 
**clientKey** | **String** | PEM representation of the replica&#39;s private key. The corresponsing public key is encoded in the client&#39;s certificate. The format of the replica&#39;s private key can be either PKCS #1 or PKCS #8. | [optional] 
**kind** | **String** | This is always &#x60;sql#demoteMasterMysqlReplicaConfiguration&#x60;. | [optional] 
**password** | **String** | The password for the replication connection. | [optional] 
**username** | **String** | The username for the replication connection. | [optional] 


