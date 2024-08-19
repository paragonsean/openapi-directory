QT += network

HEADERS += \
# Models
    $${PWD}/OAIConnectionType.h \
    $${PWD}/OAIConnectionTypeCreateOrUpdateParameters.h \
    $${PWD}/OAIConnectionTypeCreateOrUpdateProperties.h \
    $${PWD}/OAIConnectionTypeListResult.h \
    $${PWD}/OAIConnectionTypeProperties.h \
    $${PWD}/OAIConnectionType_ListByAutomationAccount_default_response.h \
    $${PWD}/OAIFieldDefinition.h \
# APIs
    $${PWD}/OAIConnectionTypeApi.h \
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
    $${PWD}/OAIConnectionType.cpp \
    $${PWD}/OAIConnectionTypeCreateOrUpdateParameters.cpp \
    $${PWD}/OAIConnectionTypeCreateOrUpdateProperties.cpp \
    $${PWD}/OAIConnectionTypeListResult.cpp \
    $${PWD}/OAIConnectionTypeProperties.cpp \
    $${PWD}/OAIConnectionType_ListByAutomationAccount_default_response.cpp \
    $${PWD}/OAIFieldDefinition.cpp \
# APIs
    $${PWD}/OAIConnectionTypeApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
