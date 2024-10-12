# ContentApiForShopping.AccountAdwordsLink

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adwordsId** | **String** | Customer ID of the AdWords account. | [optional] 
**status** | **String** | Status of the link between this Merchant Center account and the AdWords account. Upon retrieval, it represents the actual status of the link and can be either &#x60;active&#x60; if it was approved in Google AdWords or &#x60;pending&#x60; if it&#39;s pending approval. Upon insertion, it represents the *intended* status of the link. Re-uploading a link with status &#x60;active&#x60; when it&#39;s still pending or with status &#x60;pending&#x60; when it&#39;s already active will have no effect: the status will remain unchanged. Re-uploading a link with deprecated status &#x60;inactive&#x60; is equivalent to not submitting the link at all and will delete the link if it was active or cancel the link request if it was pending. Acceptable values are: - \&quot;&#x60;active&#x60;\&quot; - \&quot;&#x60;pending&#x60;\&quot;  | [optional] 


