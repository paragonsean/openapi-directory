QT += network

HEADERS += \
# Models
    $${PWD}/OAIExpressRouteLink.h \
    $${PWD}/OAIExpressRouteLinkListResult.h \
    $${PWD}/OAIExpressRouteLinkPropertiesFormat.h \
    $${PWD}/OAIExpressRoutePort.h \
    $${PWD}/OAIExpressRoutePortListResult.h \
    $${PWD}/OAIExpressRoutePortPropertiesFormat.h \
    $${PWD}/OAIExpressRoutePortPropertiesFormat_circuits_inner.h \
    $${PWD}/OAIExpressRoutePortsLocation.h \
    $${PWD}/OAIExpressRoutePortsLocationBandwidths.h \
    $${PWD}/OAIExpressRoutePortsLocationListResult.h \
    $${PWD}/OAIExpressRoutePortsLocationPropertiesFormat.h \
    $${PWD}/OAIExpressRoutePorts_UpdateTags_request.h \
# APIs
    $${PWD}/OAIExpressRouteLinksApi.h \
    $${PWD}/OAIExpressRoutePortsApi.h \
    $${PWD}/OAIExpressRoutePortsLocationsApi.h \
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
    $${PWD}/OAIExpressRouteLink.cpp \
    $${PWD}/OAIExpressRouteLinkListResult.cpp \
    $${PWD}/OAIExpressRouteLinkPropertiesFormat.cpp \
    $${PWD}/OAIExpressRoutePort.cpp \
    $${PWD}/OAIExpressRoutePortListResult.cpp \
    $${PWD}/OAIExpressRoutePortPropertiesFormat.cpp \
    $${PWD}/OAIExpressRoutePortPropertiesFormat_circuits_inner.cpp \
    $${PWD}/OAIExpressRoutePortsLocation.cpp \
    $${PWD}/OAIExpressRoutePortsLocationBandwidths.cpp \
    $${PWD}/OAIExpressRoutePortsLocationListResult.cpp \
    $${PWD}/OAIExpressRoutePortsLocationPropertiesFormat.cpp \
    $${PWD}/OAIExpressRoutePorts_UpdateTags_request.cpp \
# APIs
    $${PWD}/OAIExpressRouteLinksApi.cpp \
    $${PWD}/OAIExpressRoutePortsApi.cpp \
    $${PWD}/OAIExpressRoutePortsLocationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
