

# ApiManagementServiceUpdateHostnameParameters

Parameters supplied to the UpdateHostname operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**delete** | [**List&lt;DeleteEnum&gt;**](#List&lt;DeleteEnum&gt;) | Hostnames types to delete. |  [optional] |
|**update** | [**List&lt;HostnameConfiguration&gt;**](HostnameConfiguration.md) | Hostnames to create or update. |  [optional] |



## Enum: List&lt;DeleteEnum&gt;

| Name | Value |
|---- | -----|
| PROXY | &quot;Proxy&quot; |
| PORTAL | &quot;Portal&quot; |
| MANAGEMENT | &quot;Management&quot; |
| SCM | &quot;Scm&quot; |



