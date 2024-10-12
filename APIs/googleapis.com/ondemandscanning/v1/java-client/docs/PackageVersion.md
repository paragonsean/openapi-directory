

# PackageVersion


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**licenses** | **List&lt;String&gt;** | The licenses associated with this package. Note that this has to go on the PackageVersion level, because we can have cases with images with the same source having different licences. E.g. in Alpine, musl and musl-utils both have the same origin musl, but have different sets of licenses. |  [optional] |
|**name** | **String** |  |  [optional] |
|**version** | **String** |  |  [optional] |



