# CloudSqlAdminApi.OnPremisesConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caCertificate** | **String** | PEM representation of the trusted CA&#39;s x509 certificate. | [optional] 
**clientCertificate** | **String** | PEM representation of the replica&#39;s x509 certificate. | [optional] 
**clientKey** | **String** | PEM representation of the replica&#39;s private key. The corresponsing public key is encoded in the client&#39;s certificate. | [optional] 
**dumpFilePath** | **String** | The dump file to create the Cloud SQL replica. | [optional] 
**hostPort** | **String** | The host and port of the on-premises instance in host:port format | [optional] 
**kind** | **String** | This is always &#x60;sql#onPremisesConfiguration&#x60;. | [optional] 
**password** | **String** | The password for connecting to on-premises instance. | [optional] 
**sourceInstance** | [**InstanceReference**](InstanceReference.md) |  | [optional] 
**username** | **String** | The username for connecting to on-premises instance. | [optional] 


