# MarketingApi.DeleteAdResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adId** | **String** | The unique identifier of the ad that was deleted, or the ad that the seller attempted to delete. | [optional] 
**errors** | [**[Error]**](Error.md) | An array of the errors or warnings associated with the request. | [optional] 
**listingId** | **String** | A unique eBay-assigned ID for a listing that is generated when the listing is created. | [optional] 
**statusCode** | **Number** | An HTTP status code that indicates the response-status of the request. Check this code to see if the ad was successfully deleted.&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt;A status code is returned for each ad that the seller deletes, or attempts to delete.&lt;/span&gt; | [optional] 


