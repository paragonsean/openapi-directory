

# UpdateConfiguration

<p>Contains an updated configuration to replace the configuration in an existing identity source.</p> <note> <p>At this time, the only valid member of this structure is a Amazon Cognito user pool configuration.</p> <p>You must specify a <code>userPoolArn</code>, and optionally, a <code>ClientId</code>.</p> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cognitoUserPoolConfiguration** | [**UpdateConfigurationCognitoUserPoolConfiguration**](UpdateConfigurationCognitoUserPoolConfiguration.md) |  |  [optional] |



