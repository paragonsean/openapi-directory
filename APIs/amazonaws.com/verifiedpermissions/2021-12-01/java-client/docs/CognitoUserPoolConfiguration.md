

# CognitoUserPoolConfiguration

<p>The configuration for an identity source that represents a connection to an Amazon Cognito user pool used as an identity provider for Verified Permissions.</p> <p>This data type is used as a field that is part of an <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_Configuration.html\">Configuration</a> structure that is used as a parameter to the <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_Configuration.html\">Configuration</a>.</p> <p>Example:<code>\"CognitoUserPoolConfiguration\":{\"UserPoolArn\":\"arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_1a2b3c4d5\",\"ClientIds\": [\"a1b2c3d4e5f6g7h8i9j0kalbmc\"]}</code> </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**userPoolArn** | [**String**](String.md) |  |  |
|**clientIds** | [**List**](List.md) |  |  [optional] |



