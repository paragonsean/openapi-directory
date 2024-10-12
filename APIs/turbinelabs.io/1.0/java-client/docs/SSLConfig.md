

# SSLConfig

Experimental: Specifies whether a domain should support SSL/TLS connections from clients.  If not set the proxy will expect unencrypted HTTP traffic. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certKeyPairs** | [**List&lt;CertKeyPathPair&gt;**](CertKeyPathPair.md) | SSLConfig must have one cert_key_pairs entry specified. |  |
|**cipherFilter** | **String** | An OpenSSL compatible filter string indicating the ciphers acceptable for this proxy to use while communicating with clients. The default value is EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH. For more information see https://wiki.openssl.org/index.php/Manual:Ciphers(1)  |  [optional] |
|**protocols** | **List&lt;String&gt;** | A list of acceptable SSL/TLS protocol. The default values are TLSv1, TLSv1.1, TLSv1.2. Additional valid values are SSLv2 and SSLv3.  |  [optional] |



