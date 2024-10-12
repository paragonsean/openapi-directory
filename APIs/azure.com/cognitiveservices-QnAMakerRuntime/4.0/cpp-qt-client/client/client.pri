QT += network

HEADERS += \
# Models
    $${PWD}/OAIContextDTO.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorCode.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIFeedbackRecordDTO.h \
    $${PWD}/OAIFeedbackRecordsDTO.h \
    $${PWD}/OAIInnerErrorModel.h \
    $${PWD}/OAIMetadataDTO.h \
    $${PWD}/OAIPromptDTO.h \
    $${PWD}/OAIQnADTO.h \
    $${PWD}/OAIQnASearchResult.h \
    $${PWD}/OAIQnASearchResultList.h \
    $${PWD}/OAIQueryContextDTO.h \
    $${PWD}/OAIQueryDTO.h \
# APIs
    $${PWD}/OAIKnowledgebasesApi.h \
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
    $${PWD}/OAIContextDTO.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorCode.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIFeedbackRecordDTO.cpp \
    $${PWD}/OAIFeedbackRecordsDTO.cpp \
    $${PWD}/OAIInnerErrorModel.cpp \
    $${PWD}/OAIMetadataDTO.cpp \
    $${PWD}/OAIPromptDTO.cpp \
    $${PWD}/OAIQnADTO.cpp \
    $${PWD}/OAIQnASearchResult.cpp \
    $${PWD}/OAIQnASearchResultList.cpp \
    $${PWD}/OAIQueryContextDTO.cpp \
    $${PWD}/OAIQueryDTO.cpp \
# APIs
    $${PWD}/OAIKnowledgebasesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
