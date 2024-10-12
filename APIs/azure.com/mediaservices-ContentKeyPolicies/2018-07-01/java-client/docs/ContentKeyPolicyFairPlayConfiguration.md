

# ContentKeyPolicyFairPlayConfiguration

Specifies a configuration for FairPlay licenses.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ask** | **byte[]** | The key that must be used as FairPlay Application Secret key. |  |
|**fairPlayPfx** | **String** | The Base64 representation of FairPlay certificate in PKCS 12 (pfx) format (including private key). |  |
|**fairPlayPfxPassword** | **String** | The password encrypting FairPlay certificate in PKCS 12 (pfx) format. |  |
|**rentalAndLeaseKeyType** | [**RentalAndLeaseKeyTypeEnum**](#RentalAndLeaseKeyTypeEnum) | The rental and lease key type. |  |
|**rentalDuration** | **Long** | The rental duration. Must be greater than or equal to 0. |  |



## Enum: RentalAndLeaseKeyTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| UNDEFINED | &quot;Undefined&quot; |
| PERSISTENT_UNLIMITED | &quot;PersistentUnlimited&quot; |
| PERSISTENT_LIMITED | &quot;PersistentLimited&quot; |



