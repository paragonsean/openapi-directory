# WebAppsApiClient.WebAppsGetHybridConnection200ResponseProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **String** | The hostname of the endpoint. | [optional] 
**port** | **Number** | The port of the endpoint. | [optional] 
**relayArmUri** | **String** | The ARM URI to the Service Bus relay. | [optional] 
**relayName** | **String** | The name of the Service Bus relay. | [optional] 
**sendKeyName** | **String** | The name of the Service Bus key which has Send permissions. This is used to authenticate to Service Bus. | [optional] 
**sendKeyValue** | **String** | The value of the Service Bus key. This is used to authenticate to Service Bus. In ARM this key will not be returned normally, use the POST /listKeys API instead. | [optional] 
**serviceBusNamespace** | **String** | The name of the Service Bus namespace. | [optional] 
**serviceBusSuffix** | **String** | The suffix for the service bus endpoint. By default this is .servicebus.windows.net | [optional] 


