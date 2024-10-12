

# SslConfiguration

SSL configuration. If configured data-plane calls to user services will be exposed over SSL only.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cert** | **String** | The SSL cert data in PEM format. |  [optional] |
|**cname** | **String** | The CName of the certificate. |  [optional] |
|**key** | **String** | The SSL key data in PEM format. This is not returned in response of GET/PUT on the resource. To see this please call listKeys API. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | SSL status. Allowed values are Enabled and Disabled. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



