QT += network

HEADERS += \
# Models
    $${PWD}/OAICertificateRequest.h \
    $${PWD}/OAIRawCertificateData.h \
    $${PWD}/OAIResourceCertificateAndAadDetails.h \
    $${PWD}/OAIResourceCertificateAndAcsDetails.h \
    $${PWD}/OAIResourceCertificateDetails.h \
    $${PWD}/OAIVaultCertificateResponse.h \
# APIs
    $${PWD}/OAIRegisteredIdentitiesApi.h \
    $${PWD}/OAIVaultCertificatesApi.h \
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
    $${PWD}/OAICertificateRequest.cpp \
    $${PWD}/OAIRawCertificateData.cpp \
    $${PWD}/OAIResourceCertificateAndAadDetails.cpp \
    $${PWD}/OAIResourceCertificateAndAcsDetails.cpp \
    $${PWD}/OAIResourceCertificateDetails.cpp \
    $${PWD}/OAIVaultCertificateResponse.cpp \
# APIs
    $${PWD}/OAIRegisteredIdentitiesApi.cpp \
    $${PWD}/OAIVaultCertificatesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
