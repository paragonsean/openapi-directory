QT += network

HEADERS += \
# Models
    $${PWD}/OAIExpressRouteCircuitReference.h \
    $${PWD}/OAIExpressRouteCrossConnection.h \
    $${PWD}/OAIExpressRouteCrossConnectionListResult.h \
    $${PWD}/OAIExpressRouteCrossConnectionPeering.h \
    $${PWD}/OAIExpressRouteCrossConnectionPeeringList.h \
    $${PWD}/OAIExpressRouteCrossConnectionPeeringProperties.h \
    $${PWD}/OAIExpressRouteCrossConnectionPeeringProperties_ipv6PeeringConfig.h \
    $${PWD}/OAIExpressRouteCrossConnectionPeeringProperties_ipv6PeeringConfig_microsoftPeeringConfig.h \
    $${PWD}/OAIExpressRouteCrossConnectionPeeringProperties_ipv6PeeringConfig_routeFilter.h \
    $${PWD}/OAIExpressRouteCrossConnectionProperties.h \
    $${PWD}/OAIExpressRouteCrossConnectionRoutesTableSummary.h \
    $${PWD}/OAIExpressRouteCrossConnectionsRoutesTableSummaryListResult.h \
    $${PWD}/OAIExpressRouteCrossConnections_ListArpTable_200_response.h \
    $${PWD}/OAIExpressRouteCrossConnections_ListArpTable_200_response_value_inner.h \
    $${PWD}/OAIExpressRouteCrossConnections_ListRoutesTable_200_response.h \
    $${PWD}/OAIExpressRouteCrossConnections_ListRoutesTable_200_response_value_inner.h \
    $${PWD}/OAIExpressRouteCrossConnections_UpdateTags_request.h \
# APIs
    $${PWD}/OAIExpressRouteCrossConnectionArpTableApi.h \
    $${PWD}/OAIExpressRouteCrossConnectionPeeringsApi.h \
    $${PWD}/OAIExpressRouteCrossConnectionRouteTableApi.h \
    $${PWD}/OAIExpressRouteCrossConnectionRouteTableSummaryApi.h \
    $${PWD}/OAIExpressRouteCrossConnectionsApi.h \
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
    $${PWD}/OAIExpressRouteCircuitReference.cpp \
    $${PWD}/OAIExpressRouteCrossConnection.cpp \
    $${PWD}/OAIExpressRouteCrossConnectionListResult.cpp \
    $${PWD}/OAIExpressRouteCrossConnectionPeering.cpp \
    $${PWD}/OAIExpressRouteCrossConnectionPeeringList.cpp \
    $${PWD}/OAIExpressRouteCrossConnectionPeeringProperties.cpp \
    $${PWD}/OAIExpressRouteCrossConnectionPeeringProperties_ipv6PeeringConfig.cpp \
    $${PWD}/OAIExpressRouteCrossConnectionPeeringProperties_ipv6PeeringConfig_microsoftPeeringConfig.cpp \
    $${PWD}/OAIExpressRouteCrossConnectionPeeringProperties_ipv6PeeringConfig_routeFilter.cpp \
    $${PWD}/OAIExpressRouteCrossConnectionProperties.cpp \
    $${PWD}/OAIExpressRouteCrossConnectionRoutesTableSummary.cpp \
    $${PWD}/OAIExpressRouteCrossConnectionsRoutesTableSummaryListResult.cpp \
    $${PWD}/OAIExpressRouteCrossConnections_ListArpTable_200_response.cpp \
    $${PWD}/OAIExpressRouteCrossConnections_ListArpTable_200_response_value_inner.cpp \
    $${PWD}/OAIExpressRouteCrossConnections_ListRoutesTable_200_response.cpp \
    $${PWD}/OAIExpressRouteCrossConnections_ListRoutesTable_200_response_value_inner.cpp \
    $${PWD}/OAIExpressRouteCrossConnections_UpdateTags_request.cpp \
# APIs
    $${PWD}/OAIExpressRouteCrossConnectionArpTableApi.cpp \
    $${PWD}/OAIExpressRouteCrossConnectionPeeringsApi.cpp \
    $${PWD}/OAIExpressRouteCrossConnectionRouteTableApi.cpp \
    $${PWD}/OAIExpressRouteCrossConnectionRouteTableSummaryApi.cpp \
    $${PWD}/OAIExpressRouteCrossConnectionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
