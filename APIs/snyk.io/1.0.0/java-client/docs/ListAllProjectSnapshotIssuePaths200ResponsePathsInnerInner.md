

# ListAllProjectSnapshotIssuePaths200ResponsePathsInnerInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fixVersion** | **String** | The version to upgrade the package to in order to resolve the issue. This will only appear on the first element of the path, and only if the issue can be fixed by upgrading packages. Note that if the fix requires upgrading transitive dependencies, &#x60;fixVersion&#x60; will be the same as &#x60;version&#x60;. |  [optional] |
|**name** | **String** | The package name |  [optional] |
|**version** | **String** | The package version |  [optional] |



