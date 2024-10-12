# MarketingApi.AdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adGroupId** | **String** | A unique eBay-assigned ID for an ad group in a Promoted Listings Advanced (PLA) campaign that uses the Cost Per Click (CPC) funding model.&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This field will always be returned for  campaigns that use the CPC funding model. It will not be returned for campaigns that use the Cost Per Sale (CPS) funding model.&lt;/span&gt; | [optional] 
**adId** | **String** | A unique eBay-assigned ID for an ad. This ID is generated when an ad is created.&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt;This field is only returned when an ad is successfully created for the corresponding listing.&lt;/span&gt; | [optional] 
**errors** | [**[Error]**](Error.md) | An array of errors associated with the request. | [optional] 
**href** | **String** | The getAd URI that points to the ad.&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt;This field is only returned when an ad is successfully created for the corresponding listing.&lt;/span&gt; | [optional] 
**listingId** | **String** | A unique eBay-assigned ID for a listing that is generated when the listing is created. | [optional] 
**statusCode** | **Number** | An HTTP status code indicating if the corresponding ad was successfully created or not. &lt;code&gt;200 Successful&lt;/code&gt; should be returned for successfully created ads.&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt;A status code is returned for each ad that the seller creates, or attempts to create.&lt;/span&gt; | [optional] 


