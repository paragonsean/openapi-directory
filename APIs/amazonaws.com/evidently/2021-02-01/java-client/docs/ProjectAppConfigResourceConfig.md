

# ProjectAppConfigResourceConfig

<p>Use this parameter to configure client-side evaluation for your project. Client-side evaluation allows your application to assign variations to user sessions locally instead of by calling the <a href=\"https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_EvaluateFeature.html\">EvaluateFeature</a> operation to assign the variations. This mitigates the latency and availability risks that come with an API call.</p> <p> <code>ProjectAppConfigResource</code> is a structure that defines the configuration of how your application integrates with AppConfig to run client-side evaluation.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationId** | [**String**](String.md) |  |  [optional] |
|**environmentId** | [**String**](String.md) |  |  [optional] |



