QT += network

HEADERS += \
# Models
    $${PWD}/OAIDisableUser.h \
    $${PWD}/OAIEnableUser.h \
    $${PWD}/OAIRegister.h \
    $${PWD}/OAIUserLogin.h \
# APIs
    $${PWD}/OAISimpliVPNAPIApi.h \
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
    $${PWD}/OAIDisableUser.cpp \
    $${PWD}/OAIEnableUser.cpp \
    $${PWD}/OAIRegister.cpp \
    $${PWD}/OAIUserLogin.cpp \
# APIs
    $${PWD}/OAISimpliVPNAPIApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
