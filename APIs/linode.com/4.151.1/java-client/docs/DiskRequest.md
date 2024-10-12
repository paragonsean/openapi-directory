

# DiskRequest

Disk object request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizedKeys** | **List&lt;String&gt;** | A list of public SSH keys that will be automatically appended to the root user&#39;s &#x60;~/.ssh/authorized_keys&#x60; file when deploying from an Image.  |  [optional] |
|**authorizedUsers** | **List&lt;String&gt;** | A list of usernames. If the usernames have associated SSH keys, the keys will be appended to the root users &#x60;~/.ssh/authorized_keys&#x60; file automatically when deploying from an Image.  |  [optional] |
|**filesystem** | [**FilesystemEnum**](#FilesystemEnum) | The Disk filesystem can be one of:    * raw - No filesystem, just a raw binary stream.   * swap - Linux swap area.   * ext3 - The ext3 journaling filesystem for Linux.   * ext4 - The ext4 journaling filesystem for Linux.   * initrd - initrd (uncompressed initrd, ext2, max 32 MB).  |  [optional] |
|**image** | **String** | An Image ID to deploy the Linode Disk from.  Access the Images List ([GET /images](/docs/api/images/#images-list)) endpoint with authentication to view all available Images. Official Linode Images start with &#x60;linode/&#x60;, while your Account&#39;s Images start with &#x60;private/&#x60;. Creating a disk from a Private Image requires &#x60;read_only&#x60; or &#x60;read_write&#x60; permissions for that Image. Access the User&#39;s Grant Update ([PUT /account/users/{username}/grants](/docs/api/account/#users-grants-update)) endpoint to adjust permissions for an Account Image.  |  [optional] |
|**label** | **String** | The Disk&#39;s label is for display purposes only.  |  [optional] |
|**rootPass** | **String** | This sets the root user&#39;s password on a newly-created Linode Disk when deploying from an Image.  * **Required** when creating a Linode Disk from an Image, including when using a StackScript.  * Must meet a password strength score requirement that is calculated internally by the API. If the strength requirement is not met, you will receive a &#x60;Password does not meet strength requirement&#x60; error.  |  [optional] |
|**size** | **Integer** | The size of the Disk in MB.  Images require a minimum size. Access the Image View ([GET /images/{imageID}](/docs/api/images/#image-view)) endpoint to view its size.  |  [optional] |
|**stackscriptData** | **Object** | This field is required only if the StackScript being deployed requires input data from the User for successful completion. See [User Defined Fields (UDFs)](/docs/guides/writing-scripts-for-use-with-linode-stackscripts-a-tutorial/#user-defined-fields-udfs) for more details.  This field is required to be valid JSON.  Total length cannot exceed 65,535 characters.  |  [optional] |
|**stackscriptId** | **Integer** | A StackScript ID that will cause the referenced StackScript to be run during deployment of this Linode. A compatible &#x60;image&#x60; is required to use a StackScript. To get a list of available StackScript and their permitted Images see [/stackscripts](/docs/api/stackscripts/#stackscripts-list). This field cannot be used when deploying from a Backup or a Private Image.  |  [optional] |



## Enum: FilesystemEnum

| Name | Value |
|---- | -----|
| RAW | &quot;raw&quot; |
| SWAP | &quot;swap&quot; |
| EXT3 | &quot;ext3&quot; |
| EXT4 | &quot;ext4&quot; |
| INITRD | &quot;initrd&quot; |



