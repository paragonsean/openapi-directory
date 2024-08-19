

# SslConfig

SSL configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caSource** | [**CaSourceEnum**](#CaSourceEnum) | Optional. Certificate Authority (CA) source. Only CA_SOURCE_MANAGED is supported currently, and is the default value. |  [optional] |
|**sslMode** | [**SslModeEnum**](#SslModeEnum) | Optional. SSL mode. Specifies client-server SSL/TLS connection behavior. |  [optional] |



## Enum: CaSourceEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;CA_SOURCE_UNSPECIFIED&quot; |
| MANAGED | &quot;CA_SOURCE_MANAGED&quot; |



## Enum: SslModeEnum

| Name | Value |
|---- | -----|
| SSL_MODE_UNSPECIFIED | &quot;SSL_MODE_UNSPECIFIED&quot; |
| SSL_MODE_ALLOW | &quot;SSL_MODE_ALLOW&quot; |
| SSL_MODE_REQUIRE | &quot;SSL_MODE_REQUIRE&quot; |
| SSL_MODE_VERIFY_CA | &quot;SSL_MODE_VERIFY_CA&quot; |
| ALLOW_UNENCRYPTED_AND_ENCRYPTED | &quot;ALLOW_UNENCRYPTED_AND_ENCRYPTED&quot; |
| ENCRYPTED_ONLY | &quot;ENCRYPTED_ONLY&quot; |



