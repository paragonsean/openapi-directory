QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIEventData.h \
    $${PWD}/OAIEventDataCollection.h \
    $${PWD}/OAIHttpRequestInfo.h \
    $${PWD}/OAILocalizableString.h \
    $${PWD}/OAISenderAuthorization.h \
# APIs
    $${PWD}/OAIActivityLogsApi.h \
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
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIEventData.cpp \
    $${PWD}/OAIEventDataCollection.cpp \
    $${PWD}/OAIHttpRequestInfo.cpp \
    $${PWD}/OAILocalizableString.cpp \
    $${PWD}/OAISenderAuthorization.cpp \
# APIs
    $${PWD}/OAIActivityLogsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
