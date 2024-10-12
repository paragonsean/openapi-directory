QT += network

HEADERS += \
# Models
    $${PWD}/OAIConnection.h \
    $${PWD}/OAIConnectionCreateOrUpdateParameters.h \
    $${PWD}/OAIConnectionCreateOrUpdateProperties.h \
    $${PWD}/OAIConnectionListResult.h \
    $${PWD}/OAIConnectionProperties.h \
    $${PWD}/OAIConnectionTypeAssociationProperty.h \
    $${PWD}/OAIConnectionUpdateParameters.h \
    $${PWD}/OAIConnectionUpdateProperties.h \
    $${PWD}/OAIConnection_ListByAutomationAccount_default_response.h \
# APIs
    $${PWD}/OAIConnectionApi.h \
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
    $${PWD}/OAIConnection.cpp \
    $${PWD}/OAIConnectionCreateOrUpdateParameters.cpp \
    $${PWD}/OAIConnectionCreateOrUpdateProperties.cpp \
    $${PWD}/OAIConnectionListResult.cpp \
    $${PWD}/OAIConnectionProperties.cpp \
    $${PWD}/OAIConnectionTypeAssociationProperty.cpp \
    $${PWD}/OAIConnectionUpdateParameters.cpp \
    $${PWD}/OAIConnectionUpdateProperties.cpp \
    $${PWD}/OAIConnection_ListByAutomationAccount_default_response.cpp \
# APIs
    $${PWD}/OAIConnectionApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
