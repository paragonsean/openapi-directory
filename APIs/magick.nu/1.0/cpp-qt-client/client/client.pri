QT += network

HEADERS += \
# Models
    $${PWD}/OAIPasswordDTO.h \
    $${PWD}/OAITradingAccount.h \
    $${PWD}/OAIUserDTO.h \
# APIs
    $${PWD}/OAIStrategiesApi.h \
    $${PWD}/OAITradingAccountsApi.h \
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
    $${PWD}/OAIPasswordDTO.cpp \
    $${PWD}/OAITradingAccount.cpp \
    $${PWD}/OAIUserDTO.cpp \
# APIs
    $${PWD}/OAIStrategiesApi.cpp \
    $${PWD}/OAITradingAccountsApi.cpp \
    $${PWD}/OAIUsersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
