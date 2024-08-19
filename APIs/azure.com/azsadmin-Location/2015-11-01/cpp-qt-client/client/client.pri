QT += network

HEADERS += \
# Models
    $${PWD}/OAIExtendedErrorInfo.h \
    $${PWD}/OAIExtendedErrorInfoList.h \
    $${PWD}/OAILocation.h \
    $${PWD}/OAILocationList.h \
    $${PWD}/OAIOperationsStatus.h \
    $${PWD}/OAIOperationsStatusIdentifier.h \
# APIs
    $${PWD}/OAILocationsApi.h \
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
    $${PWD}/OAIExtendedErrorInfo.cpp \
    $${PWD}/OAIExtendedErrorInfoList.cpp \
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAILocationList.cpp \
    $${PWD}/OAIOperationsStatus.cpp \
    $${PWD}/OAIOperationsStatusIdentifier.cpp \
# APIs
    $${PWD}/OAILocationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
