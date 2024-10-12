# ControlApiV1.AppPatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apnsCertificate** | **String** | The Apple Push Notification service certificate. | [optional] 
**apnsPrivateKey** | **String** | The Apple Push Notification service private key. | [optional] 
**apnsUseSandboxEndpoint** | **Boolean** | The Apple Push Notification service sandbox endpoint. | [optional] 
**fcmKey** | **String** | The Firebase Cloud Messaging key. | [optional] 
**name** | **String** | The name of the application for your reference only. | [optional] 
**status** | **String** | The status of the application. Can be &#x60;enabled&#x60; or &#x60;disabled&#x60;. Enabled means available to accept inbound connections and all services are available. | [optional] 
**tlsOnly** | **Boolean** | Enforce TLS for all connections. | [optional] 



## Enum: StatusEnum


* `enabled` (value: `"enabled"`)

* `disabled` (value: `"disabled"`)




