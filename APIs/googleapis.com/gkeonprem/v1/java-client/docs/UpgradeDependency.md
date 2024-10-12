

# UpgradeDependency

UpgradeDependency represents a dependency when upgrading a resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentVersion** | **String** | Current version of the dependency e.g. 1.15.0. |  [optional] |
|**membership** | **String** | Membership names are formatted as &#x60;projects//locations//memberships/&#x60;. |  [optional] |
|**resourceName** | **String** | Resource name of the dependency. |  [optional] |
|**targetVersion** | **String** | Target version of the dependency e.g. 1.16.1. This is the version the dependency needs to be upgraded to before a resource can be upgraded. |  [optional] |



