

# OSPolicyResourceFileResource

A resource that manages the state of a file.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | **String** | A a file with this content. The size of the content is limited to 32KiB. |  [optional] |
|**_file** | [**OSPolicyResourceFile**](OSPolicyResourceFile.md) |  |  [optional] |
|**path** | **String** | Required. The absolute path of the file within the VM. |  [optional] |
|**permissions** | **String** | Consists of three octal digits which represent, in order, the permissions of the owner, group, and other users for the file (similarly to the numeric mode used in the linux chmod utility). Each digit represents a three bit number with the 4 bit corresponding to the read permissions, the 2 bit corresponds to the write bit, and the one bit corresponds to the execute permission. Default behavior is 755. Below are some examples of permissions and their associated values: read, write, and execute: 7 read and execute: 5 read and write: 6 read only: 4 |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Required. Desired state of the file. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| DESIRED_STATE_UNSPECIFIED | &quot;DESIRED_STATE_UNSPECIFIED&quot; |
| PRESENT | &quot;PRESENT&quot; |
| ABSENT | &quot;ABSENT&quot; |
| CONTENTS_MATCH | &quot;CONTENTS_MATCH&quot; |



