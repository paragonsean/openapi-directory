QT += network

HEADERS += \
# Models
    $${PWD}/OAIBadRequestException.h \
    $${PWD}/OAIEvent.h \
    $${PWD}/OAIEvent_session.h \
    $${PWD}/OAIPutEventsInput.h \
    $${PWD}/OAIPutEvents_request.h \
    $${PWD}/OAISession.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIBadRequestException.cpp \
    $${PWD}/OAIEvent.cpp \
    $${PWD}/OAIEvent_session.cpp \
    $${PWD}/OAIPutEventsInput.cpp \
    $${PWD}/OAIPutEvents_request.cpp \
    $${PWD}/OAISession.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
