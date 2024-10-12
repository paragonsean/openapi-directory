QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccessibilityState.h \
    $${PWD}/OAIDelegatedProviderOffer.h \
    $${PWD}/OAIDelegatedProviderOfferList.h \
    $${PWD}/OAIDelegatedProviderOfferProperties.h \
# APIs
    $${PWD}/OAIDelegatedProviderOffersApi.h \
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
    $${PWD}/OAIAccessibilityState.cpp \
    $${PWD}/OAIDelegatedProviderOffer.cpp \
    $${PWD}/OAIDelegatedProviderOfferList.cpp \
    $${PWD}/OAIDelegatedProviderOfferProperties.cpp \
# APIs
    $${PWD}/OAIDelegatedProviderOffersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
