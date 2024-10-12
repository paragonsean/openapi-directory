# OsConfigApi.OSPolicyResourceFileResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **String** | A a file with this content. The size of the content is limited to 32KiB. | [optional] 
**file** | [**OSPolicyResourceFile**](OSPolicyResourceFile.md) |  | [optional] 
**path** | **String** | Required. The absolute path of the file within the VM. | [optional] 
**permissions** | **String** | Consists of three octal digits which represent, in order, the permissions of the owner, group, and other users for the file (similarly to the numeric mode used in the linux chmod utility). Each digit represents a three bit number with the 4 bit corresponding to the read permissions, the 2 bit corresponds to the write bit, and the one bit corresponds to the execute permission. Default behavior is 755. Below are some examples of permissions and their associated values: read, write, and execute: 7 read and execute: 5 read and write: 6 read only: 4 | [optional] 
**state** | **String** | Required. Desired state of the file. | [optional] 



## Enum: StateEnum


* `DESIRED_STATE_UNSPECIFIED` (value: `"DESIRED_STATE_UNSPECIFIED"`)

* `PRESENT` (value: `"PRESENT"`)

* `ABSENT` (value: `"ABSENT"`)

* `CONTENTS_MATCH` (value: `"CONTENTS_MATCH"`)




