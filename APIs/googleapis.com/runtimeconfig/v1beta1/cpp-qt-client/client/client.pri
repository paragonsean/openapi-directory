QT += network

HEADERS += \
# Models
    $${PWD}/OAIBinding.h \
    $${PWD}/OAICardinality.h \
    $${PWD}/OAIEndCondition.h \
    $${PWD}/OAIExpr.h \
    $${PWD}/OAIListConfigsResponse.h \
    $${PWD}/OAIListVariablesResponse.h \
    $${PWD}/OAIListWaitersResponse.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIPolicy.h \
    $${PWD}/OAIRuntimeConfig.h \
    $${PWD}/OAISetIamPolicyRequest.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAITestIamPermissionsRequest.h \
    $${PWD}/OAITestIamPermissionsResponse.h \
    $${PWD}/OAIVariable.h \
    $${PWD}/OAIWaiter.h \
    $${PWD}/OAIWatchVariableRequest.h \
# APIs
    $${PWD}/OAIProjectsApi.h \
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
    $${PWD}/OAIBinding.cpp \
    $${PWD}/OAICardinality.cpp \
    $${PWD}/OAIEndCondition.cpp \
    $${PWD}/OAIExpr.cpp \
    $${PWD}/OAIListConfigsResponse.cpp \
    $${PWD}/OAIListVariablesResponse.cpp \
    $${PWD}/OAIListWaitersResponse.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIPolicy.cpp \
    $${PWD}/OAIRuntimeConfig.cpp \
    $${PWD}/OAISetIamPolicyRequest.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAITestIamPermissionsRequest.cpp \
    $${PWD}/OAITestIamPermissionsResponse.cpp \
    $${PWD}/OAIVariable.cpp \
    $${PWD}/OAIWaiter.cpp \
    $${PWD}/OAIWatchVariableRequest.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
