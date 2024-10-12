

# CreateEmailIdentityResponse

<p>If the email identity is a domain, this object contains tokens that you can use to create a set of CNAME records. To sucessfully verify your domain, you have to add these records to the DNS configuration for your domain.</p> <p>If the email identity is an email address, this object is empty. </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**identityType** | [**IdentityType**](IdentityType.md) |  |  [optional] |
|**verifiedForSendingStatus** | [**Boolean**](Boolean.md) |  |  [optional] |
|**dkimAttributes** | [**CreateEmailIdentityResponseDkimAttributes**](CreateEmailIdentityResponseDkimAttributes.md) |  |  [optional] |



