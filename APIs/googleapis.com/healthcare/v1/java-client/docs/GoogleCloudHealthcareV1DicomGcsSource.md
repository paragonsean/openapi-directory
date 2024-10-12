

# GoogleCloudHealthcareV1DicomGcsSource

Specifies the configuration for importing data from Cloud Storage.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**uri** | **String** | Points to a Cloud Storage URI containing file(s) with content only. The URI must be in the following format: &#x60;gs://{bucket_id}/{object_id}&#x60;. The URI can include wildcards in &#x60;object_id&#x60; and thus identify multiple files. Supported wildcards: * &#39;*&#39; to match 0 or more non-separator characters * &#39;**&#39; to match 0 or more characters (including separators). Must be used at the end of a path and with no other wildcards in the path. Can also be used with a file extension (such as .dcm), which imports all files with the extension in the specified directory and its sub-directories. For example, &#x60;gs://my-bucket/my-directory/_**.dcm&#x60; imports all files with .dcm extensions in &#x60;my-directory/&#x60; and its sub-directories. * &#39;?&#39; to match 1 character. All other URI formats are invalid. Files matching the wildcard are expected to contain content only, no metadata. |  [optional] |



