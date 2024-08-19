

# Error

Schema of object returned in 4XX and 5XX responses. Note:  The name is unfortunate, since it conflicts with `java.lang.Error` and other generic error classes.  It is the name used in XML responses, so it is used for consistency and possible future XML deserialization support. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** |  |  |
|**modelState** | **Map&lt;String, List&lt;String&gt;&gt;** | When present, this property is a map of property names in the format &#x60;request.&lt;capitalized name&gt;&#x60; to an &#x60;Array&#x60; of validation error message strings for the property.  |  [optional] |



