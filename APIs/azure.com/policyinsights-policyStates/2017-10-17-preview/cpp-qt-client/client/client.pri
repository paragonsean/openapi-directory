QT += network

HEADERS += \
# Models
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIOperationsListResults.h \
    $${PWD}/OAIPolicyState.h \
    $${PWD}/OAIPolicyStatesQueryResults.h \
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
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIOperationsListResults.cpp \
    $${PWD}/OAIPolicyState.cpp \
    $${PWD}/OAIPolicyStatesQueryResults.cpp \
    $${PWD}/OAIQueryFailure.cpp \
    $${PWD}/OAIQueryFailure_error.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
