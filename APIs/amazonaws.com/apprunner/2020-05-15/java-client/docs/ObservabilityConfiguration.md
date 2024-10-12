

# ObservabilityConfiguration

<p>Describes an App Runner observability configuration resource. Multiple revisions of a configuration have the same <code>ObservabilityConfigurationName</code> and different <code>ObservabilityConfigurationRevision</code> values.</p> <p>The resource is designed to configure multiple features (currently one feature, tracing). This type contains optional members that describe the configuration of these features (currently one member, <code>TraceConfiguration</code>). If a feature member isn't specified, the feature isn't enabled.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**observabilityConfigurationArn** | [**String**](String.md) |  |  [optional] |
|**observabilityConfigurationName** | [**String**](String.md) |  |  [optional] |
|**traceConfiguration** | [**ObservabilityConfigurationTraceConfiguration**](ObservabilityConfigurationTraceConfiguration.md) |  |  [optional] |
|**observabilityConfigurationRevision** | [**Integer**](Integer.md) |  |  [optional] |
|**latest** | [**Boolean**](Boolean.md) |  |  [optional] |
|**status** | [**ObservabilityConfigurationStatus**](ObservabilityConfigurationStatus.md) |  |  [optional] |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**deletedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



