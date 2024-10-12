QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccountActivity.h \
    $${PWD}/OAIAccountDetails.h \
    $${PWD}/OAIAppAccessRiskVerdict.h \
    $${PWD}/OAIAppIntegrity.h \
    $${PWD}/OAIDecodeIntegrityTokenRequest.h \
    $${PWD}/OAIDecodeIntegrityTokenResponse.h \
    $${PWD}/OAIDeviceIntegrity.h \
    $${PWD}/OAIEnvironmentDetails.h \
    $${PWD}/OAIRecentDeviceActivity.h \
    $${PWD}/OAIRequestDetails.h \
    $${PWD}/OAITestingDetails.h \
    $${PWD}/OAITokenPayloadExternal.h \
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
    $${PWD}/OAIAccountActivity.cpp \
    $${PWD}/OAIAccountDetails.cpp \
    $${PWD}/OAIAppAccessRiskVerdict.cpp \
    $${PWD}/OAIAppIntegrity.cpp \
    $${PWD}/OAIDecodeIntegrityTokenRequest.cpp \
    $${PWD}/OAIDecodeIntegrityTokenResponse.cpp \
    $${PWD}/OAIDeviceIntegrity.cpp \
    $${PWD}/OAIEnvironmentDetails.cpp \
    $${PWD}/OAIRecentDeviceActivity.cpp \
    $${PWD}/OAIRequestDetails.cpp \
    $${PWD}/OAITestingDetails.cpp \
    $${PWD}/OAITokenPayloadExternal.cpp \
# APIs
    $${PWD}/OAIV1Api.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
