QT += network

HEADERS += \
# Models
    $${PWD}/OAIColumn.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperation_display.h \
    $${PWD}/OAIOperationsListResults.h \
    $${PWD}/OAIPolicyStatesQueryResults.h \
    $${PWD}/OAIPolicyStatesQueryResultsTable.h \
    $${PWD}/OAIPolicyStatesQueryResultsTable_metadata.h \
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
    $${PWD}/OAIColumn.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperation_display.cpp \
    $${PWD}/OAIOperationsListResults.cpp \
    $${PWD}/OAIPolicyStatesQueryResults.cpp \
    $${PWD}/OAIPolicyStatesQueryResultsTable.cpp \
    $${PWD}/OAIPolicyStatesQueryResultsTable_metadata.cpp \
    $${PWD}/OAIQueryFailure.cpp \
    $${PWD}/OAIQueryFailure_error.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
