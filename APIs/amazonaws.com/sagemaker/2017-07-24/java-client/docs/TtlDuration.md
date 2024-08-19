

# TtlDuration

Time to live duration, where the record is hard deleted after the expiration time is reached; <code>ExpiresAt</code> = <code>EventTime</code> + <code>TtlDuration</code>. For information on HardDelete, see the <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html\">DeleteRecord</a> API in the Amazon SageMaker API Reference guide.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**unit** | [**TtlDurationUnit**](TtlDurationUnit.md) |  |  [optional] |
|**value** | [**Integer**](Integer.md) |  |  [optional] |



