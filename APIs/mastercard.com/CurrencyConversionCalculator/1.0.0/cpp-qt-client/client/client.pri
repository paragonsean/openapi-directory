QT += network

HEADERS += \
# Models
    $${PWD}/OAIConversion.h \
    $${PWD}/OAIConversionRateRequest.h \
    $${PWD}/OAICurrency.h \
    $${PWD}/OAISettlementCurrency.h \
    $${PWD}/OAISettlementCurrencyRequest.h \
    $${PWD}/OAISettlementRateIssued.h \
    $${PWD}/OAISettlementRateIssuedRequest.h \
# APIs
    $${PWD}/OAIConversionRateApi.h \
    $${PWD}/OAICurrenciesApi.h \
    $${PWD}/OAIRateIssuedApi.h \
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
    $${PWD}/OAIConversion.cpp \
    $${PWD}/OAIConversionRateRequest.cpp \
    $${PWD}/OAICurrency.cpp \
    $${PWD}/OAISettlementCurrency.cpp \
    $${PWD}/OAISettlementCurrencyRequest.cpp \
    $${PWD}/OAISettlementRateIssued.cpp \
    $${PWD}/OAISettlementRateIssuedRequest.cpp \
# APIs
    $${PWD}/OAIConversionRateApi.cpp \
    $${PWD}/OAICurrenciesApi.cpp \
    $${PWD}/OAIRateIssuedApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
