

# TeamsAddOrUpdateProjectPermissionsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**permission** | [**PermissionEnum**](#PermissionEnum) | The permission to grant to the team for this project. Can be one of:   \\* &#x60;read&#x60; - team members can read, but not write to or administer this project.   \\* &#x60;write&#x60; - team members can read and write, but not administer this project.   \\* &#x60;admin&#x60; - team members can read, write and administer this project.   Default: the team&#39;s &#x60;permission&#x60; attribute will be used to determine what permission to grant the team on this project. Note that, if you choose not to pass any parameters, you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.19/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;   **Note**: If you pass the &#x60;hellcat-preview&#x60; media type, you can promote—but not demote—a &#x60;permission&#x60; attribute inherited from a parent team. |  [optional] |



## Enum: PermissionEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |
| ADMIN | &quot;admin&quot; |



