QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccessInformationContract.h \
    $${PWD}/OAIAccessInformationUpdateParameters.h \
    $${PWD}/OAIDeployConfigurationParameters.h \
    $${PWD}/OAIOperationResultContract.h \
    $${PWD}/OAISaveConfigurationParameter.h \
    $${PWD}/OAITenantAccess_Update_default_response.h \
    $${PWD}/OAITenantAccess_Update_default_response_details_inner.h \
    $${PWD}/OAITenantConfigurationSyncStateContract.h \
# APIs
    $${PWD}/OAITenantAccessApi.h \
    $${PWD}/OAITenantAccessGitApi.h \
    $${PWD}/OAITenantConfigurationApi.h \
    $${PWD}/OAITenantConfigurationSyncStateApi.h \
    $${PWD}/OAITenantPolicyApi.h \
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
    $${PWD}/OAIAccessInformationContract.cpp \
    $${PWD}/OAIAccessInformationUpdateParameters.cpp \
    $${PWD}/OAIDeployConfigurationParameters.cpp \
    $${PWD}/OAIOperationResultContract.cpp \
    $${PWD}/OAISaveConfigurationParameter.cpp \
    $${PWD}/OAITenantAccess_Update_default_response.cpp \
    $${PWD}/OAITenantAccess_Update_default_response_details_inner.cpp \
    $${PWD}/OAITenantConfigurationSyncStateContract.cpp \
# APIs
    $${PWD}/OAITenantAccessApi.cpp \
    $${PWD}/OAITenantAccessGitApi.cpp \
    $${PWD}/OAITenantConfigurationApi.cpp \
    $${PWD}/OAITenantConfigurationSyncStateApi.cpp \
    $${PWD}/OAITenantPolicyApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
