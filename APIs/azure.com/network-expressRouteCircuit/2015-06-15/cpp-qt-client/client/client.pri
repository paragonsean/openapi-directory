QT += network

HEADERS += \
# Models
    $${PWD}/OAIAuthorizationListResult.h \
    $${PWD}/OAIAuthorizationPropertiesFormat.h \
    $${PWD}/OAIExpressRouteCircuit.h \
    $${PWD}/OAIExpressRouteCircuitArpTable.h \
    $${PWD}/OAIExpressRouteCircuitAuthorization.h \
    $${PWD}/OAIExpressRouteCircuitListResult.h \
    $${PWD}/OAIExpressRouteCircuitPeering.h \
    $${PWD}/OAIExpressRouteCircuitPeeringConfig.h \
    $${PWD}/OAIExpressRouteCircuitPeeringListResult.h \
    $${PWD}/OAIExpressRouteCircuitPeeringPropertiesFormat.h \
    $${PWD}/OAIExpressRouteCircuitPropertiesFormat.h \
    $${PWD}/OAIExpressRouteCircuitRoutesTable.h \
    $${PWD}/OAIExpressRouteCircuitServiceProviderProperties.h \
    $${PWD}/OAIExpressRouteCircuitSku.h \
    $${PWD}/OAIExpressRouteCircuitStats.h \
    $${PWD}/OAIExpressRouteCircuitsArpTableListResult.h \
    $${PWD}/OAIExpressRouteCircuitsRoutesTableListResult.h \
    $${PWD}/OAIExpressRouteCircuitsStatsListResult.h \
    $${PWD}/OAIExpressRouteServiceProvider.h \
    $${PWD}/OAIExpressRouteServiceProviderBandwidthsOffered.h \
    $${PWD}/OAIExpressRouteServiceProviderListResult.h \
    $${PWD}/OAIExpressRouteServiceProviderPropertiesFormat.h \
# APIs
    $${PWD}/OAIExpressRouteCircuitAuthorizationsApi.h \
    $${PWD}/OAIExpressRouteCircuitPeeringsApi.h \
    $${PWD}/OAIExpressRouteCircuitStatsApi.h \
    $${PWD}/OAIExpressRouteCircuitsApi.h \
    $${PWD}/OAIExpressRouteServiceProvidersApi.h \
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
    $${PWD}/OAIAuthorizationListResult.cpp \
    $${PWD}/OAIAuthorizationPropertiesFormat.cpp \
    $${PWD}/OAIExpressRouteCircuit.cpp \
    $${PWD}/OAIExpressRouteCircuitArpTable.cpp \
    $${PWD}/OAIExpressRouteCircuitAuthorization.cpp \
    $${PWD}/OAIExpressRouteCircuitListResult.cpp \
    $${PWD}/OAIExpressRouteCircuitPeering.cpp \
    $${PWD}/OAIExpressRouteCircuitPeeringConfig.cpp \
    $${PWD}/OAIExpressRouteCircuitPeeringListResult.cpp \
    $${PWD}/OAIExpressRouteCircuitPeeringPropertiesFormat.cpp \
    $${PWD}/OAIExpressRouteCircuitPropertiesFormat.cpp \
    $${PWD}/OAIExpressRouteCircuitRoutesTable.cpp \
    $${PWD}/OAIExpressRouteCircuitServiceProviderProperties.cpp \
    $${PWD}/OAIExpressRouteCircuitSku.cpp \
    $${PWD}/OAIExpressRouteCircuitStats.cpp \
    $${PWD}/OAIExpressRouteCircuitsArpTableListResult.cpp \
    $${PWD}/OAIExpressRouteCircuitsRoutesTableListResult.cpp \
    $${PWD}/OAIExpressRouteCircuitsStatsListResult.cpp \
    $${PWD}/OAIExpressRouteServiceProvider.cpp \
    $${PWD}/OAIExpressRouteServiceProviderBandwidthsOffered.cpp \
    $${PWD}/OAIExpressRouteServiceProviderListResult.cpp \
    $${PWD}/OAIExpressRouteServiceProviderPropertiesFormat.cpp \
# APIs
    $${PWD}/OAIExpressRouteCircuitAuthorizationsApi.cpp \
    $${PWD}/OAIExpressRouteCircuitPeeringsApi.cpp \
    $${PWD}/OAIExpressRouteCircuitStatsApi.cpp \
    $${PWD}/OAIExpressRouteCircuitsApi.cpp \
    $${PWD}/OAIExpressRouteServiceProvidersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
