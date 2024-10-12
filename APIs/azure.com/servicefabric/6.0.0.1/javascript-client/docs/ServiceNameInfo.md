# ServiceFabricClientApis.ServiceNameInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | The identity of the service. This is an encoded representation of the service name. This is used in the REST APIs to identify the service resource.  Starting in version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric://myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions.  | [optional] 
**name** | **String** | The full name of the service with &#39;fabric:&#39; URI scheme. | [optional] 


