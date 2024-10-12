QT += network

HEADERS += \
# Models
# APIs
    $${PWD}/OAIBaggageApi.h \
    $${PWD}/OAIOffersApi.h \
    $${PWD}/OAIOrdersApi.h \
    $${PWD}/OAIPreflightApi.h \
    $${PWD}/OAIPromotionsApi.h \
    $${PWD}/OAIReferenceDataApi.h \
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
    $${PWD}/OAIBaggageApi.cpp \
    $${PWD}/OAIOffersApi.cpp \
    $${PWD}/OAIOrdersApi.cpp \
    $${PWD}/OAIPreflightApi.cpp \
    $${PWD}/OAIPromotionsApi.cpp \
    $${PWD}/OAIReferenceDataApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
