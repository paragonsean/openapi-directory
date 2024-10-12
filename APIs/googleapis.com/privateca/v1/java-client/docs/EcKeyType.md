

# EcKeyType

Describes an Elliptic Curve key that may be used in a Certificate issued from a CaPool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**signatureAlgorithm** | [**SignatureAlgorithmEnum**](#SignatureAlgorithmEnum) | Optional. A signature algorithm that must be used. If this is omitted, any EC-based signature algorithm will be allowed. |  [optional] |



## Enum: SignatureAlgorithmEnum

| Name | Value |
|---- | -----|
| EC_SIGNATURE_ALGORITHM_UNSPECIFIED | &quot;EC_SIGNATURE_ALGORITHM_UNSPECIFIED&quot; |
| ECDSA_P256 | &quot;ECDSA_P256&quot; |
| ECDSA_P384 | &quot;ECDSA_P384&quot; |
| EDDSA_25519 | &quot;EDDSA_25519&quot; |



