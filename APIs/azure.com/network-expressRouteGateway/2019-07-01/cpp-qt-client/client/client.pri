QT += network

HEADERS += \
# Models
    $${PWD}/OAIExpressRouteCircuitPeeringId.h \
    $${PWD}/OAIExpressRouteConnection.h \
    $${PWD}/OAIExpressRouteConnectionId.h \
    $${PWD}/OAIExpressRouteConnectionList.h \
    $${PWD}/OAIExpressRouteConnectionProperties.h \
    $${PWD}/OAIExpressRouteGateway.h \
    $${PWD}/OAIExpressRouteGatewayList.h \
    $${PWD}/OAIExpressRouteGatewayProperties.h \
    $${PWD}/OAIExpressRouteGatewayProperties_autoScaleConfiguration.h \
    $${PWD}/OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds.h \
    $${PWD}/OAIVirtualHubId.h \
# APIs
    $${PWD}/OAIExpressRouteConnectionsApi.h \
    $${PWD}/OAIExpressRouteGatewaysApi.h \
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
    $${PWD}/OAIExpressRouteCircuitPeeringId.cpp \
    $${PWD}/OAIExpressRouteConnection.cpp \
    $${PWD}/OAIExpressRouteConnectionId.cpp \
    $${PWD}/OAIExpressRouteConnectionList.cpp \
    $${PWD}/OAIExpressRouteConnectionProperties.cpp \
    $${PWD}/OAIExpressRouteGateway.cpp \
    $${PWD}/OAIExpressRouteGatewayList.cpp \
    $${PWD}/OAIExpressRouteGatewayProperties.cpp \
    $${PWD}/OAIExpressRouteGatewayProperties_autoScaleConfiguration.cpp \
    $${PWD}/OAIExpressRouteGatewayProperties_autoScaleConfiguration_bounds.cpp \
    $${PWD}/OAIVirtualHubId.cpp \
# APIs
    $${PWD}/OAIExpressRouteConnectionsApi.cpp \
    $${PWD}/OAIExpressRouteGatewaysApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
