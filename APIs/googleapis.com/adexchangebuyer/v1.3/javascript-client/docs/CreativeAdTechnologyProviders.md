# AdExchangeBuyerApi.CreativeAdTechnologyProviders

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detectedProviderIds** | **[String]** | The detected ad technology provider IDs for this creative. See https://storage.googleapis.com/adx-rtb-dictionaries/providers.csv for mapping of provider ID to provided name, a privacy policy URL, and a list of domains which can be attributed to the provider. If this creative contains provider IDs that are outside of those listed in the &#x60;BidRequest.adslot.consented_providers_settings.consented_providers&#x60; field on the  Authorized Buyers Real-Time Bidding protocol or the &#x60;BidRequest.user.ext.consented_providers_settings.consented_providers&#x60; field on the OpenRTB protocol, a bid submitted for a European Economic Area (EEA) user with this creative is not compliant with the GDPR policies as mentioned in the \&quot;Third-party Ad Technology Vendors\&quot; section of Authorized Buyers Program Guidelines. | [optional] 
**hasUnidentifiedProvider** | **Boolean** | Whether the creative contains an unidentified ad technology provider. If true, a bid submitted for a European Economic Area (EEA) user with this creative is not compliant with the GDPR policies as mentioned in the \&quot;Third-party Ad Technology Vendors\&quot; section of Authorized Buyers Program Guidelines. | [optional] 


