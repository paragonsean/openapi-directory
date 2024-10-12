# PdfBrokerIoApi.WkHtmlToPdfRequestDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**htmlBase64String** | **String** | Base64 encoded string with html. If property Url is set, it will be used, not HtmlBase64String. | [optional] 
**resources** | **{String: String}** | This is a set of key-value pairs of digital resources like images that is referenced in the HtmlBase64String document. It uses the filename including relative path as key and the data is provided as a Base64 encoded string. | [optional] 
**url** | **String** | The url to generate pdf from. Url has precedence over HtmlBase64String value if both are set. | [optional] 
**wkHtmlToPdfArguments** | **{String: String}** | Command line arguments passed to wkhtmltopdf. | [optional] 


