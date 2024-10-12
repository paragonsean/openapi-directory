QT += network

HEADERS += \
# Models
    $${PWD}/OAIAuditEvent.h \
    $${PWD}/OAIAuditEventType.h \
    $${PWD}/OAIAuditEventTypesResp.h \
    $${PWD}/OAIAuditEvent_context.h \
    $${PWD}/OAIAuditResp.h \
    $${PWD}/OAIAuditResp__embedded.h \
    $${PWD}/OAICallbackUrl.h \
    $${PWD}/OAIContextAppCreate.h \
    $${PWD}/OAIContextAppCreate_created.h \
    $${PWD}/OAIContextNumberLinking.h \
    $${PWD}/OAIContextNumberUpdate.h \
    $${PWD}/OAIErrorBadRequest.h \
    $${PWD}/OAIErrorForbidden.h \
    $${PWD}/OAIErrorNotFound.h \
    $${PWD}/OAIErrorUnauthorized.h \
    $${PWD}/OAIEventLink.h \
    $${PWD}/OAIEventLink_self.h \
    $${PWD}/OAIEventTypes.h \
    $${PWD}/OAINoContent.h \
    $${PWD}/OAIPaginationData.h \
    $${PWD}/OAIPaginationLinks.h \
    $${PWD}/OAIPaginationLinks_last.h \
    $${PWD}/OAIPaginationLinks_next.h \
    $${PWD}/OAIPaginationLinks_self.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIAuditEventType.cpp \
    $${PWD}/OAIAuditEventTypesResp.cpp \
    $${PWD}/OAIAuditEvent_context.cpp \
    $${PWD}/OAIAuditResp.cpp \
    $${PWD}/OAIAuditResp__embedded.cpp \
    $${PWD}/OAICallbackUrl.cpp \
    $${PWD}/OAIContextAppCreate.cpp \
    $${PWD}/OAIContextAppCreate_created.cpp \
    $${PWD}/OAIContextNumberLinking.cpp \
    $${PWD}/OAIContextNumberUpdate.cpp \
    $${PWD}/OAIErrorBadRequest.cpp \
    $${PWD}/OAIErrorForbidden.cpp \
    $${PWD}/OAIErrorNotFound.cpp \
    $${PWD}/OAIErrorUnauthorized.cpp \
    $${PWD}/OAIEventLink.cpp \
    $${PWD}/OAIEventLink_self.cpp \
    $${PWD}/OAIEventTypes.cpp \
    $${PWD}/OAINoContent.cpp \
    $${PWD}/OAIPaginationData.cpp \
    $${PWD}/OAIPaginationLinks.cpp \
    $${PWD}/OAIPaginationLinks_last.cpp \
    $${PWD}/OAIPaginationLinks_next.cpp \
    $${PWD}/OAIPaginationLinks_self.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
