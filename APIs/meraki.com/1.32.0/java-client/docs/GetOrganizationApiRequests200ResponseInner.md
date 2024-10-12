

# GetOrganizationApiRequests200ResponseInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminId** | **String** | Database ID for the admin user who made the API request. |  [optional] |
|**host** | **String** | The host which the API request was directed at. |  [optional] |
|**method** | **String** | HTTP method used in the API request. |  [optional] |
|**operationId** | **String** | Operation ID for the endpoint. |  [optional] |
|**path** | **String** | The API request path. |  [optional] |
|**queryString** | **String** | The query string sent with the API request. |  [optional] |
|**responseCode** | **Integer** | API request response code. |  [optional] |
|**sourceIp** | **String** | Public IP address from which the API request was made. |  [optional] |
|**ts** | **OffsetDateTime** | Timestamp, in iso8601 format, indicating when the API request was made. |  [optional] |
|**userAgent** | **String** | The API request user agent. |  [optional] |
|**version** | [**VersionEnum**](#VersionEnum) | API version of the endpoint. |  [optional] |



## Enum: VersionEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |



