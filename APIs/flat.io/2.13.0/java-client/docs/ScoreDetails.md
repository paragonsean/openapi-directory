

# ScoreDetails

The score and all its details

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**htmlUrl** | **String** | The url where the score can be viewed in a web browser |  [optional] |
|**id** | **String** | The unique identifier of the score |  [optional] |
|**privacy** | **ScorePrivacy** |  |  [optional] |
|**sharingKey** | **String** | The private sharing key of the score (available when the &#x60;privacy&#x60; mode is set to &#x60;privateLink&#x60;) |  [optional] |
|**title** | **String** | The title of the score |  [optional] |
|**user** | [**UserPublicSummary**](UserPublicSummary.md) |  |  [optional] |
|**arranger** | **String** | Arranger of the score |  [optional] |
|**collaborators** | [**List&lt;ResourceCollaborator&gt;**](ResourceCollaborator.md) | The list of the collaborators of the score |  [optional] |
|**collections** | **List&lt;String&gt;** | The List of parent collections, which includes all the collections this score is included. Please note that you might not have access to all of them. |  [optional] |
|**comments** | [**ScoreCommentsCounts**](ScoreCommentsCounts.md) |  |  [optional] |
|**composer** | **String** | Composer of the score |  [optional] |
|**creationDate** | **OffsetDateTime** | The date when the score was created |  [optional] |
|**creationType** | **ScoreCreationType** |  |  [optional] |
|**description** | **String** | Description of the creation |  [optional] |
|**durationTime** | **BigDecimal** | In seconds, an approximative duration of the score |  [optional] |
|**googleDriveFileId** | **String** | If the user uses Google Drive and the score exists on Google Drive, this field will contain the unique identifier of the Flat score on Google Drive. You can access the document using the url: &#x60;https://drive.google.com/open?id&#x3D;{googleDriveFileId}&#x60;  |  [optional] |
|**instruments** | **List&lt;String&gt;** | An array of the instrument identifiers used in the last version of the score. This is mainly used to display a list of the instruments in the Flat&#39;s UI or instruments icons. The format of the strings is &#x60;{instrument-group}.{instrument-id}&#x60;.  |  [optional] |
|**license** | **ScoreLicense** |  |  [optional] |
|**licenseText** | **String** | Additional license text written on the exported/printed score |  [optional] |
|**likes** | [**ScoreLikesCounts**](ScoreLikesCounts.md) |  |  [optional] |
|**lyricist** | **String** | Lyricist of the score |  [optional] |
|**mainTempoQpm** | **BigDecimal** | The main tempo of the score (in QPM) |  [optional] |
|**modificationDate** | **OffsetDateTime** | The date of the last revision of the score |  [optional] |
|**numberMeasures** | **Integer** | The number of measures in the score |  [optional] |
|**organization** | **String** | If the score has been created in an organization, the identifier of this organization. This property is especially used with the score privacy &#x60;organizationPublic&#x60;.  |  [optional] |
|**parentScore** | **String** | If the score has been forked, the unique identifier of the parent score.  |  [optional] |
|**plays** | [**ScorePlaysCounts**](ScorePlaysCounts.md) |  |  [optional] |
|**publicationDate** | **OffsetDateTime** | The date when the score was published on Flat |  [optional] |
|**rights** | [**ResourceRights**](ResourceRights.md) |  |  [optional] |
|**samples** | **List&lt;String&gt;** | An array of the audio samples identifiers used the different score parts. The format of the strings is &#x60;{instrument-group}.{sample-id}&#x60;.  |  [optional] |
|**subtitle** | **String** | Subtitle of the score |  [optional] |
|**tags** | **List&lt;String&gt;** | Tags describing the score |  [optional] |
|**views** | [**ScoreViewsCounts**](ScoreViewsCounts.md) |  |  [optional] |



