QT += network

HEADERS += \
# Models
    $${PWD}/OAICloudError.h \
    $${PWD}/OAICloudErrorBody.h \
    $${PWD}/OAIPrivateLinkResource.h \
    $${PWD}/OAIPrivateLinkResourceListResult.h \
    $${PWD}/OAIPrivateLinkResourceProperties.h \
    $${PWD}/OAIProxyResource.h \
    $${PWD}/OAIResource.h \
# APIs
    $${PWD}/OAIPrivateLinkResourcesApi.h \
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
    $${PWD}/OAICloudError.cpp \
    $${PWD}/OAICloudErrorBody.cpp \
    $${PWD}/OAIPrivateLinkResource.cpp \
    $${PWD}/OAIPrivateLinkResourceListResult.cpp \
    $${PWD}/OAIPrivateLinkResourceProperties.cpp \
    $${PWD}/OAIProxyResource.cpp \
    $${PWD}/OAIResource.cpp \
# APIs
    $${PWD}/OAIPrivateLinkResourcesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
