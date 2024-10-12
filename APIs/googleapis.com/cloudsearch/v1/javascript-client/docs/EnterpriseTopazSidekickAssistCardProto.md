# CloudSearchApi.EnterpriseTopazSidekickAssistCardProto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agendaGroupCardProto** | [**EnterpriseTopazSidekickAgendaGroupCardProto**](EnterpriseTopazSidekickAgendaGroupCardProto.md) |  | [optional] 
**cardMetadata** | [**EnterpriseTopazSidekickCardMetadata**](EnterpriseTopazSidekickCardMetadata.md) |  | [optional] 
**cardType** | **String** | Card type. | [optional] 
**conflictingMeetingsCard** | [**EnterpriseTopazSidekickConflictingEventsCardProto**](EnterpriseTopazSidekickConflictingEventsCardProto.md) |  | [optional] 
**documentListCard** | [**EnterpriseTopazSidekickDocumentPerCategoryList**](EnterpriseTopazSidekickDocumentPerCategoryList.md) |  | [optional] 
**documentsWithMentions** | [**EnterpriseTopazSidekickDocumentPerCategoryList**](EnterpriseTopazSidekickDocumentPerCategoryList.md) |  | [optional] 
**findMeetingTimeCard** | [**EnterpriseTopazSidekickFindMeetingTimeCardProto**](EnterpriseTopazSidekickFindMeetingTimeCardProto.md) |  | [optional] 
**genericAnswerCard** | [**EnterpriseTopazSidekickGenericAnswerCard**](EnterpriseTopazSidekickGenericAnswerCard.md) |  | [optional] 
**getAndKeepAheadCard** | [**EnterpriseTopazSidekickGetAndKeepAheadCardProto**](EnterpriseTopazSidekickGetAndKeepAheadCardProto.md) |  | [optional] 
**meeting** | [**EnterpriseTopazSidekickAgendaEntry**](EnterpriseTopazSidekickAgendaEntry.md) |  | [optional] 
**meetingNotesCard** | [**EnterpriseTopazSidekickMeetingNotesCardProto**](EnterpriseTopazSidekickMeetingNotesCardProto.md) |  | [optional] 
**meetingNotesCardRequest** | [**EnterpriseTopazSidekickMeetingNotesCardRequest**](EnterpriseTopazSidekickMeetingNotesCardRequest.md) |  | [optional] 
**peopleDisambiguationCard** | [**EnterpriseTopazSidekickPeopleDisambiguationCard**](EnterpriseTopazSidekickPeopleDisambiguationCard.md) |  | [optional] 
**peoplePromotionCard** | [**PeoplePromotionCard**](PeoplePromotionCard.md) |  | [optional] 
**personAnswerCard** | [**EnterpriseTopazSidekickPeopleAnswerPersonAnswerCard**](EnterpriseTopazSidekickPeopleAnswerPersonAnswerCard.md) |  | [optional] 
**personProfileCard** | [**EnterpriseTopazSidekickPersonProfileCard**](EnterpriseTopazSidekickPersonProfileCard.md) |  | [optional] 
**personalizedDocsCard** | [**EnterpriseTopazSidekickPersonalizedDocsCardProto**](EnterpriseTopazSidekickPersonalizedDocsCardProto.md) |  | [optional] 
**relatedPeopleAnswerCard** | [**EnterpriseTopazSidekickPeopleAnswerRelatedPeopleAnswerCard**](EnterpriseTopazSidekickPeopleAnswerRelatedPeopleAnswerCard.md) |  | [optional] 
**shareMeetingDocsCard** | [**EnterpriseTopazSidekickShareMeetingDocsCardProto**](EnterpriseTopazSidekickShareMeetingDocsCardProto.md) |  | [optional] 
**sharedDocuments** | [**EnterpriseTopazSidekickDocumentPerCategoryList**](EnterpriseTopazSidekickDocumentPerCategoryList.md) |  | [optional] 
**suggestedQueryAnswerCard** | [**EnterpriseTopazSidekickAnswerSuggestedQueryAnswerCard**](EnterpriseTopazSidekickAnswerSuggestedQueryAnswerCard.md) |  | [optional] 
**thirdPartyAnswerCard** | [**ThirdPartyGenericCard**](ThirdPartyGenericCard.md) |  | [optional] 
**workInProgressCardProto** | [**EnterpriseTopazSidekickRecentDocumentsCardProto**](EnterpriseTopazSidekickRecentDocumentsCardProto.md) |  | [optional] 



## Enum: CardTypeEnum


* `UNKNOWN_TYPE` (value: `"UNKNOWN_TYPE"`)

* `AGENDA` (value: `"AGENDA"`)

* `CHANGELISTS` (value: `"CHANGELISTS"`)

* `CONFLICTING_MEETINGS` (value: `"CONFLICTING_MEETINGS"`)

* `CREATE_NOTES_FOR_MEETING` (value: `"CREATE_NOTES_FOR_MEETING"`)

* `CREATE_NOTES_FOR_MEETING_REQUEST` (value: `"CREATE_NOTES_FOR_MEETING_REQUEST"`)

* `CUSTOMER_NEWS` (value: `"CUSTOMER_NEWS"`)

* `FIND_MEETING_TIME` (value: `"FIND_MEETING_TIME"`)

* `NEXT_MEETING` (value: `"NEXT_MEETING"`)

* `PERSONALIZED_DOCS` (value: `"PERSONALIZED_DOCS"`)

* `TRENDING_DOCS` (value: `"TRENDING_DOCS"`)

* `UPCOMING_TRIP` (value: `"UPCOMING_TRIP"`)

* `SUMMARY` (value: `"SUMMARY"`)

* `MEETINGS` (value: `"MEETINGS"`)

* `HOMEPAGE` (value: `"HOMEPAGE"`)

* `SHARE_MEETING_DOCS` (value: `"SHARE_MEETING_DOCS"`)

* `DISCOVER_PEOPLE` (value: `"DISCOVER_PEOPLE"`)

* `HOMEPAGE_V3` (value: `"HOMEPAGE_V3"`)

* `AGENDA_GROUP` (value: `"AGENDA_GROUP"`)

* `WORK_IN_PROGRESS` (value: `"WORK_IN_PROGRESS"`)

* `GET_AND_KEEP_AHEAD` (value: `"GET_AND_KEEP_AHEAD"`)

* `GENERIC_ANSWER_CARD` (value: `"GENERIC_ANSWER_CARD"`)

* `THIRD_PARTY_ANSWER_CARD` (value: `"THIRD_PARTY_ANSWER_CARD"`)

* `DOMAIN_TRENDING_DOCS` (value: `"DOMAIN_TRENDING_DOCS"`)

* `TEAM_TRENDING_DOCS` (value: `"TEAM_TRENDING_DOCS"`)

* `DOCUMENT_LIST_ANSWER_CARD` (value: `"DOCUMENT_LIST_ANSWER_CARD"`)

* `SUGGESTED_QUERY_ANSWER_CARD` (value: `"SUGGESTED_QUERY_ANSWER_CARD"`)

* `PERSON_ANSWER_CARD` (value: `"PERSON_ANSWER_CARD"`)

* `RELATED_PEOPLE_ANSWER_CARD` (value: `"RELATED_PEOPLE_ANSWER_CARD"`)

* `PERSON_KNOWLEDGE_CARD` (value: `"PERSON_KNOWLEDGE_CARD"`)

* `PEOPLE_SEARCH_PROMOTION_CARD` (value: `"PEOPLE_SEARCH_PROMOTION_CARD"`)




