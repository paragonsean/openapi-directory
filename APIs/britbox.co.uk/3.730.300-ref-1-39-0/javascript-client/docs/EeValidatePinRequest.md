# RocketServices.EeValidatePinRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | **String** | EE API authorization Token received from GET /ee/token/create. | 
**pin** | **String** | The pin entered by a user. 6 digits | 
**pinReference** | **String** | The pinReference. | 
**trackingHeader** | **String** | Tracking header to be able to search logs for a specific user requests. If not provided it will be generated. FE should store it for later user. | [optional] 


