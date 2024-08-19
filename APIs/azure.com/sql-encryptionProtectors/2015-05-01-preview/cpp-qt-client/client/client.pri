QT += network

HEADERS += \
# Models
    $${PWD}/OAIEncryptionProtector.h \
    $${PWD}/OAIEncryptionProtectorListResult.h \
    $${PWD}/OAIEncryptionProtectorProperties.h \
# APIs
    $${PWD}/OAIEncryptionProtectorsApi.h \
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
    $${PWD}/OAIEncryptionProtector.cpp \
    $${PWD}/OAIEncryptionProtectorListResult.cpp \
    $${PWD}/OAIEncryptionProtectorProperties.cpp \
# APIs
    $${PWD}/OAIEncryptionProtectorsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
