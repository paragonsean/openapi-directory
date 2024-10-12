

# DevicePolicy

`DevicePolicy` specifies device specific restrictions necessary to acquire a given access level. A `DevicePolicy` specifies requirements for requests from devices to be granted access levels, it does not do any enforcement on the device. `DevicePolicy` acts as an AND over all specified fields, and each repeated field is an OR over its elements. Any unset fields are ignored. For example, if the proto is { os_type : DESKTOP_WINDOWS, os_type : DESKTOP_LINUX, encryption_status: ENCRYPTED}, then the DevicePolicy will be true for requests originating from encrypted Linux desktops and encrypted Windows desktops.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedDeviceManagementLevels** | [**List&lt;AllowedDeviceManagementLevelsEnum&gt;**](#List&lt;AllowedDeviceManagementLevelsEnum&gt;) | Allowed device management levels, an empty list allows all management levels. |  [optional] |
|**allowedEncryptionStatuses** | [**List&lt;AllowedEncryptionStatusesEnum&gt;**](#List&lt;AllowedEncryptionStatusesEnum&gt;) | Allowed encryptions statuses, an empty list allows all statuses. |  [optional] |
|**osConstraints** | [**List&lt;OsConstraint&gt;**](OsConstraint.md) | Allowed OS versions, an empty list allows all types and all versions. |  [optional] |
|**requireAdminApproval** | **Boolean** | Whether the device needs to be approved by the customer admin. |  [optional] |
|**requireCorpOwned** | **Boolean** | Whether the device needs to be corp owned. |  [optional] |
|**requireScreenlock** | **Boolean** | Whether or not screenlock is required for the DevicePolicy to be true. Defaults to &#x60;false&#x60;. |  [optional] |



## Enum: List&lt;AllowedDeviceManagementLevelsEnum&gt;

| Name | Value |
|---- | -----|
| MANAGEMENT_UNSPECIFIED | &quot;MANAGEMENT_UNSPECIFIED&quot; |
| NONE | &quot;NONE&quot; |
| BASIC | &quot;BASIC&quot; |
| COMPLETE | &quot;COMPLETE&quot; |



## Enum: List&lt;AllowedEncryptionStatusesEnum&gt;

| Name | Value |
|---- | -----|
| ENCRYPTION_UNSPECIFIED | &quot;ENCRYPTION_UNSPECIFIED&quot; |
| ENCRYPTION_UNSUPPORTED | &quot;ENCRYPTION_UNSUPPORTED&quot; |
| UNENCRYPTED | &quot;UNENCRYPTED&quot; |
| ENCRYPTED | &quot;ENCRYPTED&quot; |



