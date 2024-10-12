QT += network

HEADERS += \
# Models
    $${PWD}/OAIGoogleIamV1__Binding.h \
    $${PWD}/OAIGoogleIamV1__Policy.h \
    $${PWD}/OAIGoogleIamV1__SetIamPolicyRequest.h \
    $${PWD}/OAIGoogleIamV1__TestIamPermissionsRequest.h \
    $${PWD}/OAIGoogleIamV1__TestIamPermissionsResponse.h \
    $${PWD}/OAIGoogleType__Expr.h \
# APIs
    $${PWD}/OAIV1Api.h \
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
    $${PWD}/OAIGoogleIamV1__Binding.cpp \
    $${PWD}/OAIGoogleIamV1__Policy.cpp \
    $${PWD}/OAIGoogleIamV1__SetIamPolicyRequest.cpp \
    $${PWD}/OAIGoogleIamV1__TestIamPermissionsRequest.cpp \
    $${PWD}/OAIGoogleIamV1__TestIamPermissionsResponse.cpp \
    $${PWD}/OAIGoogleType__Expr.cpp \
# APIs
    $${PWD}/OAIV1Api.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
