

# ApplicationDescription

Describes a Service Fabric application.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationCapacity** | [**ApplicationCapacityDescription**](ApplicationCapacityDescription.md) |  |  [optional] |
|**name** | **String** | The name of the application, including the &#39;fabric:&#39; URI scheme. |  |
|**parameterList** | [**List&lt;ApplicationParameter&gt;**](ApplicationParameter.md) | List of application parameters with overridden values from their default values specified in the application manifest. |  [optional] |
|**typeName** | **String** | The application type name as defined in the application manifest. |  |
|**typeVersion** | **String** | The version of the application type as defined in the application manifest. |  |



