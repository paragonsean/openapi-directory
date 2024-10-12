# DockerHubApi.PostNamespacesDeleteImagesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activeFrom** | **String** | Sets the time from which an image must have been pushed or pulled to be counted as active.  Defaults to 1 month before the current time.  | [optional] 
**dryRun** | **Boolean** | If &#x60;true&#x60; then will check and return errors and unignored warnings for the deletion request but will not delete any images. | [optional] 
**ignoreWarnings** | [**[PostNamespacesDeleteImagesRequestIgnoreWarningsInner]**](PostNamespacesDeleteImagesRequestIgnoreWarningsInner.md) | Warnings to ignore. If a warning is not ignored then no deletions will happen and the  warning is returned in the response.  These warnings include:  - is_active: warning when attempting to delete an image that is marked as active. - current_tag: warning when attempting to delete an image that has one or more current  tags in the repository.  Warnings can be copied from the response to the request.  | [optional] 
**manifests** | [**[PostNamespacesDeleteImagesRequestManifestsInner]**](PostNamespacesDeleteImagesRequestManifestsInner.md) | Image manifests to delete. | [optional] 


