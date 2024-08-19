

# OutboundEnvironmentEndpoint

Endpoints accessed for a common purpose that the App Service Environment requires outbound network access to.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | **String** | The type of service accessed by the App Service Environment, e.g., Azure Storage, Azure SQL Database, and Azure Active Directory. |  [optional] |
|**endpoints** | [**List&lt;EndpointDependency&gt;**](EndpointDependency.md) | The endpoints that the App Service Environment reaches the service at. |  [optional] |



