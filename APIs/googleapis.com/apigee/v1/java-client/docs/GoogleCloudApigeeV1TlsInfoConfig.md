

# GoogleCloudApigeeV1TlsInfoConfig


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ciphers** | **List&lt;String&gt;** | List of ciphers that are granted access. |  [optional] |
|**clientAuthEnabled** | **Boolean** | Flag that specifies whether client-side authentication is enabled for the target server. Enables two-way TLS. |  [optional] |
|**commonName** | [**GoogleCloudApigeeV1CommonNameConfig**](GoogleCloudApigeeV1CommonNameConfig.md) |  |  [optional] |
|**enabled** | **Boolean** | Flag that specifies whether one-way TLS is enabled. Set to &#x60;true&#x60; to enable one-way TLS. |  [optional] |
|**ignoreValidationErrors** | **Boolean** | Flag that specifies whether to ignore TLS certificate validation errors. Set to &#x60;true&#x60; to ignore errors. |  [optional] |
|**keyAlias** | **String** | Name of the alias used for client-side authentication in the following format: &#x60;organizations/{org}/environments/{env}/keystores/{keystore}/aliases/{alias}&#x60; |  [optional] |
|**keyAliasReference** | [**GoogleCloudApigeeV1KeyAliasReference**](GoogleCloudApigeeV1KeyAliasReference.md) |  |  [optional] |
|**protocols** | **List&lt;String&gt;** | List of TLS protocols that are granted access. |  [optional] |
|**trustStore** | **String** | Name of the keystore or keystore reference containing trusted certificates for the server in the following format: &#x60;organizations/{org}/environments/{env}/keystores/{keystore}&#x60; or &#x60;organizations/{org}/environments/{env}/references/{reference}&#x60; |  [optional] |



