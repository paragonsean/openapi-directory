

# PutPermissionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**principals** | **List&lt;String&gt;** |  A list ARNs for the roles and users you want to grant access to the profiling group. Wildcards are not are supported in the ARNs.  |  |
|**revisionId** | **String** |  A universally unique identifier (UUID) for the revision of the policy you are adding to the profiling group. Do not specify this when you add permissions to a profiling group for the first time. If a policy already exists on the profiling group, you must specify the &lt;code&gt;revisionId&lt;/code&gt;.  |  [optional] |



