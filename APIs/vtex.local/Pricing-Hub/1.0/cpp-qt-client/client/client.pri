QT += network

HEADERS += \
# Models
    $${PWD}/OAIConfigExternalPriceSourceRequest.h \
    $${PWD}/OAIGetPricesRequestObject.h \
    $${PWD}/OAIItem1.h \
    $${PWD}/OAIItems_inner.h \
    $${PWD}/OAIResponse2.h \
# APIs
    $${PWD}/OAIPricingHubPricesApi.h \
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
    $${PWD}/OAIConfigExternalPriceSourceRequest.cpp \
    $${PWD}/OAIGetPricesRequestObject.cpp \
    $${PWD}/OAIItem1.cpp \
    $${PWD}/OAIItems_inner.cpp \
    $${PWD}/OAIResponse2.cpp \
# APIs
    $${PWD}/OAIPricingHubPricesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
