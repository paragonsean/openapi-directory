QT += network

HEADERS += \
# Models
    $${PWD}/OAIGetIceServerConfigRequest.h \
    $${PWD}/OAIGetIceServerConfigResponse.h \
    $${PWD}/OAIGetIceServerConfig_request.h \
    $${PWD}/OAIIceServer.h \
    $${PWD}/OAISendAlexaOfferToMasterRequest.h \
    $${PWD}/OAISendAlexaOfferToMasterResponse.h \
    $${PWD}/OAISendAlexaOfferToMaster_request.h \
    $${PWD}/OAIService.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIGetIceServerConfigRequest.cpp \
    $${PWD}/OAIGetIceServerConfigResponse.cpp \
    $${PWD}/OAIGetIceServerConfig_request.cpp \
    $${PWD}/OAIIceServer.cpp \
    $${PWD}/OAISendAlexaOfferToMasterRequest.cpp \
    $${PWD}/OAISendAlexaOfferToMasterResponse.cpp \
    $${PWD}/OAISendAlexaOfferToMaster_request.cpp \
    $${PWD}/OAIService.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
