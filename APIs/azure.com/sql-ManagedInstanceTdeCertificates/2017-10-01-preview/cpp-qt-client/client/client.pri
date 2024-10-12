QT += network

HEADERS += \
# Models
    $${PWD}/OAITdeCertificate.h \
    $${PWD}/OAITdeCertificateProperties.h \
# APIs
    $${PWD}/OAIManagedInstanceTdeCertificatesApi.h \
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
    $${PWD}/OAITdeCertificate.cpp \
    $${PWD}/OAITdeCertificateProperties.cpp \
# APIs
    $${PWD}/OAIManagedInstanceTdeCertificatesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
