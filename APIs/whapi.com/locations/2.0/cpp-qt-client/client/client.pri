QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddress.h \
    $${PWD}/OAIAddresses.h \
    $${PWD}/OAICountries.h \
    $${PWD}/OAICountry.h \
    $${PWD}/OAICurrencies.h \
    $${PWD}/OAICurrency.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAILocationsErrors.h \
# APIs
    $${PWD}/OAILocationsApi.h \
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
    $${PWD}/OAIAddress.cpp \
    $${PWD}/OAIAddresses.cpp \
    $${PWD}/OAICountries.cpp \
    $${PWD}/OAICountry.cpp \
    $${PWD}/OAICurrencies.cpp \
    $${PWD}/OAICurrency.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAILocationsErrors.cpp \
# APIs
    $${PWD}/OAILocationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
