QT += network

HEADERS += \
# Models
    $${PWD}/OAIDisableSerialConsoleResult.h \
    $${PWD}/OAIEnableSerialConsoleResult.h \
    $${PWD}/OAIGetSerialConsoleSubscriptionNotFound.h \
    $${PWD}/OAISerialConsoleOperations.h \
    $${PWD}/OAISerialConsoleOperations_value_inner.h \
    $${PWD}/OAISerialConsoleOperations_value_inner_display.h \
    $${PWD}/OAISerialConsoleStatus.h \
# APIs
    $${PWD}/OAISerialConsoleApi.h \
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
    $${PWD}/OAIDisableSerialConsoleResult.cpp \
    $${PWD}/OAIEnableSerialConsoleResult.cpp \
    $${PWD}/OAIGetSerialConsoleSubscriptionNotFound.cpp \
    $${PWD}/OAISerialConsoleOperations.cpp \
    $${PWD}/OAISerialConsoleOperations_value_inner.cpp \
    $${PWD}/OAISerialConsoleOperations_value_inner_display.cpp \
    $${PWD}/OAISerialConsoleStatus.cpp \
# APIs
    $${PWD}/OAISerialConsoleApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
