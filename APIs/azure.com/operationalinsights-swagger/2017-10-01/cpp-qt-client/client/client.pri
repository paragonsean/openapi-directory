QT += network

HEADERS += \
# Models
    $${PWD}/OAIColumn.h \
    $${PWD}/OAIErrorDetail.h \
    $${PWD}/OAIErrorInfo.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIQueryBody.h \
    $${PWD}/OAIQueryResults.h \
    $${PWD}/OAITable.h \
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
    $${PWD}/OAIErrorDetail.cpp \
    $${PWD}/OAIErrorInfo.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIQueryBody.cpp \
    $${PWD}/OAIQueryResults.cpp \
    $${PWD}/OAITable.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
