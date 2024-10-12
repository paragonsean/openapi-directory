# TwilioNumbers.NumbersV1BulkEligibility

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dateCompleted** | **Date** |  | [optional] 
**dateCreated** | **Date** |  | [optional] 
**friendlyName** | **String** | This is the string that you assigned as a friendly name for describing the eligibility check request. | [optional] 
**requestId** | **String** | The SID of the bulk eligibility check that you want to know about. | [optional] 
**results** | **[Object]** | The result set that contains the eligibility check response for each requested number, each result has at least the following attributes:  phone_number: The requested phone number ,hosting_account_sid: The account sid where the phone number will be hosted, country: Phone number’s country, eligibility_status: Indicates the eligibility status of the PN (Eligible/Ineligible), eligibility_sub_status: Indicates the sub status of the eligibility , ineligibility_reason: Reason for number&#39;s ineligibility (if applicable), next_step: Suggested next step in the hosting process based on the eligibility status. | [optional] 
**status** | **String** | This is the status of the bulk eligibility check request. (Example: COMPLETE, IN_PROGRESS) | [optional] 
**url** | **String** | This is the url of the request that you&#39;re trying to reach out to locate the resource. | [optional] 


