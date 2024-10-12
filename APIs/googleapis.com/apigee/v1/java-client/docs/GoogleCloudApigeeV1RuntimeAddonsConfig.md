

# GoogleCloudApigeeV1RuntimeAddonsConfig

RuntimeAddonsConfig defines the runtime configurations for add-ons in an environment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**analyticsConfig** | [**GoogleCloudApigeeV1RuntimeAnalyticsConfig**](GoogleCloudApigeeV1RuntimeAnalyticsConfig.md) |  |  [optional] |
|**apiSecurityConfig** | [**GoogleCloudApigeeV1RuntimeApiSecurityConfig**](GoogleCloudApigeeV1RuntimeApiSecurityConfig.md) |  |  [optional] |
|**name** | **String** | Name of the addons config in the format: &#x60;organizations/{org}/environments/{env}/addonsConfig&#x60; |  [optional] |
|**revisionId** | **String** | Revision number used by the runtime to detect config changes. |  [optional] |
|**uid** | **String** | UID is to detect if config is recreated after deletion. The add-on config will only be deleted when the environment itself gets deleted, thus it will always be the same as the UID of EnvironmentConfig. |  [optional] |



