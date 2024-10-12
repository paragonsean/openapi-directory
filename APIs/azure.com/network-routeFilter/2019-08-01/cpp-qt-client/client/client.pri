QT += network

HEADERS += \
# Models
    $${PWD}/OAIPatchRouteFilter.h \
    $${PWD}/OAIPatchRouteFilterRule.h \
    $${PWD}/OAIRouteFilter.h \
    $${PWD}/OAIRouteFilterListResult.h \
    $${PWD}/OAIRouteFilterPropertiesFormat.h \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner.h \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner_properties.h \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner_properties_connections_inner.h \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner_properties_connections_inner_properties.h \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner_properties_connections_inner_properties_expressRouteCircuitPeering.h \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner_properties_expressRouteConnection.h \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner_properties_ipv6PeeringConfig.h \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner_properties_ipv6PeeringConfig_microsoftPeeringConfig.h \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner_properties_peeredConnections_inner.h \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner_properties_peeredConnections_inner_properties.h \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner_properties_stats.h \
    $${PWD}/OAIRouteFilterRule.h \
    $${PWD}/OAIRouteFilterRuleListResult.h \
    $${PWD}/OAIRouteFilterRulePropertiesFormat.h \
# APIs
    $${PWD}/OAIRouteFilterRulesApi.h \
    $${PWD}/OAIRouteFiltersApi.h \
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
    $${PWD}/OAIPatchRouteFilter.cpp \
    $${PWD}/OAIPatchRouteFilterRule.cpp \
    $${PWD}/OAIRouteFilter.cpp \
    $${PWD}/OAIRouteFilterListResult.cpp \
    $${PWD}/OAIRouteFilterPropertiesFormat.cpp \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner.cpp \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner_properties.cpp \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner_properties_connections_inner.cpp \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner_properties_connections_inner_properties.cpp \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner_properties_connections_inner_properties_expressRouteCircuitPeering.cpp \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner_properties_expressRouteConnection.cpp \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner_properties_ipv6PeeringConfig.cpp \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner_properties_ipv6PeeringConfig_microsoftPeeringConfig.cpp \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner_properties_peeredConnections_inner.cpp \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner_properties_peeredConnections_inner_properties.cpp \
    $${PWD}/OAIRouteFilterPropertiesFormat_ipv6Peerings_inner_properties_stats.cpp \
    $${PWD}/OAIRouteFilterRule.cpp \
    $${PWD}/OAIRouteFilterRuleListResult.cpp \
    $${PWD}/OAIRouteFilterRulePropertiesFormat.cpp \
# APIs
    $${PWD}/OAIRouteFilterRulesApi.cpp \
    $${PWD}/OAIRouteFiltersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
