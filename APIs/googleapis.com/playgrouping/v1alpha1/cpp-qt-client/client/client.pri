QT += network

HEADERS += \
# Models
    $${PWD}/OAICreateOrUpdateTagsRequest.h \
    $${PWD}/OAICreateOrUpdateTagsResponse.h \
    $${PWD}/OAITag.h \
    $${PWD}/OAIVerifyTokenRequest.h \
# APIs
    $${PWD}/OAIAppsApi.h \
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
    $${PWD}/OAICreateOrUpdateTagsRequest.cpp \
    $${PWD}/OAICreateOrUpdateTagsResponse.cpp \
    $${PWD}/OAITag.cpp \
    $${PWD}/OAIVerifyTokenRequest.cpp \
# APIs
    $${PWD}/OAIAppsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
