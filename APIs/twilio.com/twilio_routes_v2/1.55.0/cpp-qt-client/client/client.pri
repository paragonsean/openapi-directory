QT += network

HEADERS += \
# Models
    $${PWD}/OAIRoutes_v2_phone_number.h \
    $${PWD}/OAIRoutes_v2_sip_domain.h \
    $${PWD}/OAIRoutes_v2_trunks.h \
# APIs
    $${PWD}/OAIRoutesV2PhoneNumberApi.h \
    $${PWD}/OAIRoutesV2SipDomainApi.h \
    $${PWD}/OAIRoutesV2TrunkApi.h \
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
    $${PWD}/OAIRoutes_v2_phone_number.cpp \
    $${PWD}/OAIRoutes_v2_sip_domain.cpp \
    $${PWD}/OAIRoutes_v2_trunks.cpp \
# APIs
    $${PWD}/OAIRoutesV2PhoneNumberApi.cpp \
    $${PWD}/OAIRoutesV2SipDomainApi.cpp \
    $${PWD}/OAIRoutesV2TrunkApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
