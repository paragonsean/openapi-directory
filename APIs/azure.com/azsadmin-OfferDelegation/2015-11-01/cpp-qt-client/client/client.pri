QT += network

HEADERS += \
# Models
    $${PWD}/OAIOfferDelegation.h \
    $${PWD}/OAIOfferDelegationList.h \
    $${PWD}/OAIOfferDelegationProperties.h \
# APIs
    $${PWD}/OAIOfferDelegationsApi.h \
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
    $${PWD}/OAIOfferDelegation.cpp \
    $${PWD}/OAIOfferDelegationList.cpp \
    $${PWD}/OAIOfferDelegationProperties.cpp \
# APIs
    $${PWD}/OAIOfferDelegationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
