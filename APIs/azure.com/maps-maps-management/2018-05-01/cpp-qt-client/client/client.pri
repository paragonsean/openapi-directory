QT += network

HEADERS += \
# Models
    $${PWD}/OAIError.h \
    $${PWD}/OAIError_details_inner.h \
    $${PWD}/OAIMapsAccount.h \
    $${PWD}/OAIMapsAccountCreateParameters.h \
    $${PWD}/OAIMapsAccountKeys.h \
    $${PWD}/OAIMapsAccountProperties.h \
    $${PWD}/OAIMapsAccountUpdateParameters.h \
    $${PWD}/OAIMapsAccounts.h \
    $${PWD}/OAIMapsAccountsMoveRequest.h \
    $${PWD}/OAIMapsKeySpecification.h \
    $${PWD}/OAIMapsOperations.h \
    $${PWD}/OAIMapsOperations_value_inner.h \
    $${PWD}/OAIMapsOperations_value_inner_display.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAISku.h \
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
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIError_details_inner.cpp \
    $${PWD}/OAIMapsAccount.cpp \
    $${PWD}/OAIMapsAccountCreateParameters.cpp \
    $${PWD}/OAIMapsAccountKeys.cpp \
    $${PWD}/OAIMapsAccountProperties.cpp \
    $${PWD}/OAIMapsAccountUpdateParameters.cpp \
    $${PWD}/OAIMapsAccounts.cpp \
    $${PWD}/OAIMapsAccountsMoveRequest.cpp \
    $${PWD}/OAIMapsKeySpecification.cpp \
    $${PWD}/OAIMapsOperations.cpp \
    $${PWD}/OAIMapsOperations_value_inner.cpp \
    $${PWD}/OAIMapsOperations_value_inner_display.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAISku.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
