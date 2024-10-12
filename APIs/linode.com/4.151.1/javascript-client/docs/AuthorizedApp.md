# LinodeApi.AuthorizedApp

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Date** | When this app was authorized. | [optional] [readonly] 
**expiry** | **Date** | When the app&#39;s access to your account expires. If &#x60;null&#x60;, the app&#39;s access must be revoked manually.  | [optional] [readonly] 
**id** | **Number** | This authorization&#39;s ID, used for revoking access.  | [optional] [readonly] 
**label** | **String** | The name of the application you&#39;ve authorized.  | [optional] [readonly] 
**scopes** | **String** | The OAuth scopes this app was authorized with.  This defines what parts of your Account the app is allowed to access.  | [optional] [readonly] 
**thumbnailUrl** | **String** | The URL at which this app&#39;s thumbnail may be accessed.  | [optional] [readonly] 
**website** | **String** | The website where you can get more information about this app.  | [optional] [readonly] 


