

# CreateEmailIdentityResponse

<p>If the email identity is a domain, this object contains information about the DKIM verification status for the domain.</p> <p>If the email identity is an email address, this object is empty. </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**identityType** | [**IdentityType**](IdentityType.md) |  |  [optional] |
|**verifiedForSendingStatus** | [**Boolean**](Boolean.md) |  |  [optional] |
|**dkimAttributes** | [**CreateEmailIdentityResponseDkimAttributes**](CreateEmailIdentityResponseDkimAttributes.md) |  |  [optional] |



