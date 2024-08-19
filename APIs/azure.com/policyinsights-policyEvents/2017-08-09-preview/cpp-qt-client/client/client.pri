QT += network

HEADERS += \
# Models
    $${PWD}/OAIColumn.h \
    $${PWD}/OAIPolicyEventsQueryResults.h \
    $${PWD}/OAIPolicyEventsQueryResultsTable.h \
    $${PWD}/OAIPolicyEventsQueryResultsTable_metadata.h \
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
    $${PWD}/OAIPolicyEventsQueryResults.cpp \
    $${PWD}/OAIPolicyEventsQueryResultsTable.cpp \
    $${PWD}/OAIPolicyEventsQueryResultsTable_metadata.cpp \
    $${PWD}/OAIQueryFailure.cpp \
    $${PWD}/OAIQueryFailure_error.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
