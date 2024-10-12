QT += network

HEADERS += \
# Models
    $${PWD}/OAIAttributes.h \
    $${PWD}/OAISecret.h \
    $${PWD}/OAISecretAttributes.h \
    $${PWD}/OAISecretCreateOrUpdateParameters.h \
    $${PWD}/OAISecretListResult.h \
    $${PWD}/OAISecretPatchParameters.h \
    $${PWD}/OAISecretPatchProperties.h \
    $${PWD}/OAISecretProperties.h \
# APIs
    $${PWD}/OAISecretsApi.h \
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
    $${PWD}/OAIAttributes.cpp \
    $${PWD}/OAISecret.cpp \
    $${PWD}/OAISecretAttributes.cpp \
    $${PWD}/OAISecretCreateOrUpdateParameters.cpp \
    $${PWD}/OAISecretListResult.cpp \
    $${PWD}/OAISecretPatchParameters.cpp \
    $${PWD}/OAISecretPatchProperties.cpp \
    $${PWD}/OAISecretProperties.cpp \
# APIs
    $${PWD}/OAISecretsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
