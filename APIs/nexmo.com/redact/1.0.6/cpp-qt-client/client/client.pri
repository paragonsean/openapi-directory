QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorInvalidId.h \
    $${PWD}/OAIErrorInvalidJson.h \
    $${PWD}/OAIErrorPrematureRedaction.h \
    $${PWD}/OAIErrorThrottled.h \
    $${PWD}/OAIErrorUnauthorized.h \
    $${PWD}/OAIErrorUnprovisioned.h \
    $${PWD}/OAIErrorUnsupportedProduct.h \
    $${PWD}/OAIRedactTransaction.h \
    $${PWD}/OAIRedact_message_403_response.h \
    $${PWD}/OAIRedact_message_422_response.h \
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
    $${PWD}/OAIErrorInvalidId.cpp \
    $${PWD}/OAIErrorInvalidJson.cpp \
    $${PWD}/OAIErrorPrematureRedaction.cpp \
    $${PWD}/OAIErrorThrottled.cpp \
    $${PWD}/OAIErrorUnauthorized.cpp \
    $${PWD}/OAIErrorUnprovisioned.cpp \
    $${PWD}/OAIErrorUnsupportedProduct.cpp \
    $${PWD}/OAIRedactTransaction.cpp \
    $${PWD}/OAIRedact_message_403_response.cpp \
    $${PWD}/OAIRedact_message_422_response.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
