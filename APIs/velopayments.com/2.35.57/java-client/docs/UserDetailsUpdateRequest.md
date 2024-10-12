

# UserDetailsUpdateRequest

<p>All properties are optional</p> <p>Only provided properties will be updated</p> <p>Use null to null out a property that is allowed to be nullable</p> 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** | the email address of the user |  [optional] |
|**firstName** | **String** |  |  [optional] |
|**lastName** | **String** |  |  [optional] |
|**mfaType** | **MFAType** |  |  [optional] |
|**primaryContactNumber** | **String** | The main contact number for the user  |  [optional] |
|**secondaryContactNumber** | **String** | The secondary contact number for the user  |  [optional] |
|**smsNumber** | **String** | The phone number of a device that the user can receive sms messages on  |  [optional] |
|**verificationCode** | **String** | &lt;p&gt;Optional property that MUST be suppied when manually verifying a user&lt;/p&gt; &lt;p&gt;The user&#39;s smsNumber is registered via a separate endpoint and an OTP sent to them&lt;/p&gt;  |  [optional] |



