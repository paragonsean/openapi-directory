# AlloyDbApi.SslConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caSource** | **String** | Optional. Certificate Authority (CA) source. Only CA_SOURCE_MANAGED is supported currently, and is the default value. | [optional] 
**sslMode** | **String** | Optional. SSL mode. Specifies client-server SSL/TLS connection behavior. | [optional] 



## Enum: CaSourceEnum


* `UNSPECIFIED` (value: `"CA_SOURCE_UNSPECIFIED"`)

* `MANAGED` (value: `"CA_SOURCE_MANAGED"`)





## Enum: SslModeEnum


* `SSL_MODE_UNSPECIFIED` (value: `"SSL_MODE_UNSPECIFIED"`)

* `SSL_MODE_ALLOW` (value: `"SSL_MODE_ALLOW"`)

* `SSL_MODE_REQUIRE` (value: `"SSL_MODE_REQUIRE"`)

* `SSL_MODE_VERIFY_CA` (value: `"SSL_MODE_VERIFY_CA"`)

* `ALLOW_UNENCRYPTED_AND_ENCRYPTED` (value: `"ALLOW_UNENCRYPTED_AND_ENCRYPTED"`)

* `ENCRYPTED_ONLY` (value: `"ENCRYPTED_ONLY"`)




