QT += network

HEADERS += \
# Models
    $${PWD}/OAIEdgeGatewayPool.h \
    $${PWD}/OAIEdgeGatewayPoolList.h \
    $${PWD}/OAIEdgeGatewayPoolModel.h \
# APIs
    $${PWD}/OAIEdgeGatewayPoolsApi.h \
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
    $${PWD}/OAIEdgeGatewayPool.cpp \
    $${PWD}/OAIEdgeGatewayPoolList.cpp \
    $${PWD}/OAIEdgeGatewayPoolModel.cpp \
# APIs
    $${PWD}/OAIEdgeGatewayPoolsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
