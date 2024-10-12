# GitHubV3RestApi.ChecksUpdateRequestOutput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | [**[ChecksCreateRequestOutputAnnotationsInner]**](ChecksCreateRequestOutputAnnotationsInner.md) | Adds information from your analysis to specific lines of code. Annotations are visible in GitHub&#39;s pull request UI. Annotations are visible in GitHub&#39;s pull request UI. The Checks API limits the number of annotations to a maximum of 50 per API request. To create more than 50 annotations, you have to make multiple requests to the [Update a check run](https://docs.github.com/enterprise-server@3.4/rest/reference/checks#update-a-check-run) endpoint. Each time you update the check run, annotations are appended to the list of annotations that already exist for the check run. For details about annotations in the UI, see \&quot;[About status checks](https://docs.github.com/enterprise-server@3.4/articles/about-status-checks#checks)\&quot;. | [optional] 
**images** | [**[ChecksCreateRequestOutputImagesInner]**](ChecksCreateRequestOutputImagesInner.md) | Adds images to the output displayed in the GitHub pull request UI. | [optional] 
**summary** | **String** | Can contain Markdown. | 
**text** | **String** | Can contain Markdown. | [optional] 
**title** | **String** | **Required**. | [optional] 


