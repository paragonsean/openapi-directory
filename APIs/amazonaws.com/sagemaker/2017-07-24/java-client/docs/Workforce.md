

# Workforce

A single private workforce, which is automatically created when you create your first private work team. You can create one private work force in each Amazon Web Services Region. By default, any workforce-related API operation used in a specific region will apply to the workforce created in that region. To learn how to create a private workforce, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-create-private.html\">Create a Private Workforce</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**workforceName** | [**String**](String.md) |  |  |
|**workforceArn** | [**String**](String.md) |  |  |
|**lastUpdatedDate** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**sourceIpConfig** | [**WorkforceSourceIpConfig**](WorkforceSourceIpConfig.md) |  |  [optional] |
|**subDomain** | [**String**](String.md) |  |  [optional] |
|**cognitoConfig** | [**WorkforceCognitoConfig**](WorkforceCognitoConfig.md) |  |  [optional] |
|**oidcConfig** | [**WorkforceOidcConfig**](WorkforceOidcConfig.md) |  |  [optional] |
|**createDate** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**workforceVpcConfig** | [**WorkforceWorkforceVpcConfig**](WorkforceWorkforceVpcConfig.md) |  |  [optional] |
|**status** | [**WorkforceStatus**](WorkforceStatus.md) |  |  [optional] |
|**failureReason** | [**String**](String.md) |  |  [optional] |



