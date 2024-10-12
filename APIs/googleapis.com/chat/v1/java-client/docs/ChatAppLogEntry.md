

# ChatAppLogEntry

JSON payload of error messages. If the Cloud Logging API is enabled, these error messages are logged to [Google Cloud Logging](https://cloud.google.com/logging/docs).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deployment** | **String** | The deployment that caused the error. For Chat apps built in Apps Script, this is the deployment ID defined by Apps Script. |  [optional] |
|**deploymentFunction** | **String** | The unencrypted &#x60;callback_method&#x60; name that was running when the error was encountered. |  [optional] |
|**error** | [**Status**](Status.md) |  |  [optional] |



