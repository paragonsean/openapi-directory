# CloudLoggingApi.RequestLog

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appEngineRelease** | **String** | App Engine release version. | [optional] 
**appId** | **String** | Application that handled this request. | [optional] 
**cost** | **Number** | An indication of the relative cost of serving this request. | [optional] 
**endTime** | **String** | Time when the request finished. | [optional] 
**finished** | **Boolean** | Whether this request is finished or active. | [optional] 
**first** | **Boolean** | Whether this is the first RequestLog entry for this request. If an active request has several RequestLog entries written to Stackdriver Logging, then this field will be set for one of them. | [optional] 
**host** | **String** | Internet host and port number of the resource being requested. | [optional] 
**httpVersion** | **String** | HTTP version of request. Example: \&quot;HTTP/1.1\&quot;. | [optional] 
**instanceId** | **String** | An identifier for the instance that handled the request. | [optional] 
**instanceIndex** | **Number** | If the instance processing this request belongs to a manually scaled module, then this is the 0-based index of the instance. Otherwise, this value is -1. | [optional] 
**ip** | **String** | Origin IP address. | [optional] 
**latency** | **String** | Latency of the request. | [optional] 
**line** | [**[LogLine]**](LogLine.md) | A list of log lines emitted by the application while serving this request. | [optional] 
**megaCycles** | **String** | Number of CPU megacycles used to process request. | [optional] 
**method** | **String** | Request method. Example: \&quot;GET\&quot;, \&quot;HEAD\&quot;, \&quot;PUT\&quot;, \&quot;POST\&quot;, \&quot;DELETE\&quot;. | [optional] 
**moduleId** | **String** | Module of the application that handled this request. | [optional] 
**nickname** | **String** | The logged-in user who made the request.Most likely, this is the part of the user&#39;s email before the @ sign. The field value is the same for different requests from the same user, but different users can have similar names. This information is also available to the application via the App Engine Users API.This field will be populated starting with App Engine 1.9.21. | [optional] 
**pendingTime** | **String** | Time this request spent in the pending request queue. | [optional] 
**referrer** | **String** | Referrer URL of request. | [optional] 
**requestId** | **String** | Globally unique identifier for a request, which is based on the request start time. Request IDs for requests which started later will compare greater as strings than those for requests which started earlier. | [optional] 
**resource** | **String** | Contains the path and query portion of the URL that was requested. For example, if the URL was \&quot;http://example.com/app?name&#x3D;val\&quot;, the resource would be \&quot;/app?name&#x3D;val\&quot;. The fragment identifier, which is identified by the # character, is not included. | [optional] 
**responseSize** | **String** | Size in bytes sent back to client by request. | [optional] 
**sourceReference** | [**[SourceReference]**](SourceReference.md) | Source code for the application that handled this request. There can be more than one source reference per deployed application if source code is distributed among multiple repositories. | [optional] 
**spanId** | **String** | Stackdriver Trace span identifier for this request. | [optional] 
**startTime** | **String** | Time when the request started. | [optional] 
**status** | **Number** | HTTP response status code. Example: 200, 404. | [optional] 
**taskName** | **String** | Task name of the request, in the case of an offline request. | [optional] 
**taskQueueName** | **String** | Queue name of the request, in the case of an offline request. | [optional] 
**traceId** | **String** | Stackdriver Trace identifier for this request. | [optional] 
**traceSampled** | **Boolean** | If true, the value in the &#39;trace_id&#39; field was sampled for storage in a trace backend. | [optional] 
**urlMapEntry** | **String** | File or class that handled the request. | [optional] 
**userAgent** | **String** | User agent that made the request. | [optional] 
**versionId** | **String** | Version of the application that handled this request. | [optional] 
**wasLoadingRequest** | **Boolean** | Whether this was a loading request for the instance. | [optional] 


