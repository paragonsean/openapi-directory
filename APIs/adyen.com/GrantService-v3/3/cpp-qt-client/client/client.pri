QT += network

HEADERS += \
# Models
    $${PWD}/OAIAmount.h \
    $${PWD}/OAICapitalBalance.h \
    $${PWD}/OAICapitalGrant.h \
    $${PWD}/OAICapitalGrantInfo.h \
    $${PWD}/OAICapitalGrants.h \
    $${PWD}/OAICounterparty.h \
    $${PWD}/OAIFee.h \
    $${PWD}/OAIInvalidField.h \
    $${PWD}/OAIJSONObject.h \
    $${PWD}/OAIJSONPath.h \
    $${PWD}/OAIRepayment.h \
    $${PWD}/OAIRepaymentTerm.h \
    $${PWD}/OAIRestServiceError.h \
    $${PWD}/OAIThresholdRepayment.h \
# APIs
    $${PWD}/OAICapitalApi.h \
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
    $${PWD}/OAIAmount.cpp \
    $${PWD}/OAICapitalBalance.cpp \
    $${PWD}/OAICapitalGrant.cpp \
    $${PWD}/OAICapitalGrantInfo.cpp \
    $${PWD}/OAICapitalGrants.cpp \
    $${PWD}/OAICounterparty.cpp \
    $${PWD}/OAIFee.cpp \
    $${PWD}/OAIInvalidField.cpp \
    $${PWD}/OAIJSONObject.cpp \
    $${PWD}/OAIJSONPath.cpp \
    $${PWD}/OAIRepayment.cpp \
    $${PWD}/OAIRepaymentTerm.cpp \
    $${PWD}/OAIRestServiceError.cpp \
    $${PWD}/OAIThresholdRepayment.cpp \
# APIs
    $${PWD}/OAICapitalApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
