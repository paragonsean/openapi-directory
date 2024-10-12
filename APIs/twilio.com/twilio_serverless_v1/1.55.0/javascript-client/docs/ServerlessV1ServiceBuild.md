# TwilioServerless.ServerlessV1ServiceBuild

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Build resource. | [optional] 
**assetVersions** | **[Object]** | The list of Asset Version resource SIDs that are included in the Build. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the Build resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the Build resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dependencies** | **[Object]** | A list of objects that describe the Dependencies included in the Build. Each object contains the &#x60;name&#x60; and &#x60;version&#x60; of the dependency. | [optional] 
**functionVersions** | **[Object]** | The list of Function Version resource SIDs that are included in the Build. | [optional] 
**links** | **Object** |  | [optional] 
**runtime** | [**BuildEnumRuntime**](BuildEnumRuntime.md) |  | [optional] 
**serviceSid** | **String** | The SID of the Service that the Build resource is associated with. | [optional] 
**sid** | **String** | The unique string that we created to identify the Build resource. | [optional] 
**status** | [**BuildEnumStatus**](BuildEnumStatus.md) |  | [optional] 
**url** | **String** | The absolute URL of the Build resource. | [optional] 


