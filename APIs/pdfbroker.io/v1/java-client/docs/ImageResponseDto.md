

# ImageResponseDto

When setting the Accept-header in the request to \"application/json\" the image file will be return as Base64 encoded string. Note that converting data to Base64 encoded strings increases the response size with approximately 33%, if you can accept the a binary format it's better to use Accept-header \"image/jpeg\", \"image/png\" or \"image/gif\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorMessage** | **String** | If any error occurs the message will be displayed in here |  [optional] |
|**imageBase64String** | **String** | The Base64 encoded string that is the image file. This is a complete data uri, including media type that can be used directly as src on a img-tag e.g. |  [optional] |



