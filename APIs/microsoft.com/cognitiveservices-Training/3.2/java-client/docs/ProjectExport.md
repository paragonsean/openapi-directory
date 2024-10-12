

# ProjectExport

Represents information about a project export.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**estimatedImportTimeInMS** | **Integer** | Estimated time this project will take to import, can change based on network connectivity and load between  source and destination regions. |  [optional] [readonly] |
|**imageCount** | **Integer** | Count of images that will be exported. |  [optional] [readonly] |
|**iterationCount** | **Integer** | Count of iterations that will be exported. |  [optional] [readonly] |
|**regionCount** | **Integer** | Count of regions that will be exported. |  [optional] [readonly] |
|**tagCount** | **Integer** | Count of tags that will be exported. |  [optional] [readonly] |
|**token** | **String** | Opaque token that should be passed to ImportProject to perform the import. This token grants access to import this  project to all that have the token. |  [optional] [readonly] |



