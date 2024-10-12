QT += network

HEADERS += \
# Models
    $${PWD}/OAIInappPurchase.h \
    $${PWD}/OAISubscriptionPurchase.h \
# APIs
    $${PWD}/OAIInapppurchasesApi.h \
    $${PWD}/OAIPurchasesApi.h \
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
    $${PWD}/OAIInappPurchase.cpp \
    $${PWD}/OAISubscriptionPurchase.cpp \
# APIs
    $${PWD}/OAIInapppurchasesApi.cpp \
    $${PWD}/OAIPurchasesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
