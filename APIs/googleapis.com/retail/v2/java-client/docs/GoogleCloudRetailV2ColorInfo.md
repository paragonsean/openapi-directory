

# GoogleCloudRetailV2ColorInfo

The color information of a Product.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**colorFamilies** | **List&lt;String&gt;** | The standard color families. Strongly recommended to use the following standard color groups: \&quot;Red\&quot;, \&quot;Pink\&quot;, \&quot;Orange\&quot;, \&quot;Yellow\&quot;, \&quot;Purple\&quot;, \&quot;Green\&quot;, \&quot;Cyan\&quot;, \&quot;Blue\&quot;, \&quot;Brown\&quot;, \&quot;White\&quot;, \&quot;Gray\&quot;, \&quot;Black\&quot; and \&quot;Mixed\&quot;. Normally it is expected to have only 1 color family. May consider using single \&quot;Mixed\&quot; instead of multiple values. A maximum of 5 values are allowed. Each value must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned. Google Merchant Center property [color](https://support.google.com/merchants/answer/6324487). Schema.org property [Product.color](https://schema.org/color). |  [optional] |
|**colors** | **List&lt;String&gt;** | The color display names, which may be different from standard color family names, such as the color aliases used in the website frontend. Normally it is expected to have only 1 color. May consider using single \&quot;Mixed\&quot; instead of multiple values. A maximum of 75 colors are allowed. Each value must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned. Google Merchant Center property [color](https://support.google.com/merchants/answer/6324487). Schema.org property [Product.color](https://schema.org/color). |  [optional] |



