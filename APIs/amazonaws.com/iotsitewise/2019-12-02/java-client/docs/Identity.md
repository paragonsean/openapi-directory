

# Identity

<p>Contains an identity that can access an IoT SiteWise Monitor resource.</p> <note> <p>Currently, you can't use Amazon Web Services APIs to retrieve IAM Identity Center identity IDs. You can find the IAM Identity Center identity IDs in the URL of user and group pages in the <a href=\"https://console.aws.amazon.com/singlesignon\">IAM Identity Center console</a>.</p> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**user** | [**CreateAccessPolicyRequestAccessPolicyIdentityUser**](CreateAccessPolicyRequestAccessPolicyIdentityUser.md) |  |  [optional] |
|**group** | [**CreateAccessPolicyRequestAccessPolicyIdentityGroup**](CreateAccessPolicyRequestAccessPolicyIdentityGroup.md) |  |  [optional] |
|**iamUser** | [**CreateAccessPolicyRequestAccessPolicyIdentityIamUser**](CreateAccessPolicyRequestAccessPolicyIdentityIamUser.md) |  |  [optional] |
|**iamRole** | [**CreateAccessPolicyRequestAccessPolicyIdentityIamRole**](CreateAccessPolicyRequestAccessPolicyIdentityIamRole.md) |  |  [optional] |



