QT += network

HEADERS += \
# Models
    $${PWD}/OAIClusterConfigurations.h \
    $${PWD}/OAIConfigurations_List_default_response.h \
# APIs
    $${PWD}/OAIConfigurationsApi.h \
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
    $${PWD}/OAIClusterConfigurations.cpp \
    $${PWD}/OAIConfigurations_List_default_response.cpp \
# APIs
    $${PWD}/OAIConfigurationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
