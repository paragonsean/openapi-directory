# CloudTasksApi.AppEngineHttpRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appEngineRouting** | [**AppEngineRouting**](AppEngineRouting.md) |  | [optional] 
**body** | **Blob** | HTTP request body. A request body is allowed only if the HTTP method is POST or PUT. It is an error to set a body on a task with an incompatible HttpMethod. | [optional] 
**headers** | **{String: String}** | HTTP request headers. This map contains the header field names and values. Headers can be set when the task is created. Repeated headers are not supported but a header value can contain commas. Cloud Tasks sets some headers to default values: * &#x60;User-Agent&#x60;: By default, this header is &#x60;\&quot;AppEngine-Google; (+http://code.google.com/appengine)\&quot;&#x60;. This header can be modified, but Cloud Tasks will append &#x60;\&quot;AppEngine-Google; (+http://code.google.com/appengine)\&quot;&#x60; to the modified &#x60;User-Agent&#x60;. If the task has a body, Cloud Tasks sets the following headers: * &#x60;Content-Type&#x60;: By default, the &#x60;Content-Type&#x60; header is set to &#x60;\&quot;application/octet-stream\&quot;&#x60;. The default can be overridden by explicitly setting &#x60;Content-Type&#x60; to a particular media type when the task is created. For example, &#x60;Content-Type&#x60; can be set to &#x60;\&quot;application/json\&quot;&#x60;. * &#x60;Content-Length&#x60;: This is computed by Cloud Tasks. This value is output only. It cannot be changed. The headers below cannot be set or overridden: * &#x60;Host&#x60; * &#x60;X-Google-*&#x60; * &#x60;X-AppEngine-*&#x60; In addition, Cloud Tasks sets some headers when the task is dispatched, such as headers containing information about the task; see [request headers](https://cloud.google.com/tasks/docs/creating-appengine-handlers#reading_request_headers). These headers are set only when the task is dispatched, so they are not visible when the task is returned in a Cloud Tasks response. Although there is no specific limit for the maximum number of headers or the size, there is a limit on the maximum size of the Task. For more information, see the CreateTask documentation. | [optional] 
**httpMethod** | **String** | The HTTP method to use for the request. The default is POST. The app&#39;s request handler for the task&#39;s target URL must be able to handle HTTP requests with this http_method, otherwise the task attempt fails with error code 405 (Method Not Allowed). See [Writing a push task request handler](https://cloud.google.com/appengine/docs/java/taskqueue/push/creating-handlers#writing_a_push_task_request_handler) and the App Engine documentation for your runtime on [How Requests are Handled](https://cloud.google.com/appengine/docs/standard/python3/how-requests-are-handled). | [optional] 
**relativeUri** | **String** | The relative URI. The relative URI must begin with \&quot;/\&quot; and must be a valid HTTP relative URI. It can contain a path and query string arguments. If the relative URI is empty, then the root path \&quot;/\&quot; will be used. No spaces are allowed, and the maximum length allowed is 2083 characters. | [optional] 



## Enum: HttpMethodEnum


* `HTTP_METHOD_UNSPECIFIED` (value: `"HTTP_METHOD_UNSPECIFIED"`)

* `POST` (value: `"POST"`)

* `GET` (value: `"GET"`)

* `HEAD` (value: `"HEAD"`)

* `PUT` (value: `"PUT"`)

* `DELETE` (value: `"DELETE"`)

* `PATCH` (value: `"PATCH"`)

* `OPTIONS` (value: `"OPTIONS"`)




