QT += network

HEADERS += \
# Models
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationDisplay.h \
    $${PWD}/OAIOperationList.h \
    $${PWD}/OAIOperations_List_default_response.h \
    $${PWD}/OAIOperations_List_default_response_error.h \
# APIs
    $${PWD}/OAIOperationsApi.h \
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
    $${PWD}/OAIOperationDisplay.cpp \
    $${PWD}/OAIOperationList.cpp \
    $${PWD}/OAIOperations_List_default_response.cpp \
    $${PWD}/OAIOperations_List_default_response_error.cpp \
# APIs
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
