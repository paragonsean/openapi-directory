

# ContaineranalysisGoogleDevtoolsCloudbuildV1RepoSource

Location of the source in a Google Cloud Source Repository.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**branchName** | **String** | Regex matching branches to build. The syntax of the regular expressions accepted is the syntax accepted by RE2 and described at https://github.com/google/re2/wiki/Syntax |  [optional] |
|**commitSha** | **String** | Explicit commit SHA to build. |  [optional] |
|**dir** | **String** | Directory, relative to the source root, in which to run the build. This must be a relative path. If a step&#39;s &#x60;dir&#x60; is specified and is an absolute path, this value is ignored for that step&#39;s execution. |  [optional] |
|**invertRegex** | **Boolean** | Only trigger a build if the revision regex does NOT match the revision regex. |  [optional] |
|**projectId** | **String** | ID of the project that owns the Cloud Source Repository. If omitted, the project ID requesting the build is assumed. |  [optional] |
|**repoName** | **String** | Name of the Cloud Source Repository. |  [optional] |
|**substitutions** | **Map&lt;String, String&gt;** | Substitutions to use in a triggered build. Should only be used with RunBuildTrigger |  [optional] |
|**tagName** | **String** | Regex matching tags to build. The syntax of the regular expressions accepted is the syntax accepted by RE2 and described at https://github.com/google/re2/wiki/Syntax |  [optional] |



