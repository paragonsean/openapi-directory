QT += network

HEADERS += \
# Models
    $${PWD}/OAICluster.h \
    $${PWD}/OAIClusterListResult.h \
    $${PWD}/OAIClusterPatch.h \
    $${PWD}/OAIClusterPatchProperties.h \
    $${PWD}/OAIClusterProperties.h \
    $${PWD}/OAIErrorDetails.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIIdentity.h \
    $${PWD}/OAIResource.h \
# APIs
    $${PWD}/OAIClustersApi.h \
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
    $${PWD}/OAICluster.cpp \
    $${PWD}/OAIClusterListResult.cpp \
    $${PWD}/OAIClusterPatch.cpp \
    $${PWD}/OAIClusterPatchProperties.cpp \
    $${PWD}/OAIClusterProperties.cpp \
    $${PWD}/OAIErrorDetails.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIIdentity.cpp \
    $${PWD}/OAIResource.cpp \
# APIs
    $${PWD}/OAIClustersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
