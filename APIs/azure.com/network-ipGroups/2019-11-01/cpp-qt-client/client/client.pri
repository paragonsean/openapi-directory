QT += network

HEADERS += \
# Models
    $${PWD}/OAIIpGroup.h \
    $${PWD}/OAIIpGroupListResult.h \
    $${PWD}/OAIIpGroupPropertiesFormat.h \
    $${PWD}/OAIIpGroupPropertiesFormat_firewalls_inner.h \
    $${PWD}/OAIIpGroups_List_default_response.h \
    $${PWD}/OAIIpGroups_List_default_response_details_inner.h \
    $${PWD}/OAIIpGroups_UpdateGroups_request.h \
# APIs
    $${PWD}/OAIIpGroupsApi.h \
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
    $${PWD}/OAIIpGroup.cpp \
    $${PWD}/OAIIpGroupListResult.cpp \
    $${PWD}/OAIIpGroupPropertiesFormat.cpp \
    $${PWD}/OAIIpGroupPropertiesFormat_firewalls_inner.cpp \
    $${PWD}/OAIIpGroups_List_default_response.cpp \
    $${PWD}/OAIIpGroups_List_default_response_details_inner.cpp \
    $${PWD}/OAIIpGroups_UpdateGroups_request.cpp \
# APIs
    $${PWD}/OAIIpGroupsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
