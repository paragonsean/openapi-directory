# SessionsApi.LoginRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extended** | **Boolean** | Whether extended login or normal login is required. If the parameter is set to Y your application will generate an authentication ticket valid for a period of 60 days, without expiring due to inactivity. If the parameter is left blank or set to N this means your application will support the normal expiry times for tickets: The ticket expires after 2 hours of inactivity. The ticket is valid for a maximum of 8 hours after it has been issued. | [optional] [default to false]
**password** | **String** | Customer Password | 
**username** | **String** | Customer Username | 


