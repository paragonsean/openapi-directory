QT += network

HEADERS += \
# Models
    $${PWD}/OAIBGPCommunity.h \
    $${PWD}/OAIBgpServiceCommunity.h \
    $${PWD}/OAIBgpServiceCommunityListResult.h \
    $${PWD}/OAIBgpServiceCommunityPropertiesFormat.h \
# APIs
    $${PWD}/OAIBgpServiceCommunitiesApi.h \
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
    $${PWD}/OAIBGPCommunity.cpp \
    $${PWD}/OAIBgpServiceCommunity.cpp \
    $${PWD}/OAIBgpServiceCommunityListResult.cpp \
    $${PWD}/OAIBgpServiceCommunityPropertiesFormat.cpp \
# APIs
    $${PWD}/OAIBgpServiceCommunitiesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
