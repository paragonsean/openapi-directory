QT += network

HEADERS += \
# Models
    $${PWD}/OAIAttestationPolicy.h \
    $${PWD}/OAICloudError.h \
    $${PWD}/OAICloudErrorBody.h \
# APIs
    $${PWD}/OAIAttestationApi.h \
    $${PWD}/OAIPolicyApi.h \
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
    $${PWD}/OAIAttestationPolicy.cpp \
    $${PWD}/OAICloudError.cpp \
    $${PWD}/OAICloudErrorBody.cpp \
# APIs
    $${PWD}/OAIAttestationApi.cpp \
    $${PWD}/OAIPolicyApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
