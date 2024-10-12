QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAICategoriesApi.h \
    $${PWD}/OAICharityFinancialApi.h \
    $${PWD}/OAICharityPremiumApi.h \
    $${PWD}/OAIDetailsApi.h \
    $${PWD}/OAIGeoLocationApi.h \
    $${PWD}/OAISummaryApi.h \
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
# APIs
    $${PWD}/OAICategoriesApi.cpp \
    $${PWD}/OAICharityFinancialApi.cpp \
    $${PWD}/OAICharityPremiumApi.cpp \
    $${PWD}/OAIDetailsApi.cpp \
    $${PWD}/OAIGeoLocationApi.cpp \
    $${PWD}/OAISummaryApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
