QT += network

HEADERS += \
# Models
    $${PWD}/OAILoggerCollection.h \
    $${PWD}/OAILoggerContract.h \
    $${PWD}/OAILoggerContractProperties.h \
    $${PWD}/OAILoggerUpdateContract.h \
    $${PWD}/OAILoggerUpdateParameters.h \
    $${PWD}/OAILogger_ListByService_default_response.h \
    $${PWD}/OAILogger_ListByService_default_response_error.h \
    $${PWD}/OAILogger_ListByService_default_response_error_details_inner.h \
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
    $${PWD}/OAILoggerContract.cpp \
    $${PWD}/OAILoggerContractProperties.cpp \
    $${PWD}/OAILoggerUpdateContract.cpp \
    $${PWD}/OAILoggerUpdateParameters.cpp \
    $${PWD}/OAILogger_ListByService_default_response.cpp \
    $${PWD}/OAILogger_ListByService_default_response_error.cpp \
    $${PWD}/OAILogger_ListByService_default_response_error_details_inner.cpp \
# APIs
    $${PWD}/OAILoggersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
