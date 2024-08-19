QT += network

HEADERS += \
# Models
    $${PWD}/OAIProductSecret.h \
    $${PWD}/OAIProductSecretProperties.h \
    $${PWD}/OAIProductSecretsList.h \
    $${PWD}/OAISecretDescriptor.h \
    $${PWD}/OAISecretParameters.h \
    $${PWD}/OAISecretRotationStatus.h \
    $${PWD}/OAISecretState.h \
    $${PWD}/OAISecretStatus.h \
# APIs
    $${PWD}/OAIProductSecretsApi.h \
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
    $${PWD}/OAIProductSecret.cpp \
    $${PWD}/OAIProductSecretProperties.cpp \
    $${PWD}/OAIProductSecretsList.cpp \
    $${PWD}/OAISecretDescriptor.cpp \
    $${PWD}/OAISecretParameters.cpp \
    $${PWD}/OAISecretRotationStatus.cpp \
    $${PWD}/OAISecretState.cpp \
    $${PWD}/OAISecretStatus.cpp \
# APIs
    $${PWD}/OAIProductSecretsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
