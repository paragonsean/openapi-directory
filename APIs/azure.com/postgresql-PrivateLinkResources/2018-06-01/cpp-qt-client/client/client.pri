QT += network

HEADERS += \
# Models
    $${PWD}/OAICloudError.h \
    $${PWD}/OAICloudError_error.h \
    $${PWD}/OAICloudError_error_additionalInfo_inner.h \
    $${PWD}/OAIPrivateLinkResource.h \
    $${PWD}/OAIPrivateLinkResourceListResult.h \
    $${PWD}/OAIPrivateLinkResourceProperties.h \
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
    $${PWD}/OAICloudError_error.cpp \
    $${PWD}/OAICloudError_error_additionalInfo_inner.cpp \
    $${PWD}/OAIPrivateLinkResource.cpp \
    $${PWD}/OAIPrivateLinkResourceListResult.cpp \
    $${PWD}/OAIPrivateLinkResourceProperties.cpp \
# APIs
    $${PWD}/OAIPrivateLinkResourcesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
