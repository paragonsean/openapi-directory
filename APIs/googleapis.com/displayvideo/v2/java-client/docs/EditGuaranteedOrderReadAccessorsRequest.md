

# EditGuaranteedOrderReadAccessorsRequest

Request message for GuaranteedOrderService.EditGuaranteedOrderReadAccessors.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addedAdvertisers** | **List&lt;String&gt;** | The advertisers to add as read accessors to the guaranteed order. |  [optional] |
|**partnerId** | **String** | Required. The partner context in which the change is being made. |  [optional] |
|**readAccessInherited** | **Boolean** | Whether to give all advertisers of the read/write accessor partner read access to the guaranteed order. Only applicable if read_write_partner_id is set in the guaranteed order. |  [optional] |
|**removedAdvertisers** | **List&lt;String&gt;** | The advertisers to remove as read accessors to the guaranteed order. |  [optional] |



