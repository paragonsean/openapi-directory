

# GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkup

Fields for an individual `ClaimReview` element. Except for sub-messages that group fields together, each of these fields correspond those in https://schema.org/ClaimReview. We list the precise mapping for each field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**claimAppearances** | **List&lt;String&gt;** | A list of links to works in which this claim appears, aside from the one specified in &#x60;claim_first_appearance&#x60;. Corresponds to &#x60;ClaimReview.itemReviewed[@type&#x3D;Claim].appearance.url&#x60;. |  [optional] |
|**claimAuthor** | [**GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthor**](GoogleFactcheckingFactchecktoolsV1alpha1ClaimAuthor.md) |  |  [optional] |
|**claimDate** | **String** | The date when the claim was made or entered public discourse. Corresponds to &#x60;ClaimReview.itemReviewed.datePublished&#x60;. |  [optional] |
|**claimFirstAppearance** | **String** | A link to a work in which this claim first appears. Corresponds to &#x60;ClaimReview.itemReviewed[@type&#x3D;Claim].firstAppearance.url&#x60;. |  [optional] |
|**claimLocation** | **String** | The location where this claim was made. Corresponds to &#x60;ClaimReview.itemReviewed.name&#x60;. |  [optional] |
|**claimReviewed** | **String** | A short summary of the claim being evaluated. Corresponds to &#x60;ClaimReview.claimReviewed&#x60;. |  [optional] |
|**rating** | [**GoogleFactcheckingFactchecktoolsV1alpha1ClaimRating**](GoogleFactcheckingFactchecktoolsV1alpha1ClaimRating.md) |  |  [optional] |
|**url** | **String** | This field is optional, and will default to the page URL. We provide this field to allow you the override the default value, but the only permitted override is the page URL plus an optional anchor link (\&quot;page jump\&quot;). Corresponds to &#x60;ClaimReview.url&#x60; |  [optional] |



