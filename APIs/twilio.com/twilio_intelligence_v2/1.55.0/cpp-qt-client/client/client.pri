QT += network

HEADERS += \
# Models
    $${PWD}/OAIIntelligence_v2_service.h \
    $${PWD}/OAIIntelligence_v2_transcript.h \
    $${PWD}/OAIIntelligence_v2_transcript_media.h \
    $${PWD}/OAIIntelligence_v2_transcript_operator_result.h \
    $${PWD}/OAIIntelligence_v2_transcript_sentence.h \
    $${PWD}/OAIListOperatorResultResponse.h \
    $${PWD}/OAIListSentenceResponse.h \
    $${PWD}/OAIListServiceResponse.h \
    $${PWD}/OAIListServiceResponse_meta.h \
    $${PWD}/OAIListTranscriptResponse.h \
    $${PWD}/OAIOperator_result_enum_operator_type.h \
    $${PWD}/OAIService_enum_http_method.h \
    $${PWD}/OAITranscript_enum_call_direction.h \
    $${PWD}/OAITranscript_enum_status.h \
# APIs
    $${PWD}/OAIIntelligenceV2MediaApi.h \
    $${PWD}/OAIIntelligenceV2OperatorResultApi.h \
    $${PWD}/OAIIntelligenceV2SentenceApi.h \
    $${PWD}/OAIIntelligenceV2ServiceApi.h \
    $${PWD}/OAIIntelligenceV2TranscriptApi.h \
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
    $${PWD}/OAIIntelligence_v2_service.cpp \
    $${PWD}/OAIIntelligence_v2_transcript.cpp \
    $${PWD}/OAIIntelligence_v2_transcript_media.cpp \
    $${PWD}/OAIIntelligence_v2_transcript_operator_result.cpp \
    $${PWD}/OAIIntelligence_v2_transcript_sentence.cpp \
    $${PWD}/OAIListOperatorResultResponse.cpp \
    $${PWD}/OAIListSentenceResponse.cpp \
    $${PWD}/OAIListServiceResponse.cpp \
    $${PWD}/OAIListServiceResponse_meta.cpp \
    $${PWD}/OAIListTranscriptResponse.cpp \
    $${PWD}/OAIOperator_result_enum_operator_type.cpp \
    $${PWD}/OAIService_enum_http_method.cpp \
    $${PWD}/OAITranscript_enum_call_direction.cpp \
    $${PWD}/OAITranscript_enum_status.cpp \
# APIs
    $${PWD}/OAIIntelligenceV2MediaApi.cpp \
    $${PWD}/OAIIntelligenceV2OperatorResultApi.cpp \
    $${PWD}/OAIIntelligenceV2SentenceApi.cpp \
    $${PWD}/OAIIntelligenceV2ServiceApi.cpp \
    $${PWD}/OAIIntelligenceV2TranscriptApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
