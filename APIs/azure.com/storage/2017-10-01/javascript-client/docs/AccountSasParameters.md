# StorageManagement.AccountSasParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyToSign** | **String** | The key to sign the account SAS token with. | [optional] 
**signedExpiry** | **Date** | The time at which the shared access signature becomes invalid. | 
**signedIp** | **String** | An IP address or a range of IP addresses from which to accept requests. | [optional] 
**signedPermission** | **String** | The signed permissions for the account SAS. Possible values include: Read (r), Write (w), Delete (d), List (l), Add (a), Create (c), Update (u) and Process (p). | 
**signedProtocol** | **String** | The protocol permitted for a request made with the account SAS. | [optional] 
**signedResourceTypes** | **String** | The signed resource types that are accessible with the account SAS. Service (s): Access to service-level APIs; Container (c): Access to container-level APIs; Object (o): Access to object-level APIs for blobs, queue messages, table entities, and files. | 
**signedServices** | **String** | The signed services accessible with the account SAS. Possible values include: Blob (b), Queue (q), Table (t), File (f). | 
**signedStart** | **Date** | The time at which the SAS becomes valid. | [optional] 



## Enum: SignedPermissionEnum


* `r` (value: `"r"`)

* `d` (value: `"d"`)

* `w` (value: `"w"`)

* `l` (value: `"l"`)

* `a` (value: `"a"`)

* `c` (value: `"c"`)

* `u` (value: `"u"`)

* `p` (value: `"p"`)





## Enum: SignedProtocolEnum


* `https,http` (value: `"https,http"`)

* `https` (value: `"https"`)





## Enum: SignedResourceTypesEnum


* `s` (value: `"s"`)

* `c` (value: `"c"`)

* `o` (value: `"o"`)





## Enum: SignedServicesEnum


* `b` (value: `"b"`)

* `q` (value: `"q"`)

* `t` (value: `"t"`)

* `f` (value: `"f"`)




