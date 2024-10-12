

# ShippingsettingsCustomBatchRequestEntry

A batch entry encoding a single non-batch shippingsettings request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The ID of the account for which to get/update account shipping settings. |  [optional] |
|**batchId** | **Integer** | An entry ID, unique within the batch request. |  [optional] |
|**merchantId** | **String** | The ID of the managing account. |  [optional] |
|**method** | **String** | The method of the batch entry. Acceptable values are: - \&quot;&#x60;get&#x60;\&quot; - \&quot;&#x60;update&#x60;\&quot;  |  [optional] |
|**shippingSettings** | [**ShippingSettings**](ShippingSettings.md) |  |  [optional] |



