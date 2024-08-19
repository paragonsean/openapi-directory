QT += network

HEADERS += \
# Models
    $${PWD}/OAILoggerCollection.h \
    $${PWD}/OAILoggerCreateParameters.h \
    $${PWD}/OAILoggerResponse.h \
    $${PWD}/OAILoggerUpdateParameters.h \
    $${PWD}/OAILoggers_ListByService_default_response.h \
    $${PWD}/OAILoggers_ListByService_default_response_details_inner.h \
# APIs
    $${PWD}/OAILoggersApi.h \
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
    $${PWD}/OAILoggerCollection.cpp \
    $${PWD}/OAILoggerCreateParameters.cpp \
    $${PWD}/OAILoggerResponse.cpp \
    $${PWD}/OAILoggerUpdateParameters.cpp \
    $${PWD}/OAILoggers_ListByService_default_response.cpp \
    $${PWD}/OAILoggers_ListByService_default_response_details_inner.cpp \
# APIs
    $${PWD}/OAILoggersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
