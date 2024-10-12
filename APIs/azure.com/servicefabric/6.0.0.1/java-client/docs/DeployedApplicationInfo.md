

# DeployedApplicationInfo

Information about application deployed on the node.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The identity of the application. This is an encoded representation of the application name. This is used in the REST APIs to identify the application resource.   Starting in version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric://myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions.  |  [optional] |
|**logDirectory** | **String** | The log directory of the application on the node. The log directory can be used to store application logs. |  [optional] |
|**name** | **String** | The name of the application, including the &#39;fabric:&#39; URI scheme. |  [optional] |
|**status** | **DeployedApplicationStatus** |  |  [optional] |
|**tempDirectory** | **String** | The temp directory of the application on the node. The code packages belonging to the application are forked with this directory set as their temporary directory. |  [optional] |
|**typeName** | **String** | The application type name as defined in the application manifest. |  [optional] |
|**workDirectory** | **String** | The work directory of the application on the node. The work directory can be used to store application data. |  [optional] |



