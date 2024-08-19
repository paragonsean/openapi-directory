QT += network

HEADERS += \
# Models
    $${PWD}/OAIRegulatoryComplianceAssessment.h \
    $${PWD}/OAIRegulatoryComplianceAssessmentList.h \
    $${PWD}/OAIRegulatoryComplianceAssessmentProperties.h \
    $${PWD}/OAIRegulatoryComplianceControl.h \
    $${PWD}/OAIRegulatoryComplianceControlList.h \
    $${PWD}/OAIRegulatoryComplianceControlProperties.h \
    $${PWD}/OAIRegulatoryComplianceStandard.h \
    $${PWD}/OAIRegulatoryComplianceStandardList.h \
    $${PWD}/OAIRegulatoryComplianceStandardProperties.h \
    $${PWD}/OAIRegulatoryComplianceStandards_List_default_response.h \
    $${PWD}/OAIRegulatoryComplianceStandards_List_default_response_error.h \
# APIs
    $${PWD}/OAIRegulatoryComplianceApi.h \
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
    $${PWD}/OAIRegulatoryComplianceAssessment.cpp \
    $${PWD}/OAIRegulatoryComplianceAssessmentList.cpp \
    $${PWD}/OAIRegulatoryComplianceAssessmentProperties.cpp \
    $${PWD}/OAIRegulatoryComplianceControl.cpp \
    $${PWD}/OAIRegulatoryComplianceControlList.cpp \
    $${PWD}/OAIRegulatoryComplianceControlProperties.cpp \
    $${PWD}/OAIRegulatoryComplianceStandard.cpp \
    $${PWD}/OAIRegulatoryComplianceStandardList.cpp \
    $${PWD}/OAIRegulatoryComplianceStandardProperties.cpp \
    $${PWD}/OAIRegulatoryComplianceStandards_List_default_response.cpp \
    $${PWD}/OAIRegulatoryComplianceStandards_List_default_response_error.cpp \
# APIs
    $${PWD}/OAIRegulatoryComplianceApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
