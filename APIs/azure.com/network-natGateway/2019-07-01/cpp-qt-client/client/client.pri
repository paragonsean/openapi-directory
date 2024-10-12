QT += network

HEADERS += \
# Models
    $${PWD}/OAINatGateway.h \
    $${PWD}/OAINatGatewayListResult.h \
    $${PWD}/OAINatGatewayPropertiesFormat.h \
    $${PWD}/OAINatGatewayPropertiesFormat_publicIpAddresses_inner.h \
    $${PWD}/OAINatGatewaySku.h \
    $${PWD}/OAINatGateways_UpdateTags_request.h \
# APIs
    $${PWD}/OAINatGatewaysApi.h \
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
    $${PWD}/OAINatGateway.cpp \
    $${PWD}/OAINatGatewayListResult.cpp \
    $${PWD}/OAINatGatewayPropertiesFormat.cpp \
    $${PWD}/OAINatGatewayPropertiesFormat_publicIpAddresses_inner.cpp \
    $${PWD}/OAINatGatewaySku.cpp \
    $${PWD}/OAINatGateways_UpdateTags_request.cpp \
# APIs
    $${PWD}/OAINatGatewaysApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
