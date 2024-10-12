# DisplayVideo360Api.EditGuaranteedOrderReadAccessorsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addedAdvertisers** | **[String]** | The advertisers to add as read accessors to the guaranteed order. | [optional] 
**partnerId** | **String** | Required. The partner context in which the change is being made. | [optional] 
**readAccessInherited** | **Boolean** | Whether to give all advertisers of the read/write accessor partner read access to the guaranteed order. Only applicable if read_write_partner_id is set in the guaranteed order. | [optional] 
**removedAdvertisers** | **[String]** | The advertisers to remove as read accessors to the guaranteed order. | [optional] 


