QT += network

HEADERS += \
# Models
    $${PWD}/OAIComplianceResult.h \
    $${PWD}/OAIComplianceResultList.h \
    $${PWD}/OAIComplianceResultProperties.h \
    $${PWD}/OAIComplianceResults_Get_default_response.h \
    $${PWD}/OAIComplianceResults_Get_default_response_error.h \
# APIs
    $${PWD}/OAIComplianceResultsApi.h \
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
    $${PWD}/OAIComplianceResult.cpp \
    $${PWD}/OAIComplianceResultList.cpp \
    $${PWD}/OAIComplianceResultProperties.cpp \
    $${PWD}/OAIComplianceResults_Get_default_response.cpp \
    $${PWD}/OAIComplianceResults_Get_default_response_error.cpp \
# APIs
    $${PWD}/OAIComplianceResultsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
