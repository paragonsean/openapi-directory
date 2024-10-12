QT += network

HEADERS += \
# Models
    $${PWD}/OAIServerCommunicationLink.h \
    $${PWD}/OAIServerCommunicationLinkListResult.h \
    $${PWD}/OAIServerCommunicationLinkProperties.h \
# APIs
    $${PWD}/OAIServerCommunicationLinksApi.h \
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
    $${PWD}/OAIServerCommunicationLink.cpp \
    $${PWD}/OAIServerCommunicationLinkListResult.cpp \
    $${PWD}/OAIServerCommunicationLinkProperties.cpp \
# APIs
    $${PWD}/OAIServerCommunicationLinksApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
