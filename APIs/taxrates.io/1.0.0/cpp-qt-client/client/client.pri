QT += network

HEADERS += \
# Models
    $${PWD}/OAIAllTaxRates_200_response_inner.h \
    $${PWD}/OAIAllTaxRates_200_response_inner_rates_inner.h \
    $${PWD}/OAITaxRatesByCountryCode_200_response.h \
    $${PWD}/OAITaxRatesByCountryCode_200_response_taxes_inner.h \
    $${PWD}/OAITaxRatesByCountryCode_500_response.h \
# APIs
    $${PWD}/OAIV1TaxApi.h \
    $${PWD}/OAIV3TaxApi.h \
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
    $${PWD}/OAIAllTaxRates_200_response_inner.cpp \
    $${PWD}/OAIAllTaxRates_200_response_inner_rates_inner.cpp \
    $${PWD}/OAITaxRatesByCountryCode_200_response.cpp \
    $${PWD}/OAITaxRatesByCountryCode_200_response_taxes_inner.cpp \
    $${PWD}/OAITaxRatesByCountryCode_500_response.cpp \
# APIs
    $${PWD}/OAIV1TaxApi.cpp \
    $${PWD}/OAIV3TaxApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
