

# CryptoHashConfig

Pseudonymization method that generates surrogates via cryptographic hashing. Uses SHA-256. Outputs a base64-encoded representation of the hashed output. For example, `L7k0BHmF1ha5U3NfGykjro4xWi1MPVQPjhMAZbSV9mM=`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cryptoKey** | **byte[]** | An AES 128/192/256 bit key. Causes the hash to be computed based on this key. A default key is generated for each Deidentify operation and is used when neither crypto_key nor kms_wrapped is specified. Must not be set if kms_wrapped is set. |  [optional] |
|**kmsWrapped** | [**KmsWrappedCryptoKey**](KmsWrappedCryptoKey.md) |  |  [optional] |



