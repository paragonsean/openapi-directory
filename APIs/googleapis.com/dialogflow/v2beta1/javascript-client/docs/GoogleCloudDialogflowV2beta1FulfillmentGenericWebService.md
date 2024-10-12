# DialogflowApi.GoogleCloudDialogflowV2beta1FulfillmentGenericWebService

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isCloudFunction** | **Boolean** | Optional. Indicates if generic web service is created through Cloud Functions integration. Defaults to false. is_cloud_function is deprecated. Cloud functions can be configured by its uri as a regular web service now. | [optional] 
**password** | **String** | The password for HTTP Basic authentication. | [optional] 
**requestHeaders** | **{String: String}** | The HTTP request headers to send together with fulfillment requests. | [optional] 
**uri** | **String** | Required. The fulfillment URI for receiving POST requests. It must use https protocol. | [optional] 
**username** | **String** | The user name for HTTP Basic authentication. | [optional] 


