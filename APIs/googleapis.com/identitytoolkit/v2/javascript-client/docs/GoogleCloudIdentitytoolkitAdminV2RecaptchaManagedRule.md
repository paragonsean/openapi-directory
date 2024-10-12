# IdentityToolkitApi.GoogleCloudIdentitytoolkitAdminV2RecaptchaManagedRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | The action taken if the reCAPTCHA score of a request is within the interval [start_score, end_score]. | [optional] 
**endScore** | **Number** | The end score (inclusive) of the score range for an action. Must be a value between 0.0 and 1.0, at 11 discrete values; e.g. 0, 0.1, 0.2, 0.3, ... 0.9, 1.0. A score of 0.0 indicates the riskiest request (likely a bot), whereas 1.0 indicates the safest request (likely a human). See https://cloud.google.com/recaptcha-enterprise/docs/interpret-assessment. | [optional] 



## Enum: ActionEnum


* `RECAPTCHA_ACTION_UNSPECIFIED` (value: `"RECAPTCHA_ACTION_UNSPECIFIED"`)

* `BLOCK` (value: `"BLOCK"`)




