QT += network

HEADERS += \
# Models
    $${PWD}/OAIInstanceFailoverGroup.h \
    $${PWD}/OAIInstanceFailoverGroupListResult.h \
    $${PWD}/OAIInstanceFailoverGroupProperties.h \
    $${PWD}/OAIInstanceFailoverGroupReadOnlyEndpoint.h \
    $${PWD}/OAIInstanceFailoverGroupReadWriteEndpoint.h \
    $${PWD}/OAIManagedInstancePairInfo.h \
    $${PWD}/OAIPartnerRegionInfo.h \
# APIs
    $${PWD}/OAIInstanceFailoverGroupsApi.h \
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
    $${PWD}/OAIInstanceFailoverGroup.cpp \
    $${PWD}/OAIInstanceFailoverGroupListResult.cpp \
    $${PWD}/OAIInstanceFailoverGroupProperties.cpp \
    $${PWD}/OAIInstanceFailoverGroupReadOnlyEndpoint.cpp \
    $${PWD}/OAIInstanceFailoverGroupReadWriteEndpoint.cpp \
    $${PWD}/OAIManagedInstancePairInfo.cpp \
    $${PWD}/OAIPartnerRegionInfo.cpp \
# APIs
    $${PWD}/OAIInstanceFailoverGroupsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
