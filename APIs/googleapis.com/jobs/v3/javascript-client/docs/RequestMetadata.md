# CloudTalentSolutionApi.RequestMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deviceInfo** | [**DeviceInfo**](DeviceInfo.md) |  | [optional] 
**domain** | **String** | Required. The client-defined scope or source of the service call, which typically is the domain on which the service has been implemented and is currently being run. For example, if the service is being run by client *Foo, Inc.*, on job board www.foo.com and career site www.bar.com, then this field is set to \&quot;foo.com\&quot; for use on the job board, and \&quot;bar.com\&quot; for use on the career site. If this field isn&#39;t available for some reason, send \&quot;UNKNOWN\&quot;. Any improvements to the model for a particular tenant site rely on this field being set correctly to a domain. The maximum number of allowed characters is 255. | [optional] 
**sessionId** | **String** | Required. A unique session identification string. A session is defined as the duration of an end user&#39;s interaction with the service over a certain period. Obfuscate this field for privacy concerns before providing it to the service. If this field is not available for some reason, send \&quot;UNKNOWN\&quot;. Note that any improvements to the model for a particular tenant site, rely on this field being set correctly to some unique session_id. The maximum number of allowed characters is 255. | [optional] 
**userId** | **String** | Required. A unique user identification string, as determined by the client. To have the strongest positive impact on search quality make sure the client-level is unique. Obfuscate this field for privacy concerns before providing it to the service. If this field is not available for some reason, send \&quot;UNKNOWN\&quot;. Note that any improvements to the model for a particular tenant site, rely on this field being set correctly to a unique user_id. The maximum number of allowed characters is 255. | [optional] 


