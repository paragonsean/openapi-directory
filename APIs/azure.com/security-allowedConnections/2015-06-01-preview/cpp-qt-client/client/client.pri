QT += network

HEADERS += \
# Models
    $${PWD}/OAIAllowedConnectionsList.h \
    $${PWD}/OAIAllowedConnectionsResource.h \
    $${PWD}/OAIAllowedConnectionsResourceProperties.h \
    $${PWD}/OAIAllowedConnections_List_default_response.h \
    $${PWD}/OAIAllowedConnections_List_default_response_error.h \
    $${PWD}/OAIConnectableResource.h \
    $${PWD}/OAIConnectedResource.h \
# APIs
    $${PWD}/OAIAllowedConnectionsApi.h \
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
    $${PWD}/OAIAllowedConnectionsList.cpp \
    $${PWD}/OAIAllowedConnectionsResource.cpp \
    $${PWD}/OAIAllowedConnectionsResourceProperties.cpp \
    $${PWD}/OAIAllowedConnections_List_default_response.cpp \
    $${PWD}/OAIAllowedConnections_List_default_response_error.cpp \
    $${PWD}/OAIConnectableResource.cpp \
    $${PWD}/OAIConnectedResource.cpp \
# APIs
    $${PWD}/OAIAllowedConnectionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
