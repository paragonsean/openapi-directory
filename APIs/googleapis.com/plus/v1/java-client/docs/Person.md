

# Person


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aboutMe** | **String** | A short biography for this person. |  [optional] |
|**ageRange** | [**PersonAgeRange**](PersonAgeRange.md) |  |  [optional] |
|**birthday** | **String** | The person&#39;s date of birth, represented as YYYY-MM-DD. |  [optional] |
|**braggingRights** | **String** | The \&quot;bragging rights\&quot; line of this person. |  [optional] |
|**circledByCount** | **Integer** | For followers who are visible, the number of people who have added this person or page to a circle. |  [optional] |
|**cover** | [**PersonCover**](PersonCover.md) |  |  [optional] |
|**currentLocation** | **String** | (this field is not currently used) |  [optional] |
|**displayName** | **String** | The name of this person, which is suitable for display. |  [optional] |
|**domain** | **String** | The hosted domain name for the user&#39;s Google Apps account. For instance, example.com. The plus.profile.emails.read or email scope is needed to get this domain name. |  [optional] |
|**emails** | [**List&lt;PersonEmailsInner&gt;**](PersonEmailsInner.md) | A list of email addresses that this person has, including their Google account email address, and the public verified email addresses on their Google+ profile. The plus.profile.emails.read scope is needed to retrieve these email addresses, or the email scope can be used to retrieve just the Google account email address. |  [optional] |
|**etag** | **String** | ETag of this response for caching purposes. |  [optional] |
|**gender** | **String** | The person&#39;s gender. Possible values include, but are not limited to, the following values:   - \&quot;male\&quot; - Male gender.  - \&quot;female\&quot; - Female gender.  - \&quot;other\&quot; - Other. |  [optional] |
|**id** | **String** | The ID of this person. |  [optional] |
|**image** | [**PersonImage**](PersonImage.md) |  |  [optional] |
|**isPlusUser** | **Boolean** | Whether this user has signed up for Google+. |  [optional] |
|**kind** | **String** | Identifies this resource as a person. Value: \&quot;plus#person\&quot;. |  [optional] |
|**language** | **String** | The user&#39;s preferred language for rendering. |  [optional] |
|**name** | [**PersonName**](PersonName.md) |  |  [optional] |
|**nickname** | **String** | The nickname of this person. |  [optional] |
|**objectType** | **String** | Type of person within Google+. Possible values include, but are not limited to, the following values:   - \&quot;person\&quot; - represents an actual person.  - \&quot;page\&quot; - represents a page. |  [optional] |
|**occupation** | **String** | The occupation of this person. |  [optional] |
|**organizations** | [**List&lt;PersonOrganizationsInner&gt;**](PersonOrganizationsInner.md) | A list of current or past organizations with which this person is associated. |  [optional] |
|**placesLived** | [**List&lt;PersonPlacesLivedInner&gt;**](PersonPlacesLivedInner.md) | A list of places where this person has lived. |  [optional] |
|**plusOneCount** | **Integer** | If a Google+ Page, the number of people who have +1&#39;d this page. |  [optional] |
|**relationshipStatus** | **String** | The person&#39;s relationship status. Possible values include, but are not limited to, the following values:   - \&quot;single\&quot; - Person is single.  - \&quot;in_a_relationship\&quot; - Person is in a relationship.  - \&quot;engaged\&quot; - Person is engaged.  - \&quot;married\&quot; - Person is married.  - \&quot;its_complicated\&quot; - The relationship is complicated.  - \&quot;open_relationship\&quot; - Person is in an open relationship.  - \&quot;widowed\&quot; - Person is widowed.  - \&quot;in_domestic_partnership\&quot; - Person is in a domestic partnership.  - \&quot;in_civil_union\&quot; - Person is in a civil union. |  [optional] |
|**skills** | **String** | The person&#39;s skills. |  [optional] |
|**tagline** | **String** | The brief description (tagline) of this person. |  [optional] |
|**url** | **String** | The URL of this person&#39;s profile. |  [optional] |
|**urls** | [**List&lt;PersonUrlsInner&gt;**](PersonUrlsInner.md) | A list of URLs for this person. |  [optional] |
|**verified** | **Boolean** | Whether the person or Google+ Page has been verified. |  [optional] |



