

# EncryptionService

A service that allows server-side encryption to be used.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | A boolean indicating whether or not the service encrypts the data as it is stored. |  [optional] |
|**keyType** | [**KeyTypeEnum**](#KeyTypeEnum) | Encryption key type to be used for the encryption service. &#39;Account&#39; key type implies that an account-scoped encryption key will be used. &#39;Service&#39; key type implies that a default service key is used. |  [optional] |
|**lastEnabledTime** | **OffsetDateTime** | Gets a rough estimate of the date/time when the encryption was last enabled by the user. Only returned when encryption is enabled. There might be some unencrypted blobs which were written after this time, as it is just a rough estimate. |  [optional] [readonly] |



## Enum: KeyTypeEnum

| Name | Value |
|---- | -----|
| SERVICE | &quot;Service&quot; |
| ACCOUNT | &quot;Account&quot; |



