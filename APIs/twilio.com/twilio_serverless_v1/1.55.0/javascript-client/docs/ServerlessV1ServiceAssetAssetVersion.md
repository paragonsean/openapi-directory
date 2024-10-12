# TwilioServerless.ServerlessV1ServiceAssetAssetVersion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Asset Version resource. | [optional] 
**assetSid** | **String** | The SID of the Asset resource that is the parent of the Asset Version. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the Asset Version resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**path** | **String** | The URL-friendly string by which the Asset Version can be referenced. It can be a maximum of 255 characters. All paths begin with a forward slash (&#39;/&#39;). If an Asset Version creation request is submitted with a path not containing a leading slash, the path will automatically be prepended with one. | [optional] 
**serviceSid** | **String** | The SID of the Service that the Asset Version resource is associated with. | [optional] 
**sid** | **String** | The unique string that we created to identify the Asset Version resource. | [optional] 
**url** | **String** | The absolute URL of the Asset Version resource. | [optional] 
**visibility** | [**AssetVersionEnumVisibility**](AssetVersionEnumVisibility.md) |  | [optional] 


