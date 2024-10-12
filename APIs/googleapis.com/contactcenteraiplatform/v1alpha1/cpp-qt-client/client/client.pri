QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdminUser.h \
    $${PWD}/OAIContactCenter.h \
    $${PWD}/OAIContactCenterQuota.h \
    $${PWD}/OAIGoogleCloudCommonOperationMetadata.h \
    $${PWD}/OAIInstanceConfig.h \
    $${PWD}/OAIListContactCentersResponse.h \
    $${PWD}/OAIListLocationsResponse.h \
    $${PWD}/OAIListOperationsResponse.h \
    $${PWD}/OAILocation.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationMetadata.h \
    $${PWD}/OAIQuota.h \
    $${PWD}/OAISAMLParams.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAIURIs.h \
# APIs
    $${PWD}/OAIProjectsApi.h \
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
    $${PWD}/OAIAdminUser.cpp \
    $${PWD}/OAIContactCenter.cpp \
    $${PWD}/OAIContactCenterQuota.cpp \
    $${PWD}/OAIGoogleCloudCommonOperationMetadata.cpp \
    $${PWD}/OAIInstanceConfig.cpp \
    $${PWD}/OAIListContactCentersResponse.cpp \
    $${PWD}/OAIListLocationsResponse.cpp \
    $${PWD}/OAIListOperationsResponse.cpp \
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationMetadata.cpp \
    $${PWD}/OAIQuota.cpp \
    $${PWD}/OAISAMLParams.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAIURIs.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
