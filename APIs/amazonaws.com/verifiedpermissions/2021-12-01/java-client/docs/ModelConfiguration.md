

# ModelConfiguration

<p>Contains configuration information used when creating a new identity source.</p> <note> <p>At this time, the only valid member of this structure is a Amazon Cognito user pool configuration.</p> <p>You must specify a <code>userPoolArn</code>, and optionally, a <code>ClientId</code>.</p> </note> <p>This data type is used as a request parameter for the <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreateIdentitySource.html\">CreateIdentitySource</a> operation.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cognitoUserPoolConfiguration** | [**ConfigurationCognitoUserPoolConfiguration**](ConfigurationCognitoUserPoolConfiguration.md) |  |  [optional] |



