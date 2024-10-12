# AuthorizedPartnerApiSpecification.UploadFileToLockerId400Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **String** |  | [optional] 
**errorDescription** | **String** |  | [optional] 



## Enum: ErrorEnum


* `path_missing` (value: `"path_missing"`)

* `contenttype_missing` (value: `"contenttype_missing"`)

* `hmac_missing` (value: `"hmac_missing"`)

* `filename_missing` (value: `"filename_missing"`)

* `hmac_mismatch` (value: `"hmac_mismatch"`)

* `invalid_filename` (value: `"invalid_filename"`)

* `invalid_filesize` (value: `"invalid_filesize"`)

* `invalid_filetype` (value: `"invalid_filetype"`)

* `invalid_path` (value: `"invalid_path"`)

* `file_data_missing` (value: `"file_data_missing"`)

* `mimetype_mismatch` (value: `"mimetype_mismatch"`)





## Enum: ErrorDescriptionEnum


* `Path parameter is missing` (value: `"Path parameter is missing"`)

* `Content-Type parameter is missing` (value: `"Content-Type parameter is missing"`)

* `HMAC parameter is missing` (value: `"HMAC parameter is missing"`)

* `Filename is missing in path parameter` (value: `"Filename is missing in path parameter"`)

* `HMAC does not match` (value: `"HMAC does not match"`)

* `Restricted characters are not allowed in file name` (value: `"Restricted characters are not allowed in file name"`)

* `The file size exceeds maximum allowed file size of 10MB` (value: `"The file size exceeds maximum allowed file size of 10MB"`)

* `The file type is not allowed` (value: `"The file type is not allowed"`)

* `The destination folder does not exist` (value: `"The destination folder does not exist"`)

* `Missing file content in the request` (value: `"Missing file content in the request"`)

* `The mimetype provided in Content-Type parameter does not match with the mimetype of the file` (value: `"The mimetype provided in Content-Type parameter does not match with the mimetype of the file"`)




