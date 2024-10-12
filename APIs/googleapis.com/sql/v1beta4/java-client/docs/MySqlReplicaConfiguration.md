

# MySqlReplicaConfiguration

Read-replica configuration specific to MySQL databases.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caCertificate** | **String** | PEM representation of the trusted CA&#39;s x509 certificate. |  [optional] |
|**clientCertificate** | **String** | PEM representation of the replica&#39;s x509 certificate. |  [optional] |
|**clientKey** | **String** | PEM representation of the replica&#39;s private key. The corresponsing public key is encoded in the client&#39;s certificate. |  [optional] |
|**connectRetryInterval** | **Integer** | Seconds to wait between connect retries. MySQL&#39;s default is 60 seconds. |  [optional] |
|**dumpFilePath** | **String** | Path to a SQL dump file in Google Cloud Storage from which the replica instance is to be created. The URI is in the form gs://bucketName/fileName. Compressed gzip files (.gz) are also supported. Dumps have the binlog co-ordinates from which replication begins. This can be accomplished by setting --master-data to 1 when using mysqldump. |  [optional] |
|**kind** | **String** | This is always &#x60;sql#mysqlReplicaConfiguration&#x60;. |  [optional] |
|**masterHeartbeatPeriod** | **String** | Interval in milliseconds between replication heartbeats. |  [optional] |
|**password** | **String** | The password for the replication connection. |  [optional] |
|**sslCipher** | **String** | A list of permissible ciphers to use for SSL encryption. |  [optional] |
|**username** | **String** | The username for the replication connection. |  [optional] |
|**verifyServerCertificate** | **Boolean** | Whether or not to check the primary instance&#39;s Common Name value in the certificate that it sends during the SSL handshake. |  [optional] |



