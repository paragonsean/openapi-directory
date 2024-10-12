QT += network

HEADERS += \
# Models
    $${PWD}/OAIChannel.h \
    $${PWD}/OAIInterval.h \
    $${PWD}/OAIListChannelsResponse.h \
    $${PWD}/OAIListPlatformsResponse.h \
    $${PWD}/OAIListReleasesResponse.h \
    $${PWD}/OAIListVersionsResponse.h \
    $${PWD}/OAIPlatform.h \
    $${PWD}/OAIRelease.h \
    $${PWD}/OAIVersion.h \
# APIs
    $${PWD}/OAIPlatformsApi.h \
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
    $${PWD}/OAIChannel.cpp \
    $${PWD}/OAIInterval.cpp \
    $${PWD}/OAIListChannelsResponse.cpp \
    $${PWD}/OAIListPlatformsResponse.cpp \
    $${PWD}/OAIListReleasesResponse.cpp \
    $${PWD}/OAIListVersionsResponse.cpp \
    $${PWD}/OAIPlatform.cpp \
    $${PWD}/OAIRelease.cpp \
    $${PWD}/OAIVersion.cpp \
# APIs
    $${PWD}/OAIPlatformsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
