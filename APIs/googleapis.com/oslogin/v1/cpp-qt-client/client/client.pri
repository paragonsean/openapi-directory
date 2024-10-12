QT += network

HEADERS += \
# Models
    $${PWD}/OAIImportSshPublicKeyResponse.h \
    $${PWD}/OAILoginProfile.h \
    $${PWD}/OAIPosixAccount.h \
    $${PWD}/OAISshPublicKey.h \
# APIs
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
    $${PWD}/OAIImportSshPublicKeyResponse.cpp \
    $${PWD}/OAILoginProfile.cpp \
    $${PWD}/OAIPosixAccount.cpp \
    $${PWD}/OAISshPublicKey.cpp \
# APIs
    $${PWD}/OAIUsersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
