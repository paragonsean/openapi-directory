QT += network

HEADERS += \
# Models
    $${PWD}/OAIBooleanArrayValue.h \
    $${PWD}/OAIBooleanValue.h \
    $${PWD}/OAIDataStoreDevice.h \
    $${PWD}/OAIDevice.h \
    $${PWD}/OAIErrorValue.h \
    $${PWD}/OAIFloatArrayValue.h \
    $${PWD}/OAIFloatValue.h \
    $${PWD}/OAIGroovInfo.h \
    $${PWD}/OAIIntegerArrayValue.h \
    $${PWD}/OAIIntegerValue.h \
    $${PWD}/OAIStringArrayValue.h \
    $${PWD}/OAIStringValue.h \
    $${PWD}/OAITagDefinition.h \
    $${PWD}/OAITagReference.h \
    $${PWD}/OAITagValue.h \
    $${PWD}/OAIUser.h \
# APIs
    $${PWD}/OAIDataStoreApi.h \
    $${PWD}/OAIInfoApi.h \
    $${PWD}/OAILoggingApi.h \
    $${PWD}/OAIWhoamiApi.h \
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
    $${PWD}/OAIBooleanArrayValue.cpp \
    $${PWD}/OAIBooleanValue.cpp \
    $${PWD}/OAIDataStoreDevice.cpp \
    $${PWD}/OAIDevice.cpp \
    $${PWD}/OAIErrorValue.cpp \
    $${PWD}/OAIFloatArrayValue.cpp \
    $${PWD}/OAIFloatValue.cpp \
    $${PWD}/OAIGroovInfo.cpp \
    $${PWD}/OAIIntegerArrayValue.cpp \
    $${PWD}/OAIIntegerValue.cpp \
    $${PWD}/OAIStringArrayValue.cpp \
    $${PWD}/OAIStringValue.cpp \
    $${PWD}/OAITagDefinition.cpp \
    $${PWD}/OAITagReference.cpp \
    $${PWD}/OAITagValue.cpp \
    $${PWD}/OAIUser.cpp \
# APIs
    $${PWD}/OAIDataStoreApi.cpp \
    $${PWD}/OAIInfoApi.cpp \
    $${PWD}/OAILoggingApi.cpp \
    $${PWD}/OAIWhoamiApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
