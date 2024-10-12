

# PdfResponseDto

When setting the Accept-header in the request to \"application/json\" the content of the pdf file will be return as Base64 encoded string. Note that converting data to Base64 encoded strings increases the response size with approximately 33%, if you can accept the a binary format it's better to use Accept-header \"application/pdf\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorMessage** | **String** | If any error occurs the message will be displayed in here |  [optional] |
|**pdfFileBase64String** | **String** | The Base64 encoded string that is the pdf file. |  [optional] |



