

# CreateServiceNetworkServiceAssociationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren&#39;t identical, the retry fails. |  [optional] |
|**serviceIdentifier** | **String** | The ID or Amazon Resource Name (ARN) of the service. |  |
|**serviceNetworkIdentifier** | **String** | The ID or Amazon Resource Name (ARN) of the service network. You must use the ARN if the resources specified in the operation are in different accounts. |  |
|**tags** | **Map&lt;String, String&gt;** | The tags for the association. |  [optional] |



