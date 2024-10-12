QT += network

HEADERS += \
# Models
    $${PWD}/OAIAssessmentsMetadata_List_default_response.h \
    $${PWD}/OAIAssessmentsMetadata_List_default_response_error.h \
    $${PWD}/OAISecurityAssessmentMetadata.h \
    $${PWD}/OAISecurityAssessmentMetadataList.h \
    $${PWD}/OAISecurityAssessmentMetadataPartnerData.h \
    $${PWD}/OAISecurityAssessmentMetadataProperties.h \
# APIs
    $${PWD}/OAIAssessmentsMetadataApi.h \
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
    $${PWD}/OAIAssessmentsMetadata_List_default_response.cpp \
    $${PWD}/OAIAssessmentsMetadata_List_default_response_error.cpp \
    $${PWD}/OAISecurityAssessmentMetadata.cpp \
    $${PWD}/OAISecurityAssessmentMetadataList.cpp \
    $${PWD}/OAISecurityAssessmentMetadataPartnerData.cpp \
    $${PWD}/OAISecurityAssessmentMetadataProperties.cpp \
# APIs
    $${PWD}/OAIAssessmentsMetadataApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
