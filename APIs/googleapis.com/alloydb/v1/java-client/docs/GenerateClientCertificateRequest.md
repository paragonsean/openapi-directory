

# GenerateClientCertificateRequest

Message for requests to generate a client certificate signed by the Cluster CA.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certDuration** | **String** | Optional. An optional hint to the endpoint to generate the client certificate with the requested duration. The duration can be from 1 hour to 24 hours. The endpoint may or may not honor the hint. If the hint is left unspecified or is not honored, then the endpoint will pick an appropriate default duration. |  [optional] |
|**publicKey** | **String** | Optional. The public key from the client. |  [optional] |
|**requestId** | **String** | Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). |  [optional] |
|**useMetadataExchange** | **Boolean** | Optional. An optional hint to the endpoint to generate a client ceritificate that can be used by AlloyDB connectors to exchange additional metadata with the server after TLS handshake. |  [optional] |



