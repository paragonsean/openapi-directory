QT += network

HEADERS += \
# Models
    $${PWD}/OAIOperation.h \
    $${PWD}/OAIStatus.h \
    $${PWD}/OAIV2AndroidApplication.h \
    $${PWD}/OAIV2AndroidKeyRestrictions.h \
    $${PWD}/OAIV2ApiTarget.h \
    $${PWD}/OAIV2BrowserKeyRestrictions.h \
    $${PWD}/OAIV2GetKeyStringResponse.h \
    $${PWD}/OAIV2IosKeyRestrictions.h \
    $${PWD}/OAIV2Key.h \
    $${PWD}/OAIV2ListKeysResponse.h \
    $${PWD}/OAIV2LookupKeyResponse.h \
    $${PWD}/OAIV2Restrictions.h \
    $${PWD}/OAIV2ServerKeyRestrictions.h \
# APIs
    $${PWD}/OAIKeysApi.h \
    $${PWD}/OAIProjectsApi.h \
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
    $${PWD}/OAIOperation.cpp \
    $${PWD}/OAIStatus.cpp \
    $${PWD}/OAIV2AndroidApplication.cpp \
    $${PWD}/OAIV2AndroidKeyRestrictions.cpp \
    $${PWD}/OAIV2ApiTarget.cpp \
    $${PWD}/OAIV2BrowserKeyRestrictions.cpp \
    $${PWD}/OAIV2GetKeyStringResponse.cpp \
    $${PWD}/OAIV2IosKeyRestrictions.cpp \
    $${PWD}/OAIV2Key.cpp \
    $${PWD}/OAIV2ListKeysResponse.cpp \
    $${PWD}/OAIV2LookupKeyResponse.cpp \
    $${PWD}/OAIV2Restrictions.cpp \
    $${PWD}/OAIV2ServerKeyRestrictions.cpp \
# APIs
    $${PWD}/OAIKeysApi.cpp \
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
