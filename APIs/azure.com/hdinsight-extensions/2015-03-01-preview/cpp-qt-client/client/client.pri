QT += network

HEADERS += \
# Models
    $${PWD}/OAIClusterMonitoringRequest.h \
    $${PWD}/OAIClusterMonitoringResponse.h \
    $${PWD}/OAIExtension.h \
    $${PWD}/OAIExtension_GetMonitoringStatus_default_response.h \
# APIs
    $${PWD}/OAIExtensionsApi.h \
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
    $${PWD}/OAIClusterMonitoringRequest.cpp \
    $${PWD}/OAIClusterMonitoringResponse.cpp \
    $${PWD}/OAIExtension.cpp \
    $${PWD}/OAIExtension_GetMonitoringStatus_default_response.cpp \
# APIs
    $${PWD}/OAIExtensionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
