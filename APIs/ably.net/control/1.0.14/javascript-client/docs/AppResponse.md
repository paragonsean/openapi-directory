# ControlApiV1.AppResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **Object** | A link self-referencing the app that has been created. | [optional] 
**accountId** | **String** | The ID of your Ably account. | [optional] 
**apnsUseSandboxEndpoint** | **Boolean** | Apple Push Notification service endpoint. | [optional] 
**id** | **String** | The application ID. | [optional] 
**name** | **String** | The application name. | [optional] 
**status** | **String** | The application status. Disabled applications will not accept new connections and will return an error to all clients. | [optional] 
**tlsOnly** | **Boolean** | Enforce TLS for all connections. This setting overrides any channel setting. | [optional] 



## Enum: StatusEnum


* `enabled` (value: `"enabled"`)

* `disabled` (value: `"disabled"`)




