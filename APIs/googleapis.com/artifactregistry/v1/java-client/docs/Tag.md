

# Tag

Tags point to a version and represent an alternative name that can be used to access the version.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the tag, for example: \&quot;projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/tags/tag1\&quot;. If the package part contains slashes, the slashes are escaped. The tag part can only have characters in [a-zA-Z0-9\\-._~:@], anything else must be URL encoded. |  [optional] |
|**version** | **String** | The name of the version the tag refers to, for example: \&quot;projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/versions/sha256:5243811\&quot; If the package or version ID parts contain slashes, the slashes are escaped. |  [optional] |



