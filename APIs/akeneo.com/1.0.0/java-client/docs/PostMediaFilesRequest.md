

# PostMediaFilesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_file** | **File** | The binaries of the file |  |
|**product** | **String** | The product to which the media file will be associated. It is a JSON string that follows this format &#39;{\&quot;identifier\&quot;:\&quot;product_identifier\&quot;, \&quot;attribute\&quot;:\&quot;attribute_code\&quot;, \&quot;scope\&quot;:\&quot;channel_code\&quot;,\&quot;locale\&quot;:\&quot;locale_code\&quot;}&#39;. You have to either use this field or the &#x60;product_model&#x60; field, but not both at the same time. |  [optional] |
|**productModel** | **String** | The product model to which the media file will be associated. It is a JSON string that follows this format &#39;{\&quot;code\&quot;:\&quot;product_model_code\&quot;, \&quot;attribute\&quot;:\&quot;attribute_code\&quot;, \&quot;scope\&quot;:\&quot;channel_code\&quot;,\&quot;locale\&quot;:\&quot;locale_code\&quot;}&#39;. You have to either use this field or the &#x60;product&#x60; field, but not both at the same time. |  [optional] |



