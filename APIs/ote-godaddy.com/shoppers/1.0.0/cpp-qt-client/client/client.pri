QT += network

HEADERS += \
# Models
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorField.h \
    $${PWD}/OAIErrorLimit.h \
    $${PWD}/OAIPasswordError.h \
    $${PWD}/OAISecret.h \
    $${PWD}/OAIShopper.h \
    $${PWD}/OAIShopperId.h \
    $${PWD}/OAIShopperStatus.h \
    $${PWD}/OAIShopperUpdate.h \
    $${PWD}/OAISubaccountCreate.h \
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
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorField.cpp \
    $${PWD}/OAIErrorLimit.cpp \
    $${PWD}/OAIPasswordError.cpp \
    $${PWD}/OAISecret.cpp \
    $${PWD}/OAIShopper.cpp \
    $${PWD}/OAIShopperId.cpp \
    $${PWD}/OAIShopperStatus.cpp \
    $${PWD}/OAIShopperUpdate.cpp \
    $${PWD}/OAISubaccountCreate.cpp \
# APIs
    $${PWD}/OAIV1Api.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
