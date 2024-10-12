

# EnterpriseTopazSidekickAssistCardProto

Wrapper proto for the Assist cards.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agendaGroupCardProto** | [**EnterpriseTopazSidekickAgendaGroupCardProto**](EnterpriseTopazSidekickAgendaGroupCardProto.md) |  |  [optional] |
|**cardMetadata** | [**EnterpriseTopazSidekickCardMetadata**](EnterpriseTopazSidekickCardMetadata.md) |  |  [optional] |
|**cardType** | [**CardTypeEnum**](#CardTypeEnum) | Card type. |  [optional] |
|**conflictingMeetingsCard** | [**EnterpriseTopazSidekickConflictingEventsCardProto**](EnterpriseTopazSidekickConflictingEventsCardProto.md) |  |  [optional] |
|**documentListCard** | [**EnterpriseTopazSidekickDocumentPerCategoryList**](EnterpriseTopazSidekickDocumentPerCategoryList.md) |  |  [optional] |
|**documentsWithMentions** | [**EnterpriseTopazSidekickDocumentPerCategoryList**](EnterpriseTopazSidekickDocumentPerCategoryList.md) |  |  [optional] |
|**findMeetingTimeCard** | [**EnterpriseTopazSidekickFindMeetingTimeCardProto**](EnterpriseTopazSidekickFindMeetingTimeCardProto.md) |  |  [optional] |
|**genericAnswerCard** | [**EnterpriseTopazSidekickGenericAnswerCard**](EnterpriseTopazSidekickGenericAnswerCard.md) |  |  [optional] |
|**getAndKeepAheadCard** | [**EnterpriseTopazSidekickGetAndKeepAheadCardProto**](EnterpriseTopazSidekickGetAndKeepAheadCardProto.md) |  |  [optional] |
|**meeting** | [**EnterpriseTopazSidekickAgendaEntry**](EnterpriseTopazSidekickAgendaEntry.md) |  |  [optional] |
|**meetingNotesCard** | [**EnterpriseTopazSidekickMeetingNotesCardProto**](EnterpriseTopazSidekickMeetingNotesCardProto.md) |  |  [optional] |
|**meetingNotesCardRequest** | [**EnterpriseTopazSidekickMeetingNotesCardRequest**](EnterpriseTopazSidekickMeetingNotesCardRequest.md) |  |  [optional] |
|**peopleDisambiguationCard** | [**EnterpriseTopazSidekickPeopleDisambiguationCard**](EnterpriseTopazSidekickPeopleDisambiguationCard.md) |  |  [optional] |
|**peoplePromotionCard** | [**PeoplePromotionCard**](PeoplePromotionCard.md) |  |  [optional] |
|**personAnswerCard** | [**EnterpriseTopazSidekickPeopleAnswerPersonAnswerCard**](EnterpriseTopazSidekickPeopleAnswerPersonAnswerCard.md) |  |  [optional] |
|**personProfileCard** | [**EnterpriseTopazSidekickPersonProfileCard**](EnterpriseTopazSidekickPersonProfileCard.md) |  |  [optional] |
|**personalizedDocsCard** | [**EnterpriseTopazSidekickPersonalizedDocsCardProto**](EnterpriseTopazSidekickPersonalizedDocsCardProto.md) |  |  [optional] |
|**relatedPeopleAnswerCard** | [**EnterpriseTopazSidekickPeopleAnswerRelatedPeopleAnswerCard**](EnterpriseTopazSidekickPeopleAnswerRelatedPeopleAnswerCard.md) |  |  [optional] |
|**shareMeetingDocsCard** | [**EnterpriseTopazSidekickShareMeetingDocsCardProto**](EnterpriseTopazSidekickShareMeetingDocsCardProto.md) |  |  [optional] |
|**sharedDocuments** | [**EnterpriseTopazSidekickDocumentPerCategoryList**](EnterpriseTopazSidekickDocumentPerCategoryList.md) |  |  [optional] |
|**suggestedQueryAnswerCard** | [**EnterpriseTopazSidekickAnswerSuggestedQueryAnswerCard**](EnterpriseTopazSidekickAnswerSuggestedQueryAnswerCard.md) |  |  [optional] |
|**thirdPartyAnswerCard** | [**ThirdPartyGenericCard**](ThirdPartyGenericCard.md) |  |  [optional] |
|**workInProgressCardProto** | [**EnterpriseTopazSidekickRecentDocumentsCardProto**](EnterpriseTopazSidekickRecentDocumentsCardProto.md) |  |  [optional] |



## Enum: CardTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN_TYPE | &quot;UNKNOWN_TYPE&quot; |
| AGENDA | &quot;AGENDA&quot; |
| CHANGELISTS | &quot;CHANGELISTS&quot; |
| CONFLICTING_MEETINGS | &quot;CONFLICTING_MEETINGS&quot; |
| CREATE_NOTES_FOR_MEETING | &quot;CREATE_NOTES_FOR_MEETING&quot; |
| CREATE_NOTES_FOR_MEETING_REQUEST | &quot;CREATE_NOTES_FOR_MEETING_REQUEST&quot; |
| CUSTOMER_NEWS | &quot;CUSTOMER_NEWS&quot; |
| FIND_MEETING_TIME | &quot;FIND_MEETING_TIME&quot; |
| NEXT_MEETING | &quot;NEXT_MEETING&quot; |
| PERSONALIZED_DOCS | &quot;PERSONALIZED_DOCS&quot; |
| TRENDING_DOCS | &quot;TRENDING_DOCS&quot; |
| UPCOMING_TRIP | &quot;UPCOMING_TRIP&quot; |
| SUMMARY | &quot;SUMMARY&quot; |
| MEETINGS | &quot;MEETINGS&quot; |
| HOMEPAGE | &quot;HOMEPAGE&quot; |
| SHARE_MEETING_DOCS | &quot;SHARE_MEETING_DOCS&quot; |
| DISCOVER_PEOPLE | &quot;DISCOVER_PEOPLE&quot; |
| HOMEPAGE_V3 | &quot;HOMEPAGE_V3&quot; |
| AGENDA_GROUP | &quot;AGENDA_GROUP&quot; |
| WORK_IN_PROGRESS | &quot;WORK_IN_PROGRESS&quot; |
| GET_AND_KEEP_AHEAD | &quot;GET_AND_KEEP_AHEAD&quot; |
| GENERIC_ANSWER_CARD | &quot;GENERIC_ANSWER_CARD&quot; |
| THIRD_PARTY_ANSWER_CARD | &quot;THIRD_PARTY_ANSWER_CARD&quot; |
| DOMAIN_TRENDING_DOCS | &quot;DOMAIN_TRENDING_DOCS&quot; |
| TEAM_TRENDING_DOCS | &quot;TEAM_TRENDING_DOCS&quot; |
| DOCUMENT_LIST_ANSWER_CARD | &quot;DOCUMENT_LIST_ANSWER_CARD&quot; |
| SUGGESTED_QUERY_ANSWER_CARD | &quot;SUGGESTED_QUERY_ANSWER_CARD&quot; |
| PERSON_ANSWER_CARD | &quot;PERSON_ANSWER_CARD&quot; |
| RELATED_PEOPLE_ANSWER_CARD | &quot;RELATED_PEOPLE_ANSWER_CARD&quot; |
| PERSON_KNOWLEDGE_CARD | &quot;PERSON_KNOWLEDGE_CARD&quot; |
| PEOPLE_SEARCH_PROMOTION_CARD | &quot;PEOPLE_SEARCH_PROMOTION_CARD&quot; |



