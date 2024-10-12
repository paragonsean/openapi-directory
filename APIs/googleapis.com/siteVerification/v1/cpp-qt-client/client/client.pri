QT += network

HEADERS += \
# Models
    $${PWD}/OAISiteVerificationWebResourceGettokenRequest.h \
    $${PWD}/OAISiteVerificationWebResourceGettokenRequest_site.h \
    $${PWD}/OAISiteVerificationWebResourceGettokenResponse.h \
    $${PWD}/OAISiteVerificationWebResourceListResponse.h \
    $${PWD}/OAISiteVerificationWebResourceResource.h \
    $${PWD}/OAISiteVerificationWebResourceResource_site.h \
# APIs
    $${PWD}/OAIWebResourceApi.h \
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
    $${PWD}/OAISiteVerificationWebResourceGettokenRequest.cpp \
    $${PWD}/OAISiteVerificationWebResourceGettokenRequest_site.cpp \
    $${PWD}/OAISiteVerificationWebResourceGettokenResponse.cpp \
    $${PWD}/OAISiteVerificationWebResourceListResponse.cpp \
    $${PWD}/OAISiteVerificationWebResourceResource.cpp \
    $${PWD}/OAISiteVerificationWebResourceResource_site.cpp \
# APIs
    $${PWD}/OAIWebResourceApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
