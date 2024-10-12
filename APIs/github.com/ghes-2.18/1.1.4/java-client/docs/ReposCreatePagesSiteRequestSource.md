

# ReposCreatePagesSiteRequestSource

The source branch and directory used to publish your Pages site.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**branch** | [**BranchEnum**](#BranchEnum) | The repository branch used to publish your site&#39;s source files. Can be either &#x60;master&#x60; or &#x60;gh-pages&#x60;. |  |
|**path** | [**PathEnum**](#PathEnum) | The repository directory that includes the source files for the Pages site. When &#x60;branch&#x60; is &#x60;master&#x60;, you can change &#x60;path&#x60; to &#x60;/docs&#x60;. When &#x60;branch&#x60; is &#x60;gh-pages&#x60;, you are unable to specify a &#x60;path&#x60; other than &#x60;/&#x60;. |  [optional] |



## Enum: BranchEnum

| Name | Value |
|---- | -----|
| MASTER | &quot;master&quot; |
| GH_PAGES | &quot;gh-pages&quot; |



## Enum: PathEnum

| Name | Value |
|---- | -----|
| SLASH | &quot;/&quot; |
| DOCS | &quot;/docs&quot; |



