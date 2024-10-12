# PhantAuth.FleetFleetnameGet200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | URL of the Fleet&#39;s JSON representation. | [optional] 
**logo** | **String** | The URL of the fleet logo, which can be customized by the gravatar associated with the email address in the &#x60;logo_email&#x60; property. | [optional] 
**logoEmail** | **String** | The email address of the fleet, either generated or provided in the &#x60;sub&#x60; property. The fleet logo can be customized by the use of the gravater associated with this email address. | [optional] 
**members** | **[Object]** | The client objects included in a fleet. | [optional] 
**name** | **String** | The displayed fleet name. | [optional] 
**profile** | **String** | The URL of the Fleet profile. | [optional] 
**sub** | **String** | The name or email address of a given fleet. The fleet properties and fleet members are generated from this name. If provide an email address, you can customize the fleet logo by the use of the gravatar associated with the email address. | 


