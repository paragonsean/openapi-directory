QT += network

HEADERS += \
# Models
    $${PWD}/OAIPolicyEvent.h \
    $${PWD}/OAIPolicyEventsQueryResults.h \
    $${PWD}/OAIQueryFailure.h \
    $${PWD}/OAIQueryFailure_error.h \
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
    $${PWD}/OAIPolicyEvent.cpp \
    $${PWD}/OAIPolicyEventsQueryResults.cpp \
    $${PWD}/OAIQueryFailure.cpp \
    $${PWD}/OAIQueryFailure_error.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
