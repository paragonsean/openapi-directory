QT += network

HEADERS += \
# Models
    $${PWD}/OAISendSSHPublicKeyRequest.h \
    $${PWD}/OAISendSSHPublicKeyResponse.h \
    $${PWD}/OAISendSerialConsoleSSHPublicKeyRequest.h \
    $${PWD}/OAISendSerialConsoleSSHPublicKeyResponse.h \
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
    $${PWD}/OAISendSSHPublicKeyRequest.cpp \
    $${PWD}/OAISendSSHPublicKeyResponse.cpp \
    $${PWD}/OAISendSerialConsoleSSHPublicKeyRequest.cpp \
    $${PWD}/OAISendSerialConsoleSSHPublicKeyResponse.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
