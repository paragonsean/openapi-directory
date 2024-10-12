# AzureMediaServices.ContentKeyPolicyFairPlayConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ask** | **Blob** | The key that must be used as FairPlay ASk. | 
**fairPlayPfx** | **String** | The Base64 representation of FairPlay certificate in PKCS 12 (pfx) format (including private key). | 
**fairPlayPfxPassword** | **String** | The password encrypting FairPlay certificate in PKCS 12 (pfx) format. | 
**rentalAndLeaseKeyType** | **String** | The rental and lease key type. | 
**rentalDuration** | **Number** | The rental duration. Must be greater than or equal to 0. | 



## Enum: RentalAndLeaseKeyTypeEnum


* `Unknown` (value: `"Unknown"`)

* `Undefined` (value: `"Undefined"`)

* `PersistentUnlimited` (value: `"PersistentUnlimited"`)

* `PersistentLimited` (value: `"PersistentLimited"`)




