

# GoogleFirebaseFcmDataV1beta1AndroidDeliveryData

Message delivery data for a given date, app, and analytics label combination.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**analyticsLabel** | **String** | The analytics label associated with the messages sent. All messages sent without an analytics label will be grouped together in a single entry. |  [optional] |
|**appId** | **String** | The app ID to which the messages were sent. |  [optional] |
|**data** | [**GoogleFirebaseFcmDataV1beta1Data**](GoogleFirebaseFcmDataV1beta1Data.md) |  |  [optional] |
|**date** | [**GoogleTypeDate**](GoogleTypeDate.md) |  |  [optional] |



