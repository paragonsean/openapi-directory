

# PublisherProfile

The values in the publisher profile are supplied by the publisher. All fields are not filterable unless stated otherwise.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**audienceDescription** | **String** | Description on the publisher&#39;s audience. |  [optional] |
|**directDealsContact** | **String** | Contact information for direct reservation deals. This is free text entered by the publisher and may include information like names, phone numbers and email addresses. |  [optional] |
|**displayName** | **String** | Display name of the publisher profile. Can be used to filter the response of the publisherProfiles.list method. |  [optional] |
|**domains** | **List&lt;String&gt;** | The list of domains represented in this publisher profile. Empty if this is a parent profile. These are top private domains, meaning that these will not contain a string like \&quot;photos.google.co.uk/123\&quot;, but will instead contain \&quot;google.co.uk\&quot;. Can be used to filter the response of the publisherProfiles.list method. |  [optional] |
|**isParent** | **Boolean** | Indicates if this profile is the parent profile of the seller. A parent profile represents all the inventory from the seller, as opposed to child profile that is created to brand a portion of inventory. One seller has only one parent publisher profile, and can have multiple child profiles. See https://support.google.com/admanager/answer/6035806 for details. Can be used to filter the response of the publisherProfiles.list method by setting the filter to \&quot;is_parent: true\&quot;. |  [optional] |
|**logoUrl** | **String** | A Google public URL to the logo for this publisher profile. The logo is stored as a PNG, JPG, or GIF image. |  [optional] |
|**mediaKitUrl** | **String** | URL to additional marketing and sales materials. |  [optional] |
|**mobileApps** | [**List&lt;PublisherProfileMobileApplication&gt;**](PublisherProfileMobileApplication.md) | The list of apps represented in this publisher profile. Empty if this is a parent profile. |  [optional] |
|**name** | **String** | Name of the publisher profile. Format: &#x60;buyers/{buyer}/publisherProfiles/{publisher_profile}&#x60; |  [optional] |
|**overview** | **String** | Overview of the publisher. |  [optional] |
|**pitchStatement** | **String** | Statement explaining what&#39;s unique about publisher&#39;s business, and why buyers should partner with the publisher. |  [optional] |
|**programmaticDealsContact** | **String** | Contact information for programmatic deals. This is free text entered by the publisher and may include information like names, phone numbers and email addresses. |  [optional] |
|**publisherCode** | **String** | A unique identifying code for the seller. This value is the same for all of the seller&#39;s parent and child publisher profiles. Can be used to filter the response of the publisherProfiles.list method. |  [optional] |
|**samplePageUrl** | **String** | URL to a sample content page. |  [optional] |
|**topHeadlines** | **List&lt;String&gt;** | Up to three key metrics and rankings. For example, \&quot;#1 Mobile News Site for 20 Straight Months\&quot;. |  [optional] |



