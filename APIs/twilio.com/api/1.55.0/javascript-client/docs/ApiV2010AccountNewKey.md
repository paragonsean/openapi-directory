# TwilioApi.ApiV2010AccountNewKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dateCreated** | **String** | The date and time in GMT that the API Key was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**dateUpdated** | **String** | The date and time in GMT that the new API Key was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. | [optional] 
**friendlyName** | **String** | The string that you assigned to describe the resource. | [optional] 
**secret** | **String** | The secret your application uses to sign Access Tokens and to authenticate to the REST API (you will use this as the basic-auth &#x60;password&#x60;).  **Note that for security reasons, this field is ONLY returned when the API Key is first created.** | [optional] 
**sid** | **String** | The unique string that that we created to identify the NewKey resource. You will use this as the basic-auth &#x60;user&#x60; when authenticating to the API. | [optional] 


