QT += network

HEADERS += \
# Models
    $${PWD}/OAIProxyResource.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIWorkloadGroup.h \
    $${PWD}/OAIWorkloadGroupListResult.h \
    $${PWD}/OAIWorkloadGroupProperties.h \
# APIs
    $${PWD}/OAIWorkloadGroupsApi.h \
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
    $${PWD}/OAIProxyResource.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIWorkloadGroup.cpp \
    $${PWD}/OAIWorkloadGroupListResult.cpp \
    $${PWD}/OAIWorkloadGroupProperties.cpp \
# APIs
    $${PWD}/OAIWorkloadGroupsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
