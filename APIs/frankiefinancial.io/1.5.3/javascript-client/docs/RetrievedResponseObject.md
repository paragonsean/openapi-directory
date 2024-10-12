# FrankieFinancialApi.RetrievedResponseObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origHTTPstatus** | **Number** | This will be the HTTP response code that was returned originally (200, 404, etc).   In the case where you&#39;re requesting the result of a callback (previously backgrounded call), then this is the response that would have been sent, had you waited for the call to finish.  | [optional] 
**payload** | **{String: Object}** | This is a placeholder field. It will actually be a JSON object that is the payload that would have been returned (or was returned) in the original request. You&#39;ll need to process this as if it were the original response, and act accordingly.  | [optional] 


