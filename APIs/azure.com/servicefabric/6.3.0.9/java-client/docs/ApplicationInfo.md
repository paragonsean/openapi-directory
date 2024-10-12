

# ApplicationInfo

Information about a Service Fabric application.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationDefinitionKind** | **ApplicationDefinitionKind** |  |  [optional] |
|**healthState** | **HealthState** |  |  [optional] |
|**id** | **String** | The identity of the application. This is an encoded representation of the application name. This is used in the REST APIs to identify the application resource. Starting in version 6.0, hierarchical names are delimited with the \&quot;\\~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp\\~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. |  [optional] |
|**name** | **String** | The name of the application, including the &#39;fabric:&#39; URI scheme. |  [optional] |
|**parameters** | [**List&lt;ApplicationParameter&gt;**](ApplicationParameter.md) | List of application parameters with overridden values from their default values specified in the application manifest. |  [optional] |
|**status** | **ApplicationStatus** |  |  [optional] |
|**typeName** | **String** | The application type name as defined in the application manifest. |  [optional] |
|**typeVersion** | **String** | The version of the application type as defined in the application manifest. |  [optional] |



