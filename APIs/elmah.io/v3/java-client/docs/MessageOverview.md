

# MessageOverview


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**application** | **String** | Used to identify which application logged this message. You can use this if you have multiple applications and services logging to the same log |  [optional] |
|**breadcrumbs** | [**List&lt;Breadcrumb&gt;**](Breadcrumb.md) | A list of breadcrumbs preceding this log message. |  [optional] |
|**category** | **String** | The log message category. Category can be a string of choice but typically contain a logging category set by a logging framework like NLog or Serilog. |  [optional] |
|**code** | **String** | Code can be used to include source code related to the log message. The code will typically span from a few lines before the line causing the log message  to a few lines after. For now, all lines above 21 will be removed. This makes room for showing 10 lines before the logging line, the logging line, and  10 lines after the logging line. Don&#39;t include a very large string in this property since that will quickly make the entire messages exceed the max limit  of 256 kb. |  [optional] |
|**cookies** | [**List&lt;Item&gt;**](Item.md) | A key/value pair of cookies. This property only makes sense for logging messages related to web requests. |  [optional] |
|**correlationId** | **String** | CorrelationId can be used to group similar log messages together into a single discoverable batch. A correlation ID could be a session ID from ASP.NET Core,  a unique string spanning multiple microsservices handling the same request, or similar. |  [optional] |
|**data** | [**List&lt;Item&gt;**](Item.md) | A key/value pair of user-defined fields and their values. When logging an exception, the Data dictionary of  the exception is copied to this property. You can add additional key/value pairs, by modifying the Data  dictionary on the exception or by supplying additional key/values to this API. |  [optional] |
|**dateTime** | **OffsetDateTime** | The date and time in UTC of the message. If you don&#39;t provide us with a value in dateTime, we will set the current date and time in UTC. |  [optional] |
|**detail** | **String** | A longer description of the message. For errors this could be a stacktrace, but it&#39;s really up to you what to log in there. |  [optional] |
|**form** | [**List&lt;Item&gt;**](Item.md) | A key/value pair of form fields and their values. This property makes sense if logging message related to users inputting data in a form. |  [optional] |
|**hostname** | **String** | The hostname of the server logging the message. |  [optional] |
|**id** | **String** | The ID of this message. |  [optional] |
|**method** | **String** | If message relates to a HTTP request, you may send the HTTP method of that request. If you don&#39;t provide us with a method, we will try to find a key named REQUEST_METHOD in serverVariables. |  [optional] |
|**queryString** | [**List&lt;Item&gt;**](Item.md) | A key/value pair of query string parameters. This property makes sense if logging message related to a HTTP request. |  [optional] |
|**serverVariables** | [**List&lt;Item&gt;**](Item.md) | A key/value pair of server values. Server variables are typically related to handling requests in a webserver but could be used for other types of information as well. |  [optional] |
|**severity** | **String** | An enum value representing the severity of this message. The following values are allowed: Verbose, Debug, Information, Warning, Error, Fatal |  [optional] |
|**source** | **String** | The source of the code logging the message. This could be the assembly name. |  [optional] |
|**statusCode** | **Integer** | If the message logged relates to a HTTP status code, you can put the code in this property. This would probably only be relevant for errors,  but could be used for logging successful status codes as well. |  [optional] |
|**title** | **String** | The textual title or headline of the message to log. |  [optional] |
|**titleTemplate** | **String** | The title template of the message to log. This property can be used from logging frameworks that supports  structured logging like: \&quot;{user} says {quote}\&quot;. In the example, titleTemplate will be this string and title  will be \&quot;Gilfoyle says It&#39;s not magic. It&#39;s talent and sweat\&quot;. |  [optional] |
|**type** | **String** | The type of message. If logging an error, the type of the exception would go into type but you can put anything in there, that makes sense for your domain. |  [optional] |
|**url** | **String** | If message relates to a HTTP request, you may send the URL of that request. If you don&#39;t provide us with an URL, we will try to find a key named URL in serverVariables. |  [optional] |
|**user** | **String** | An identification of the user triggering this message. You can put the users email address or your user key into this property. |  [optional] |
|**version** | **String** | Versions can be used to distinguish messages from different versions of your software. The value of version can be a SemVer compliant string or any other  syntax that you are using as your version numbering scheme. |  [optional] |



