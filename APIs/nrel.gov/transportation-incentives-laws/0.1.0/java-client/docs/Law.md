

# Law

This is a Law

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agency** | **String** | The agency with primary responsibility for federal incentives/regulations. |  [optional] |
|**amendedDate** | **OffsetDateTime** | The date the incentive/law/regulation was updated through new legislation or rulemaking. |  [optional] |
|**archivedDate** | **OffsetDateTime** | The date that an incentive/law/regulation is no longer relevant to the database. This may include longstanding Executive Orders or laws requiring legislative studies that have been completed. |  [optional] |
|**categories** | [**List&lt;Category&gt;**](Category.md) | The various law categories that apply to this law |  |
|**contacts** | [**List&lt;Poc&gt;**](Poc.md) | The contacts for the given law, returned only if the parameter poc is true |  [optional] |
|**enactedDate** | **OffsetDateTime** | The date the enacting legislation (if applicable) was signed into law. |  [optional] |
|**expiredDate** | **OffsetDateTime** | The date the incentive/law/regulation is set to end. |  [optional] |
|**id** | **Integer** | A unique identifier for this specific incentive/law/regulation. |  |
|**isRecent** | **Boolean** | The true or false value used to distinguish between recent federal executive actions (TRUE) and active incentives/laws/regulations (FALSE). |  [optional] |
|**plaintext** | **String** | Description of the incentive/law/regulation, including applicable legislative references, in &lt;a href&#x3D;\&quot;https://guides.github.com/features/mastering-markdown/\&quot;&gt;markdown formatting&lt;/a&gt; |  |
|**recentUpdateOrNew** | **String** | An indicator if the last significant update was an update or the laws creation. |  [optional] |
|**references** | [**List&lt;LawReference&gt;**](LawReference.md) | The URL associated with any bill or legislative reference included in the description. |  |
|**repealedDate** | **OffsetDateTime** | The date legislation is enacted or a rulemaking is finalized to repeal the incentive/law/regulation. |  [optional] |
|**seqNum** | **Integer** | The numerical value assigned to a description to show the order in which it is displayed online within a jurisdiction (state). |  [optional] |
|**significantUpdateDate** | **OffsetDateTime** | When the last significant update to the law was made. |  [optional] |
|**state** | **String** | The state in which the incentive/law/regulation was enacted and is active. |  |
|**text** | **String** | Description of the incentive/law/regulation, including applicable legislative references, html formated. |  |
|**title** | **String** | The brief title assigned to the incentive/law/regulation description. |  |
|**topics** | [**List&lt;LawTopics&gt;**](LawTopics.md) | For local incentive/regulation descriptions, the category that the incentive/regulation falls under, described below: Infrastructure Requirements, Vehicle Purchase and Infrastructure Development Incentives, Fuel Use Incentives, Parking Incentives, Technical Assistance, Vehicle Acquisition Requirements, Promotion Initiatives, Idle Reduction Requirements, Renewable Fuels Mandates and Standards |  |
|**type** | **String** | The category that the incentive/law/regulation falls under, described below: -State Incentives, -Laws and Regulations, -Utility/Private Incentives |  |
|**types** | [**List&lt;LawType&gt;**](LawType.md) | The types that apply to this law |  |



