

# ContaineranalysisGoogleDevtoolsCloudbuildV1GitSource

Location of the source in any accessible Git repository.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dir** | **String** | Directory, relative to the source root, in which to run the build. This must be a relative path. If a step&#39;s &#x60;dir&#x60; is specified and is an absolute path, this value is ignored for that step&#39;s execution. |  [optional] |
|**revision** | **String** | The revision to fetch from the Git repository such as a branch, a tag, a commit SHA, or any Git ref. Cloud Build uses &#x60;git fetch&#x60; to fetch the revision from the Git repository; therefore make sure that the string you provide for &#x60;revision&#x60; is parsable by the command. For information on string values accepted by &#x60;git fetch&#x60;, see https://git-scm.com/docs/gitrevisions#_specifying_revisions. For information on &#x60;git fetch&#x60;, see https://git-scm.com/docs/git-fetch. |  [optional] |
|**url** | **String** | Location of the Git repo to build. This will be used as a &#x60;git remote&#x60;, see https://git-scm.com/docs/git-remote. |  [optional] |



