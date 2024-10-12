

# VolumeAccessInfo

Any information about a volume related to reading or obtaining that volume text. This information can depend on country (books may be public domain in one country but not in another, e.g.).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessViewStatus** | **String** | Combines the access and viewability of this volume into a single status field for this user. Values can be FULL_PURCHASED, FULL_PUBLIC_DOMAIN, SAMPLE or NONE. (In LITE projection.) |  [optional] |
|**country** | **String** | The two-letter ISO_3166-1 country code for which this access information is valid. (In LITE projection.) |  [optional] |
|**downloadAccess** | [**DownloadAccessRestriction**](DownloadAccessRestriction.md) |  |  [optional] |
|**driveImportedContentLink** | **String** | URL to the Google Drive viewer if this volume is uploaded by the user by selecting the file from Google Drive. |  [optional] |
|**embeddable** | **Boolean** | Whether this volume can be embedded in a viewport using the Embedded Viewer API. |  [optional] |
|**epub** | [**VolumeAccessInfoEpub**](VolumeAccessInfoEpub.md) |  |  [optional] |
|**explicitOfflineLicenseManagement** | **Boolean** | Whether this volume requires that the client explicitly request offline download license rather than have it done automatically when loading the content, if the client supports it. |  [optional] |
|**pdf** | [**VolumeAccessInfoPdf**](VolumeAccessInfoPdf.md) |  |  [optional] |
|**publicDomain** | **Boolean** | Whether or not this book is public domain in the country listed above. |  [optional] |
|**quoteSharingAllowed** | **Boolean** | Whether quote sharing is allowed for this volume. |  [optional] |
|**textToSpeechPermission** | **String** | Whether text-to-speech is permitted for this volume. Values can be ALLOWED, ALLOWED_FOR_ACCESSIBILITY, or NOT_ALLOWED. |  [optional] |
|**viewOrderUrl** | **String** | For ordered but not yet processed orders, we give a URL that can be used to go to the appropriate Google Wallet page. |  [optional] |
|**viewability** | **String** | The read access of a volume. Possible values are PARTIAL, ALL_PAGES, NO_PAGES or UNKNOWN. This value depends on the country listed above. A value of PARTIAL means that the publisher has allowed some portion of the volume to be viewed publicly, without purchase. This can apply to eBooks as well as non-eBooks. Public domain books will always have a value of ALL_PAGES. |  [optional] |
|**webReaderLink** | **String** | URL to read this volume on the Google Books site. Link will not allow users to read non-viewable volumes. |  [optional] |



