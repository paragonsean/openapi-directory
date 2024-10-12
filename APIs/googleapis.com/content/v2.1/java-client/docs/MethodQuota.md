

# MethodQuota

The quota information per method in the Content API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**method** | **String** | The method name, for example &#x60;products.list&#x60;. Method name does not contain version because quota can be shared between different API versions of the same method. |  [optional] |
|**quotaLimit** | **String** | The current quota limit per day, meaning the maximum number of calls for the method. |  [optional] |
|**quotaUsage** | **String** | The current quota usage, meaning the number of calls already made to the method. |  [optional] |



