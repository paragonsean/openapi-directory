QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddPublicKeyRequest.h \
    $${PWD}/OAIAddPublicKeyResponse.h \
    $${PWD}/OAIAuthorizeEnvironmentRequest.h \
    $${PWD}/OAIEnvironment.h \
    $${PWD}/OAIListOperationsResponse.h \
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIRemovePublicKeyRequest.h \
    $${PWD}/OAIStartEnvironmentMetadata.h \
    $${PWD}/OAIStartEnvironmentRequest.h \
    $${PWD}/OAIStartEnvironmentResponse.h \
    $${PWD}/OAIStatus.h \
# APIs
    $${PWD}/OAIOperationsApi.h \
    $${PWD}/OAIUsersApi.h \
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
    $${PWD}/OAIAddPublicKeyRequest.cpp \
    $${PWD}/OAIAddPublicKeyResponse.cpp \
    $${PWD}/OAIAuthorizeEnvironmentRequest.cpp \
    $${PWD}/OAIEnvironment.cpp \
    $${PWD}/OAIListOperationsResponse.cpp \
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIRemovePublicKeyRequest.cpp \
    $${PWD}/OAIStartEnvironmentMetadata.cpp \
    $${PWD}/OAIStartEnvironmentRequest.cpp \
    $${PWD}/OAIStartEnvironmentResponse.cpp \
    $${PWD}/OAIStatus.cpp \
# APIs
    $${PWD}/OAIOperationsApi.cpp \
    $${PWD}/OAIUsersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
