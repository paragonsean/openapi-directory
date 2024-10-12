QT += network

HEADERS += \
# Models
    $${PWD}/OAIResourceSku.h \
    $${PWD}/OAIResourceSkuCapabilities.h \
    $${PWD}/OAIResourceSkuCapacity.h \
    $${PWD}/OAIResourceSkuCosts.h \
    $${PWD}/OAIResourceSkuLocationInfo.h \
    $${PWD}/OAIResourceSkuRestrictionInfo.h \
    $${PWD}/OAIResourceSkuRestrictions.h \
    $${PWD}/OAIResourceSkusResult.h \
# APIs
    $${PWD}/OAIAvailabilitySetsApi.h \
    $${PWD}/OAISkusApi.h \
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
    $${PWD}/OAIResourceSku.cpp \
    $${PWD}/OAIResourceSkuCapabilities.cpp \
    $${PWD}/OAIResourceSkuCapacity.cpp \
    $${PWD}/OAIResourceSkuCosts.cpp \
    $${PWD}/OAIResourceSkuLocationInfo.cpp \
    $${PWD}/OAIResourceSkuRestrictionInfo.cpp \
    $${PWD}/OAIResourceSkuRestrictions.cpp \
    $${PWD}/OAIResourceSkusResult.cpp \
# APIs
    $${PWD}/OAIAvailabilitySetsApi.cpp \
    $${PWD}/OAISkusApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
