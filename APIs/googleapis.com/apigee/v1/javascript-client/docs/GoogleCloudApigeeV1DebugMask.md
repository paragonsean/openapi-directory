# ApigeeApi.GoogleCloudApigeeV1DebugMask

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**faultJSONPaths** | **[String]** | List of JSON paths that specify the JSON elements to be filtered from JSON payloads in error flows. | [optional] 
**faultXPaths** | **[String]** | List of XPaths that specify the XML elements to be filtered from XML payloads in error flows. | [optional] 
**name** | **String** | Name of the debug mask. | [optional] 
**namespaces** | **{String: String}** | Map of namespaces to URIs. | [optional] 
**requestJSONPaths** | **[String]** | List of JSON paths that specify the JSON elements to be filtered from JSON request message payloads. | [optional] 
**requestXPaths** | **[String]** | List of XPaths that specify the XML elements to be filtered from XML request message payloads. | [optional] 
**responseJSONPaths** | **[String]** | List of JSON paths that specify the JSON elements to be filtered from JSON response message payloads. | [optional] 
**responseXPaths** | **[String]** | List of XPaths that specify the XML elements to be filtered from XML response message payloads. | [optional] 
**variables** | **[String]** | List of variables that should be masked from the debug output. | [optional] 


