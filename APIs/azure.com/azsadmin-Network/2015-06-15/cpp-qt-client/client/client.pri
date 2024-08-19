QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdminOverview.h \
    $${PWD}/OAIAdminOverviewProperties.h \
    $${PWD}/OAIAdminOverviewResourceHealth.h \
    $${PWD}/OAIAdminOverviewResourceUsage.h \
    $${PWD}/OAIDisplay.h \
    $${PWD}/OAILocation.h \
    $${PWD}/OAILocationsList.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationList.h \
    $${PWD}/OAIOperationResult.h \
    $${PWD}/OAIOperationResultList.h \
    $${PWD}/OAIProvisionedResource.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAITenantResource.h \
# APIs
    $${PWD}/OAINetworkApi.h \
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
    $${PWD}/OAIAdminOverview.cpp \
    $${PWD}/OAIAdminOverviewProperties.cpp \
    $${PWD}/OAIAdminOverviewResourceHealth.cpp \
    $${PWD}/OAIAdminOverviewResourceUsage.cpp \
    $${PWD}/OAIDisplay.cpp \
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAILocationsList.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationList.cpp \
    $${PWD}/OAIOperationResult.cpp \
    $${PWD}/OAIOperationResultList.cpp \
    $${PWD}/OAIProvisionedResource.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAITenantResource.cpp \
# APIs
    $${PWD}/OAINetworkApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
