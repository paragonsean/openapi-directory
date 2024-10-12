

# GoogleCloudRetailV2betaFulfillmentInfo

Fulfillment information, such as the store IDs for in-store pickup or region IDs for different shipping methods.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**placeIds** | **List&lt;String&gt;** | The IDs for this type, such as the store IDs for FulfillmentInfo.type.pickup-in-store or the region IDs for FulfillmentInfo.type.same-day-delivery. A maximum of 3000 values are allowed. Each value must be a string with a length limit of 30 characters, matching the pattern &#x60;[a-zA-Z0-9_-]+&#x60;, such as \&quot;store1\&quot; or \&quot;REGION-2\&quot;. Otherwise, an INVALID_ARGUMENT error is returned. |  [optional] |
|**type** | **String** | The fulfillment type, including commonly used types (such as pickup in store and same day delivery), and custom types. Customers have to map custom types to their display names before rendering UI. Supported values: * \&quot;pickup-in-store\&quot; * \&quot;ship-to-store\&quot; * \&quot;same-day-delivery\&quot; * \&quot;next-day-delivery\&quot; * \&quot;custom-type-1\&quot; * \&quot;custom-type-2\&quot; * \&quot;custom-type-3\&quot; * \&quot;custom-type-4\&quot; * \&quot;custom-type-5\&quot; If this field is set to an invalid value other than these, an INVALID_ARGUMENT error is returned. |  [optional] |



