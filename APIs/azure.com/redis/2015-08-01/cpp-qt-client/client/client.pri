QT += network

HEADERS += \
# Models
    $${PWD}/OAIRedisAccessKeys.h \
    $${PWD}/OAIRedisCreateOrUpdateParameters.h \
    $${PWD}/OAIRedisListKeysResult.h \
    $${PWD}/OAIRedisListResult.h \
    $${PWD}/OAIRedisProperties.h \
    $${PWD}/OAIRedisReadableProperties.h \
    $${PWD}/OAIRedisReadablePropertiesWithAccessKey.h \
    $${PWD}/OAIRedisRebootParameters.h \
    $${PWD}/OAIRedisRegenerateKeyParameters.h \
    $${PWD}/OAIRedisResource.h \
    $${PWD}/OAIRedisResourceWithAccessKey.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAISku.h \
# APIs
    $${PWD}/OAIRedisApi.h \
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
    $${PWD}/OAIRedisAccessKeys.cpp \
    $${PWD}/OAIRedisCreateOrUpdateParameters.cpp \
    $${PWD}/OAIRedisListKeysResult.cpp \
    $${PWD}/OAIRedisListResult.cpp \
    $${PWD}/OAIRedisProperties.cpp \
    $${PWD}/OAIRedisReadableProperties.cpp \
    $${PWD}/OAIRedisReadablePropertiesWithAccessKey.cpp \
    $${PWD}/OAIRedisRebootParameters.cpp \
    $${PWD}/OAIRedisRegenerateKeyParameters.cpp \
    $${PWD}/OAIRedisResource.cpp \
    $${PWD}/OAIRedisResourceWithAccessKey.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAISku.cpp \
# APIs
    $${PWD}/OAIRedisApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
