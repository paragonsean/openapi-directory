# GitHubV3RestApi.TeamsAddOrUpdateProjectPermissionsLegacyRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | **String** | The permission to grant to the team for this project. Can be one of:   \\* &#x60;read&#x60; - team members can read, but not write to or administer this project.   \\* &#x60;write&#x60; - team members can read and write, but not administer this project.   \\* &#x60;admin&#x60; - team members can read, write and administer this project.   Default: the team&#39;s &#x60;permission&#x60; attribute will be used to determine what permission to grant the team on this project. Note that, if you choose not to pass any parameters, you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@3.0/rest/overview/resources-in-the-rest-api#http-verbs).\&quot; | [optional] 



## Enum: PermissionEnum


* `read` (value: `"read"`)

* `write` (value: `"write"`)

* `admin` (value: `"admin"`)




