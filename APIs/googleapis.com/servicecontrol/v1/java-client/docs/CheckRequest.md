

# CheckRequest

Request message for the Check method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**operation** | [**Operation**](Operation.md) |  |  [optional] |
|**requestProjectSettings** | **Boolean** | Requests the project settings to be returned as part of the check response. |  [optional] |
|**serviceConfigId** | **String** | Specifies which version of service configuration should be used to process the request. If unspecified or no matching version can be found, the latest one will be used. |  [optional] |
|**skipActivationCheck** | **Boolean** | Indicates if service activation check should be skipped for this request. Default behavior is to perform the check and apply relevant quota. WARNING: Setting this flag to \&quot;true\&quot; will disable quota enforcement. |  [optional] |



