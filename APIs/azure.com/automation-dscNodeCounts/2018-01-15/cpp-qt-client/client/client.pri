QT += network

HEADERS += \
# Models
    $${PWD}/OAINodeCount.h \
    $${PWD}/OAINodeCountInformation_Get_default_response.h \
    $${PWD}/OAINodeCountProperties.h \
    $${PWD}/OAINodeCounts.h \
# APIs
    $${PWD}/OAINodeCountInformationApi.h \
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
    $${PWD}/OAINodeCount.cpp \
    $${PWD}/OAINodeCountInformation_Get_default_response.cpp \
    $${PWD}/OAINodeCountProperties.cpp \
    $${PWD}/OAINodeCounts.cpp \
# APIs
    $${PWD}/OAINodeCountInformationApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
