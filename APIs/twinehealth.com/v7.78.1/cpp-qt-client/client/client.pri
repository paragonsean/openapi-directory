QT += network

HEADERS += \
# Models
    $${PWD}/OAIActionMetric.h \
    $${PWD}/OAIActionMetric_validations.h \
    $${PWD}/OAIActionMetric_validations_maximum.h \
    $${PWD}/OAIActionResource.h \
    $${PWD}/OAIActionResource_attributes.h \
    $${PWD}/OAIActionResource_attributes_adherence.h \
    $${PWD}/OAIActionResource_attributes_adherence_streak.h \
    $${PWD}/OAIActionResource_attributes_frequency_goal.h \
    $${PWD}/OAIActionResource_attributes_frequency_goal_weeks.h \
    $${PWD}/OAIActionResource_relationships.h \
    $${PWD}/OAIActionResource_relationships_plan.h \
    $${PWD}/OAIActionResource_relationships_plan_data.h \
    $${PWD}/OAIActionWindow.h \
    $${PWD}/OAIAddress.h \
    $${PWD}/OAIArchiveHistory.h \
    $${PWD}/OAIBundleResource.h \
    $${PWD}/OAIBundleResource_attributes.h \
    $${PWD}/OAIBundleResource_relationships.h \
    $${PWD}/OAICalendarEventResource.h \
    $${PWD}/OAICalendarEventResource_attributes.h \
    $${PWD}/OAICalendarEventResource_attributes_attendees_inner.h \
    $${PWD}/OAICalendarEventResource_links.h \
    $${PWD}/OAICalendarEventResource_relationships.h \
    $${PWD}/OAICalendarEventResource_relationships_owner.h \
    $${PWD}/OAICalendarEventResource_relationships_owner_links.h \
    $${PWD}/OAICalendarEventResponseResource.h \
    $${PWD}/OAICalendarEventResponseResource_attributes.h \
    $${PWD}/OAICalendarEventResponseResource_links.h \
    $${PWD}/OAICalendarEventResponseResource_relationships.h \
    $${PWD}/OAICalendarEventResponseResource_relationships_calendar_event.h \
    $${PWD}/OAICalendarEventResponseResource_relationships_calendar_event_links.h \
    $${PWD}/OAICalendarEventResponseResource_relationships_user.h \
    $${PWD}/OAICalendarEventResponseResource_relationships_user_links.h \
    $${PWD}/OAICoachResource.h \
    $${PWD}/OAICoachResource_attributes.h \
    $${PWD}/OAICoachResource_links.h \
    $${PWD}/OAICollectionResponseLinks.h \
    $${PWD}/OAICreateActionRequest.h \
    $${PWD}/OAICreateActionResponse.h \
    $${PWD}/OAICreateBundleRequest.h \
    $${PWD}/OAICreateBundleResponse.h \
    $${PWD}/OAICreateCalendarEventRequest.h \
    $${PWD}/OAICreateCalendarEventRequest_data.h \
    $${PWD}/OAICreateCalendarEventRequest_data_relationships.h \
    $${PWD}/OAICreateCalendarEventRequest_data_relationships_owner.h \
    $${PWD}/OAICreateCalendarEventResponse.h \
    $${PWD}/OAICreateCalendarEventResponseRequest.h \
    $${PWD}/OAICreateCalendarEventResponseRequest_data.h \
    $${PWD}/OAICreateCalendarEventResponseRequest_data_relationships.h \
    $${PWD}/OAICreateCalendarEventResponseRequest_data_relationships_calendar_event.h \
    $${PWD}/OAICreateCalendarEventResponseRequest_data_relationships_user.h \
    $${PWD}/OAICreateGroupRequest.h \
    $${PWD}/OAICreateGroupResponse.h \
    $${PWD}/OAICreateOrUpdateErrorResponse.h \
    $${PWD}/OAICreateOrUpdateMetaResponse.h \
    $${PWD}/OAICreatePatientHealthMetricRequest.h \
    $${PWD}/OAICreatePatientHealthMetricRequest_meta.h \
    $${PWD}/OAICreatePatientHealthMetricResponse.h \
    $${PWD}/OAICreatePatientRequest.h \
    $${PWD}/OAICreatePatientRequest_meta.h \
    $${PWD}/OAICreatePatientResponse.h \
    $${PWD}/OAICreateRewardEarningFulfillmentRequest.h \
    $${PWD}/OAICreateRewardEarningFulfillmentResponse.h \
    $${PWD}/OAICreateRewardEarningRequest.h \
    $${PWD}/OAICreateRewardEarningResponse.h \
    $${PWD}/OAICreateRewardProgramActivationRequest.h \
    $${PWD}/OAICreateRewardProgramActivationResponse.h \
    $${PWD}/OAICreateRewardProgramRequest.h \
    $${PWD}/OAICreateRewardProgramResponse.h \
    $${PWD}/OAICreateRewardRequest.h \
    $${PWD}/OAICreateRewardResponse.h \
    $${PWD}/OAICreateTokenRequest.h \
    $${PWD}/OAICreateTokenRequest_data.h \
    $${PWD}/OAICreateTokenRequest_data_attributes.h \
    $${PWD}/OAICreateTokenResponse.h \
    $${PWD}/OAIEmailHistoryResource.h \
    $${PWD}/OAIEmailHistoryResource_attributes.h \
    $${PWD}/OAIEmailHistoryResource_attributes_status_times.h \
    $${PWD}/OAIEmailHistoryResource_relationships.h \
    $${PWD}/OAIEmailHistoryResource_relationships_receiver.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIError_source.h \
    $${PWD}/OAIFetchActionResponse.h \
    $${PWD}/OAIFetchBundleResponse.h \
    $${PWD}/OAIFetchCalendarEventResponse.h \
    $${PWD}/OAIFetchCalendarEventsResponse.h \
    $${PWD}/OAIFetchCoachResponse.h \
    $${PWD}/OAIFetchCoachesResponse.h \
    $${PWD}/OAIFetchEmailHistoriesResponse.h \
    $${PWD}/OAIFetchEmailHistoryResponse.h \
    $${PWD}/OAIFetchErrorResponse.h \
    $${PWD}/OAIFetchGroupResponse.h \
    $${PWD}/OAIFetchGroupsResponse.h \
    $${PWD}/OAIFetchHealthProfileAnswerResponse.h \
    $${PWD}/OAIFetchHealthProfileAnswersResponse.h \
    $${PWD}/OAIFetchHealthProfileQuestionResponse.h \
    $${PWD}/OAIFetchHealthProfileQuestionsResponse.h \
    $${PWD}/OAIFetchHealthProfileResponse.h \
    $${PWD}/OAIFetchHealthProfilesResponse.h \
    $${PWD}/OAIFetchHealthQuestionDefinitionResponse.h \
    $${PWD}/OAIFetchHealthQuestionDefinitionsResponse.h \
    $${PWD}/OAIFetchMetaResponse.h \
    $${PWD}/OAIFetchOrganizationResponse.h \
    $${PWD}/OAIFetchPatientHealthMetricResponse.h \
    $${PWD}/OAIFetchPatientHealthResultResponse.h \
    $${PWD}/OAIFetchPatientPlanSummariesResponse.h \
    $${PWD}/OAIFetchPatientPlanSummaryResponse.h \
    $${PWD}/OAIFetchPatientResponse.h \
    $${PWD}/OAIFetchPatientsResponse.h \
    $${PWD}/OAIFetchRewardEarningFulfillmentResponse.h \
    $${PWD}/OAIFetchRewardEarningFulfillmentsResponse.h \
    $${PWD}/OAIFetchRewardEarningResponse.h \
    $${PWD}/OAIFetchRewardEarningsResponse.h \
    $${PWD}/OAIFetchRewardProgramActivationResponse.h \
    $${PWD}/OAIFetchRewardProgramActivationsResponse.h \
    $${PWD}/OAIFetchRewardProgramResponse.h \
    $${PWD}/OAIFetchRewardProgramsResponse.h \
    $${PWD}/OAIFetchRewardResponse.h \
    $${PWD}/OAIFetchRewardsResponse.h \
    $${PWD}/OAIGroupResource.h \
    $${PWD}/OAIGroupResource_attributes.h \
    $${PWD}/OAIGroupResource_links.h \
    $${PWD}/OAIHealthProfileAnswerResource.h \
    $${PWD}/OAIHealthProfileAnswerResource_attributes.h \
    $${PWD}/OAIHealthProfileAnswerResource_attributes_history_inner.h \
    $${PWD}/OAIHealthProfileAnswerResource_attributes_latest.h \
    $${PWD}/OAIHealthProfileAnswerResource_links.h \
    $${PWD}/OAIHealthProfileAnswerResource_relationships.h \
    $${PWD}/OAIHealthProfileAnswerResource_relationships_patient.h \
    $${PWD}/OAIHealthProfileAnswerResource_relationships_patient_links.h \
    $${PWD}/OAIHealthProfileQuestionResource.h \
    $${PWD}/OAIHealthProfileQuestionResource_links.h \
    $${PWD}/OAIHealthProfileQuestionResource_relationships.h \
    $${PWD}/OAIHealthProfileQuestionResource_relationships_answer.h \
    $${PWD}/OAIHealthProfileQuestionResource_relationships_answer_links.h \
    $${PWD}/OAIHealthProfileQuestionResource_relationships_profile.h \
    $${PWD}/OAIHealthProfileQuestionResource_relationships_profile_links.h \
    $${PWD}/OAIHealthProfileQuestionResource_relationships_question_definition.h \
    $${PWD}/OAIHealthProfileQuestionResource_relationships_question_definition_links.h \
    $${PWD}/OAIHealthProfileQuestionResource_relationships_question_definition_links_links.h \
    $${PWD}/OAIHealthProfileResource.h \
    $${PWD}/OAIHealthProfileResource_attributes.h \
    $${PWD}/OAIHealthProfileResource_attributes_stats_inner.h \
    $${PWD}/OAIHealthProfileResource_links.h \
    $${PWD}/OAIHealthProfileResource_relationships.h \
    $${PWD}/OAIHealthProfileResource_relationships_patient.h \
    $${PWD}/OAIHealthProfileResource_relationships_patient_links.h \
    $${PWD}/OAIHealthProfileResource_relationships_questions.h \
    $${PWD}/OAIHealthProfileResource_relationships_questions_links.h \
    $${PWD}/OAIHealthQuestionDefinitionResource.h \
    $${PWD}/OAIHealthQuestionDefinitionResource_attributes.h \
    $${PWD}/OAIHealthQuestionDefinitionResource_attributes_format.h \
    $${PWD}/OAIHealthQuestionDefinitionResource_attributes_format_data_inner.h \
    $${PWD}/OAIHealthQuestionDefinitionResource_attributes_requirements_inner.h \
    $${PWD}/OAIHealthQuestionDefinitionResource_links.h \
    $${PWD}/OAIIdentifier.h \
    $${PWD}/OAIOrganizationResource.h \
    $${PWD}/OAIOrganizationResource_attributes.h \
    $${PWD}/OAIOrganizationResource_links.h \
    $${PWD}/OAIPatientCreateResource.h \
    $${PWD}/OAIPatientCreateResource_allOf_relationships.h \
    $${PWD}/OAIPatientCreateResource_allOf_relationships_coaches.h \
    $${PWD}/OAIPatientCreateResource_allOf_relationships_coaches_data.h \
    $${PWD}/OAIPatientCreateResource_allOf_relationships_coaches_links.h \
    $${PWD}/OAIPatientCreateResource_allOf_relationships_coaches_meta.h \
    $${PWD}/OAIPatientCreateResource_allOf_relationships_groups.h \
    $${PWD}/OAIPatientCreateResource_allOf_relationships_groups_data.h \
    $${PWD}/OAIPatientCreateResource_allOf_relationships_groups_meta.h \
    $${PWD}/OAIPatientCreateResource_allOf_relationships_groups_meta_query.h \
    $${PWD}/OAIPatientHealthMetricCreateResource.h \
    $${PWD}/OAIPatientHealthMetricResource.h \
    $${PWD}/OAIPatientHealthMetricResource_attributes.h \
    $${PWD}/OAIPatientHealthMetricResource_attributes_code.h \
    $${PWD}/OAIPatientHealthMetricResource_relationships.h \
    $${PWD}/OAIPatientHealthMetricResource_relationships_patient.h \
    $${PWD}/OAIPatientHealthMetricResource_relationships_patient_data.h \
    $${PWD}/OAIPatientHealthMetricResource_relationships_patient_data_meta.h \
    $${PWD}/OAIPatientHealthMetricResource_relationships_patient_data_meta_query.h \
    $${PWD}/OAIPatientHealthResultResource.h \
    $${PWD}/OAIPatientHealthResultResource_attributes.h \
    $${PWD}/OAIPatientHealthResultResource_attributes_annotations_inner.h \
    $${PWD}/OAIPatientHealthResultResource_attributes_data.h \
    $${PWD}/OAIPatientHealthResultResource_attributes_source.h \
    $${PWD}/OAIPatientHealthResultResource_relationships.h \
    $${PWD}/OAIPatientHealthResultResource_relationships_patient.h \
    $${PWD}/OAIPatientHealthResultResource_relationships_patient_data.h \
    $${PWD}/OAIPatientIdentifier.h \
    $${PWD}/OAIPatientPlanSummaryResource.h \
    $${PWD}/OAIPatientPlanSummaryResource_attributes.h \
    $${PWD}/OAIPatientPlanSummaryResource_attributes_window_notification_times.h \
    $${PWD}/OAIPatientPlanSummaryResource_attributes_window_order_inner.h \
    $${PWD}/OAIPatientPlanSummaryResource_links.h \
    $${PWD}/OAIPatientPlanSummaryResource_relationships.h \
    $${PWD}/OAIPatientPlanSummaryResource_relationships_actions.h \
    $${PWD}/OAIPatientPlanSummaryResource_relationships_actions_data_inner.h \
    $${PWD}/OAIPatientPlanSummaryResource_relationships_actions_links.h \
    $${PWD}/OAIPatientPlanSummaryResource_relationships_patient.h \
    $${PWD}/OAIPatientResource.h \
    $${PWD}/OAIPatientResource_attributes.h \
    $${PWD}/OAIPatientResource_attributes_statement.h \
    $${PWD}/OAIPatientResource_links.h \
    $${PWD}/OAIPatientResource_relationships.h \
    $${PWD}/OAIPatientResource_relationships_coaches.h \
    $${PWD}/OAIPatientResource_relationships_coaches_links.h \
    $${PWD}/OAIPatientResource_relationships_groups.h \
    $${PWD}/OAIPatientResource_relationships_groups_data_inner.h \
    $${PWD}/OAIPhoneNumber.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIRewardEarningFulfillmentResource.h \
    $${PWD}/OAIRewardEarningFulfillmentResource_attributes.h \
    $${PWD}/OAIRewardEarningFulfillmentResource_relationships.h \
    $${PWD}/OAIRewardEarningFulfillmentResource_relationships_patient.h \
    $${PWD}/OAIRewardEarningResource.h \
    $${PWD}/OAIRewardEarningResource_attributes.h \
    $${PWD}/OAIRewardEarningResource_relationships.h \
    $${PWD}/OAIRewardProgramActivationResource.h \
    $${PWD}/OAIRewardProgramActivationResource_attributes.h \
    $${PWD}/OAIRewardProgramActivationResource_relationships.h \
    $${PWD}/OAIRewardProgramResource.h \
    $${PWD}/OAIRewardProgramResource_attributes.h \
    $${PWD}/OAIRewardProgramResource_relationships.h \
    $${PWD}/OAIRewardProgramResource_relationships_group.h \
    $${PWD}/OAIRewardResource.h \
    $${PWD}/OAIRewardResource_attributes.h \
    $${PWD}/OAIRewardResource_relationships.h \
    $${PWD}/OAITokenResource.h \
    $${PWD}/OAITokenResource_attributes.h \
    $${PWD}/OAITokenResource_relationships.h \
    $${PWD}/OAITokenResource_relationships_groups.h \
    $${PWD}/OAITokenResource_relationships_groups_data_inner.h \
    $${PWD}/OAITokenResource_relationships_groups_links.h \
    $${PWD}/OAITokenResource_relationships_organization.h \
    $${PWD}/OAITokenResource_relationships_organization_data.h \
    $${PWD}/OAITokenResource_relationships_organization_links.h \
    $${PWD}/OAIUpdateActionRequest.h \
    $${PWD}/OAIUpdateActionResponse.h \
    $${PWD}/OAIUpdateBundleRequest.h \
    $${PWD}/OAIUpdateBundleResponse.h \
    $${PWD}/OAIUpdateCalendarEventRequest.h \
    $${PWD}/OAIUpdateCalendarEventRequest_data.h \
    $${PWD}/OAIUpdateCalendarEventRequest_data_relationships.h \
    $${PWD}/OAIUpdateCalendarEventRequest_data_relationships_owner.h \
    $${PWD}/OAIUpdateCalendarEventResponse.h \
    $${PWD}/OAIUpdatePatientPlanSummaryRequest.h \
    $${PWD}/OAIUpdatePatientPlanSummaryResponse.h \
    $${PWD}/OAIUpdatePatientRequest.h \
    $${PWD}/OAIUpdatePatientResponse.h \
    $${PWD}/OAIUpsertPatientRequest.h \
    $${PWD}/OAIUpsertPatientRequest_meta.h \
    $${PWD}/OAIUpsertPatientRequest_meta_query.h \
    $${PWD}/OAIUpsertPatientRequest_meta_query_identifier.h \
# APIs
    $${PWD}/OAIActionApi.h \
    $${PWD}/OAIBundleApi.h \
    $${PWD}/OAICalendarEventApi.h \
    $${PWD}/OAICalendarEventResponseApi.h \
    $${PWD}/OAICoachApi.h \
    $${PWD}/OAIEmailHistoryApi.h \
    $${PWD}/OAIGroupApi.h \
    $${PWD}/OAIHealthProfileApi.h \
    $${PWD}/OAIHealthProfileAnswerApi.h \
    $${PWD}/OAIHealthProfileQuestionApi.h \
    $${PWD}/OAIHealthQuestionDefinitionApi.h \
    $${PWD}/OAIMetricApi.h \
    $${PWD}/OAIOauthApi.h \
    $${PWD}/OAIOrganizationApi.h \
    $${PWD}/OAIPatientApi.h \
    $${PWD}/OAIPlanApi.h \
    $${PWD}/OAIResultApi.h \
    $${PWD}/OAIRewardApi.h \
    $${PWD}/OAIRewardEarningApi.h \
    $${PWD}/OAIRewardEarningFulfillmentApi.h \
    $${PWD}/OAIRewardProgramApi.h \
    $${PWD}/OAIRewardProgramActivationApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIActionMetric.cpp \
    $${PWD}/OAIActionMetric_validations.cpp \
    $${PWD}/OAIActionMetric_validations_maximum.cpp \
    $${PWD}/OAIActionResource.cpp \
    $${PWD}/OAIActionResource_attributes.cpp \
    $${PWD}/OAIActionResource_attributes_adherence.cpp \
    $${PWD}/OAIActionResource_attributes_adherence_streak.cpp \
    $${PWD}/OAIActionResource_attributes_frequency_goal.cpp \
    $${PWD}/OAIActionResource_attributes_frequency_goal_weeks.cpp \
    $${PWD}/OAIActionResource_relationships.cpp \
    $${PWD}/OAIActionResource_relationships_plan.cpp \
    $${PWD}/OAIActionResource_relationships_plan_data.cpp \
    $${PWD}/OAIActionWindow.cpp \
    $${PWD}/OAIAddress.cpp \
    $${PWD}/OAIArchiveHistory.cpp \
    $${PWD}/OAIBundleResource.cpp \
    $${PWD}/OAIBundleResource_attributes.cpp \
    $${PWD}/OAIBundleResource_relationships.cpp \
    $${PWD}/OAICalendarEventResource.cpp \
    $${PWD}/OAICalendarEventResource_attributes.cpp \
    $${PWD}/OAICalendarEventResource_attributes_attendees_inner.cpp \
    $${PWD}/OAICalendarEventResource_links.cpp \
    $${PWD}/OAICalendarEventResource_relationships.cpp \
    $${PWD}/OAICalendarEventResource_relationships_owner.cpp \
    $${PWD}/OAICalendarEventResource_relationships_owner_links.cpp \
    $${PWD}/OAICalendarEventResponseResource.cpp \
    $${PWD}/OAICalendarEventResponseResource_attributes.cpp \
    $${PWD}/OAICalendarEventResponseResource_links.cpp \
    $${PWD}/OAICalendarEventResponseResource_relationships.cpp \
    $${PWD}/OAICalendarEventResponseResource_relationships_calendar_event.cpp \
    $${PWD}/OAICalendarEventResponseResource_relationships_calendar_event_links.cpp \
    $${PWD}/OAICalendarEventResponseResource_relationships_user.cpp \
    $${PWD}/OAICalendarEventResponseResource_relationships_user_links.cpp \
    $${PWD}/OAICoachResource.cpp \
    $${PWD}/OAICoachResource_attributes.cpp \
    $${PWD}/OAICoachResource_links.cpp \
    $${PWD}/OAICollectionResponseLinks.cpp \
    $${PWD}/OAICreateActionRequest.cpp \
    $${PWD}/OAICreateActionResponse.cpp \
    $${PWD}/OAICreateBundleRequest.cpp \
    $${PWD}/OAICreateBundleResponse.cpp \
    $${PWD}/OAICreateCalendarEventRequest.cpp \
    $${PWD}/OAICreateCalendarEventRequest_data.cpp \
    $${PWD}/OAICreateCalendarEventRequest_data_relationships.cpp \
    $${PWD}/OAICreateCalendarEventRequest_data_relationships_owner.cpp \
    $${PWD}/OAICreateCalendarEventResponse.cpp \
    $${PWD}/OAICreateCalendarEventResponseRequest.cpp \
    $${PWD}/OAICreateCalendarEventResponseRequest_data.cpp \
    $${PWD}/OAICreateCalendarEventResponseRequest_data_relationships.cpp \
    $${PWD}/OAICreateCalendarEventResponseRequest_data_relationships_calendar_event.cpp \
    $${PWD}/OAICreateCalendarEventResponseRequest_data_relationships_user.cpp \
    $${PWD}/OAICreateGroupRequest.cpp \
    $${PWD}/OAICreateGroupResponse.cpp \
    $${PWD}/OAICreateOrUpdateErrorResponse.cpp \
    $${PWD}/OAICreateOrUpdateMetaResponse.cpp \
    $${PWD}/OAICreatePatientHealthMetricRequest.cpp \
    $${PWD}/OAICreatePatientHealthMetricRequest_meta.cpp \
    $${PWD}/OAICreatePatientHealthMetricResponse.cpp \
    $${PWD}/OAICreatePatientRequest.cpp \
    $${PWD}/OAICreatePatientRequest_meta.cpp \
    $${PWD}/OAICreatePatientResponse.cpp \
    $${PWD}/OAICreateRewardEarningFulfillmentRequest.cpp \
    $${PWD}/OAICreateRewardEarningFulfillmentResponse.cpp \
    $${PWD}/OAICreateRewardEarningRequest.cpp \
    $${PWD}/OAICreateRewardEarningResponse.cpp \
    $${PWD}/OAICreateRewardProgramActivationRequest.cpp \
    $${PWD}/OAICreateRewardProgramActivationResponse.cpp \
    $${PWD}/OAICreateRewardProgramRequest.cpp \
    $${PWD}/OAICreateRewardProgramResponse.cpp \
    $${PWD}/OAICreateRewardRequest.cpp \
    $${PWD}/OAICreateRewardResponse.cpp \
    $${PWD}/OAICreateTokenRequest.cpp \
    $${PWD}/OAICreateTokenRequest_data.cpp \
    $${PWD}/OAICreateTokenRequest_data_attributes.cpp \
    $${PWD}/OAICreateTokenResponse.cpp \
    $${PWD}/OAIEmailHistoryResource.cpp \
    $${PWD}/OAIEmailHistoryResource_attributes.cpp \
    $${PWD}/OAIEmailHistoryResource_attributes_status_times.cpp \
    $${PWD}/OAIEmailHistoryResource_relationships.cpp \
    $${PWD}/OAIEmailHistoryResource_relationships_receiver.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIError_source.cpp \
    $${PWD}/OAIFetchActionResponse.cpp \
    $${PWD}/OAIFetchBundleResponse.cpp \
    $${PWD}/OAIFetchCalendarEventResponse.cpp \
    $${PWD}/OAIFetchCalendarEventsResponse.cpp \
    $${PWD}/OAIFetchCoachResponse.cpp \
    $${PWD}/OAIFetchCoachesResponse.cpp \
    $${PWD}/OAIFetchEmailHistoriesResponse.cpp \
    $${PWD}/OAIFetchEmailHistoryResponse.cpp \
    $${PWD}/OAIFetchErrorResponse.cpp \
    $${PWD}/OAIFetchGroupResponse.cpp \
    $${PWD}/OAIFetchGroupsResponse.cpp \
    $${PWD}/OAIFetchHealthProfileAnswerResponse.cpp \
    $${PWD}/OAIFetchHealthProfileAnswersResponse.cpp \
    $${PWD}/OAIFetchHealthProfileQuestionResponse.cpp \
    $${PWD}/OAIFetchHealthProfileQuestionsResponse.cpp \
    $${PWD}/OAIFetchHealthProfileResponse.cpp \
    $${PWD}/OAIFetchHealthProfilesResponse.cpp \
    $${PWD}/OAIFetchHealthQuestionDefinitionResponse.cpp \
    $${PWD}/OAIFetchHealthQuestionDefinitionsResponse.cpp \
    $${PWD}/OAIFetchMetaResponse.cpp \
    $${PWD}/OAIFetchOrganizationResponse.cpp \
    $${PWD}/OAIFetchPatientHealthMetricResponse.cpp \
    $${PWD}/OAIFetchPatientHealthResultResponse.cpp \
    $${PWD}/OAIFetchPatientPlanSummariesResponse.cpp \
    $${PWD}/OAIFetchPatientPlanSummaryResponse.cpp \
    $${PWD}/OAIFetchPatientResponse.cpp \
    $${PWD}/OAIFetchPatientsResponse.cpp \
    $${PWD}/OAIFetchRewardEarningFulfillmentResponse.cpp \
    $${PWD}/OAIFetchRewardEarningFulfillmentsResponse.cpp \
    $${PWD}/OAIFetchRewardEarningResponse.cpp \
    $${PWD}/OAIFetchRewardEarningsResponse.cpp \
    $${PWD}/OAIFetchRewardProgramActivationResponse.cpp \
    $${PWD}/OAIFetchRewardProgramActivationsResponse.cpp \
    $${PWD}/OAIFetchRewardProgramResponse.cpp \
    $${PWD}/OAIFetchRewardProgramsResponse.cpp \
    $${PWD}/OAIFetchRewardResponse.cpp \
    $${PWD}/OAIFetchRewardsResponse.cpp \
    $${PWD}/OAIGroupResource.cpp \
    $${PWD}/OAIGroupResource_attributes.cpp \
    $${PWD}/OAIGroupResource_links.cpp \
    $${PWD}/OAIHealthProfileAnswerResource.cpp \
    $${PWD}/OAIHealthProfileAnswerResource_attributes.cpp \
    $${PWD}/OAIHealthProfileAnswerResource_attributes_history_inner.cpp \
    $${PWD}/OAIHealthProfileAnswerResource_attributes_latest.cpp \
    $${PWD}/OAIHealthProfileAnswerResource_links.cpp \
    $${PWD}/OAIHealthProfileAnswerResource_relationships.cpp \
    $${PWD}/OAIHealthProfileAnswerResource_relationships_patient.cpp \
    $${PWD}/OAIHealthProfileAnswerResource_relationships_patient_links.cpp \
    $${PWD}/OAIHealthProfileQuestionResource.cpp \
    $${PWD}/OAIHealthProfileQuestionResource_links.cpp \
    $${PWD}/OAIHealthProfileQuestionResource_relationships.cpp \
    $${PWD}/OAIHealthProfileQuestionResource_relationships_answer.cpp \
    $${PWD}/OAIHealthProfileQuestionResource_relationships_answer_links.cpp \
    $${PWD}/OAIHealthProfileQuestionResource_relationships_profile.cpp \
    $${PWD}/OAIHealthProfileQuestionResource_relationships_profile_links.cpp \
    $${PWD}/OAIHealthProfileQuestionResource_relationships_question_definition.cpp \
    $${PWD}/OAIHealthProfileQuestionResource_relationships_question_definition_links.cpp \
    $${PWD}/OAIHealthProfileQuestionResource_relationships_question_definition_links_links.cpp \
    $${PWD}/OAIHealthProfileResource.cpp \
    $${PWD}/OAIHealthProfileResource_attributes.cpp \
    $${PWD}/OAIHealthProfileResource_attributes_stats_inner.cpp \
    $${PWD}/OAIHealthProfileResource_links.cpp \
    $${PWD}/OAIHealthProfileResource_relationships.cpp \
    $${PWD}/OAIHealthProfileResource_relationships_patient.cpp \
    $${PWD}/OAIHealthProfileResource_relationships_patient_links.cpp \
    $${PWD}/OAIHealthProfileResource_relationships_questions.cpp \
    $${PWD}/OAIHealthProfileResource_relationships_questions_links.cpp \
    $${PWD}/OAIHealthQuestionDefinitionResource.cpp \
    $${PWD}/OAIHealthQuestionDefinitionResource_attributes.cpp \
    $${PWD}/OAIHealthQuestionDefinitionResource_attributes_format.cpp \
    $${PWD}/OAIHealthQuestionDefinitionResource_attributes_format_data_inner.cpp \
    $${PWD}/OAIHealthQuestionDefinitionResource_attributes_requirements_inner.cpp \
    $${PWD}/OAIHealthQuestionDefinitionResource_links.cpp \
    $${PWD}/OAIIdentifier.cpp \
    $${PWD}/OAIOrganizationResource.cpp \
    $${PWD}/OAIOrganizationResource_attributes.cpp \
    $${PWD}/OAIOrganizationResource_links.cpp \
    $${PWD}/OAIPatientCreateResource.cpp \
    $${PWD}/OAIPatientCreateResource_allOf_relationships.cpp \
    $${PWD}/OAIPatientCreateResource_allOf_relationships_coaches.cpp \
    $${PWD}/OAIPatientCreateResource_allOf_relationships_coaches_data.cpp \
    $${PWD}/OAIPatientCreateResource_allOf_relationships_coaches_links.cpp \
    $${PWD}/OAIPatientCreateResource_allOf_relationships_coaches_meta.cpp \
    $${PWD}/OAIPatientCreateResource_allOf_relationships_groups.cpp \
    $${PWD}/OAIPatientCreateResource_allOf_relationships_groups_data.cpp \
    $${PWD}/OAIPatientCreateResource_allOf_relationships_groups_meta.cpp \
    $${PWD}/OAIPatientCreateResource_allOf_relationships_groups_meta_query.cpp \
    $${PWD}/OAIPatientHealthMetricCreateResource.cpp \
    $${PWD}/OAIPatientHealthMetricResource.cpp \
    $${PWD}/OAIPatientHealthMetricResource_attributes.cpp \
    $${PWD}/OAIPatientHealthMetricResource_attributes_code.cpp \
    $${PWD}/OAIPatientHealthMetricResource_relationships.cpp \
    $${PWD}/OAIPatientHealthMetricResource_relationships_patient.cpp \
    $${PWD}/OAIPatientHealthMetricResource_relationships_patient_data.cpp \
    $${PWD}/OAIPatientHealthMetricResource_relationships_patient_data_meta.cpp \
    $${PWD}/OAIPatientHealthMetricResource_relationships_patient_data_meta_query.cpp \
    $${PWD}/OAIPatientHealthResultResource.cpp \
    $${PWD}/OAIPatientHealthResultResource_attributes.cpp \
    $${PWD}/OAIPatientHealthResultResource_attributes_annotations_inner.cpp \
    $${PWD}/OAIPatientHealthResultResource_attributes_data.cpp \
    $${PWD}/OAIPatientHealthResultResource_attributes_source.cpp \
    $${PWD}/OAIPatientHealthResultResource_relationships.cpp \
    $${PWD}/OAIPatientHealthResultResource_relationships_patient.cpp \
    $${PWD}/OAIPatientHealthResultResource_relationships_patient_data.cpp \
    $${PWD}/OAIPatientIdentifier.cpp \
    $${PWD}/OAIPatientPlanSummaryResource.cpp \
    $${PWD}/OAIPatientPlanSummaryResource_attributes.cpp \
    $${PWD}/OAIPatientPlanSummaryResource_attributes_window_notification_times.cpp \
    $${PWD}/OAIPatientPlanSummaryResource_attributes_window_order_inner.cpp \
    $${PWD}/OAIPatientPlanSummaryResource_links.cpp \
    $${PWD}/OAIPatientPlanSummaryResource_relationships.cpp \
    $${PWD}/OAIPatientPlanSummaryResource_relationships_actions.cpp \
    $${PWD}/OAIPatientPlanSummaryResource_relationships_actions_data_inner.cpp \
    $${PWD}/OAIPatientPlanSummaryResource_relationships_actions_links.cpp \
    $${PWD}/OAIPatientPlanSummaryResource_relationships_patient.cpp \
    $${PWD}/OAIPatientResource.cpp \
    $${PWD}/OAIPatientResource_attributes.cpp \
    $${PWD}/OAIPatientResource_attributes_statement.cpp \
    $${PWD}/OAIPatientResource_links.cpp \
    $${PWD}/OAIPatientResource_relationships.cpp \
    $${PWD}/OAIPatientResource_relationships_coaches.cpp \
    $${PWD}/OAIPatientResource_relationships_coaches_links.cpp \
    $${PWD}/OAIPatientResource_relationships_groups.cpp \
    $${PWD}/OAIPatientResource_relationships_groups_data_inner.cpp \
    $${PWD}/OAIPhoneNumber.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIRewardEarningFulfillmentResource.cpp \
    $${PWD}/OAIRewardEarningFulfillmentResource_attributes.cpp \
    $${PWD}/OAIRewardEarningFulfillmentResource_relationships.cpp \
    $${PWD}/OAIRewardEarningFulfillmentResource_relationships_patient.cpp \
    $${PWD}/OAIRewardEarningResource.cpp \
    $${PWD}/OAIRewardEarningResource_attributes.cpp \
    $${PWD}/OAIRewardEarningResource_relationships.cpp \
    $${PWD}/OAIRewardProgramActivationResource.cpp \
    $${PWD}/OAIRewardProgramActivationResource_attributes.cpp \
    $${PWD}/OAIRewardProgramActivationResource_relationships.cpp \
    $${PWD}/OAIRewardProgramResource.cpp \
    $${PWD}/OAIRewardProgramResource_attributes.cpp \
    $${PWD}/OAIRewardProgramResource_relationships.cpp \
    $${PWD}/OAIRewardProgramResource_relationships_group.cpp \
    $${PWD}/OAIRewardResource.cpp \
    $${PWD}/OAIRewardResource_attributes.cpp \
    $${PWD}/OAIRewardResource_relationships.cpp \
    $${PWD}/OAITokenResource.cpp \
    $${PWD}/OAITokenResource_attributes.cpp \
    $${PWD}/OAITokenResource_relationships.cpp \
    $${PWD}/OAITokenResource_relationships_groups.cpp \
    $${PWD}/OAITokenResource_relationships_groups_data_inner.cpp \
    $${PWD}/OAITokenResource_relationships_groups_links.cpp \
    $${PWD}/OAITokenResource_relationships_organization.cpp \
    $${PWD}/OAITokenResource_relationships_organization_data.cpp \
    $${PWD}/OAITokenResource_relationships_organization_links.cpp \
    $${PWD}/OAIUpdateActionRequest.cpp \
    $${PWD}/OAIUpdateActionResponse.cpp \
    $${PWD}/OAIUpdateBundleRequest.cpp \
    $${PWD}/OAIUpdateBundleResponse.cpp \
    $${PWD}/OAIUpdateCalendarEventRequest.cpp \
    $${PWD}/OAIUpdateCalendarEventRequest_data.cpp \
    $${PWD}/OAIUpdateCalendarEventRequest_data_relationships.cpp \
    $${PWD}/OAIUpdateCalendarEventRequest_data_relationships_owner.cpp \
    $${PWD}/OAIUpdateCalendarEventResponse.cpp \
    $${PWD}/OAIUpdatePatientPlanSummaryRequest.cpp \
    $${PWD}/OAIUpdatePatientPlanSummaryResponse.cpp \
    $${PWD}/OAIUpdatePatientRequest.cpp \
    $${PWD}/OAIUpdatePatientResponse.cpp \
    $${PWD}/OAIUpsertPatientRequest.cpp \
    $${PWD}/OAIUpsertPatientRequest_meta.cpp \
    $${PWD}/OAIUpsertPatientRequest_meta_query.cpp \
    $${PWD}/OAIUpsertPatientRequest_meta_query_identifier.cpp \
# APIs
    $${PWD}/OAIActionApi.cpp \
    $${PWD}/OAIBundleApi.cpp \
    $${PWD}/OAICalendarEventApi.cpp \
    $${PWD}/OAICalendarEventResponseApi.cpp \
    $${PWD}/OAICoachApi.cpp \
    $${PWD}/OAIEmailHistoryApi.cpp \
    $${PWD}/OAIGroupApi.cpp \
    $${PWD}/OAIHealthProfileApi.cpp \
    $${PWD}/OAIHealthProfileAnswerApi.cpp \
    $${PWD}/OAIHealthProfileQuestionApi.cpp \
    $${PWD}/OAIHealthQuestionDefinitionApi.cpp \
    $${PWD}/OAIMetricApi.cpp \
    $${PWD}/OAIOauthApi.cpp \
    $${PWD}/OAIOrganizationApi.cpp \
    $${PWD}/OAIPatientApi.cpp \
    $${PWD}/OAIPlanApi.cpp \
    $${PWD}/OAIResultApi.cpp \
    $${PWD}/OAIRewardApi.cpp \
    $${PWD}/OAIRewardEarningApi.cpp \
    $${PWD}/OAIRewardEarningFulfillmentApi.cpp \
    $${PWD}/OAIRewardProgramApi.cpp \
    $${PWD}/OAIRewardProgramActivationApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
