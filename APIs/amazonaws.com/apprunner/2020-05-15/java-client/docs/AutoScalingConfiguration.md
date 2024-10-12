

# AutoScalingConfiguration

<p>Describes an App Runner automatic scaling configuration resource.</p> <p>A higher <code>MinSize</code> increases the spread of your App Runner service over more Availability Zones in the Amazon Web Services Region. The tradeoff is a higher minimal cost.</p> <p>A lower <code>MaxSize</code> controls your cost. The tradeoff is lower responsiveness during peak demand.</p> <p>Multiple revisions of a configuration might have the same <code>AutoScalingConfigurationName</code> and different <code>AutoScalingConfigurationRevision</code> values.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoScalingConfigurationArn** | [**String**](String.md) |  |  [optional] |
|**autoScalingConfigurationName** | [**String**](String.md) |  |  [optional] |
|**autoScalingConfigurationRevision** | [**Integer**](Integer.md) |  |  [optional] |
|**latest** | [**Boolean**](Boolean.md) |  |  [optional] |
|**status** | [**AutoScalingConfigurationStatus**](AutoScalingConfigurationStatus.md) |  |  [optional] |
|**maxConcurrency** | [**Integer**](Integer.md) |  |  [optional] |
|**minSize** | [**Integer**](Integer.md) |  |  [optional] |
|**maxSize** | [**Integer**](Integer.md) |  |  [optional] |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**deletedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



