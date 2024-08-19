

# TeamsAddOrUpdateProjectPermissionsInOrgRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**permission** | [**PermissionEnum**](#PermissionEnum) | The permission to grant to the team for this project. Default: the team&#39;s &#x60;permission&#x60; attribute will be used to determine what permission to grant the team on this project. Note that, if you choose not to pass any parameters, you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@3.1/rest/overview/resources-in-the-rest-api#http-verbs).\&quot; |  [optional] |



## Enum: PermissionEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |
| ADMIN | &quot;admin&quot; |



