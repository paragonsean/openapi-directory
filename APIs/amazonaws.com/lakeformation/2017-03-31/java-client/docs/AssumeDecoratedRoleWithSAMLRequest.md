

# AssumeDecoratedRoleWithSAMLRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**saMLAssertion** | **String** | A SAML assertion consisting of an assertion statement for the user who needs temporary credentials. This must match the SAML assertion that was issued to IAM. This must be Base64 encoded. |  |
|**roleArn** | **String** | The role that represents an IAM principal whose scope down policy allows it to call credential vending APIs such as &lt;code&gt;GetTemporaryTableCredentials&lt;/code&gt;. The caller must also have iam:PassRole permission on this role.  |  |
|**principalArn** | **String** | The Amazon Resource Name (ARN) of the SAML provider in IAM that describes the IdP. |  |
|**durationSeconds** | **Integer** | The time period, between 900 and 43,200 seconds, for the timeout of the temporary credentials. |  [optional] |



