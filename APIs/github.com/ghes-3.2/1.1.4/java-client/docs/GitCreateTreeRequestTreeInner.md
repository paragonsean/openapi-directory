

# GitCreateTreeRequestTreeInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | **String** | The content you want this file to have. GitHub will write this blob out and use that SHA for this entry. Use either this, or &#x60;tree.sha&#x60;.      **Note:** Use either &#x60;tree.sha&#x60; or &#x60;content&#x60; to specify the contents of the entry. Using both &#x60;tree.sha&#x60; and &#x60;content&#x60; will return an error. |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | The file mode; one of &#x60;100644&#x60; for file (blob), &#x60;100755&#x60; for executable (blob), &#x60;040000&#x60; for subdirectory (tree), &#x60;160000&#x60; for submodule (commit), or &#x60;120000&#x60; for a blob that specifies the path of a symlink. |  [optional] |
|**path** | **String** | The file referenced in the tree. |  [optional] |
|**sha** | **String** | The SHA1 checksum ID of the object in the tree. Also called &#x60;tree.sha&#x60;. If the value is &#x60;null&#x60; then the file will be deleted.      **Note:** Use either &#x60;tree.sha&#x60; or &#x60;content&#x60; to specify the contents of the entry. Using both &#x60;tree.sha&#x60; and &#x60;content&#x60; will return an error. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Either &#x60;blob&#x60;, &#x60;tree&#x60;, or &#x60;commit&#x60;. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| _100644 | &quot;100644&quot; |
| _100755 | &quot;100755&quot; |
| _040000 | &quot;040000&quot; |
| _160000 | &quot;160000&quot; |
| _120000 | &quot;120000&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BLOB | &quot;blob&quot; |
| TREE | &quot;tree&quot; |
| COMMIT | &quot;commit&quot; |



