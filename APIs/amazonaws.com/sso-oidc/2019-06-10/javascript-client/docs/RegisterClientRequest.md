# AwsSsoOidc.RegisterClientRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientName** | **String** | The friendly name of the client. | 
**clientType** | **String** | The type of client. The service supports only &lt;code&gt;public&lt;/code&gt; as a client type. Anything other than public will be rejected by the service. | 
**scopes** | **[String]** | The list of scopes that are defined by the client. Upon authorization, this list is used to restrict permissions when granting an access token. | [optional] 


