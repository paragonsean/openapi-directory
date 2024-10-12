# AndroidDeviceProvisioningPartnerApi.Dpc

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dpcName** | **String** | Output only. The title of the DPC app in Google Play. For example, _Google Apps Device Policy_. Useful in an application&#39;s user interface. | [optional] [readonly] 
**name** | **String** | Output only. The API resource name in the format &#x60;customers/[CUSTOMER_ID]/dpcs/[DPC_ID]&#x60;. Assigned by the server. To maintain a reference to a DPC across customer accounts, persist and match the last path component (&#x60;DPC_ID&#x60;). | [optional] [readonly] 
**packageName** | **String** | Output only. The DPC&#39;s Android application ID that looks like a Java package name. Zero-touch enrollment installs the DPC app onto a device using this identifier. | [optional] [readonly] 


