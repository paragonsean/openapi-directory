

# Database

Represents a SQL database on the Cloud SQL instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**charset** | **String** | The Cloud SQL charset value. |  [optional] |
|**collation** | **String** | The Cloud SQL collation value. |  [optional] |
|**etag** | **String** | This field is deprecated and will be removed from a future version of the API. |  [optional] |
|**instance** | **String** | The name of the Cloud SQL instance. This does not include the project ID. |  [optional] |
|**kind** | **String** | This is always &#x60;sql#database&#x60;. |  [optional] |
|**name** | **String** | The name of the database in the Cloud SQL instance. This does not include the project ID or instance name. |  [optional] |
|**project** | **String** | The project ID of the project containing the Cloud SQL database. The Google apps domain is prefixed if applicable. |  [optional] |
|**selfLink** | **String** | The URI of this resource. |  [optional] |
|**sqlserverDatabaseDetails** | [**SqlServerDatabaseDetails**](SqlServerDatabaseDetails.md) |  |  [optional] |



