QT += network

HEADERS += \
# Models
    $${PWD}/OAIVirtualNetwork.h \
    $${PWD}/OAIVirtualNetworkConfigurationState.h \
    $${PWD}/OAIVirtualNetworkConfigurationStatus.h \
    $${PWD}/OAIVirtualNetworkProperties.h \
    $${PWD}/OAIVirtualNetworksList.h \
# APIs
    $${PWD}/OAIVirtualNetworksApi.h \
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
    $${PWD}/OAIVirtualNetwork.cpp \
    $${PWD}/OAIVirtualNetworkConfigurationState.cpp \
    $${PWD}/OAIVirtualNetworkConfigurationStatus.cpp \
    $${PWD}/OAIVirtualNetworkProperties.cpp \
    $${PWD}/OAIVirtualNetworksList.cpp \
# APIs
    $${PWD}/OAIVirtualNetworksApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
