# GitHubV3RestApi.ReposCreatePagesSiteRequestSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **String** | The repository branch used to publish your site&#39;s source files. Can be either &#x60;master&#x60; or &#x60;gh-pages&#x60;. | 
**path** | **String** | The repository directory that includes the source files for the Pages site. When &#x60;branch&#x60; is &#x60;master&#x60;, you can change &#x60;path&#x60; to &#x60;/docs&#x60;. When &#x60;branch&#x60; is &#x60;gh-pages&#x60;, you are unable to specify a &#x60;path&#x60; other than &#x60;/&#x60;. | [optional] [default to &#39;/&#39;]



## Enum: BranchEnum


* `master` (value: `"master"`)

* `gh-pages` (value: `"gh-pages"`)





## Enum: PathEnum


* `SLASH` (value: `"/"`)

* `docs` (value: `"/docs"`)




