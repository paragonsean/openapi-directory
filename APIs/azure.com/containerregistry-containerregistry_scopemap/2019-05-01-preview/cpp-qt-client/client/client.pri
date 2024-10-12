QT += network

HEADERS += \
# Models
    $${PWD}/OAIGenerateCredentialsParameters.h \
    $${PWD}/OAIGenerateCredentialsResult.h \
    $${PWD}/OAIProxyResource.h \
    $${PWD}/OAIScopeMap.h \
    $${PWD}/OAIScopeMapListResult.h \
    $${PWD}/OAIScopeMapProperties.h \
    $${PWD}/OAIScopeMapPropertiesUpdateParameters.h \
    $${PWD}/OAIScopeMapUpdateParameters.h \
    $${PWD}/OAIToken.h \
    $${PWD}/OAITokenCertificate.h \
    $${PWD}/OAITokenCredentialsProperties.h \
    $${PWD}/OAITokenListResult.h \
    $${PWD}/OAITokenPassword.h \
    $${PWD}/OAITokenProperties.h \
    $${PWD}/OAITokenUpdateParameters.h \
    $${PWD}/OAITokenUpdateProperties.h \
# APIs
    $${PWD}/OAIRegistriesApi.h \
    $${PWD}/OAIScopeMapsApi.h \
    $${PWD}/OAITokensApi.h \
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
    $${PWD}/OAIGenerateCredentialsParameters.cpp \
    $${PWD}/OAIGenerateCredentialsResult.cpp \
    $${PWD}/OAIProxyResource.cpp \
    $${PWD}/OAIScopeMap.cpp \
    $${PWD}/OAIScopeMapListResult.cpp \
    $${PWD}/OAIScopeMapProperties.cpp \
    $${PWD}/OAIScopeMapPropertiesUpdateParameters.cpp \
    $${PWD}/OAIScopeMapUpdateParameters.cpp \
    $${PWD}/OAIToken.cpp \
    $${PWD}/OAITokenCertificate.cpp \
    $${PWD}/OAITokenCredentialsProperties.cpp \
    $${PWD}/OAITokenListResult.cpp \
    $${PWD}/OAITokenPassword.cpp \
    $${PWD}/OAITokenProperties.cpp \
    $${PWD}/OAITokenUpdateParameters.cpp \
    $${PWD}/OAITokenUpdateProperties.cpp \
# APIs
    $${PWD}/OAIRegistriesApi.cpp \
    $${PWD}/OAIScopeMapsApi.cpp \
    $${PWD}/OAITokensApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
