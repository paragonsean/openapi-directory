

# KeySigningKey

A key-signing key (KSK) is a complex type that represents a public/private key pair. The private key is used to generate a digital signature for the zone signing key (ZSK). The public key is stored in the DNS and is used to authenticate the ZSK. A KSK is always associated with a hosted zone; it cannot exist by itself.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  [optional] |
|**kmsArn** | [**String**](String.md) |  |  [optional] |
|**flag** | [**Integer**](Integer.md) |  |  [optional] |
|**signingAlgorithmMnemonic** | [**String**](String.md) |  |  [optional] |
|**signingAlgorithmType** | [**Integer**](Integer.md) |  |  [optional] |
|**digestAlgorithmMnemonic** | [**String**](String.md) |  |  [optional] |
|**digestAlgorithmType** | [**Integer**](Integer.md) |  |  [optional] |
|**keyTag** | [**Integer**](Integer.md) |  |  [optional] |
|**digestValue** | [**String**](String.md) |  |  [optional] |
|**publicKey** | [**String**](String.md) |  |  [optional] |
|**dsRecord** | [**String**](String.md) |  |  [optional] |
|**dnSKEYRecord** | [**String**](String.md) |  |  [optional] |
|**status** | [**String**](String.md) |  |  [optional] |
|**statusMessage** | [**String**](String.md) |  |  [optional] |
|**createdDate** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastModifiedDate** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



