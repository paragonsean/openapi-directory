

# GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPage

Holds one or more instances of `ClaimReview` markup for a webpage.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**claimReviewAuthor** | [**GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthor**](GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewAuthor.md) |  |  [optional] |
|**claimReviewMarkups** | [**List&lt;GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkup&gt;**](GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkup.md) | A list of individual claim reviews for this page. Each item in the list corresponds to one &#x60;ClaimReview&#x60; element. |  [optional] |
|**name** | **String** | The name of this &#x60;ClaimReview&#x60; markup page resource, in the form of &#x60;pages/{page_id}&#x60;. Except for update requests, this field is output-only and should not be set by the user. |  [optional] |
|**pageUrl** | **String** | The URL of the page associated with this &#x60;ClaimReview&#x60; markup. While every individual &#x60;ClaimReview&#x60; has its own URL field, semantically this is a page-level field, and each &#x60;ClaimReview&#x60; on this page will use this value unless individually overridden. Corresponds to &#x60;ClaimReview.url&#x60; |  [optional] |
|**publishDate** | **String** | The date when the fact check was published. Similar to the URL, semantically this is a page-level field, and each &#x60;ClaimReview&#x60; on this page will contain the same value. Corresponds to &#x60;ClaimReview.datePublished&#x60; |  [optional] |
|**versionId** | **String** | The version ID for this markup. Except for update requests, this field is output-only and should not be set by the user. |  [optional] |



