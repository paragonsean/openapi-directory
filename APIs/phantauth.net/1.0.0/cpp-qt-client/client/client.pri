QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddress.h \
    $${PWD}/OAIClient.h \
    $${PWD}/OAIDomain.h \
    $${PWD}/OAIFleet.h \
    $${PWD}/OAITeam.h \
    $${PWD}/OAITenant.h \
    $${PWD}/OAIUser.h \
    $${PWD}/OAI_client__client_id__get_200_response.h \
    $${PWD}/OAI_client_post_request.h \
    $${PWD}/OAI_domain__domainname__get_200_response.h \
    $${PWD}/OAI_fleet__fleetname__get_200_response.h \
    $${PWD}/OAI_team__teamname__get_200_response.h \
    $${PWD}/OAI_tenant__tenantname__get_200_response.h \
    $${PWD}/OAI_user__username__get_200_response.h \
    $${PWD}/OAI_user_post_request.h \
    $${PWD}/OAI_user_post_request_address.h \
# APIs
    $${PWD}/OAIClientApi.h \
    $${PWD}/OAIDomainApi.h \
    $${PWD}/OAIFleetApi.h \
    $${PWD}/OAITeamApi.h \
    $${PWD}/OAITenantApi.h \
    $${PWD}/OAIUserApi.h \
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
    $${PWD}/OAIAddress.cpp \
    $${PWD}/OAIClient.cpp \
    $${PWD}/OAIDomain.cpp \
    $${PWD}/OAIFleet.cpp \
    $${PWD}/OAITeam.cpp \
    $${PWD}/OAITenant.cpp \
    $${PWD}/OAIUser.cpp \
    $${PWD}/OAI_client__client_id__get_200_response.cpp \
    $${PWD}/OAI_client_post_request.cpp \
    $${PWD}/OAI_domain__domainname__get_200_response.cpp \
    $${PWD}/OAI_fleet__fleetname__get_200_response.cpp \
    $${PWD}/OAI_team__teamname__get_200_response.cpp \
    $${PWD}/OAI_tenant__tenantname__get_200_response.cpp \
    $${PWD}/OAI_user__username__get_200_response.cpp \
    $${PWD}/OAI_user_post_request.cpp \
    $${PWD}/OAI_user_post_request_address.cpp \
# APIs
    $${PWD}/OAIClientApi.cpp \
    $${PWD}/OAIDomainApi.cpp \
    $${PWD}/OAIFleetApi.cpp \
    $${PWD}/OAITeamApi.cpp \
    $${PWD}/OAITenantApi.cpp \
    $${PWD}/OAIUserApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
