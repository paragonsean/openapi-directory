

# UploadFileToLockerId400Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | [**ErrorEnum**](#ErrorEnum) |  |  [optional] |
|**errorDescription** | [**ErrorDescriptionEnum**](#ErrorDescriptionEnum) |  |  [optional] |



## Enum: ErrorEnum

| Name | Value |
|---- | -----|
| PATH_MISSING | &quot;path_missing&quot; |
| CONTENTTYPE_MISSING | &quot;contenttype_missing&quot; |
| HMAC_MISSING | &quot;hmac_missing&quot; |
| FILENAME_MISSING | &quot;filename_missing&quot; |
| HMAC_MISMATCH | &quot;hmac_mismatch&quot; |
| INVALID_FILENAME | &quot;invalid_filename&quot; |
| INVALID_FILESIZE | &quot;invalid_filesize&quot; |
| INVALID_FILETYPE | &quot;invalid_filetype&quot; |
| INVALID_PATH | &quot;invalid_path&quot; |
| FILE_DATA_MISSING | &quot;file_data_missing&quot; |
| MIMETYPE_MISMATCH | &quot;mimetype_mismatch&quot; |



## Enum: ErrorDescriptionEnum

| Name | Value |
|---- | -----|
| PATH_PARAMETER_IS_MISSING | &quot;Path parameter is missing&quot; |
| CONTENT_TYPE_PARAMETER_IS_MISSING | &quot;Content-Type parameter is missing&quot; |
| HMAC_PARAMETER_IS_MISSING | &quot;HMAC parameter is missing&quot; |
| FILENAME_IS_MISSING_IN_PATH_PARAMETER | &quot;Filename is missing in path parameter&quot; |
| HMAC_DOES_NOT_MATCH | &quot;HMAC does not match&quot; |
| RESTRICTED_CHARACTERS_ARE_NOT_ALLOWED_IN_FILE_NAME | &quot;Restricted characters are not allowed in file name&quot; |
| THE_FILE_SIZE_EXCEEDS_MAXIMUM_ALLOWED_FILE_SIZE_OF_10_MB | &quot;The file size exceeds maximum allowed file size of 10MB&quot; |
| THE_FILE_TYPE_IS_NOT_ALLOWED | &quot;The file type is not allowed&quot; |
| THE_DESTINATION_FOLDER_DOES_NOT_EXIST | &quot;The destination folder does not exist&quot; |
| MISSING_FILE_CONTENT_IN_THE_REQUEST | &quot;Missing file content in the request&quot; |
| THE_MIMETYPE_PROVIDED_IN_CONTENT_TYPE_PARAMETER_DOES_NOT_MATCH_WITH_THE_MIMETYPE_OF_THE_FILE | &quot;The mimetype provided in Content-Type parameter does not match with the mimetype of the file&quot; |



