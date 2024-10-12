# VertexAiSearchForRetailApi.GoogleCloudRetailV2betaRemoveFulfillmentPlacesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowMissing** | **Boolean** | If set to true, and the Product is not found, the fulfillment information will still be processed and retained for at most 1 day and processed once the Product is created. If set to false, a NOT_FOUND error is returned if the Product is not found. | [optional] 
**placeIds** | **[String]** | Required. The IDs for this type, such as the store IDs for \&quot;pickup-in-store\&quot; or the region IDs for \&quot;same-day-delivery\&quot;, to be removed for this type. At least 1 value is required, and a maximum of 2000 values are allowed. Each value must be a string with a length limit of 10 characters, matching the pattern &#x60;[a-zA-Z0-9_-]+&#x60;, such as \&quot;store1\&quot; or \&quot;REGION-2\&quot;. Otherwise, an INVALID_ARGUMENT error is returned. | [optional] 
**removeTime** | **String** | The time when the fulfillment updates are issued, used to prevent out-of-order updates on fulfillment information. If not provided, the internal system time will be used. | [optional] 
**type** | **String** | Required. The fulfillment type, including commonly used types (such as pickup in store and same day delivery), and custom types. Supported values: * \&quot;pickup-in-store\&quot; * \&quot;ship-to-store\&quot; * \&quot;same-day-delivery\&quot; * \&quot;next-day-delivery\&quot; * \&quot;custom-type-1\&quot; * \&quot;custom-type-2\&quot; * \&quot;custom-type-3\&quot; * \&quot;custom-type-4\&quot; * \&quot;custom-type-5\&quot; If this field is set to an invalid value other than these, an INVALID_ARGUMENT error is returned. This field directly corresponds to Product.fulfillment_info.type. | [optional] 


