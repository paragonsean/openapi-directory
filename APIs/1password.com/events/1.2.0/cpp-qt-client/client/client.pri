QT += network

HEADERS += \
# Models
    $${PWD}/OAIAuditEvent.h \
    $${PWD}/OAIAuditEventActions.h \
    $${PWD}/OAIAuditEventItems.h \
    $${PWD}/OAIAuditEventObjectTypes.h \
    $${PWD}/OAIClient.h \
    $${PWD}/OAICursor.h \
    $${PWD}/OAICursorCollection.h \
    $${PWD}/OAIDetails.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIError_Error.h \
    $${PWD}/OAIIntrospection.h \
    $${PWD}/OAIIntrospectionV2.h \
    $${PWD}/OAIItemUsage.h \
    $${PWD}/OAIItemUsageItems.h \
    $${PWD}/OAILocation.h \
    $${PWD}/OAIResetCursor.h \
    $${PWD}/OAISession.h \
    $${PWD}/OAISignInAttempt.h \
    $${PWD}/OAISignInAttemptItems.h \
    $${PWD}/OAIUser.h \
# APIs
    $${PWD}/OAIApiV1Api.h \
    $${PWD}/OAIAuthApi.h \
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
    $${PWD}/OAIAuditEvent.cpp \
    $${PWD}/OAIAuditEventActions.cpp \
    $${PWD}/OAIAuditEventItems.cpp \
    $${PWD}/OAIAuditEventObjectTypes.cpp \
    $${PWD}/OAIClient.cpp \
    $${PWD}/OAICursor.cpp \
    $${PWD}/OAICursorCollection.cpp \
    $${PWD}/OAIDetails.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIError_Error.cpp \
    $${PWD}/OAIIntrospection.cpp \
    $${PWD}/OAIIntrospectionV2.cpp \
    $${PWD}/OAIItemUsage.cpp \
    $${PWD}/OAIItemUsageItems.cpp \
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAIResetCursor.cpp \
    $${PWD}/OAISession.cpp \
    $${PWD}/OAISignInAttempt.cpp \
    $${PWD}/OAISignInAttemptItems.cpp \
    $${PWD}/OAIUser.cpp \
# APIs
    $${PWD}/OAIApiV1Api.cpp \
    $${PWD}/OAIAuthApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
