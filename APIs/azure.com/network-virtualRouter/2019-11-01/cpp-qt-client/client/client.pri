QT += network

HEADERS += \
# Models
    $${PWD}/OAIVirtualRouter.h \
    $${PWD}/OAIVirtualRouterListResult.h \
    $${PWD}/OAIVirtualRouterPeering.h \
    $${PWD}/OAIVirtualRouterPeeringListResult.h \
    $${PWD}/OAIVirtualRouterPeeringProperties.h \
    $${PWD}/OAIVirtualRouterPropertiesFormat.h \
    $${PWD}/OAIVirtualRouterPropertiesFormat_hostedGateway.h \
    $${PWD}/OAIVirtualRouters_List_default_response.h \
    $${PWD}/OAIVirtualRouters_List_default_response_details_inner.h \
# APIs
    $${PWD}/OAIVirtualRouterPeeringsApi.h \
    $${PWD}/OAIVirtualRoutersApi.h \
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
    $${PWD}/OAIVirtualRouter.cpp \
    $${PWD}/OAIVirtualRouterListResult.cpp \
    $${PWD}/OAIVirtualRouterPeering.cpp \
    $${PWD}/OAIVirtualRouterPeeringListResult.cpp \
    $${PWD}/OAIVirtualRouterPeeringProperties.cpp \
    $${PWD}/OAIVirtualRouterPropertiesFormat.cpp \
    $${PWD}/OAIVirtualRouterPropertiesFormat_hostedGateway.cpp \
    $${PWD}/OAIVirtualRouters_List_default_response.cpp \
    $${PWD}/OAIVirtualRouters_List_default_response_details_inner.cpp \
# APIs
    $${PWD}/OAIVirtualRouterPeeringsApi.cpp \
    $${PWD}/OAIVirtualRoutersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
