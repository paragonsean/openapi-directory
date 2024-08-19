QT += network

HEADERS += \
# Models
    $${PWD}/OAIBillPayAccountValidation.h \
    $${PWD}/OAIBillPayRequest.h \
    $${PWD}/OAIBillPayResponse.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIErrors.h \
# APIs
    $${PWD}/OAIRPPSPaymentValidatorAPIApi.h \
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
    $${PWD}/OAIBillPayAccountValidation.cpp \
    $${PWD}/OAIBillPayRequest.cpp \
    $${PWD}/OAIBillPayResponse.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIErrors.cpp \
# APIs
    $${PWD}/OAIRPPSPaymentValidatorAPIApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
