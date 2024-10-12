QT += network

HEADERS += \
# Models
    $${PWD}/OAIOffer.h \
    $${PWD}/OAIOfferList.h \
# APIs
    $${PWD}/OAIDelegatedProviderOffersApi.h \
    $${PWD}/OAIOffersApi.h \
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
    $${PWD}/OAIOffer.cpp \
    $${PWD}/OAIOfferList.cpp \
# APIs
    $${PWD}/OAIDelegatedProviderOffersApi.cpp \
    $${PWD}/OAIOffersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
