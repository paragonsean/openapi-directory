

# AccountSasParameters

The parameters to list SAS credentials of a storage account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keyToSign** | **String** | The key to sign the account SAS token with. |  [optional] |
|**signedExpiry** | **OffsetDateTime** | The time at which the shared access signature becomes invalid. |  |
|**signedIp** | **String** | An IP address or a range of IP addresses from which to accept requests. |  [optional] |
|**signedPermission** | [**SignedPermissionEnum**](#SignedPermissionEnum) | The signed permissions for the account SAS. Possible values include: Read (r), Write (w), Delete (d), List (l), Add (a), Create (c), Update (u) and Process (p). |  |
|**signedProtocol** | [**SignedProtocolEnum**](#SignedProtocolEnum) | The protocol permitted for a request made with the account SAS. |  [optional] |
|**signedResourceTypes** | [**SignedResourceTypesEnum**](#SignedResourceTypesEnum) | The signed resource types that are accessible with the account SAS. Service (s): Access to service-level APIs; Container (c): Access to container-level APIs; Object (o): Access to object-level APIs for blobs, queue messages, table entities, and files. |  |
|**signedServices** | [**SignedServicesEnum**](#SignedServicesEnum) | The signed services accessible with the account SAS. Possible values include: Blob (b), Queue (q), Table (t), File (f). |  |
|**signedStart** | **OffsetDateTime** | The time at which the SAS becomes valid. |  [optional] |



## Enum: SignedPermissionEnum

| Name | Value |
|---- | -----|
| R | &quot;r&quot; |
| D | &quot;d&quot; |
| W | &quot;w&quot; |
| L | &quot;l&quot; |
| A | &quot;a&quot; |
| C | &quot;c&quot; |
| U | &quot;u&quot; |
| P | &quot;p&quot; |



## Enum: SignedProtocolEnum

| Name | Value |
|---- | -----|
| HTTPS_HTTP | &quot;https,http&quot; |
| HTTPS | &quot;https&quot; |



## Enum: SignedResourceTypesEnum

| Name | Value |
|---- | -----|
| S | &quot;s&quot; |
| C | &quot;c&quot; |
| O | &quot;o&quot; |



## Enum: SignedServicesEnum

| Name | Value |
|---- | -----|
| B | &quot;b&quot; |
| Q | &quot;q&quot; |
| T | &quot;t&quot; |
| F | &quot;f&quot; |



