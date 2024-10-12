

# BulkEditPartnerAssignedTargetingOptionsRequest

Request message for BulkEditPartnerAssignedTargetingOptions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createRequests** | [**List&lt;CreateAssignedTargetingOptionsRequest&gt;**](CreateAssignedTargetingOptionsRequest.md) | The assigned targeting options to create in batch, specified as a list of &#x60;CreateAssignedTargetingOptionsRequest&#x60;. Supported targeting types: * &#x60;TARGETING_TYPE_CHANNEL&#x60; |  [optional] |
|**deleteRequests** | [**List&lt;DeleteAssignedTargetingOptionsRequest&gt;**](DeleteAssignedTargetingOptionsRequest.md) | The assigned targeting options to delete in batch, specified as a list of &#x60;DeleteAssignedTargetingOptionsRequest&#x60;. Supported targeting types: * &#x60;TARGETING_TYPE_CHANNEL&#x60; |  [optional] |



