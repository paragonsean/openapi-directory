QT += network

HEADERS += \
# Models
    $${PWD}/OAIFailoverGroup.h \
    $${PWD}/OAIFailoverGroupListResult.h \
    $${PWD}/OAIFailoverGroupProperties.h \
    $${PWD}/OAIFailoverGroupReadOnlyEndpoint.h \
    $${PWD}/OAIFailoverGroupReadWriteEndpoint.h \
    $${PWD}/OAIFailoverGroupUpdate.h \
    $${PWD}/OAIFailoverGroupUpdateProperties.h \
    $${PWD}/OAIPartnerInfo.h \
# APIs
    $${PWD}/OAIFailoverGroupsApi.h \
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
    $${PWD}/OAIFailoverGroup.cpp \
    $${PWD}/OAIFailoverGroupListResult.cpp \
    $${PWD}/OAIFailoverGroupProperties.cpp \
    $${PWD}/OAIFailoverGroupReadOnlyEndpoint.cpp \
    $${PWD}/OAIFailoverGroupReadWriteEndpoint.cpp \
    $${PWD}/OAIFailoverGroupUpdate.cpp \
    $${PWD}/OAIFailoverGroupUpdateProperties.cpp \
    $${PWD}/OAIPartnerInfo.cpp \
# APIs
    $${PWD}/OAIFailoverGroupsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
