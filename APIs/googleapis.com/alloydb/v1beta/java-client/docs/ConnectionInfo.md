

# ConnectionInfo

ConnectionInfo singleton resource. https://google.aip.dev/156

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**instanceUid** | **String** | Output only. The unique ID of the Instance. |  [optional] [readonly] |
|**ipAddress** | **String** | Output only. The private network IP address for the Instance. This is the default IP for the instance and is always created (even if enable_public_ip is set). This is the connection endpoint for an end-user application. |  [optional] [readonly] |
|**name** | **String** | The name of the ConnectionInfo singleton resource, e.g.: projects/{project}/locations/{location}/clusters/_*_/instances/_*_/connectionInfo This field currently has no semantic meaning. |  [optional] |
|**pemCertificateChain** | **List&lt;String&gt;** | Output only. The pem-encoded chain that may be used to verify the X.509 certificate. Expected to be in issuer-to-root order according to RFC 5246. |  [optional] [readonly] |
|**pscDnsName** | **String** | Output only. The DNS name to use with PSC for the Instance. |  [optional] [readonly] |
|**publicIpAddress** | **String** | Output only. The public IP addresses for the Instance. This is available ONLY when enable_public_ip is set. This is the connection endpoint for an end-user application. |  [optional] [readonly] |



