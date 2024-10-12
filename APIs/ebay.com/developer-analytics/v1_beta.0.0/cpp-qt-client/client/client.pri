QT += network

HEADERS += \
# Models
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorParameter.h \
    $${PWD}/OAIRate.h \
    $${PWD}/OAIRateLimit.h \
    $${PWD}/OAIRateLimitsResponse.h \
    $${PWD}/OAIResource.h \
# APIs
    $${PWD}/OAIRateLimitApi.h \
    $${PWD}/OAIUserRateLimitApi.h \
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
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorParameter.cpp \
    $${PWD}/OAIRate.cpp \
    $${PWD}/OAIRateLimit.cpp \
    $${PWD}/OAIRateLimitsResponse.cpp \
    $${PWD}/OAIResource.cpp \
# APIs
    $${PWD}/OAIRateLimitApi.cpp \
    $${PWD}/OAIUserRateLimitApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
