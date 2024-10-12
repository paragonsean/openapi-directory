QT += network

HEADERS += \
# Models
    $${PWD}/OAIGroupCollection.h \
    $${PWD}/OAIGroupContract.h \
    $${PWD}/OAIGroupCreateParameters.h \
    $${PWD}/OAIGroupUpdateParameters.h \
    $${PWD}/OAIGroupUsers_ListByGroups_200_response.h \
    $${PWD}/OAIGroupUsers_ListByGroups_200_response_value_inner.h \
    $${PWD}/OAIGroupUsers_ListByGroups_200_response_value_inner_identities_inner.h \
    $${PWD}/OAIGroups_Get_default_response.h \
    $${PWD}/OAIGroups_Get_default_response_details_inner.h \
# APIs
    $${PWD}/OAIGroupUsersApi.h \
    $${PWD}/OAIGroupsApi.h \
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
    $${PWD}/OAIGroupCollection.cpp \
    $${PWD}/OAIGroupContract.cpp \
    $${PWD}/OAIGroupCreateParameters.cpp \
    $${PWD}/OAIGroupUpdateParameters.cpp \
    $${PWD}/OAIGroupUsers_ListByGroups_200_response.cpp \
    $${PWD}/OAIGroupUsers_ListByGroups_200_response_value_inner.cpp \
    $${PWD}/OAIGroupUsers_ListByGroups_200_response_value_inner_identities_inner.cpp \
    $${PWD}/OAIGroups_Get_default_response.cpp \
    $${PWD}/OAIGroups_Get_default_response_details_inner.cpp \
# APIs
    $${PWD}/OAIGroupUsersApi.cpp \
    $${PWD}/OAIGroupsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
