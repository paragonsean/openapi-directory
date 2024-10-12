

# KeyProperties

Properties of the key pair backing a certificate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**crv** | [**CrvEnum**](#CrvEnum) | Elliptic curve name. For valid values, see JsonWebKeyCurveName. |  [optional] |
|**exportable** | **Boolean** | Indicates if the private key can be exported. |  [optional] |
|**keySize** | **Integer** | The key size in bits. For example: 2048, 3072, or 4096 for RSA. |  [optional] |
|**kty** | [**KtyEnum**](#KtyEnum) | The type of key pair to be used for the certificate. |  [optional] |
|**reuseKey** | **Boolean** | Indicates if the same key pair will be used on certificate renewal. |  [optional] |



## Enum: CrvEnum

| Name | Value |
|---- | -----|
| _256 | &quot;P-256&quot; |
| _384 | &quot;P-384&quot; |
| _521 | &quot;P-521&quot; |
| _256_K | &quot;P-256K&quot; |



## Enum: KtyEnum

| Name | Value |
|---- | -----|
| EC | &quot;EC&quot; |
| EC_HSM | &quot;EC-HSM&quot; |
| RSA | &quot;RSA&quot; |
| RSA_HSM | &quot;RSA-HSM&quot; |
| OCT | &quot;oct&quot; |



