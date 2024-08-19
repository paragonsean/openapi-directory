# CloudSchedulerApi.AppEngineHttpTarget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appEngineRouting** | [**AppEngineRouting**](AppEngineRouting.md) |  | [optional] 
**body** | **Blob** | Body. HTTP request body. A request body is allowed only if the HTTP method is POST or PUT. It will result in invalid argument error to set a body on a job with an incompatible HttpMethod. | [optional] 
**headers** | **{String: String}** | HTTP request headers. This map contains the header field names and values. Headers can be set when the job is created. Cloud Scheduler sets some headers to default values: * &#x60;User-Agent&#x60;: By default, this header is &#x60;\&quot;AppEngine-Google; (+http://code.google.com/appengine)\&quot;&#x60;. This header can be modified, but Cloud Scheduler will append &#x60;\&quot;AppEngine-Google; (+http://code.google.com/appengine)\&quot;&#x60; to the modified &#x60;User-Agent&#x60;. * &#x60;X-CloudScheduler&#x60;: This header will be set to true. * &#x60;X-CloudScheduler-JobName&#x60;: This header will contain the job name. * &#x60;X-CloudScheduler-ScheduleTime&#x60;: For Cloud Scheduler jobs specified in the unix-cron format, this header will contain the job schedule as an offset of UTC parsed according to RFC3339. If the job has a body and the following headers are not set by the user, Cloud Scheduler sets default values: * &#x60;Content-Type&#x60;: This will be set to &#x60;\&quot;application/octet-stream\&quot;&#x60;. You can override this default by explicitly setting &#x60;Content-Type&#x60; to a particular media type when creating the job. For example, you can set &#x60;Content-Type&#x60; to &#x60;\&quot;application/json\&quot;&#x60;. The headers below are output only. They cannot be set or overridden: * &#x60;Content-Length&#x60;: This is computed by Cloud Scheduler. * &#x60;X-Google-*&#x60;: For Google internal use only. * &#x60;X-AppEngine-*&#x60;: For Google internal use only. In addition, some App Engine headers, which contain job-specific information, are also be sent to the job handler. | [optional] 
**httpMethod** | **String** | The HTTP method to use for the request. PATCH and OPTIONS are not permitted. | [optional] 
**relativeUri** | **String** | The relative URI. The relative URL must begin with \&quot;/\&quot; and must be a valid HTTP relative URL. It can contain a path, query string arguments, and &#x60;#&#x60; fragments. If the relative URL is empty, then the root path \&quot;/\&quot; will be used. No spaces are allowed, and the maximum length allowed is 2083 characters. | [optional] 



## Enum: HttpMethodEnum


* `HTTP_METHOD_UNSPECIFIED` (value: `"HTTP_METHOD_UNSPECIFIED"`)

* `POST` (value: `"POST"`)

* `GET` (value: `"GET"`)

* `HEAD` (value: `"HEAD"`)

* `PUT` (value: `"PUT"`)

* `DELETE` (value: `"DELETE"`)

* `PATCH` (value: `"PATCH"`)

* `OPTIONS` (value: `"OPTIONS"`)




