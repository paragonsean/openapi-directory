# BatchService.OutputFileBlobContainerDestination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containerUrl** | **String** | The URL must include a Shared Access Signature (SAS) granting write permissions to the container. | 
**path** | **String** | If filePattern refers to a specific file (i.e. contains no wildcards), then path is the name of the blob to which to upload that file. If filePattern contains one or more wildcards (and therefore may match multiple files), then path is the name of the blob virtual directory (which is prepended to each blob name) to which to upload the file(s). If omitted, file(s) are uploaded to the root of the container with a blob name matching their file name. | [optional] 


