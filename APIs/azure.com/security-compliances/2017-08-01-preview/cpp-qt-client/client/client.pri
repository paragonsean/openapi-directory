QT += network

HEADERS += \
# Models
    $${PWD}/OAICompliance.h \
    $${PWD}/OAIComplianceList.h \
    $${PWD}/OAIComplianceProperties.h \
    $${PWD}/OAIComplianceSegment.h \
    $${PWD}/OAICompliances_List_default_response.h \
    $${PWD}/OAICompliances_List_default_response_error.h \
# APIs
    $${PWD}/OAICompliancesApi.h \
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
    $${PWD}/OAICompliance.cpp \
    $${PWD}/OAIComplianceList.cpp \
    $${PWD}/OAIComplianceProperties.cpp \
    $${PWD}/OAIComplianceSegment.cpp \
    $${PWD}/OAICompliances_List_default_response.cpp \
    $${PWD}/OAICompliances_List_default_response_error.cpp \
# APIs
    $${PWD}/OAICompliancesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
