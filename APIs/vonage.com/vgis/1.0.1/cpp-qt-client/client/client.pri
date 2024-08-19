QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccount.h \
    $${PWD}/OAIAccount_ucis_inner.h \
    $${PWD}/OAIAccount_ucis_inner_health.h \
    $${PWD}/OAICall.h \
    $${PWD}/OAICallCreate.h \
    $${PWD}/OAICallTransfer.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIEvent.h \
    $${PWD}/OAIEventsCount.h \
    $${PWD}/OAIUser.h \
    $${PWD}/OAIUser_roles_inner.h \
    $${PWD}/OAIUser_ucis_inner.h \
    $${PWD}/OAIWebhook.h \
    $${PWD}/OAIWebhookCreate.h \
    $${PWD}/OAIWebhook_statistics.h \
# APIs
    $${PWD}/OAIAccountsApi.h \
    $${PWD}/OAICallsApi.h \
    $${PWD}/OAIEventsApi.h \
    $${PWD}/OAIUsersApi.h \
    $${PWD}/OAIWebhooksApi.h \
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
    $${PWD}/OAIAccount.cpp \
    $${PWD}/OAIAccount_ucis_inner.cpp \
    $${PWD}/OAIAccount_ucis_inner_health.cpp \
    $${PWD}/OAICall.cpp \
    $${PWD}/OAICallCreate.cpp \
    $${PWD}/OAICallTransfer.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIEvent.cpp \
    $${PWD}/OAIEventsCount.cpp \
    $${PWD}/OAIUser.cpp \
    $${PWD}/OAIUser_roles_inner.cpp \
    $${PWD}/OAIUser_ucis_inner.cpp \
    $${PWD}/OAIWebhook.cpp \
    $${PWD}/OAIWebhookCreate.cpp \
    $${PWD}/OAIWebhook_statistics.cpp \
# APIs
    $${PWD}/OAIAccountsApi.cpp \
    $${PWD}/OAICallsApi.cpp \
    $${PWD}/OAIEventsApi.cpp \
    $${PWD}/OAIUsersApi.cpp \
    $${PWD}/OAIWebhooksApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
