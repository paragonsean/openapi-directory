# CloudRunAdminApi.ConfigMapVolumeSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultMode** | **Number** | (Optional) Integer representation of mode bits to use on created files by default. Must be a value between 01 and 0777 (octal). If 0 or not set, it will default to 0644. Directories within the path are not affected by this setting. Notes * Internally, a umask of 0222 will be applied to any non-zero value. * This is an integer representation of the mode bits. So, the octal integer value should look exactly as the chmod numeric notation with a leading zero. Some examples: for chmod 777 (a&#x3D;rwx), set to 0777 (octal) or 511 (base-10). For chmod 640 (u&#x3D;rw,g&#x3D;r), set to 0640 (octal) or 416 (base-10). For chmod 755 (u&#x3D;rwx,g&#x3D;rx,o&#x3D;rx), set to 0755 (octal) or 493 (base-10). * This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. | [optional] 
**items** | [**[KeyToPath]**](KeyToPath.md) | (Optional) If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified that is not present in the Secret, the volume setup will error unless it is marked optional. | [optional] 
**name** | **String** | Name of the config. | [optional] 
**optional** | **Boolean** | (Optional) Specify whether the Secret or its keys must be defined. | [optional] 


