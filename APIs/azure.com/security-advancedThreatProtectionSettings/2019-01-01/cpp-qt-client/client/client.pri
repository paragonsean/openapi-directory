QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdvancedThreatProtectionProperties.h \
    $${PWD}/OAIAdvancedThreatProtectionSetting.h \
    $${PWD}/OAIAdvancedThreatProtection_Get_default_response.h \
    $${PWD}/OAIAdvancedThreatProtection_Get_default_response_error.h \
# APIs
    $${PWD}/OAIAdvancedThreatProtectionApi.h \
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
    $${PWD}/OAIAdvancedThreatProtectionProperties.cpp \
    $${PWD}/OAIAdvancedThreatProtectionSetting.cpp \
    $${PWD}/OAIAdvancedThreatProtection_Get_default_response.cpp \
    $${PWD}/OAIAdvancedThreatProtection_Get_default_response_error.cpp \
# APIs
    $${PWD}/OAIAdvancedThreatProtectionApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
