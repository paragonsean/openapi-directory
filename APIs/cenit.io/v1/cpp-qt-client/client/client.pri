QT += network

HEADERS += \
# Models
    $${PWD}/OAIConnection.h \
    $${PWD}/OAIConnection_headers_inner.h \
    $${PWD}/OAIConnection_role.h \
    $${PWD}/OAIData_type.h \
    $${PWD}/OAIFlow.h \
    $${PWD}/OAINamespace.h \
    $${PWD}/OAIObserver.h \
    $${PWD}/OAIScheduler.h \
    $${PWD}/OAISchema.h \
    $${PWD}/OAITranslator.h \
    $${PWD}/OAIWebhook.h \
# APIs
    $${PWD}/OAIConnectionApi.h \
    $${PWD}/OAIConnectionRoleApi.h \
    $${PWD}/OAIDataEventApi.h \
    $${PWD}/OAIDataTypeApi.h \
    $${PWD}/OAIFlowApi.h \
    $${PWD}/OAINamespaceApi.h \
    $${PWD}/OAISchedulerApi.h \
    $${PWD}/OAISchemaApi.h \
    $${PWD}/OAITranslatorApi.h \
    $${PWD}/OAIWebhookApi.h \
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
    $${PWD}/OAIConnection.cpp \
    $${PWD}/OAIConnection_headers_inner.cpp \
    $${PWD}/OAIConnection_role.cpp \
    $${PWD}/OAIData_type.cpp \
    $${PWD}/OAIFlow.cpp \
    $${PWD}/OAINamespace.cpp \
    $${PWD}/OAIObserver.cpp \
    $${PWD}/OAIScheduler.cpp \
    $${PWD}/OAISchema.cpp \
    $${PWD}/OAITranslator.cpp \
    $${PWD}/OAIWebhook.cpp \
# APIs
    $${PWD}/OAIConnectionApi.cpp \
    $${PWD}/OAIConnectionRoleApi.cpp \
    $${PWD}/OAIDataEventApi.cpp \
    $${PWD}/OAIDataTypeApi.cpp \
    $${PWD}/OAIFlowApi.cpp \
    $${PWD}/OAINamespaceApi.cpp \
    $${PWD}/OAISchedulerApi.cpp \
    $${PWD}/OAISchemaApi.cpp \
    $${PWD}/OAITranslatorApi.cpp \
    $${PWD}/OAIWebhookApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
