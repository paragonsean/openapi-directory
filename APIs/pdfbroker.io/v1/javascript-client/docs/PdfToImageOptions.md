# PdfBrokerIoApi.PdfToImageOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **Number** | Set the height of the output image, default value is width of source document. To scale height, and keeping proportions, do not set width; | [optional] 
**horizontalResolution** | **Number** | Set the horizontal resolution, default is 96 dpi; | [optional] 
**imageFormat** | **String** | Valid options are \&quot;image/jpeg\&quot;, \&quot;image/png\&quot; or \&quot;image/gif\&quot;. Default is \&quot;image/png\&quot; | [optional] 
**jpegQuality** | **Number** | Sets the quality of jpeg images, range 0 to 100, default is 75 | [optional] 
**pageNumber** | **Number** | Which page of the pdf file to generate image from, default is first page | [optional] 
**pngCompressionLevel** | **Number** | Sets the png compression level, range 1 - 9, default is 6 | [optional] 
**transparent** | **Boolean** | Keep the background of the image transparent. This setting is not available in JPEG-files, since transparency is not supported in the JPEG format. | [optional] 
**verticalResolution** | **Number** | Set the vertical resolution, default is 96 dpi; | [optional] 
**width** | **Number** | Set the width of the output image, default value is width of source document. To scale width, and keeping proportions, do not set height; | [optional] 


