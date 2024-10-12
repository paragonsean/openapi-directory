

# VolumeVolumeInfo

General volume information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowAnonLogging** | **Boolean** | Whether anonymous logging should be allowed. |  [optional] |
|**authors** | **List&lt;String&gt;** | The names of the authors and/or editors for this volume. (In LITE projection) |  [optional] |
|**averageRating** | **Double** | The mean review rating for this volume. (min &#x3D; 1.0, max &#x3D; 5.0) |  [optional] |
|**canonicalVolumeLink** | **String** | Canonical URL for a volume. (In LITE projection.) |  [optional] |
|**categories** | **List&lt;String&gt;** | A list of subject categories, such as \&quot;Fiction\&quot;, \&quot;Suspense\&quot;, etc. |  [optional] |
|**comicsContent** | **Boolean** | Whether the volume has comics content. |  [optional] |
|**contentVersion** | **String** | An identifier for the version of the volume content (text &amp; images). (In LITE projection) |  [optional] |
|**description** | **String** | A synopsis of the volume. The text of the description is formatted in HTML and includes simple formatting elements, such as b, i, and br tags. (In LITE projection.) |  [optional] |
|**dimensions** | [**VolumeVolumeInfoDimensions**](VolumeVolumeInfoDimensions.md) |  |  [optional] |
|**imageLinks** | [**VolumeVolumeInfoImageLinks**](VolumeVolumeInfoImageLinks.md) |  |  [optional] |
|**industryIdentifiers** | [**List&lt;VolumeVolumeInfoIndustryIdentifiersInner&gt;**](VolumeVolumeInfoIndustryIdentifiersInner.md) | Industry standard identifiers for this volume. |  [optional] |
|**infoLink** | **String** | URL to view information about this volume on the Google Books site. (In LITE projection) |  [optional] |
|**language** | **String** | Best language for this volume (based on content). It is the two-letter ISO 639-1 code such as &#39;fr&#39;, &#39;en&#39;, etc. |  [optional] |
|**mainCategory** | **String** | The main category to which this volume belongs. It will be the category from the categories list returned below that has the highest weight. |  [optional] |
|**maturityRating** | **String** |  |  [optional] |
|**pageCount** | **Integer** | Total number of pages as per publisher metadata. |  [optional] |
|**panelizationSummary** | [**VolumeVolumeInfoPanelizationSummary**](VolumeVolumeInfoPanelizationSummary.md) |  |  [optional] |
|**previewLink** | **String** | URL to preview this volume on the Google Books site. |  [optional] |
|**printType** | **String** | Type of publication of this volume. Possible values are BOOK or MAGAZINE. |  [optional] |
|**printedPageCount** | **Integer** | Total number of printed pages in generated pdf representation. |  [optional] |
|**publishedDate** | **String** | Date of publication. (In LITE projection.) |  [optional] |
|**publisher** | **String** | Publisher of this volume. (In LITE projection.) |  [optional] |
|**ratingsCount** | **Integer** | The number of review ratings for this volume. |  [optional] |
|**readingModes** | [**VolumeVolumeInfoReadingModes**](VolumeVolumeInfoReadingModes.md) |  |  [optional] |
|**samplePageCount** | **Integer** | Total number of sample pages as per publisher metadata. |  [optional] |
|**seriesInfo** | [**Volumeseriesinfo**](Volumeseriesinfo.md) |  |  [optional] |
|**subtitle** | **String** | Volume subtitle. (In LITE projection.) |  [optional] |
|**title** | **String** | Volume title. (In LITE projection.) |  [optional] |



