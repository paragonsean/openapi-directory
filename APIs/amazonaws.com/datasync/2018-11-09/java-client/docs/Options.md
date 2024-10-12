

# Options

<p>Configures your DataSync task settings. These options include how DataSync handles files, objects, and their associated metadata. You also can specify how DataSync verifies data integrity, set bandwidth limits for your task, among other options.</p> <p>Each task setting has a default value. Unless you need to, you don't have to configure any of these <code>Options</code> before starting your task.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**verifyMode** | [**VerifyMode**](VerifyMode.md) |  |  [optional] |
|**overwriteMode** | [**OverwriteMode**](OverwriteMode.md) |  |  [optional] |
|**atime** | [**Atime**](Atime.md) |  |  [optional] |
|**mtime** | [**Mtime**](Mtime.md) |  |  [optional] |
|**uid** | [**Uid**](Uid.md) |  |  [optional] |
|**gid** | [**Gid**](Gid.md) |  |  [optional] |
|**preserveDeletedFiles** | [**PreserveDeletedFiles**](PreserveDeletedFiles.md) |  |  [optional] |
|**preserveDevices** | [**PreserveDevices**](PreserveDevices.md) |  |  [optional] |
|**posixPermissions** | [**PosixPermissions**](PosixPermissions.md) |  |  [optional] |
|**bytesPerSecond** | [**Integer**](Integer.md) |  |  [optional] |
|**taskQueueing** | [**TaskQueueing**](TaskQueueing.md) |  |  [optional] |
|**logLevel** | [**LogLevel**](LogLevel.md) |  |  [optional] |
|**transferMode** | [**TransferMode**](TransferMode.md) |  |  [optional] |
|**securityDescriptorCopyFlags** | [**SmbSecurityDescriptorCopyFlags**](SmbSecurityDescriptorCopyFlags.md) |  |  [optional] |
|**objectTags** | [**ObjectTags**](ObjectTags.md) |  |  [optional] |



