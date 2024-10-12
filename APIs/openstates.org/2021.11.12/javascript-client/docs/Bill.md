# OpenStatesApiV3.Bill

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abstracts** | [**[BillAbstract]**](BillAbstract.md) |  | [optional] 
**actions** | [**[BillAction]**](BillAction.md) |  | [optional] 
**classification** | **[String]** |  | [optional] 
**createdAt** | **Date** |  | 
**documents** | [**[BillDocumentOrVersion]**](BillDocumentOrVersion.md) |  | [optional] 
**extras** | **Object** |  | [optional] 
**firstActionDate** | **String** |  | [optional] [default to &#39;&#39;]
**fromOrganization** | [**Organization**](Organization.md) |  | 
**id** | **String** |  | 
**identifier** | **String** |  | 
**jurisdiction** | [**CompactJurisdiction**](CompactJurisdiction.md) |  | 
**latestActionDate** | **String** |  | [optional] [default to &#39;&#39;]
**latestActionDescription** | **String** |  | [optional] [default to &#39;&#39;]
**latestPassageDate** | **String** |  | [optional] [default to &#39;&#39;]
**openstatesUrl** | **String** |  | 
**otherIdentifiers** | [**[BillIdentifier]**](BillIdentifier.md) |  | [optional] 
**otherTitles** | [**[BillTitle]**](BillTitle.md) |  | [optional] 
**relatedBills** | [**[RelatedBill]**](RelatedBill.md) |  | [optional] 
**session** | **String** |  | 
**sources** | [**[Link]**](Link.md) |  | [optional] 
**sponsorships** | [**[BillSponsorship]**](BillSponsorship.md) |  | [optional] 
**subject** | **[String]** |  | [optional] 
**title** | **String** |  | 
**updatedAt** | **Date** |  | 
**versions** | [**[BillDocumentOrVersion]**](BillDocumentOrVersion.md) |  | [optional] 
**votes** | [**[VoteEvent]**](VoteEvent.md) |  | [optional] 


