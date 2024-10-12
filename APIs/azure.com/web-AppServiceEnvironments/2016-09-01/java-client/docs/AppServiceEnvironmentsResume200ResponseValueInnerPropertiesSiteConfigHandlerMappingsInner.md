

# AppServiceEnvironmentsResume200ResponseValueInnerPropertiesSiteConfigHandlerMappingsInner

The IIS handler mappings used to define which handler processes HTTP requests with certain extension.  For example, it is used to configure php-cgi.exe process to handle all HTTP requests with *.php extension.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arguments** | **String** | Command-line arguments to be passed to the script processor. |  [optional] |
|**extension** | **String** | Requests with this extension will be handled using the specified FastCGI application. |  [optional] |
|**scriptProcessor** | **String** | The absolute path to the FastCGI application. |  [optional] |



