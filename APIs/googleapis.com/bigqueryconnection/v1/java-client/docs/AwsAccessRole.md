

# AwsAccessRole

Authentication method for Amazon Web Services (AWS) that uses Google owned Google service account to assume into customer's AWS IAM Role.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**iamRoleId** | **String** | The user’s AWS IAM Role that trusts the Google-owned AWS IAM user Connection. |  [optional] |
|**identity** | **String** | A unique Google-owned and Google-generated identity for the Connection. This identity will be used to access the user&#39;s AWS IAM Role. |  [optional] |



