QT += network

HEADERS += \
# Models
    $${PWD}/OAITenantAccess_Get_200_response.h \
    $${PWD}/OAITenantAccess_Get_default_response.h \
    $${PWD}/OAITenantAccess_Get_default_response_error.h \
    $${PWD}/OAITenantAccess_Get_default_response_error_details_inner.h \
    $${PWD}/OAITenantAccess_Update_request.h \
    $${PWD}/OAITenantAccess_Update_request_properties.h \
    $${PWD}/OAITenantConfiguration_Deploy_200_response.h \
    $${PWD}/OAITenantConfiguration_Deploy_200_response_actionLog_inner.h \
    $${PWD}/OAITenantConfiguration_Deploy_request.h \
    $${PWD}/OAITenantConfiguration_Deploy_request_properties.h \
    $${PWD}/OAITenantConfiguration_GetSyncState_200_response.h \
    $${PWD}/OAITenantConfiguration_Save_request.h \
    $${PWD}/OAITenantConfiguration_Save_request_properties.h \
# APIs
    $${PWD}/OAITenantAccessApi.h \
    $${PWD}/OAITenantAccessGitApi.h \
    $${PWD}/OAITenantConfigurationApi.h \
    $${PWD}/OAITenantConfigurationSyncStateApi.h \
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
    $${PWD}/OAITenantAccess_Get_200_response.cpp \
    $${PWD}/OAITenantAccess_Get_default_response.cpp \
    $${PWD}/OAITenantAccess_Get_default_response_error.cpp \
    $${PWD}/OAITenantAccess_Get_default_response_error_details_inner.cpp \
    $${PWD}/OAITenantAccess_Update_request.cpp \
    $${PWD}/OAITenantAccess_Update_request_properties.cpp \
    $${PWD}/OAITenantConfiguration_Deploy_200_response.cpp \
    $${PWD}/OAITenantConfiguration_Deploy_200_response_actionLog_inner.cpp \
    $${PWD}/OAITenantConfiguration_Deploy_request.cpp \
    $${PWD}/OAITenantConfiguration_Deploy_request_properties.cpp \
    $${PWD}/OAITenantConfiguration_GetSyncState_200_response.cpp \
    $${PWD}/OAITenantConfiguration_Save_request.cpp \
    $${PWD}/OAITenantConfiguration_Save_request_properties.cpp \
# APIs
    $${PWD}/OAITenantAccessApi.cpp \
    $${PWD}/OAITenantAccessGitApi.cpp \
    $${PWD}/OAITenantConfigurationApi.cpp \
    $${PWD}/OAITenantConfigurationSyncStateApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
