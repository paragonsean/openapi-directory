

# DiffUploadResponse

Backend response for a Diff upload request. For details on the Scotty Diff protocol, visit http://go/scotty-diff-protocol.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**objectVersion** | **String** | The object version of the object at the server. Must be included in the end notification response. The version in the end notification response must correspond to the new version of the object that is now stored at the server, after the upload. |  [optional] |
|**originalObject** | [**CompositeMedia**](CompositeMedia.md) |  |  [optional] |



