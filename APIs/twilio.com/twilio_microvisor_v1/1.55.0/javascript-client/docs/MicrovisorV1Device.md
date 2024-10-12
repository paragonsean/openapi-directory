# TwilioMicrovisor.MicrovisorV1Device

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The unique SID identifier of the Account. | [optional] 
**app** | **Object** | Information about the target App and the App reported by this Device. Contains the properties &#x60;target_sid&#x60;, &#x60;date_targeted&#x60;, &#x60;update_status&#x60; (one of &#x60;up-to-date&#x60;, &#x60;pending&#x60; and &#x60;error&#x60;), &#x60;update_error_code&#x60;, &#x60;reported_sid&#x60; and &#x60;date_reported&#x60;. | [optional] 
**dateCreated** | **Date** | The date that this Device was created, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateUpdated** | **Date** | The date that this Device was last updated, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**links** | **Object** | The absolute URLs of related resources. | [optional] 
**logging** | **Object** | Object specifying whether application logging is enabled for this Device. Contains the properties &#x60;enabled&#x60; and &#x60;date_expires&#x60;. | [optional] 
**sid** | **String** | A 34-character string that uniquely identifies this Device. | [optional] 
**uniqueName** | **String** | A developer-defined string that uniquely identifies the Device. This value must be unique for all Devices on this Account. The &#x60;unique_name&#x60; value may be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource. | [optional] 
**url** | **String** | The URL of this resource. | [optional] 


