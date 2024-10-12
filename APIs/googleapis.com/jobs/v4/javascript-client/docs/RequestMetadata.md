# CloudTalentSolutionApi.RequestMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowMissingIds** | **Boolean** | Only set when any of domain, session_id and user_id isn&#39;t available for some reason. It is highly recommended not to set this field and provide accurate domain, session_id and user_id for the best service experience. | [optional] 
**deviceInfo** | [**DeviceInfo**](DeviceInfo.md) |  | [optional] 
**domain** | **String** | Required if allow_missing_ids is unset or &#x60;false&#x60;. The client-defined scope or source of the service call, which typically is the domain on which the service has been implemented and is currently being run. For example, if the service is being run by client *Foo, Inc.*, on job board www.foo.com and career site www.bar.com, then this field is set to \&quot;foo.com\&quot; for use on the job board, and \&quot;bar.com\&quot; for use on the career site. Note that any improvements to the model for a particular tenant site rely on this field being set correctly to a unique domain. The maximum number of allowed characters is 255. | [optional] 
**sessionId** | **String** | Required if allow_missing_ids is unset or &#x60;false&#x60;. A unique session identification string. A session is defined as the duration of an end user&#39;s interaction with the service over a certain period. Obfuscate this field for privacy concerns before providing it to the service. Note that any improvements to the model for a particular tenant site rely on this field being set correctly to a unique session ID. The maximum number of allowed characters is 255. | [optional] 
**userId** | **String** | Required if allow_missing_ids is unset or &#x60;false&#x60;. A unique user identification string, as determined by the client. To have the strongest positive impact on search quality make sure the client-level is unique. Obfuscate this field for privacy concerns before providing it to the service. Note that any improvements to the model for a particular tenant site rely on this field being set correctly to a unique user ID. The maximum number of allowed characters is 255. | [optional] 


