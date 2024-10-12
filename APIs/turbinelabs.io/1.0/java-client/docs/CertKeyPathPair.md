

# CertKeyPathPair

A key/cert pair that will be served when a domain terminates a SSL/TLS request.  Paths should be absolute and accessible to the user running the proxy instance. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificatePath** | **String** | Path to a certificate in the PEM format for the domain. If multiple certificates need to be specified then should be contained in this file in the following order: first the primary certificate followed by any intermediary certificats.  |  |
|**keyPath** | **String** | Path to a file with the secret key in the PEM format for the domain.  |  |



