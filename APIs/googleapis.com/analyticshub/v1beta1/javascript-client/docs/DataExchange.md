# AnalyticsHubApi.DataExchange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Optional. Description of the data exchange. The description must not contain Unicode non-characters as well as C0 and C1 control codes except tabs (HT), new lines (LF), carriage returns (CR), and page breaks (FF). Default value is an empty string. Max length: 2000 bytes. | [optional] 
**displayName** | **String** | Required. Human-readable display name of the data exchange. The display name must contain only Unicode letters, numbers (0-9), underscores (_), dashes (-), spaces ( ), ampersands (&amp;) and must not start or end with spaces. Default value is an empty string. Max length: 63 bytes. | [optional] 
**documentation** | **String** | Optional. Documentation describing the data exchange. | [optional] 
**icon** | **Blob** | Optional. Base64 encoded image representing the data exchange. Max Size: 3.0MiB Expected image dimensions are 512x512 pixels, however the API only performs validation on size of the encoded data. Note: For byte fields, the content of the fields are base64-encoded (which increases the size of the data by 33-36%) when using JSON on the wire. | [optional] 
**listingCount** | **Number** | Output only. Number of listings contained in the data exchange. | [optional] [readonly] 
**name** | **String** | Output only. The resource name of the data exchange. e.g. &#x60;projects/myproject/locations/US/dataExchanges/123&#x60;. | [optional] [readonly] 
**primaryContact** | **String** | Optional. Email or URL of the primary point of contact of the data exchange. Max Length: 1000 bytes. | [optional] 


