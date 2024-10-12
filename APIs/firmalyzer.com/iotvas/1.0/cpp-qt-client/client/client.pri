QT += network

HEADERS += \
# Models
    $${PWD}/OAIConfigIssue.h \
    $${PWD}/OAICryptoKey.h \
    $${PWD}/OAIDefaultAccount.h \
    $${PWD}/OAIDeviceFeatures.h \
    $${PWD}/OAIDeviceInfo.h \
    $${PWD}/OAIExpiredCert.h \
    $${PWD}/OAIFirmwareInfo.h \
    $${PWD}/OAIFirmwareRisk.h \
    $${PWD}/OAIHTTPValidationError.h \
    $${PWD}/OAIPublicKey.h \
    $${PWD}/OAIRiskSummary.h \
    $${PWD}/OAIValidationError.h \
    $${PWD}/OAIVulnerability.h \
    $${PWD}/OAIVulnerableComponent.h \
    $${PWD}/OAIWeakCert.h \
# APIs
    $${PWD}/OAIDeviceApi.h \
    $${PWD}/OAIFirmwareApi.h \
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
    $${PWD}/OAIConfigIssue.cpp \
    $${PWD}/OAICryptoKey.cpp \
    $${PWD}/OAIDefaultAccount.cpp \
    $${PWD}/OAIDeviceFeatures.cpp \
    $${PWD}/OAIDeviceInfo.cpp \
    $${PWD}/OAIExpiredCert.cpp \
    $${PWD}/OAIFirmwareInfo.cpp \
    $${PWD}/OAIFirmwareRisk.cpp \
    $${PWD}/OAIHTTPValidationError.cpp \
    $${PWD}/OAIPublicKey.cpp \
    $${PWD}/OAIRiskSummary.cpp \
    $${PWD}/OAIValidationError.cpp \
    $${PWD}/OAIVulnerability.cpp \
    $${PWD}/OAIVulnerableComponent.cpp \
    $${PWD}/OAIWeakCert.cpp \
# APIs
    $${PWD}/OAIDeviceApi.cpp \
    $${PWD}/OAIFirmwareApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
