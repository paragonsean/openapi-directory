# TransportationLawsAndIncentives.Law

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agency** | **String** | The agency with primary responsibility for federal incentives/regulations. | [optional] 
**amendedDate** | **Date** | The date the incentive/law/regulation was updated through new legislation or rulemaking. | [optional] 
**archivedDate** | **Date** | The date that an incentive/law/regulation is no longer relevant to the database. This may include longstanding Executive Orders or laws requiring legislative studies that have been completed. | [optional] 
**categories** | [**[Category]**](Category.md) | The various law categories that apply to this law | 
**contacts** | [**[Poc]**](Poc.md) | The contacts for the given law, returned only if the parameter poc is true | [optional] 
**enactedDate** | **Date** | The date the enacting legislation (if applicable) was signed into law. | [optional] 
**expiredDate** | **Date** | The date the incentive/law/regulation is set to end. | [optional] 
**id** | **Number** | A unique identifier for this specific incentive/law/regulation. | 
**isRecent** | **Boolean** | The true or false value used to distinguish between recent federal executive actions (TRUE) and active incentives/laws/regulations (FALSE). | [optional] 
**plaintext** | **String** | Description of the incentive/law/regulation, including applicable legislative references, in &lt;a href&#x3D;\&quot;https://guides.github.com/features/mastering-markdown/\&quot;&gt;markdown formatting&lt;/a&gt; | 
**recentUpdateOrNew** | **String** | An indicator if the last significant update was an update or the laws creation. | [optional] 
**references** | [**[LawReference]**](LawReference.md) | The URL associated with any bill or legislative reference included in the description. | 
**repealedDate** | **Date** | The date legislation is enacted or a rulemaking is finalized to repeal the incentive/law/regulation. | [optional] 
**seqNum** | **Number** | The numerical value assigned to a description to show the order in which it is displayed online within a jurisdiction (state). | [optional] 
**significantUpdateDate** | **Date** | When the last significant update to the law was made. | [optional] 
**state** | **String** | The state in which the incentive/law/regulation was enacted and is active. | 
**text** | **String** | Description of the incentive/law/regulation, including applicable legislative references, html formated. | 
**title** | **String** | The brief title assigned to the incentive/law/regulation description. | 
**topics** | [**[LawTopics]**](LawTopics.md) | For local incentive/regulation descriptions, the category that the incentive/regulation falls under, described below: Infrastructure Requirements, Vehicle Purchase and Infrastructure Development Incentives, Fuel Use Incentives, Parking Incentives, Technical Assistance, Vehicle Acquisition Requirements, Promotion Initiatives, Idle Reduction Requirements, Renewable Fuels Mandates and Standards | 
**type** | **String** | The category that the incentive/law/regulation falls under, described below: -State Incentives, -Laws and Regulations, -Utility/Private Incentives | 
**types** | [**[LawType]**](LawType.md) | The types that apply to this law | 


