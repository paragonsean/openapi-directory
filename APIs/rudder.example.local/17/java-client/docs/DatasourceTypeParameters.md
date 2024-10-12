

# DatasourceTypeParameters

You can use Rudder variable expansion (`${rudder.node`, `${node.properties...}`)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkSsl** | **Boolean** | Check SSL certificate validity for https. Must be set to false for self-signed certificate |  [optional] |
|**headers** | [**List&lt;DatasourceTypeParametersHeadersInner&gt;**](DatasourceTypeParametersHeadersInner.md) | Represent HTTP headers for the query. Rudder expansion available. |  [optional] |
|**path** | **String** | JSON path (as defined in [the specification](https://github.com/jayway/JsonPath/), without the leading &#x60;$.&#x60;) to find the interesting sub-json or string/number/boolean value in the answer. Let empty to use the whole answer as value. |  [optional] |
|**requestMethod** | [**RequestMethodEnum**](#RequestMethodEnum) | HTTP method to use to contact the URL. |  [optional] |
|**requestMode** | [**DatasourceTypeParametersRequestMode**](DatasourceTypeParametersRequestMode.md) |  |  [optional] |
|**requestTimeout** | **Integer** | Timeout in seconds for each HTTP request |  [optional] |
|**url** | **String** | URL to contact. Rudder expansion available. |  [optional] |



## Enum: RequestMethodEnum

| Name | Value |
|---- | -----|
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |



