

# ContaineranalysisGoogleDevtoolsCloudbuildV1SecretManagerSecret

Pairs a secret environment variable with a SecretVersion in Secret Manager.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**env** | **String** | Environment variable name to associate with the secret. Secret environment variables must be unique across all of a build&#39;s secrets, and must be used by at least one build step. |  [optional] |
|**versionName** | **String** | Resource name of the SecretVersion. In format: projects/_*_/secrets/_*_/versions/_* |  [optional] |



