

# PublisherProfile

Represents a publisher profile (https://support.google.com/admanager/answer/6035806) in Marketplace. All fields are read only. All string fields are free-form text entered by the publisher unless noted otherwise.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audienceDescription** | **String** | Description on the publisher&#39;s audience. |  [optional] |
|**buyerPitchStatement** | **String** | Statement explaining what&#39;s unique about publisher&#39;s business, and why buyers should partner with the publisher. |  [optional] |
|**directDealsContact** | **String** | Contact information for direct reservation deals. This is free text entered by the publisher and may include information like names, phone numbers and email addresses. |  [optional] |
|**displayName** | **String** | Name of the publisher profile. |  [optional] |
|**domains** | **List&lt;String&gt;** | The list of domains represented in this publisher profile. Empty if this is a parent profile. These are top private domains, meaning that these will not contain a string like \&quot;photos.google.co.uk/123\&quot;, but will instead contain \&quot;google.co.uk\&quot;. |  [optional] |
|**googlePlusUrl** | **String** | URL to publisher&#39;s Google+ page. |  [optional] |
|**isParent** | **Boolean** | Indicates if this profile is the parent profile of the seller. A parent profile represents all the inventory from the seller, as opposed to child profile that is created to brand a portion of inventory. One seller should have only one parent publisher profile, and can have multiple child profiles. Publisher profiles for the same seller will have same value of field google.ads.adexchange.buyer.v2beta1.PublisherProfile.seller. See https://support.google.com/admanager/answer/6035806 for details. |  [optional] |
|**logoUrl** | **String** | A Google public URL to the logo for this publisher profile. The logo is stored as a PNG, JPG, or GIF image. |  [optional] |
|**mediaKitUrl** | **String** | URL to additional marketing and sales materials. |  [optional] |
|**mobileApps** | [**List&lt;PublisherProfileMobileApplication&gt;**](PublisherProfileMobileApplication.md) | The list of apps represented in this publisher profile. Empty if this is a parent profile. |  [optional] |
|**overview** | **String** | Overview of the publisher. |  [optional] |
|**programmaticDealsContact** | **String** | Contact information for programmatic deals. This is free text entered by the publisher and may include information like names, phone numbers and email addresses. |  [optional] |
|**publisherProfileId** | **String** | Unique ID for publisher profile. |  [optional] |
|**rateCardInfoUrl** | **String** | URL to a publisher rate card. |  [optional] |
|**samplePageUrl** | **String** | URL to a sample content page. |  [optional] |
|**seller** | [**Seller**](Seller.md) |  |  [optional] |
|**topHeadlines** | **List&lt;String&gt;** | Up to three key metrics and rankings. Max 100 characters each. For example \&quot;#1 Mobile News Site for 20 Straight Months\&quot;. |  [optional] |



