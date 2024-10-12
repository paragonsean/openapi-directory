QT += network

HEADERS += \
# Models
    $${PWD}/OAIActivity.h \
    $${PWD}/OAIActivity_and_identity.h \
    $${PWD}/OAIActivity_and_identity_activity.h \
    $${PWD}/OAIActivity_with_member.h \
    $${PWD}/OAIAlert.h \
    $${PWD}/OAICustom_or_post_activity.h \
    $${PWD}/OAIDestination.h \
    $${PWD}/OAIIdentity.h \
    $${PWD}/OAIMember.h \
    $${PWD}/OAIMember_and_identity.h \
    $${PWD}/OAINote.h \
    $${PWD}/OAIOrganization.h \
    $${PWD}/OAIPost_activity.h \
    $${PWD}/OAIPost_activity_with_member.h \
    $${PWD}/OAIWebhook_subscription.h \
# APIs
    $${PWD}/OAIActivitiesApi.h \
    $${PWD}/OAIActivityTypesApi.h \
    $${PWD}/OAIMembersApi.h \
    $${PWD}/OAINotesApi.h \
    $${PWD}/OAIOrganizationsApi.h \
    $${PWD}/OAIReportsApi.h \
    $${PWD}/OAIUsersApi.h \
    $${PWD}/OAIWebhooksApi.h \
    $${PWD}/OAIWorkspacesApi.h \
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
    $${PWD}/OAIActivity.cpp \
    $${PWD}/OAIActivity_and_identity.cpp \
    $${PWD}/OAIActivity_and_identity_activity.cpp \
    $${PWD}/OAIActivity_with_member.cpp \
    $${PWD}/OAIAlert.cpp \
    $${PWD}/OAICustom_or_post_activity.cpp \
    $${PWD}/OAIDestination.cpp \
    $${PWD}/OAIIdentity.cpp \
    $${PWD}/OAIMember.cpp \
    $${PWD}/OAIMember_and_identity.cpp \
    $${PWD}/OAINote.cpp \
    $${PWD}/OAIOrganization.cpp \
    $${PWD}/OAIPost_activity.cpp \
    $${PWD}/OAIPost_activity_with_member.cpp \
    $${PWD}/OAIWebhook_subscription.cpp \
# APIs
    $${PWD}/OAIActivitiesApi.cpp \
    $${PWD}/OAIActivityTypesApi.cpp \
    $${PWD}/OAIMembersApi.cpp \
    $${PWD}/OAINotesApi.cpp \
    $${PWD}/OAIOrganizationsApi.cpp \
    $${PWD}/OAIReportsApi.cpp \
    $${PWD}/OAIUsersApi.cpp \
    $${PWD}/OAIWebhooksApi.cpp \
    $${PWD}/OAIWorkspacesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
