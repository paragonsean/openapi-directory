

# GoogleAdsSearchads360V0ResourcesConversionTrackingSetting

A collection of customer-wide settings related to Search Ads 360 Conversion Tracking.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptedCustomerDataTerms** | **Boolean** | Output only. Whether the customer has accepted customer data terms. If using cross-account conversion tracking, this value is inherited from the manager. This field is read-only. For more information, see https://support.google.com/adspolicy/answer/7475709. |  [optional] [readonly] |
|**conversionTrackingId** | **String** | Output only. The conversion tracking id used for this account. This id doesn&#39;t indicate whether the customer uses conversion tracking (conversion_tracking_status does). This field is read-only. |  [optional] [readonly] |
|**conversionTrackingStatus** | [**ConversionTrackingStatusEnum**](#ConversionTrackingStatusEnum) | Output only. Conversion tracking status. It indicates whether the customer is using conversion tracking, and who is the conversion tracking owner of this customer. If this customer is using cross-account conversion tracking, the value returned will differ based on the &#x60;login-customer-id&#x60; of the request. |  [optional] [readonly] |
|**crossAccountConversionTrackingId** | **String** | Output only. The conversion tracking id of the customer&#39;s manager. This is set when the customer is opted into cross-account conversion tracking, and it overrides conversion_tracking_id. |  [optional] [readonly] |
|**enhancedConversionsForLeadsEnabled** | **Boolean** | Output only. Whether the customer is opted-in for enhanced conversions for leads. If using cross-account conversion tracking, this value is inherited from the manager. This field is read-only. |  [optional] [readonly] |
|**googleAdsConversionCustomer** | **String** | Output only. The resource name of the customer where conversions are created and managed. This field is read-only. |  [optional] [readonly] |
|**googleAdsCrossAccountConversionTrackingId** | **String** | Output only. The conversion tracking id of the customer&#39;s manager. This is set when the customer is opted into conversion tracking, and it overrides conversion_tracking_id. This field can only be managed through the Google Ads UI. This field is read-only. |  [optional] [readonly] |



## Enum: ConversionTrackingStatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| NOT_CONVERSION_TRACKED | &quot;NOT_CONVERSION_TRACKED&quot; |
| CONVERSION_TRACKING_MANAGED_BY_SELF | &quot;CONVERSION_TRACKING_MANAGED_BY_SELF&quot; |
| CONVERSION_TRACKING_MANAGED_BY_THIS_MANAGER | &quot;CONVERSION_TRACKING_MANAGED_BY_THIS_MANAGER&quot; |
| CONVERSION_TRACKING_MANAGED_BY_ANOTHER_MANAGER | &quot;CONVERSION_TRACKING_MANAGED_BY_ANOTHER_MANAGER&quot; |



