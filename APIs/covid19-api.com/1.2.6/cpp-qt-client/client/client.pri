QT += network

HEADERS += \
# Models
    $${PWD}/OAICountry_read.h \
    $${PWD}/OAIGetDailyReportAllCountries_200_response_inner.h \
    $${PWD}/OAIGetDailyReportAllCountries_200_response_inner_province_inner.h \
    $${PWD}/OAIGetDailyReportTotals_200_response_inner.h \
    $${PWD}/OAIGetLatestCountryDataByName_200_response_inner.h \
    $${PWD}/OAIGetLatestTotals_200_response_inner.h \
    $${PWD}/OAIGetListOfCountries_200_response_inner.h \
# APIs
    $${PWD}/OAICountryApi.h \
    $${PWD}/OAIHelpApi.h \
    $${PWD}/OAITotalsApi.h \
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
    $${PWD}/OAICountry_read.cpp \
    $${PWD}/OAIGetDailyReportAllCountries_200_response_inner.cpp \
    $${PWD}/OAIGetDailyReportAllCountries_200_response_inner_province_inner.cpp \
    $${PWD}/OAIGetDailyReportTotals_200_response_inner.cpp \
    $${PWD}/OAIGetLatestCountryDataByName_200_response_inner.cpp \
    $${PWD}/OAIGetLatestTotals_200_response_inner.cpp \
    $${PWD}/OAIGetListOfCountries_200_response_inner.cpp \
# APIs
    $${PWD}/OAICountryApi.cpp \
    $${PWD}/OAIHelpApi.cpp \
    $${PWD}/OAITotalsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
