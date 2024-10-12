QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIContactsApi.h \
    $${PWD}/OAIDnsApi.h \
    $${PWD}/OAIDomainsApi.h \
    $${PWD}/OAIKeyApi.h \
    $${PWD}/OAIPodsApi.h \
    $${PWD}/OAISolarrayApi.h \
    $${PWD}/OAITicketsApi.h \
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
# APIs
    $${PWD}/OAIContactsApi.cpp \
    $${PWD}/OAIDnsApi.cpp \
    $${PWD}/OAIDomainsApi.cpp \
    $${PWD}/OAIKeyApi.cpp \
    $${PWD}/OAIPodsApi.cpp \
    $${PWD}/OAISolarrayApi.cpp \
    $${PWD}/OAITicketsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
