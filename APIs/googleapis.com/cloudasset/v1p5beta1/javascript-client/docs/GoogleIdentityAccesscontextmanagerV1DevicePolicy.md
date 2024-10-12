# CloudAssetApi.GoogleIdentityAccesscontextmanagerV1DevicePolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedDeviceManagementLevels** | **[String]** | Allowed device management levels, an empty list allows all management levels. | [optional] 
**allowedEncryptionStatuses** | **[String]** | Allowed encryptions statuses, an empty list allows all statuses. | [optional] 
**osConstraints** | [**[GoogleIdentityAccesscontextmanagerV1OsConstraint]**](GoogleIdentityAccesscontextmanagerV1OsConstraint.md) | Allowed OS versions, an empty list allows all types and all versions. | [optional] 
**requireAdminApproval** | **Boolean** | Whether the device needs to be approved by the customer admin. | [optional] 
**requireCorpOwned** | **Boolean** | Whether the device needs to be corp owned. | [optional] 
**requireScreenlock** | **Boolean** | Whether or not screenlock is required for the DevicePolicy to be true. Defaults to &#x60;false&#x60;. | [optional] 



## Enum: [AllowedDeviceManagementLevelsEnum]


* `MANAGEMENT_UNSPECIFIED` (value: `"MANAGEMENT_UNSPECIFIED"`)

* `NONE` (value: `"NONE"`)

* `BASIC` (value: `"BASIC"`)

* `COMPLETE` (value: `"COMPLETE"`)





## Enum: [AllowedEncryptionStatusesEnum]


* `ENCRYPTION_UNSPECIFIED` (value: `"ENCRYPTION_UNSPECIFIED"`)

* `ENCRYPTION_UNSUPPORTED` (value: `"ENCRYPTION_UNSUPPORTED"`)

* `UNENCRYPTED` (value: `"UNENCRYPTED"`)

* `ENCRYPTED` (value: `"ENCRYPTED"`)




