QT += network

HEADERS += \
# Models
    $${PWD}/OAIProductLink.h \
    $${PWD}/OAIProductPackage.h \
    $${PWD}/OAIProductPackageProperties.h \
    $${PWD}/OAIProductPackagesList.h \
    $${PWD}/OAIProductProperties.h \
# APIs
    $${PWD}/OAIProductPackagesApi.h \
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
    $${PWD}/OAIProductLink.cpp \
    $${PWD}/OAIProductPackage.cpp \
    $${PWD}/OAIProductPackageProperties.cpp \
    $${PWD}/OAIProductPackagesList.cpp \
    $${PWD}/OAIProductProperties.cpp \
# APIs
    $${PWD}/OAIProductPackagesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
