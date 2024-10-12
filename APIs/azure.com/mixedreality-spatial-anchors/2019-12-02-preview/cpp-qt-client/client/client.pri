QT += network

HEADERS += \
# Models
    $${PWD}/OAISpatialAnchorsAccount.h \
    $${PWD}/OAISpatialAnchorsAccountPage.h \
    $${PWD}/OAISpatialAnchorsAccounts_GetKeys_200_response.h \
    $${PWD}/OAISpatialAnchorsAccounts_ListBySubscription_default_response.h \
    $${PWD}/OAISpatialAnchorsAccounts_RegenerateKeys_request.h \
# APIs
    $${PWD}/OAIKeyApi.h \
    $${PWD}/OAIProxyApi.h \
    $${PWD}/OAIResourceApi.h \
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
    $${PWD}/OAISpatialAnchorsAccount.cpp \
    $${PWD}/OAISpatialAnchorsAccountPage.cpp \
    $${PWD}/OAISpatialAnchorsAccounts_GetKeys_200_response.cpp \
    $${PWD}/OAISpatialAnchorsAccounts_ListBySubscription_default_response.cpp \
    $${PWD}/OAISpatialAnchorsAccounts_RegenerateKeys_request.cpp \
# APIs
    $${PWD}/OAIKeyApi.cpp \
    $${PWD}/OAIProxyApi.cpp \
    $${PWD}/OAIResourceApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
