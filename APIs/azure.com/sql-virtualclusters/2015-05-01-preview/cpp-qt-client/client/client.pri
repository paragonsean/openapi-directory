QT += network

HEADERS += \
# Models
    $${PWD}/OAIResource.h \
    $${PWD}/OAITrackedResource.h \
    $${PWD}/OAIVirtualCluster.h \
    $${PWD}/OAIVirtualClusterListResult.h \
    $${PWD}/OAIVirtualClusterProperties.h \
    $${PWD}/OAIVirtualClusterUpdate.h \
# APIs
    $${PWD}/OAIVirtualClustersApi.h \
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
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAITrackedResource.cpp \
    $${PWD}/OAIVirtualCluster.cpp \
    $${PWD}/OAIVirtualClusterListResult.cpp \
    $${PWD}/OAIVirtualClusterProperties.cpp \
    $${PWD}/OAIVirtualClusterUpdate.cpp \
# APIs
    $${PWD}/OAIVirtualClustersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
