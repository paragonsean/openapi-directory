# DockerHubApi.PostNamespacesDeleteImagesResponseErrorErrinfoAllOfDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**[PostNamespacesDeleteImagesResponseErrorErrinfoAllOfDetailsErrorsInner]**](PostNamespacesDeleteImagesResponseErrorErrinfoAllOfDetailsErrorsInner.md) | Errors from validating delete request. These cannot be ignored. | [optional] 
**warnings** | [**[PostNamespacesDeleteImagesResponseErrorErrinfoAllOfDetailsWarningsInner]**](PostNamespacesDeleteImagesResponseErrorErrinfoAllOfDetailsWarningsInner.md) | Warnings that can be ignored.  These warnings include:  - is_active: warning when attempting to delete an image that is marked as  active. - current_tag: warning when attempting to delete an image that has one or  more current tags in the repository.  Warnings can be copied from the response to the request.  | [optional] 


