QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorDefinition.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIMultipleActivationKey.h \
    $${PWD}/OAIMultipleActivationKeyList.h \
    $${PWD}/OAIMultipleActivationKeyUpdate.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationDisplay.h \
    $${PWD}/OAIOperationList.h \
# APIs
    $${PWD}/OAIMultipleActivationKeysApi.h \
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
    $${PWD}/OAIErrorDefinition.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIMultipleActivationKey.cpp \
    $${PWD}/OAIMultipleActivationKeyList.cpp \
    $${PWD}/OAIMultipleActivationKeyUpdate.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationDisplay.cpp \
    $${PWD}/OAIOperationList.cpp \
# APIs
    $${PWD}/OAIMultipleActivationKeysApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
