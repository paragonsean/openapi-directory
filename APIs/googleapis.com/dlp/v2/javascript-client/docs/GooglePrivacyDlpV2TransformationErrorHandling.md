# SensitiveDataProtectionDlp.GooglePrivacyDlpV2TransformationErrorHandling

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leaveUntransformed** | **Object** | Skips the data without modifying it if the requested transformation would cause an error. For example, if a &#x60;DateShift&#x60; transformation were applied an an IP address, this mode would leave the IP address unchanged in the response. | [optional] 
**throwError** | **Object** | Throw an error and fail the request when a transformation error occurs. | [optional] 


