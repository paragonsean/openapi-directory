QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccountResource.h \
    $${PWD}/OAIAccountResourceListResult.h \
    $${PWD}/OAIAccountResourceRequest.h \
    $${PWD}/OAIAccountTagRequest.h \
    $${PWD}/OAICheckNameAvailabilityParameter.h \
    $${PWD}/OAICheckNameAvailabilityResult.h \
    $${PWD}/OAIExtensionResource.h \
    $${PWD}/OAIExtensionResourceListResult.h \
    $${PWD}/OAIExtensionResourcePlan.h \
    $${PWD}/OAIExtensionResourceRequest.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIOperationListResult.h \
    $${PWD}/OAIOperationProperties.h \
    $${PWD}/OAIProjectResource.h \
    $${PWD}/OAIProjectResourceListResult.h \
    $${PWD}/OAIResource.h \
# APIs
    $${PWD}/OAIAccountsApi.h \
    $${PWD}/OAIExtensionsApi.h \
    $${PWD}/OAIOperationsApi.h \
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
    $${PWD}/OAIAccountResource.cpp \
    $${PWD}/OAIAccountResourceListResult.cpp \
    $${PWD}/OAIAccountResourceRequest.cpp \
    $${PWD}/OAIAccountTagRequest.cpp \
    $${PWD}/OAICheckNameAvailabilityParameter.cpp \
    $${PWD}/OAICheckNameAvailabilityResult.cpp \
    $${PWD}/OAIExtensionResource.cpp \
    $${PWD}/OAIExtensionResourceListResult.cpp \
    $${PWD}/OAIExtensionResourcePlan.cpp \
    $${PWD}/OAIExtensionResourceRequest.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIOperationListResult.cpp \
    $${PWD}/OAIOperationProperties.cpp \
    $${PWD}/OAIProjectResource.cpp \
    $${PWD}/OAIProjectResourceListResult.cpp \
    $${PWD}/OAIResource.cpp \
# APIs
    $${PWD}/OAIAccountsApi.cpp \
    $${PWD}/OAIExtensionsApi.cpp \
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
