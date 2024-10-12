QT += network

HEADERS += \
# Models
    $${PWD}/OAICreateProfileRequest.h \
    $${PWD}/OAIDeployment.h \
    $${PWD}/OAIListProfilesResponse.h \
    $${PWD}/OAIProfile.h \
# APIs
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
    $${PWD}/OAICreateProfileRequest.cpp \
    $${PWD}/OAIDeployment.cpp \
    $${PWD}/OAIListProfilesResponse.cpp \
    $${PWD}/OAIProfile.cpp \
# APIs
    $${PWD}/OAIProjectsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
