QT += network

HEADERS += \
# Models
    $${PWD}/OAIBinding.h \
    $${PWD}/OAIExpr.h \
    $${PWD}/OAIGetIamPolicyRequest.h \
    $${PWD}/OAIGetPolicyOptions.h \
    $${PWD}/OAIPolicy.h \
    $${PWD}/OAISetIamPolicyRequest.h \
    $${PWD}/OAITestIamPermissionsRequest.h \
    $${PWD}/OAITestIamPermissionsResponse.h \
# APIs
    $${PWD}/OAIV1beta1Api.h \
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
    $${PWD}/OAIExpr.cpp \
    $${PWD}/OAIGetIamPolicyRequest.cpp \
    $${PWD}/OAIGetPolicyOptions.cpp \
    $${PWD}/OAIPolicy.cpp \
    $${PWD}/OAISetIamPolicyRequest.cpp \
    $${PWD}/OAITestIamPermissionsRequest.cpp \
    $${PWD}/OAITestIamPermissionsResponse.cpp \
# APIs
    $${PWD}/OAIV1beta1Api.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
