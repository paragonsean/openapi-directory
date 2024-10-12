

# ApplicationLoadInfo

Load Information about a Service Fabric application.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationLoadMetricInformation** | [**List&lt;ApplicationMetricDescription&gt;**](ApplicationMetricDescription.md) | List of application capacity metric description. |  [optional] |
|**id** | **String** | The identity of the application. This is an encoded representation of the application name. This is used in the REST APIs to identify the application resource. Starting in version 6.0, hierarchical names are delimited with the \&quot;\\~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp\\~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions.  |  [optional] |
|**maximumNodes** | **Long** | The maximum number of nodes where this application can be instantiated. It is the number of nodes this application is allowed to span. For applications that do not have application capacity defined this value will be zero.  |  [optional] |
|**minimumNodes** | **Long** | The minimum number of nodes for this application. It is the number of nodes where Service Fabric will reserve Capacity in the cluster which equals to ReservedLoad * MinimumNodes for this Application instance. For applications that do not have application capacity defined this value will be zero.  |  [optional] |
|**nodeCount** | **Long** | The number of nodes on which this application is instantiated. For applications that do not have application capacity defined this value will be zero.  |  [optional] |



