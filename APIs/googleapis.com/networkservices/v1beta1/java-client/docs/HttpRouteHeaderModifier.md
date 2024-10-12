

# HttpRouteHeaderModifier

The specification for modifying HTTP header in HTTP request and HTTP response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**add** | **Map&lt;String, String&gt;** | Add the headers with given map where key is the name of the header, value is the value of the header. |  [optional] |
|**remove** | **List&lt;String&gt;** | Remove headers (matching by header names) specified in the list. |  [optional] |
|**set** | **Map&lt;String, String&gt;** | Completely overwrite/replace the headers with given map where key is the name of the header, value is the value of the header. |  [optional] |



