QT += network

HEADERS += \
# Models
    $${PWD}/OAIEvent.h \
    $${PWD}/OAI_query_json_get_200_response.h \
# APIs
    $${PWD}/OAIEventsApi.h \
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
    $${PWD}/OAIEvent.cpp \
    $${PWD}/OAI_query_json_get_200_response.cpp \
# APIs
    $${PWD}/OAIEventsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
