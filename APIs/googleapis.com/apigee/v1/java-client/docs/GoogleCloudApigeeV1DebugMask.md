

# GoogleCloudApigeeV1DebugMask


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**faultJSONPaths** | **List&lt;String&gt;** | List of JSON paths that specify the JSON elements to be filtered from JSON payloads in error flows. |  [optional] |
|**faultXPaths** | **List&lt;String&gt;** | List of XPaths that specify the XML elements to be filtered from XML payloads in error flows. |  [optional] |
|**name** | **String** | Name of the debug mask. |  [optional] |
|**namespaces** | **Map&lt;String, String&gt;** | Map of namespaces to URIs. |  [optional] |
|**requestJSONPaths** | **List&lt;String&gt;** | List of JSON paths that specify the JSON elements to be filtered from JSON request message payloads. |  [optional] |
|**requestXPaths** | **List&lt;String&gt;** | List of XPaths that specify the XML elements to be filtered from XML request message payloads. |  [optional] |
|**responseJSONPaths** | **List&lt;String&gt;** | List of JSON paths that specify the JSON elements to be filtered from JSON response message payloads. |  [optional] |
|**responseXPaths** | **List&lt;String&gt;** | List of XPaths that specify the XML elements to be filtered from XML response message payloads. |  [optional] |
|**variables** | **List&lt;String&gt;** | List of variables that should be masked from the debug output. |  [optional] |



