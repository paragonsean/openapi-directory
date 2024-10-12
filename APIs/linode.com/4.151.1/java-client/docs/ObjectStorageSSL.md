

# ObjectStorageSSL

Upload a TLS/SSL certificate and private key to be served when you visit your Object Storage bucket via HTTPS. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificate** | **String** | Your Base64 encoded and PEM formatted SSL certificate.  Line breaks must be represented as \&quot;\\n\&quot; in the string for requests (but not when using the Linode CLI)  |  |
|**privateKey** | **String** | The private key associated with this TLS/SSL certificate.  Line breaks must be represented as \&quot;\\n\&quot; in the string for requests (but not when using the Linode CLI)  |  |



