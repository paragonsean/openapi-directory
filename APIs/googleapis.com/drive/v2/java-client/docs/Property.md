

# Property

A key-value pair attached to a file that is either public or private to an application. The following limits apply to file properties: * Maximum of 100 properties total per file * Maximum of 30 private properties per app * Maximum of 30 public properties * Maximum of 124 bytes size limit on (key + value) string in UTF-8 encoding for a single property Some resource methods (such as `properties.update`) require a `propertyKey`. Use the `properties.list` method to retrieve the key for a property.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**etag** | **String** | Output only. ETag of the property. |  [optional] |
|**key** | **String** | The key of this property. |  [optional] |
|**kind** | **String** | Output only. This is always &#x60;drive#property&#x60;. |  [optional] |
|**selfLink** | **String** | Output only. The link back to this property. |  [optional] |
|**value** | **String** | The value of this property. |  [optional] |
|**visibility** | **String** | The visibility of this property. Allowed values are PRIVATE (default) and PUBLIC. Private properties can only be retrieved using an authenticated request. An authenticated request uses an access token obtained with a OAuth 2 client ID. You cannot use an API key to retrieve private properties. |  [optional] |



