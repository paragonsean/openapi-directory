

# CloudExportAdditionalProperties

Product property for the Cloud Retail API. For example, properties for a TV product could be \"Screen-Resolution\" or \"Screen-Size\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boolValue** | **Boolean** | Boolean value of the given property. For example for a TV product, \&quot;True\&quot; or \&quot;False\&quot; if the screen is UHD. |  [optional] |
|**floatValue** | **List&lt;Float&gt;** | Float values of the given property. For example for a TV product 1.2345. Maximum number of specified values for this field is 400. Values are stored in an arbitrary but consistent order. |  [optional] |
|**intValue** | **List&lt;String&gt;** | Integer values of the given property. For example, 1080 for a screen resolution of a TV product. Maximum number of specified values for this field is 400. Values are stored in an arbitrary but consistent order. |  [optional] |
|**maxValue** | **Float** | Maximum float value of the given property. For example for a TV product 100.00. |  [optional] |
|**minValue** | **Float** | Minimum float value of the given property. For example for a TV product 1.00. |  [optional] |
|**propertyName** | **String** | Name of the given property. For example, \&quot;Screen-Resolution\&quot; for a TV product. Maximum string size is 256 characters. |  [optional] |
|**textValue** | **List&lt;String&gt;** | Text value of the given property. For example, \&quot;8K(UHD)\&quot; could be a text value for a TV product. Maximum number of specified values for this field is 400. Values are stored in an arbitrary but consistent order. Maximum string size is 256 characters. |  [optional] |
|**unitCode** | **String** | Unit of the given property. For example, \&quot;Pixels\&quot; for a TV product. Maximum string size is 256 bytes. |  [optional] |



